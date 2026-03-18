import shutil
import os

BASE_PATH = "" # Edit this to your location of aw_camo_tool: C:/Users/fancy/Desktop/aw_camo_tool
OPTIONS = {
    'B': 'basic_weapon',
    'MK2': 'mk2',
    'MK15': 'mk15',
    'NON_ANIMATED': 'non_animated' 
    }

user_option = input("Pick camo type: \n (B)asic Weapon - non_animated - mk2 - mk15 \n").upper()
file_location = input('Drag and drop the image you want to copy: ')

if user_option not in OPTIONS:
    print(f"Error: '{user_option}' is not a valid option")
    exit()

file_extension = os.path.splitext(file_location)[1]

if not file_extension:
    print(f"Warning: No file extension found in {file_location}")
    file_extension = '.png'

camo_type = OPTIONS[user_option]
output_folder = f"{BASE_PATH}/output/{camo_type}"
storage_file = f"{BASE_PATH}/storage/{camo_type}.txt"

os.makedirs(output_folder, exist_ok=True)

try:
    with open(storage_file, 'r') as file:
        names = [line.strip() for line in file 
                if line.strip() and not line.startswith('#')]
    
    for name in names:
        destination = f"{output_folder}/{name}{file_extension}"
        shutil.copy(src=file_location, dst=destination)
        print(f"Copied {name} to {camo_type} folder")
        
except FileNotFoundError:
    print(f"Error: Could not find storage file: {storage_file}")
except Exception as e:
    print(f"An error occurred: {e}")