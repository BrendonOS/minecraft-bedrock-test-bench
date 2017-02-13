from pyraklib.server import PyRakLibServer
from pyraklib.server import ServerHandler
from world import Chunk
from handler import Handler
import config
import time
import sys

# create a chunk for use in logging in
chunk = Chunk()
for x in range(16):
	for z in range(16):
		chunk.set_block_type(x, 50, z, 2)
		chunk.set_biome(x, z, 0)
		chunk.set_biome_color(x, z, 141, 184, 113)
		for y in range(128):
			chunk.set_sky_light(x, y, z, 15)
			chunk.set_block_light(x, y, z, 15)

config = config.handle_config()
server = PyRakLibServer(config['port'])
serverInstance = Handler()
handler = ServerHandler(server, serverInstance)
handler.sendOption("name", "MCPE;" + config['name'] + ";82;0.15.4;0;20")
print("starting server on *:" + str(config['port']))
