# Ementa

O objetivo inicial é cumprir esta ementa:

## Python e Django geral

- [ ] IO
  - [x] [Ler/escrever TXT](io/txt/read_write_txt.md)
  - [x] [Ler/escrever CSV](io/csv/read_write_csv.md)
  - [ ] Ler/escrever XML
  - [x] [Ler/escrever JSON](io/json/read_write_json.md)

## Customizar Django Admin

- [x] Tela de login no admin
  - [x] Inserir logo e rodapé na [tela de login](http://localhost:8000/admin/) e alterar o texto de _Administração do Django_ para o nome do projeto
  - [x] Alterar o plano de fundo da [tela de login](http://localhost:8000/admin/)
- [x] Landing page (sugestões: [Start Bootstrap](http://startbootstrap.com/template-categories/all/) e [One Page Love](https://onepagelove.com/templates/free-templates))

## Backend

- [x] Entendendo os modelos do Django
  - [x] [One to One](dev/orm#one-to-one-um-para-um)
  - [x] [One to Many](dev/orm#one-to-many-um-para-muitos)
  - [x] [Many to Many](dev/orm#many-to-many-muitos-para-muitos)
  - [x] [Abstract Model](dev/orm#abstract-inheritance-herança-abstrata)
  - [x] [Multi table inheritance](dev/orm#multi-table-inheritance-herança-multi-tabela)
  - [x] [Proxy models](dev/orm#proxy-models)
  - [x] [Extendendo a classe User](https://github.com/rg3915/django-experience/issues/21)
- [x] Herança de templates
- [x] CRUD
  - [x] [Function Based Views](https://github.com/rg3915/django-experience/issues/26)
  - [x] [Class Based Views](https://github.com/rg3915/django-experience/issues/33)
- [x] [Mixins](https://github.com/rg3915/django-experience/issues/35)
- [x] [Managers](https://github.com/rg3915/django-experience/issues/36)
- [x] [Custom template tags](https://github.com/rg3915/django-experience/issues/19)
- [x] [Várias formas de se fazer um formulário](https://github.com/rg3915/django-experience/wiki/V%C3%A1rias-formas-de-se-fazer-um-formul%C3%A1rio)
- [ ] Inlineformset_factory
- [ ] Aggregate and Annotate
- [ ] Filtros com dois ou mais campos de listagem
- [ ] Buscas múltiplas
  - [ ] Consultas avançadas, um template com vários campos de busca (por exemplo: nome, cidade, bairro, etc.)
- [ ] Consumindo o DRF

## manager.py

- [x] [Dominando o Shell do Django](https://github.com/rg3915/django-experience/wiki/Dominando-o-shell-do-Django)
- [ ] Importando dados de CSV
- [ ] Inserindo dados randômicos
- [ ] Criando novos comandos personalizados

## Extensões e pacotes externos

- [x] [JSON e DataTable](dev/#json-e-datatable)
- [x] [Exportar para Excel com xlwt](dev/#exportar-para-excel-com-xlwt)
- [x] [Exportar para Excel com django-import-export](dev/#exportar-para-excel-com-django-import-export)
- [ ] Django Rest Framework
- [ ] Selenium
- [ ] Gráficos