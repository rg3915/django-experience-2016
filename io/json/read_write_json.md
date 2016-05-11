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
    'Location': 'Brasil',
    'Longitude': 20.76,
    'Latitude': 69.07
}

# abrindo um arquivo para escrever, e salvando os dados no arquivo
with open('io/json/test.json', 'w') as out_file:
    json.dump(my_dict, out_file, indent=4)
```

Resultado (arquivo `io/json/test.json`):

```json
{
    "Latitude": 69.07,
    "Name": "Regis",
    "Longitude": 20.76,
    "Location": "Brasil"
}
```

Você pode utilizar dicionários dentro de dicionários sem problemas, pois o
[módulo JSON do Python](https://docs.python.org/3/library/json.html) já cuida
disso para você: 

```python
import json

my_dict = {
    'Name': 'Regis',
    'Location': 'Brasil',
    'Geolocation': {
        'Longitude': 20.76,
        'Latitude': 69.07
    }
}

# abrindo um arquivo para escrever, e salvando os dados no arquivo
with open('io/json/test2.json', 'w') as out_file:
    json.dump(my_dict, out_file, indent=4)
```

Resultado (arquivo `io/json/test2.json`):

```json
{
    "Location": "Brasil",
    "Geolocation": {
        "Longitude": 20.76,
        "Latitude": 69.07
    },
    "Name": "Regis"
}
```

## Escrevendo JSON com Django

Entrando no shell do Django:

```console
$ python manage.py shell
```

Código:

```python
import json
from django.contrib.auth.models import User
from django.core.serializers import serialize

fields = ('id', 'username', 'email', 'date_joined')
with open('io/json/users.json', 'w') as file_handler:
    users_str = serialize('json', User.objects.all(), fields=fields)
    users_dict = json.loads(users_str)
    json_data = [user['fields'] for user in users_dict]
    json.dump({'users': json_data}, file_handler, indent=4)
```

São necessários três passos aqui para _limpar_ o resultado do `serialize`. Grosso modo, já poderíamos salvar como arquivo JSON o resultado do `serialize`, que é uma **string**:


```
[{"model": "auth.user", "pk": 1, "fields": {"username": "cuducos", "email": "", "date_joined": "2016-05-10T18:08:03.275Z"}}, {"model": "auth.user", "pk": 2, "fields": {"username": "admin", "email": "admin@adm.in", "date_joined": "2016-05-11T11:58:49.965Z"}}]
```

Mas talvez esse resultado seja muito poluído para o que queremos. Imagine que o que queremos é um JSON simples, somente com conteúdo do campo _fields_ de cada usuário.

Então transformamos a **string** *users_str* em um **dicionário** *users_dict* com o `json.loads(…)`. Se dermos um `print` em *users_dict* o resultado será parecido, mas agora temos **dicionários** em uma **lista** (ao invés de uma **string**):

```
[{'pk': 1, 'fields': {'email': '', 'date_joined': '2016-05-10T18:08:03.275Z', 'username': 'cuducos'}, 'model': 'auth.user'}, {'pk': 2, 'fields': {'email': 'admin@adm.in', 'date_joined': '2016-05-11T11:58:49.965Z', 'username': 'admin'}, 'model': 'auth.user'}]
```

Agora é mais simples de pegar apenas o campo _fields_ com uma _list comprehension_ `[user['fields'] for user in users_dict]`:

```
[{'email': '', 'date_joined': '2016-05-10T18:08:03.275Z', 'username': 'cuducos'}, {'email': 'admin@adm.in', 'date_joined': '2016-05-11T11:58:49.965Z', 'username': 'admin'}]
```

Gravando o JSON com esses dados temos como resultado (arquivo `io/json/users.json`):

```json
{
    "users": [
        {
            "email": "",
            "date_joined": "2016-05-10T18:08:03.275Z",
            "username": "cuducos"
        },
        {
            "email": "admin@adm.in",
            "date_joined": "2016-05-11T11:58:49.965Z",
            "username": "admin"
        }
    ]
}
```

### Exportando JSON a partir de um script em Python

Podemos criar um arquivo para exportar o JSON.

```python
# export_json.py

import json
from django.contrib.auth.models import User
from django.core.serializers import serialize

fields = ('id', 'username', 'email', 'date_joined')
with open('io/json/users.json', 'w') as file_handler:
    users_str = serialize('json', User.objects.all(), fields=fields)
    users_dict = json.loads(users_str)
    json_data = [user['fields'] for user in users_dict]
    json.dump({'users': json_data}, file_handler, indent=4)
```

Executando esse arquivo no shell do Django:

```console
$ ./manage.py shell < io/json/export_json.py
```

## Lendo JSON com Python

Entrando no shell do Python:

```console
$ python
```

Código:

```python
import json
with open('io/json/users.json') as file_handler:
    data = json.load(file_handler)
    for user in data['users']:
        print(user['username'], user['email'], user['date_joined'])
```

Resultado dos `print` do bloco anterior:

```
cuducos  2016-05-10T18:08:03.275Z
admin admin@adm.in 2016-05-11T11:58:49.965Z
```

## Importando dados de um JSON

A partir dos dados do bloco anterior já podemos popular o banco com os dados de `user`.

## Os comandos `dumpdata` e `loaddata` do Django

E por fim não podemos nos esquecer dos comandos `dumpdata` e `loaddata` do Django.

O `dumpdata` é para fazer o backup dos dados do banco de dados.

```console
$ python manage.py dumpdata --format=json --indent=2 > fixtures.json
```

O `loaddata` é para carregar dados json no banco de dados.

```console
$ python manage.py loaddata fixtures.json
```

Ambos os comandos — `dumpdata` e `loaddata` — adotam o formato de saída `serialize(…)` que limpamos na parte [Escrevendo JSON com Django](#escrevendo-json-com-django). Ou seja, se quisermos preparar dados para serem lidos pelo `loaddata` podemos salvar o arquivo direto com a **string** que `serialize(…)` retorna utilizando os [métodos de criação de arquivo de texto](../txt/read_write_txt.md).

---

Leia também:

* [JSON encoder and decoder][0]
* [Saving and loading data in Python with JSON][1]


[0]: https://docs.python.org/3/library/json.html
[1]: http://kaira.sgo.fi/2014/05/saving-and-loading-data-in-python-with.html