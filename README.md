# Django Experience

Django Experience é um projeto que visa experimentar, explorar e colocar em práticas os recursos do [Django][0] num projeto real.

## Ementa

Veja a [ementa][1] inicial.

## Versões

Estamos utilizando

* [Python][2] 3.5.0
* [Django][0] 1.9.6
* [Virtualenv Wrapper][3] 4.7.1

## Wiki

Leia a [wiki][4].

## Como desenvolver?

Baixe e rode o `setup.sh`.

```bash
# wget https://raw.githubusercontent.com/rg3915/django-experience/master/setup.sh
# source setup.sh
```

Ou siga o passo a passo.

* Clone o repositório.
* Crie um virtualenv com Python 3.5
* Ative o virtualenv.
* Instale as dependências.
* Configure a instância com o .env
* Carregue os dados no banco
* Execute os testes.

```bash
git clone https://github.com/rg3915/django-experience.git
cd django-experience
python -m venv .venv
source .venv/bin/activate
PS1="(`basename \"$VIRTUAL_ENV\"`):/\W$ " # opcional
pip install -r requirements-dev.txt
cp contrib/env-sample .env
# make initial
python manage.py test
```

## Como fazer o deploy

## Changelog


[0]: https://www.djangoproject.com/
[1]: https://github.com/rg3915/django-experience/blob/master/ementa.md
[2]: https://www.python.org/
[3]: http://virtualenvwrapper.readthedocs.io/en/latest/
[4]: https://github.com/rg3915/django-experience/wiki