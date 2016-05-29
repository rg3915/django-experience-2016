from django.utils import timezone

hashpass = 'pbkdf2_sha256$12000$Pe4addAsDo1D$xEtHWLnSIVkEppr4pbK69SBhuLwWsSHdXyhkCZBNktA='

USER_DICT = {
    'username': 'regis',
    'first_name': 'Regis',
    'last_name': 'Santos',
    'email': 'regis@example.com',
    'password': hashpass,
}

PERSON_DICT = {
    'gender': 'M',
    'treatment': 'sr',
    'first_name': 'Regis',
    'last_name': 'Santos',
    'slug': 'regis-santos',
    'birthday': '1985-12-01 02:42:30+00:00',
    'company': 'Acme',
    'department': 'Tecnologia',
    'email': 'regis@example.com',
    'cpf': '75873211795',
    'rg': '911225341',
    'cnpj': '42238377000123',
    'ie': 'isento',
    'address': 'Rua São Leopoldo, 101',
    'complement': 'Apto 303',
    'district': 'Belezinho',
    'city': 'São Paulo',
    'uf': 'SP',
    'cep': '03055000',
    'active': True,
    'blocked': False,
}

EMPLOYEE_DICT = {
    'username': 'regis',
    'first_name': 'Regis',
    'last_name': 'Santos',
    'email': 'regis@example.com',
    'password': hashpass,
    'gender': 'M',
    'treatment': 'sr',
    'slug': 'regis',
    'birthday': '1985-12-01 02:42:30+00:00',
    'company': 'Acme',
    'department': 'Tecnologia',
    'cpf': '28586897337',
    'rg': '418757896',
    'address': 'Rua Rafael Barbosa',
    'complement': '15º andar',
    'district': 'Vila Andradina',
    'city': 'Goiás',
    'uf': 'GO',
    'cep': '74665841',
    'active': True,
    'blocked': False,
    'date_release': timezone.now(),
}
