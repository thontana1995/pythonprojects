import sys
import clipboard 
import json

SAVE_DATA = 'clipboard,json'

def save_data(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)

def load_data(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return {}

if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVE_DATA)
    
    if command == 'save':
        key = input('Enter a key: ')
        data[key] = clipboard.paste()
        save_data(SAVE_DATA,data)
        print('Data saved!')
    elif command == 'load':
        key = input('Enter a key: ')
        if key in data:
            clipboard.copy(data[key])
            print('Data copied to clipboard')
    elif command == 'list':
        print(data)
    else:
        print('Unknow command')
else:
    print('Please pass exactly one command.')

