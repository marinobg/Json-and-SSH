#Looking for AP for client nodeid
def scan(filename, nodeid):
	with open(filename, 'r') as infile:
		lines = infile.readlines()
	k = -1
	for i in range(0, len(lines)-1):
		k += 1
		if lines[i+1].strip() == '"ap": true,':
			ap = lines[i].strip()[1]
			if lines[i].strip()[2].isdigit():
				ap = lines[i].strip()[1:3]
			for n in range(k, min(k+10, len(lines))):
				if lines[n].strip()[0].isdigit():
					line = lines[n].strip()
					line = line.strip(',')
					if nodeid == line:
						return int(ap)




def dump_topology(nodeids):
	import json
	with open('topology.txt', 'r') as infile:
		lines = infile.readlines()

	isap = [False]*22
	isap[1] = True # Set APs manually
	results = {}
	for nodeid in nodeids:
		results[nodeid] = {}
		if isap[nodeid]:
			results[nodeid]['ap'] = True #Adding ap section
			results[nodeid]['clients'] = [] #Adding clients section
		else:
			results[nodeid]['ap'] = False

	for nodeid in nodeids:
		if results[nodeid]['ap'] == False:
			ap = scan('topology.txt', str(nodeid))
			results[ap]['clients'].append(int(nodeid))


	obj = open('top.json', 'w')
	json.dump(results, obj, indent=4)
	obj.close()



def read_json(filename):
	import json
	from pprint import pprint
	with open(filename, 'r') as f:
		topology = json.load(fp=f)

	for f in topology:
		print(topology[f]['ap'])



#read_json('topology_mar1.json')
dump_topology([1, 7])