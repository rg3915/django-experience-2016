# Ler/escrever JSON

## Escrevendo JSON em Python

Entrando no shell do Python:

```console
$ python
```

Código:

```python
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
```

Resultado:

```console
{
    "Latitude": 69.07,
    "Name": "Regis",
    "Longitude": 20.76,
    "Location": "Brasil"
}
```

Leia também:

[JSON encoder and decoder][0]

[Saving and loading data in Python with JSON][1]

[0]: https://docs.python.org/3/library/json.html
[1]: http://kaira.sgo.fi/2014/05/saving-and-loading-data-in-python-with.html