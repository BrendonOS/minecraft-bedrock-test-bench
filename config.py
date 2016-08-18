import json
import os.path

# todo , make this oop
def generate_config():
	target = open('settings.json', 'w')
	config = """
	{
		\"port\": 19132,
		\"name\": \"A Minecraft: PE Server\"
	}
	"""
	parsed = json.loads(config)
	target.write(json.dumps(parsed, indent = 4, sort_keys = True))

def load_config():
	with open('settings.json', 'r') as handle:
		parsed = json.load(handle)
		return parsed

def handle_config():
	if os.path.isfile('settings.json'):
		return load_config()
	else:
		generate_config()
		return load_config()