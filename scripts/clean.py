import urllib.request
from pathlib import Path
import json
import re


def load():
    # Grab from: https://raw.githubusercontent.com/Mojang/bedrock-samples/main/resource_pack/ui/settings_sections/world_section.json
    urllib.request.urlretrieve("https://raw.githubusercontent.com/Mojang/bedrock-samples/main/resource_pack/ui/settings_sections/world_section.json", "raw.json")

    # load JSON data from file
    with open('raw.json') as file:
        data = removeComments(file.read())

    return json.loads(data)

def write(data,name):
    file = name + ".json"
    with open(file, 'w') as newFile:
        newFile.write(data)


def removeComments(data):
    data = re.sub(re.compile("/\*.*?\*/",re.DOTALL ) ,"" ,str(data)) # remove all occurrences streamed comments (/*COMMENT */) from string
    data = re.sub(re.compile('[^".*:.*"]//.*\n' ) ,"" , str(data)) # remove all occurrence single-line comments (//COMMENT\n ) from string
    data = re.sub(re.compile("/\*{2,}" ) ,"" , str(data)) # remove all occurrence single-line comments (/** ) from string
    data = re.sub(re.compile("^\+\*.*" ) ,"" , str(data)) # remove all occurrence single-line comments (+* ) from string
    
    return data

def findKeys(data):
    # print(json.dumps(data,sort_keys=True,indent=2))
    result = re.findall('"level_seed.*"', json.dumps(data,sort_keys=True,indent=4))
    
    for index, item in enumerate(result, start=0):
        result[index] = item.replace('"','')
    
    print(f"Keys to be removed:\t{result}\n")
    return result

def removeKeys(data):
    # key to remove
    keyToFind = findKeys(data)
    indexToRemove = []


    for key in keyToFind:
        print(f"\nLooking for key:\t{key}")
        for index, obj in enumerate(data['game_section']['controls'], start=0):
            if key in obj:
                print(f"Found Key:\t{str(key)}")
                indexToRemove.append(index)
                removed_value = data['game_section']['controls'].pop(index)
                print(f"Removed key '{key}' with value: {removed_value}\n")

    # saving the updated JSON data back to the file
    with open('HideMySeed/ui/settings_sections/world_section.json', 'w') as file:
        json.dump(data, file, indent=2)


if __name__ == "__main__":
    data = load()
    removeKeys(data)
    p = Path('raw.json')
    Path.unlink(p,True)