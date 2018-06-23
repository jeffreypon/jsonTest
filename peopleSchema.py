import json
import jsonschema

with open('people.json') as f:
    peopleData = json.load(f)

with open('people.jsd') as f:
    peopleSchema = json.load(f)

jsonschema.validate(peopleData, peopleSchema)