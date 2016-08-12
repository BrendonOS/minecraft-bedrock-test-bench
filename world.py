import math
import struct

BLOCK_DATA_SIZE = 16 * 16 * 128
REGULAR_DATA_SIZE = 16384
SKYLIGHT_DATA_SIZE = 16384
BLOCKLIGHT_DATA_SIZE = 16384
ADDITIONAL_DATA_SIZE_DIRTY = 256
ADDITIONAL_DATA_SIZE_COLOR = 1024
BUFFER_SIZE = BLOCK_DATA_SIZE + REGULAR_DATA_SIZE + SKYLIGHT_DATA_SIZE + BLOCKLIGHT_DATA_SIZE + ADDITIONAL_DATA_SIZE_COLOR + ADDITIONAL_DATA_SIZE_DIRTY

class Chunk():
	def __init__(self):
		self.data = bytearray(BUFFER_SIZE)

	def getBlockType(self, x, y, z):
		return self.data[x + 16 * (z + 16 * y)] & 0xff

	def setBlockType(self, x, y, z, id):
		self.data[x + 16 * (z + 16 * y)] = id

	def getBlockData(self, x, y, z):
		return readUInt4LE(self.data, BLOCK_DATA_SIZE + ((x + 16 * (z + 16 * y)) * 0.5))

	def setBlockData(self, x, y, z, data):
		writeUInt4LE(self.data, data, BLOCK_DATA_SIZE + ((x + 16 * (z + 16 * y)) * 0.5))
		
	def getBlockLight(self, x, y, z):
		return readUInt4LE(self.data, BLOCK_DATA_SIZE + REGULAR_DATA_SIZE + ((x + 16 * (z + 16 * y)) * 0.5))

	def setBlockLight(self, x, y, z, light):
		writeUInt4LE(self.data, light, BLOCK_DATA_SIZE + REGULAR_DATA_SIZE + ((x + 16 * (z + 16 * y)) * 0.5))

	def getSkyLight(self, x, y, z):
		return readUInt4LE(self.data, BLOCK_DATA_SIZE + REGULAR_DATA_SIZE + BLOCKLIGHT_DATA_SIZE + ((x + 16 * (z + 16 * y)) * 0.5))

	def setSkyLight(self, x, y, z, light):
		writeUInt4LE(self.data, light, BLOCK_DATA_SIZE + REGULAR_DATA_SIZE + BLOCKLIGHT_DATA_SIZE + ((x + 16 * (z + 16 * y)) * 0.5))

	def getBiomeColor(self, x, z):
		color = (struct.unpack_from(">i", self.data, BLOCK_DATA_SIZE + REGULAR_DATA_SIZE + BLOCKLIGHT_DATA_SIZE + SKYLIGHT_DATA_SIZE + ADDITIONAL_DATA_SIZE_DIRTY + (((z << 4) + x) * 4))[0] & 0xFFFFFF)
		return ((color >> 16), ((color >> 8) & 0xFF), (color & 0xFF))

	def setBiomeColor(self, x, z, r, g, b):
		cursor = BLOCK_DATA_SIZE + REGULAR_DATA_SIZE + BLOCKLIGHT_DATA_SIZE + SKYLIGHT_DATA_SIZE + ADDITIONAL_DATA_SIZE_DIRTY + (((z << 4) + x) * 4)
		value = struct.unpack_from(">i", self.data, cursor)[0]
		struct.pack_into(">i", self.data, cursor, value | ((r & 0xFF) << 16) | ((g & 0xFF) << 8) | (b & 0XFF))

	def getBiome(self, x, z):
		cursor = BLOCK_DATA_SIZE + REGULAR_DATA_SIZE + BLOCKLIGHT_DATA_SIZE + SKYLIGHT_DATA_SIZE + ADDITIONAL_DATA_SIZE_DIRTY + (((z << 4) + x) * 4)
		return (struct.unpack_from(">i", self.data, cursor)[0] >> 24)

	def setBiome(self, x, z, biome):
		cursor = BLOCK_DATA_SIZE + REGULAR_DATA_SIZE + BLOCKLIGHT_DATA_SIZE + SKYLIGHT_DATA_SIZE + ADDITIONAL_DATA_SIZE_DIRTY + (((z << 4) + x) * 4)
		value = (struct.unpack_from(">i", self.data, ((z << 4) + x) * 4)[0] & 0xFFFFFF) | (biome << 24)
		struct.pack_into(">i", self.data, cursor, value)

	def getHeight(self, x, z):
		return self.data[BLOCK_DATA_SIZE + REGULAR_DATA_SIZE + BLOCKLIGHT_DATA_SIZE + SKYLIGHT_DATA_SIZE + (z << 4) + x]

	def setHeight(self, x, z, height):
		self.data[BLOCK_DATA_SIZE + REGULAR_DATA_SIZE + BLOCKLIGHT_DATA_SIZE + SKYLIGHT_DATA_SIZE + (z << 4) + x] = height

	def load(self, data):
		self.data = data

	def dump(self):
		return self.data

def readUInt4LE(buffer, cursor):
	if(cursor % 1):
		return buffer[math.floor(cursor)] >> 4
	else:
		return buffer[cursor] & 15

def writeUInt4LE(buffer, value, cursor):
	if(value >= 16):
		raise ValueError('value is out of bounds')

	byteLoc = math.floor(cursor)
	if(cursor % 1):
		buffer[byteLoc] = (value << 4 | readUInt4LE(buffer, math.floor(cursor)))
	else:
		buffer[byteLoc] = (readUInt4LE(buffer, byteLoc) << 4 | value)