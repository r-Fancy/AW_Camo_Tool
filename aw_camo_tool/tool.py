import shutil
import os

BASE_PATH = "" # Edit this to your location of aw_camo_tool: C:/Users/fancy/Desktop/aw_camo_tool
OPTIONS = {
    'B': 'basic_weapon',
    'mk2': 'mk2', 'mk3': 'mk3', 'mk4': 'mk4', 'mk5': 'mk5',
    'mk6': 'mk6', 'mk7': 'mk7', 'mk8': 'mk8', 'mk9': 'mk9',
    'mk10': 'mk10', 'mk11': 'mk11', 'mk12': 'mk12', 'mk13': 'mk13',
    'mk14': 'mk14', 'mk15': 'mk15', 'mk16': 'mk16', 'mk17': 'mk17',
    'mk18': 'mk18', 'mk19': 'mk19', 'mk20': 'mk20', 'mk25': 'mk25'
}

user_option = input("Pick camo type: \n (B)asic Weapon, (mk2) - (mk20) & (mk25)... ")
file_location = input('Drag and drop the image you want to copy: ')

if user_option not in OPTIONS:
    print(f"Error: '{user_option}' is not a valid option")
    exit()

camo_type = OPTIONS[user_option]
output_folder = f"{BASE_PATH}/output/{camo_type}"
storage_file = f"{BASE_PATH}/storage/{camo_type}.txt"

os.makedirs(output_folder, exist_ok=True)

try:
    with open(storage_file, 'r') as file:
        names = [line.strip() for line in file 
                if line.strip() and not line.startswith('#')]
    
    for name in names:
        destination = f"{output_folder}/{name}"
        shutil.copy(src=file_location, dst=destination)
        print(f"Copied {name} to {camo_type} folder")
        
except FileNotFoundError:
    print(f"Error: Could not find storage file: {storage_file}")
except Exception as e:
    print(f"An error occurred: {e}")