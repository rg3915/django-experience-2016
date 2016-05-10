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