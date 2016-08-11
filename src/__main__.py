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
		chunk.setBlockType(x, 50, z, 2)
		chunk.setBiome(x, z, 0)
		chunk.setBiomeColor(x, z, 141, 184, 113)
		for y in range(128):
			chunk.setSkyLight(x, y, z, 15)
			chunk.setBlockLight(x, y, z, 15)

config = config.handleConfig()
server = PyRakLibServer(config['port'], True) # verbose
serverInstance = Handler()
handler = ServerHandler(server, serverInstance)
handler.sendOption("name", "MCPE;" + config['name'] + ";82 82;0.15.4;0;20")
print("starting server on *:19132")