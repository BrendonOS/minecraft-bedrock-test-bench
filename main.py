from pyraklib.server import PyRakLibServer
from pyraklib.server import ServerHandler
from pyraklib.server import ServerInstance
from world import Chunk
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

class Handler(ServerInstance):
    def openSession(self, identifier, address, port, clientID):
    	print(identifier, address, port, clientID)

    def closeSession(self, identifier, reason): 
    	print(identifier, reason)

    def handleEncapsulated(self, identifier, packet, flags):
    	print(identifier, packet, flags)

    def handleRaw(self, address, port, payload):
    	print(address, port, payload)

    def notifyACK(self, identifier, identifierACK):
    	print(identifier, identifierACK)

    def handleOption(self, option, value):
    	print(option, value)

server = PyRakLibServer(19132)
serverInstance = Handler()
handler = ServerHandler(server, serverInstance)
handler.sendOption("name", "MCPE;A Minecraft: PE Server;82 82;0.15.4;0;20")