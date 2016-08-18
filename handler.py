from pyraklib.server import ServerInstance

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