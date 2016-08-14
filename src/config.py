import json
import os.path

# TODO, this is stupid, be smart
def generateConfig():
	target = open('settings.json', 'w')
	config = '{"port": 19132, "name": "A Minecraft: PE Server"}'
	parsed = json.loads(config)
	target.write(json.dumps(parsed, indent=4, sort_keys=True))

def loadConfig():
	with open('settings.json', 'r') as handle:
		parsed = json.load(handle)
		return parsed

def handleConfig():
	if os.path.isfile('settings.json'):
		return loadConfig()
	else:
		generateConfig()
		return loadConfig()