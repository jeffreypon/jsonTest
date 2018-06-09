import json

people_string = '''
{
    "people": [
        {
            "name": "john Smith",
            "phone": "615-555-1574",
            "emails": ["johnsmith@bousf.com", "john.smith@sdsfd.com"],
            "has_license": false
        },
        {
            "name": "hane doe",
            "phone": "123-555-2321",
            "emails": null,
            "has_license": true
        }
    ]
}
'''

data = json.loads(people_string)

print(type(data['people']))

for person in data['people']:
    del person['phone']

new_string = json.dumps(data, indent=2, sort_keys=True)
print(new_string)


