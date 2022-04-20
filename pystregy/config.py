import os 
dir_path = os.path.dirname(os.path.realpath(__file__))  
with open(dir_path + '/api_key.txt', 'r') as f:
    API_KEY = f.read()