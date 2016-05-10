# Django Experience

Django Experience é um projeto que visa experimentar, explorar e colocar em práticas os recursos do [Django][0] num projeto real.

## Ementa

Veja a [ementa][1] inicial.

## Versões

Estamos utilizando

* [Python][2] 3.5.0
* [Django][0] 1.9.6
* [Virtualenv][3] 15.0.1

## Wiki

Leia a [wiki][4].

## Como desenvolver?

* Clone o repositório.
* Crie um virtualenv com Python 3.5.
* Ative o virtualenv.
* Instale as dependências.
* Configure a instância com o `.env`.
* Execute as migrações no banco de dados.
* Execute os testes.

```console
git clone https://github.com/rg3915/django-experience.git
cd django-experience
python -m venv .venv
source .venv/bin/activate
PS1="(`basename \"$VIRTUAL_ENV\"`):/\W$ " # opcional (insere nome do virtualenv no terminal)
python -m pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py migrate
python manage.py test
```

## Como fazer o deploy

## Changelog

[0]: https://www.djangoproject.com/
[1]: https://github.com/rg3915/django-experience/blob/master/ementa.md
[2]: https://www.python.org/
[3]: https://virtualenv.readthedocs.org
[4]: https://github.com/rg3915/django-experience/wiki