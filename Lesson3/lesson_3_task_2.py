from smartphone import Smartphone

catalog = [Smartphone('Huawei','P60 Pro','+712345678'),
           Smartphone('Xiaomi ','Redmi12','+1223232323'),
           Smartphone('Apple','Iphone 15','+75455121545'),
           Smartphone('Samsung','Galaxy A51','+905465550'),
           Smartphone('Honor','7A','+75455123154')
]


for phone in catalog:
    print(f'{phone.brand}  {phone.model}  {phone.number}')
