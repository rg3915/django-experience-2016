# Ler/Escrever csv

## Escrevendo csv com Python

```bash
$ python
```

```python
import csv
with open('file.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',')
    lista = ['Um', 'Dois', 'Três', 'Quatro']
    spamwriter.writerow(lista)
```

## Escrevendo csv com Django

```bash
$ ./manage.py shell
```

```python
import csv
from django.contrib.auth.models import User
users = User.objects.all().values_list('id', 'username', 'email', 'date_joined')
with open('users.csv', 'w', newline='') as csvfile:
    user_writer = csv.writer(csvfile, delimiter=',')
    titles = ['id','username','email','date_joined']
    user_writer.writerow(titles)
    for user in users:
        user_writer.writerow(user)
```

### Exportando csv a partir de um script em Python

Podemos criar um arquivo para exportar o csv.

```python
# export_csv.py
import csv
from django.contrib.auth.models import User
users = User.objects.all().values_list('id', 'username', 'email', 'date_joined')
with open('users.csv', 'w', newline='') as csvfile:
    user_writer = csv.writer(csvfile, delimiter=',')
    titles = ['id','username','email','date_joined']
    user_writer.writerow(titles)
    for user in users:
        user_writer.writerow(user)
```

```bash
$ ./manage.py shell < export_csv.py
```

## Lendo csv com Python

```bash
$ python
```

```python
import csv
with open('users.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        print(row)
    csvfile.close()
```

Note que ele retorna uma **lista**.

Para retornar um **dicionário** façamos:

```python
import csv
with open('users.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['id'], row['username'], row['email'], row['date_joined'])
    csvfile.close()
```


## Importando dados de um csv

```python
import csv
address_list = []
with open('address.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        address_list.append(row)
    f.close()
```

A partir daí iremos popular o banco com os dados de `address_list`.

Leia também:

[CSV File Reading and Writing][0]
[Outputting CSV with Django][1]

[0]: https://docs.python.org/3/library/csv.html
[1]: https://docs.djangoproject.com/ja/1.9/howto/outputting-csv/
