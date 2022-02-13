graph = {}

graph['start'] = ['A', 'B']
graph['A'] = ['finish']
graph['B'] = ['A', 'finish']
graph['finish'] = []

graph['start'] = {}
graph['start']['A'] = 6
graph['start']['B'] = 2

graph['A'] = {}
graph['A']['finish'] = 1

graph['B'] = {}
graph['B']['A'] = 3
graph['B']['finish'] = 5

graph['finish'] = {}


costs = {}
costs['A'] = 6
costs['B'] = 2
costs['finish'] = float('inf')


parents = {}
parents['A'] = 'start'
parents['B'] = 'start'
parents['finish'] = None


processed = []


