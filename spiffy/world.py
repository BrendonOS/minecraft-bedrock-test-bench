import math
import struct

BLOCK_DATA_SIZE = 16 * 16 * 128
REGULAR_DATA_SIZE = 16384
SKYLIGHT_DATA_SIZE = 16384
BLOCKLIGHT_DATA_SIZE = 16384
ADDITIONAL_DATA_SIZE_DIRTY = 256
ADDITIONAL_DATA_SIZE_COLOR = 1024
BUFFER_SIZE = BLOCK_DATA_SIZE + REGULAR_DATA_SIZE + SKYLIGHT_DATA_SIZE + BLOCKLIGHT_DATA_SIZE + ADDITIONAL_DATA_SIZE_COLOR + ADDITIONAL_DATA_SIZE_DIRTY

# todo, rewrite this as a c extension
class Chunk():
	def __init__(self):
		self.data = bytearray(BUFFER_SIZE)

	def get_block_type(self, x, y, z):
		return self.data[x + 16 * (z + 16 * y)] & 0xff

	def set_block_type(self, x, y, z, id):
		self.data[x + 16 * (z + 16 * y)] = id

	def get_block_data(self, x, y, z):
		return read_uint_4le(self.data, BLOCK_DATA_SIZE + ((x + 16 * (z + 16 * y)) * 0.5))

	def set_block_data(self, x, y, z, data):
		write_uint_4le(self.data, data, BLOCK_DATA_SIZE + ((x + 16 * (z + 16 * y)) * 0.5))
		
	def get_block_light(self, x, y, z):
		return read_uint_4le(self.data, BLOCK_DATA_SIZE + REGULAR_DATA_SIZE + ((x + 16 * (z + 16 * y)) * 0.5))

	def set_block_light(self, x, y, z, light):
		write_uint_4le(self.data, light, BLOCK_DATA_SIZE + REGULAR_DATA_SIZE + ((x + 16 * (z + 16 * y)) * 0.5))

	def get_sky_light(self, x, y, z):
		return read_uint_4le(self.data, BLOCK_DATA_SIZE + REGULAR_DATA_SIZE + BLOCKLIGHT_DATA_SIZE + ((x + 16 * (z + 16 * y)) * 0.5))

	def set_sky_light(self, x, y, z, light):
		write_uint_4le(self.data, light, BLOCK_DATA_SIZE + REGULAR_DATA_SIZE + BLOCKLIGHT_DATA_SIZE + ((x + 16 * (z + 16 * y)) * 0.5))

	def get_biome_color(self, x, z):
		color = (struct.unpack_from(">i", self.data, BLOCK_DATA_SIZE + REGULAR_DATA_SIZE + BLOCKLIGHT_DATA_SIZE + SKYLIGHT_DATA_SIZE + ADDITIONAL_DATA_SIZE_DIRTY + (((z << 4) + x) * 4))[0] & 0xFFFFFF)
		return ((color >> 16), ((color >> 8) & 0xFF), (color & 0xFF))

	def set_biome_color(self, x, z, r, g, b):
		cursor = BLOCK_DATA_SIZE + REGULAR_DATA_SIZE + BLOCKLIGHT_DATA_SIZE + SKYLIGHT_DATA_SIZE + ADDITIONAL_DATA_SIZE_DIRTY + (((z << 4) + x) * 4)
		value = struct.unpack_from(">i", self.data, cursor)[0]
		struct.pack_into(">i", self.data, cursor, value | ((r & 0xFF) << 16) | ((g & 0xFF) << 8) | (b & 0XFF))

	def get_biome(self, x, z):
		cursor = BLOCK_DATA_SIZE + REGULAR_DATA_SIZE + BLOCKLIGHT_DATA_SIZE + SKYLIGHT_DATA_SIZE + ADDITIONAL_DATA_SIZE_DIRTY + (((z << 4) + x) * 4)
		return (struct.unpack_from(">i", self.data, cursor)[0] >> 24)

	def set_biome(self, x, z, biome):
		cursor = BLOCK_DATA_SIZE + REGULAR_DATA_SIZE + BLOCKLIGHT_DATA_SIZE + SKYLIGHT_DATA_SIZE + ADDITIONAL_DATA_SIZE_DIRTY + (((z << 4) + x) * 4)
		value = (struct.unpack_from(">i", self.data, ((z << 4) + x) * 4)[0] & 0xFFFFFF) | (biome << 24)
		struct.pack_into(">i", self.data, cursor, value)

	def get_height(self, x, z):
		return self.data[BLOCK_DATA_SIZE + REGULAR_DATA_SIZE + BLOCKLIGHT_DATA_SIZE + SKYLIGHT_DATA_SIZE + (z << 4) + x]

	def set_height(self, x, z, height):
		self.data[BLOCK_DATA_SIZE + REGULAR_DATA_SIZE + BLOCKLIGHT_DATA_SIZE + SKYLIGHT_DATA_SIZE + (z << 4) + x] = height

	def load(self, data):
		self.data = data

	def dump(self):
		return self.data

def read_uint_4le(buffer, cursor):
	if(cursor % 1):
		return buffer[math.floor(cursor)] >> 4
	else:
		return buffer[cursor] & 15

def write_uint_4le(buffer, value, cursor):
	if(value >= 16):
		raise ValueError('value is out of bounds')

	byteLoc = math.floor(cursor)
	if(cursor % 1):
		buffer[byteLoc] = (value << 4 | read_uint_4le(buffer, math.floor(cursor)))
	else:
		buffer[byteLoc] = (read_uint_4le(buffer, byteLoc) << 4 | value)