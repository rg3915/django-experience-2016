<<<<<<< HEAD
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


# done
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
=======
# Ler/Escrever txt

## Escrevendo CSV em Python

Entrando no shell do Python:

```console
$ python
```

Código:

```python
import csv

with open('io/file.csv', 'w') as file_handler:
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

Você pode utilizar valor com vírgulas sem problemas, pois o [módulo CSV do Python](https://docs.python.org/3.5/library/csv.html) já cuida disso para você

```python
with open('io/file.csv', 'w') as file_handler:
    csv_writer = csv.writer(file_handler)
    csv_writer.writerow(['Um, dois', 'Três, quatro', 'Cinco'])
```

Resultado (arquivo `io/files.csv`):

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

with open('io/file.csv', 'w') as file_handler:
    csv_writer = csv.writer(file_handler)
    for user in User.objects.all():
        csv_writer.writerow([user.username, user.email,str(user.date_joined)])
```

Resultado (arquivo `io/files.csv`):

```console
$ cat io/file.csv
fulano,fulano@servidor.org.br,2016-05-10 18:08:03.275318+00:00
```

## Lendo CSV em Python

Entrando no shell do Python:

```console
$ python
```

Código:

```python
import csv 

headers = ['Inteiro', 'Português', 'Inglês']
with open('io/file.csv', 'r') as file_handler:
    csv_reader = csv.reader(file_handler)
    for line in csv_reader:
        print(line)
        values = dict(zip(headers, line))
        print(values)
        print()
```

Resultados dos `print`:

```
['1', 'Um', 'One']
{'Inteiro': '1', 'Inglês': 'One', 'Português': 'Um'}

['2', 'Dois', 'Two']
{'Inteiro': '2', 'Inglês': 'Two', 'Português': 'Dois'}

['3', 'Três', 'Three']
{'Inteiro': '3', 'Inglês': 'Three', 'Português': 'Três'}
```

> Repare que todos os valores são lidos como _strings_.
>>>>>>> a3c3c3790c5492ef836e35a73a192547edabbbb8
