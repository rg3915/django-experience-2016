# Ler/escrever CSV

## Escrevendo CSV em Python

Entrando no shell do Python:

```console
$ python
```

Código:

```python
import csv

with open('io/csv/file.csv', 'w') as file_handler:
    csv_writer = csv.writer(file_handler)

    # escrever uma linha com o writerow (singular)
    csv_writer.writerow([1, 'Um', 'One'])

    # escrever mais de uma linha com o wroterows (plural)
    extra_rows = [[2, 'Dois', 'Two'], [3, 'Três', 'Three']]
    csv_writer.writerows(extra_rows)
```

Resultado (arquivo `io/files.csv`):

```
1,Um,One
2,Dois,Two
3,Três,Three
```

Você pode utilizar valor com vírgulas sem problemas, pois o [módulo CSV do Python](https://docs.python.org/3.5/library/csv.html) já cuida disso para você:

```python
with open('io/csv/file.csv', 'w') as file_handler:
    csv_writer = csv.writer(file_handler)
    csv_writer.writerow(['Um, dois', 'Três, quatro', 'Cinco'])
```

Resultado (arquivo `io/csv/files.csv`):

```
"Um, dois","Três, quatro",Cinco
```

## Escrevendo CSV com Django

Entrando no shell do Django:

```console
$ python manage.py shell
```

Código:

```python
import csv
from django.contrib.auth.models import User
with open('io/csv/users.csv', 'w') as file_handler:
    csv_writer = csv.writer(file_handler)
    for user in User.objects.all():
        csv_writer.writerow([user.username, user.email,str(user.date_joined)])
```

Resultado (arquivo `io/users.csv`):

```console
admin,admin@example.com,2016-05-09 19:50:52+00:00
regis,regis@example.com,2016-05-10 17:27:44+00:00
```

### Exportando CSV a partir de um script em Python

Podemos criar um arquivo para exportar o CSV.

```python
# export_csv.py

import csv
from django.contrib.auth.models import User

header = ('id', 'username', 'email', 'date_joined')
users = User.objects.all().values_list(*header)
with open('io/csv/users.csv', 'w') as csvfile:
    user_writer = csv.writer(csvfile)
    user_writer.writerow(header)
    for user in users:
        user_writer.writerow(user)
```

Executando esse arquivo no shell do Django:

```console
$ ./manage.py shell < io/csv/export_csv.py
```

## Lendo CSV com Python

Entrando no shell do Python:

```console
$ python
```

Código:

```python
import csv
with open('io/csv/users.csv') as csvfile:
    users_reader = csv.reader(csvfile)
    for row in users_reader:
        print(row)
```

Resultado dos `print` do bloco anterior:

```
['id', 'username', 'email', 'date_joined']
['1', 'admin', '', '2016-05-09 21:12:00.471315+00:00']
['2', 'joao', 'j@j.com', '2016-05-10 18:32:29.424863+00:00']
```

Note que cada `row` é uma **lista** de strings. Para retornar um
**dicionário** podemos fazer:

```python
import csv
with open('io/csv/users.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['id'], row['username'], row['email'], row['date_joined'])
```

Resultado dos `print` do bloco anterior:

```
1 admin  2016-05-09 21:12:00.471315+00:00
2 joao j@j.com 2016-05-10 18:32:29.424863+00:00
```

Caso os cabeçalhos não sejam a 1ª linha do CSV, podemos passar uma _lista_ com
os cabeçalhos para o `DictReader` utilizando o argumento _fieldnames_:

```python
import csv
header = ('numero', 'portugues', 'ingles')
with open('io/csv/file.csv') as csvfile:
    reader = csv.DictReader(csvfile, fieldnames=header)
    for row in reader:
        print(row['numero'], row['portugues'], row['ingles'])
```

Resultado dos `print` do bloco anterior:

```
1 Um One
2 Dois Two
3 Três Three
```

## Importando dados de um CSV

```python
import csv
address_list = []
with open('io/csv/address.csv') as file_handler:
    reader = csv.DictReader(file_handler)
    for row in reader:
        address_list.append(row)
```

A partir daí iremos popular o banco com os dados de `address_list`.

Leia também:

* [CSV File Reading and Writing][0]
* [Outputting CSV with Django][1]


[0]: https://docs.python.org/3/library/csv.html
[1]: https://docs.djangoproject.com/ja/1.9/howto/outputting-csv/
