import json

fileName = "www.netflix.com_12-09-2024.json"

with open(fileName, "r") as file:
    data = json.load(file)
    b = json.loads
    for key, value in data.items():
        if isinstance(value, list):
            # print(value)
            for item in value:
                for k, v in item.items():
                    print(f"{k}: {v}")
        else:
            pass
            print(f"{key}: {value}")