# Apps e Tabelas

Veja em [tables_django.md][0] a relação de apps e tabelas usadas no projeto.

### Bookstore

**Bookstore** será uma app separada do escopo principal. Inicialmente ela tem uma modelagem, puramente didática, que mostra como funciona alguns tipos de relacionamentos do Django, por exemplo:

* [abstract-base-classes][1]
* [multi-table-inheritance][2]
* [proxy-models][3]

### Core

Base do projeto. Nele constam algumas tabelas abstratas como:

* TimeStampedModel
* Address

### CRM

Gerenciamento de pessoas, funcionários, clientes e fornecedores.

#### Customer

A tabela *Customer* é um *proxy model* de *Person*. Seu comportamento será dado pelo *person_type* igual a "customer".

#### Employee

A tabela *Employee* é herdada de *User*. Permitindo o acesso do funcionário ao sistema de login.

#### Seller

A tabela *Seller* é um *proxy model* de *Employee*. Seu comportamento será dado pelo *occupation* igual a "Vendedor".


### Product

Descrição dos produtos.

### Selling

Gerenciamento de vendas.

### Buying

Cria pedidos de compras.

### Proposal

Gerenciamento de orçamentos.

### Stock

Gerenciamento de estoque e recebimento de produtos.






## Modelos

Para gerar o gráfico do modelo façamos o seguinte:

```bash
sudo apt-get install graphviz libgraphviz-dev pkg-config
pip install pygraphviz
git clone https://github.com/nlhepler/pydot
cd pydot
python setup.py install
cd ..
rm -rf pydot
pip install django-extensions
pip install pyparsing
```

Para gerar o gráfico

```console
./manage.py graph_models -a -g -o dev/djexperience.png
```

Eu criei um Makefile onde você pode digitar, por exemplo:

```console
make mer n="02"
```

![mer](dj-exp03.png)

## Gerando dados randômicos

## Comandos personalizados


[0]: https://github.com/rg3915/django-experience/blob/master/dev/tables_django.md
[1]: https://docs.djangoproject.com/en/1.9/topics/db/models/#abstract-base-classes
[2]: https://docs.djangoproject.com/en/1.9/topics/db/models/#multi-table-inheritance
[3]: https://docs.djangoproject.com/en/1.9/topics/db/models/#proxy-models