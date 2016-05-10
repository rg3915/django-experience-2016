import json

my_dict = {
    'Name': 'Regis',
    'Location': u'Brasil',
    'Longitude': 20.76,
    'Latitude': 69.07
}

print(my_dict)
print('Location:', my_dict['Location'])

# Abrindo um arquivo para escrever
out_file = open('test.json', 'w')

# Salvando o dicionário no arquivo
json.dump(my_dict, out_file, indent=4)

# Fechando o arquivo
out_file.close()
