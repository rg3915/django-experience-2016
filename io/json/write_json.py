import json

my_dict = {
    'Name': 'Regis',
    'Location': 'Brasil',
    'Longitude': 20.76,
    'Latitude': 69.07
}

# abrindo um arquivo para escrever, e salvando os dados no arquivo
with open('io/json/test.json', 'w') as out_file:
    json.dump(my_dict, out_file, indent=4)
