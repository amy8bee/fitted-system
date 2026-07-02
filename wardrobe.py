import json

def load_wardrobe(filename="wardrobe.json"):
    with open(filename, "r") as file:
        return json.load(file)
        