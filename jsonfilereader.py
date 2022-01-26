import json

"""
Json capability testing 
1. loaded json state mock data file into python for parsing.
2. Write the python object out to a json file
"""

with open('states.json') as f:
    data = json.load(f)

for state in data['states']:
    print(state['name'], state['abbreviation'])


# To write this file as json we will use the json.dump method. dump converts it to a json file. dump(s) = string
with open('new_states.json', 'w') as f:
    json.dump(data, f, indent=2)