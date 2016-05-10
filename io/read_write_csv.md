# Ler/Escrever csv

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
with open('io/users.csv', 'w') as file_handler:
    csv_writer = csv.writer(file_handler)
    for user in User.objects.all():
        csv_writer.writerow([user.username, user.email,str(user.date_joined)])
```

Resultado (arquivo `io/users.csv`):

```console
$ cat io/users.csv
admin,admin@example.com,2016-05-09 19:50:52+00:00
regis,regis@example.com,2016-05-10 17:27:44+00:00
```

aqui

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
