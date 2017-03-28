GENDER = (('M', 'Masculino'), ('F', 'Feminino'))

TREATMENT = (
    ('a', 'Arq.'),
    ('aa', 'Arqa.'),
    ('d', 'Dona'),
    ('dr', 'Dr.'),
    ('dra', 'Dra.'),
    ('e', 'Eng.'),
    ('ea', 'Engª.'),
    ('p', 'Prof.'),
    ('pa', 'Profa.'),
    ('sr', 'Sr.'),
    ('sra', 'Sra.'),
    ('srta', 'Srta.'),
)


PHONE_TYPE = (
    ('pri', 'principal'),
    ('com', 'comercial'),
    ('res', 'residencial'),
    ('cel', 'celular'),
    ('cl', 'Claro'),
    ('oi', 'Oi'),
    ('t', 'Tim'),
    ('v', 'Vivo'),
    ('n', 'Nextel'),
    ('fax', 'fax'),
    ('o', 'outros'),
)

METHOD_PAID = (
    ('vi', 'a vista'),
    ('bo', 'boleto'),
    ('ch', 'cheque'),
    ('de', 'débito'),
    ('cr', 'crédito'),
)

STATUS_LIST = (
    ('c', 'cancelado'),
    ('p', 'pendente'),
    ('a', 'aprovado')
)

PERSON_TYPE = (
    ('c', 'cliente'),
    ('p', 'contato'),
    ('f', 'fornecedor'),
)

CUSTOMER_TYPE = (
    ('c', 'construtora'),
    ('a', 'arquitetura'),
    ('p', 'particular')
)

COMPANY_TYPE = (
    ('c', 'comércio'),
    ('i', 'indústria'),
    ('a', 'agronomia'),
)
