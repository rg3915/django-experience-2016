### App: Core

**TimeStampedModel**
* created
* modified

**Address**
* address
* complement
* district
* city
* uf (list)
* cep


### App: CRM

**People(TimeStampedModel, Address)**
* gender (list)
* treatment (list)
* slug *
* photo
* birthday
* company
* department
* cpf
* rg
* cnpj
* ie
* active (boolean)
* blocked (boolean)

**Person(People)**
* first_name *
* last_name
* email
* occupation (FK)
* person_type *
* customer_type *

**PhonePerson**
* phone
* people (FK)
* phone_type (list)

**Employee(People, User)**
* occupation (FK)
* date_release
* internal(boolean)
* commissioned(boolean)
* commission

**PhoneEmployee**
* phone
* employee (FK)
* phone_type (list)

**Occupation**
* occupation *

**Customer(Person)** (Proxy)

**Provider(Person)** (MTI)
* type_product (m2m)

**Seller(Employee)** (Proxy)


