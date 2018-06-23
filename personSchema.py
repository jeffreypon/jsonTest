import json
import jsonschema

with open('person.json') as f:
    personData = json.load(f)

with open('person.jsd') as f:
    personSchema = json.load(f)

jsonschema.validate(personData, personSchema)