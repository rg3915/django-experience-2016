# Ler/escrever TXT

## Escrevendo txt em Python

```bash
$ python
```

```python
with open('io/file.txt', 'w') as f:
    f.write('Um\n')
    f.write('Dois\n')
```

```python
lista = ['Um', 'Dois', 'Três', 'Quatro']
with open('io/file.txt', 'w') as f:
    for l in lista:
        f.write(l + '\n')
```

## Escrevendo txt com Django

```bash
$ ./manage.py shell
```

```python
from django.contrib.auth.models import User
users = User.objects.all()
with open('io/users.txt', 'w') as f:
    for user in users:
        f.write(user.username + ',' + user.email + ',' + str(user.date_joined) + '\n')
```

## Lendo txt em Python

```bash
$ python
```

```python
f = open('io/file.txt', 'r')
f.read(), type(f.read())

f = open('io/file.txt', 'r')
f.readline()
f.readline()

f = open('io/file.txt', 'r')
for line in f: print(line)

with open('io/file.txt', 'r') as f:
    lines = f.readlines()

type(lines)

with open('io/file.txt', 'r') as f:
    lines = f.read()

type(lines)

with open('io/file.txt', 'r') as f:
    for line in f:
        print(line)
```

Por fim usaremos:

```python
with open('io/file.txt', 'r') as f:
    lines = f.readlines()

type(lines)
```

pois ele retorna uma lista.

### Lendo txt direto pelo bash com Python

```python
# read_file.py
from sys import argv
script, filename = argv
txt = open(filename)
print(txt.read())
```

```bash
$ python read_file.py file.txt
```