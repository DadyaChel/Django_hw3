from banking.models import Client, Account, Credit, id_generator
import string
import random

c1 = Client.objects.create(name='Бердиев Н.Д', birth_year='1994-05-21', work_place='Codify')
c2 = Client.objects.create(name='Dadya', birth_year='2004-12-12', work_place='bomj')

ac1 = c1.clients.create(number=id_generator(), account_type=1)
ac2 = c2.clients.create(number=id_generator(), account_type=2)
ac3 = c1.clients.create(number=id_generator(), account_type=3)
ac4 = c2.clients.create(number=id_generator(), account_type=4)

cr1 = ac1.accounts.create(sum=99999999999999999)
cr2 = ac2.accounts.create(sum=77777777777777777)
cr3 = ac3.accounts.create(sum=66666666666666666)
cr4 = ac4.accounts.create(sum=22222222222222222)


