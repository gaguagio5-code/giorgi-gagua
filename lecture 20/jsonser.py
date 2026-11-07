import json

data = {
    "apple": 1,
    "banana": 2,
    "orange": 3,
    "grape": 4,
}

json_string = json.dumps(data,indent=4)
print(json_string)