def read_json(filename):
	import json
	from pprint import pprint
	with open(filename, 'r') as f:
		topology = json.load(fp=f)

	for f in topology:
		print(topology[f]['ap'])



read_json('topology_mar1.json')