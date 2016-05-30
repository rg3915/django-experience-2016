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
* person_type (list) *
* customer_type (list) *

**PhonePerson**
* phone
* person (FK)
* phone_type (list)

**Employee(People, User)**
* occupation (FK)
* internal (bool)
* commissioned (bool)
* commission
* date_release

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


### App: Product

**Brand**
* brand

**Product (TimeStampedModel)**
* imported (bool)
* outofline (bool)
* perishable (bool)
* ncm
* brand (FK)
* product *
* short_description *
* description
* cost (Decimal) *
* price (Decimal) *
* icms (Decimal)
* ipi (Decimal)
* stock_min (int) *
* stock (int) *

**TypeProduct**
* type_product


### App: Selling

**Ordered (TimeStampedModel)**
* customer (FK) *
* seller (FK) *
* status_ordered *

**Sale (TimeStampedModel)**
* ordered (o2o) *
* paid (bool)
* date_paid
* method_paid (forma de pagamento) (list)
* deadline (prazo de entrega) (list)


### App: Buying



### App: Proposal

**Work(Address)**
* name_work *
* slug *
* person(contato) (FK)
* customer(cliente) (FK) *

**Proposal(TimeStampedModel)**
* num_prop *
* priority (list)
* prop_type ('R','OP') *
* num_type_prop (0,1,2,...) *
* category (list)
* description
* work (FK) *
* person(contato) (FK)
* employee (FK) *
* seller (FK)
* status (list) *
* date_conclusion
* price
* obs

**Contract**
* proposal (o2o) *
* contractor (FK) *
* is_canceled (FK)

**NumLastProposal**
* num_last_prop *



### App: Stock


### App: Bookstore

**People(TimeStampedModel, Address)**
* gender (list)
* treatment (list)
* first_name *
* last_name
* email
* slug *
* photo
* birthday
* company
* department
* active (boolean)
* blocked (boolean)

**PF(People)** (MTI)
* cpf
* rg

**PJ(People)** (MTI)
* cnpj
* ie

**Customer(People)** (MTI)

**Provider(People)** (MTI)
* books (m2m)
* price (decimal)

**Author(People)** (MTI)

**Publisher**
* name
* num_awards (int)

**Book (TimeStampedModel)**
* imported (bool)
* book_type (list)
* isbn (int)
* name
* rating (float)
* authors (m2m)
* publisher (FK)
* price (decimal)
* stock_min
* stock

**Store (Address)**
* name
* books (m2m)
