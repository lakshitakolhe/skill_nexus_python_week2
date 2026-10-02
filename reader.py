import json

file = open("data.json", "w")
file.write('{"name": "Lakshita", "age": 20, "course": "CSE"}')
file.close()

file = open("data.json", "r")
data = json.load(file)
file.close()

print("Formatted JSON Data:")
print(json.dumps(data, indent=4))