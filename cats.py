from peewee import *

db = SqliteDatabase('cats.sqlite')  # name is .db

class Cat(Model):
    name = CharField()
    color = CharField()
    age = IntegerField()

    class Meta:
        database = db  #link to database

    def __str__(self):
        return f'{self.id},{self.name}, {self.color},{self.age}' # dispay cat object

db.connect()  #connects database
db.create_tables([Cat])  #creates new table list Cat class.

Cat.delete().execute()  # clears database table.

zoe = Cat(name='Zoe', color='Ginger', age= 3)
zoe.save()  #make sure to save

cinnamon = Cat(name='Cinnamon', color='mixed', age= 19)
cinnamon.save()

bun = Cat(name='Bun', color='Grey', age= 9)  # model object.
bun.save()

cats = Cat.select()
for cat in cats:  # query object.
    print(cat)

list_of_cats = list(cats)  # reg Python list.

""" CRUD operations
Create - insert
Read    - select
Update
Detele 
"""

bun.age = 10
bun.save()

print('After Bun age changed')
cats = Cat.select()
for cat in cats:  # query object.
    print(cat)

#update many rows if needed

rows_modified = Cat.update(age=6).where(Cat.name == 'Zoe').execute()

print('After Zoe age changed')
cats = Cat.select()
for cat in cats:  # query object.
    print(cat)
print(rows_modified)    

buzz = Cat(name='Buzz', color='Black', age= 3)  # model object.
buzz.save()

cats_who_are_3 = Cat.select().where(Cat.age ==3)
for cat in cats_who_are_3:
    print(cat, ' is three')

cat_with_l_in_name = Cat.select().where(Cat.name.contains('n'))
for cat in cat_with_l_in_name:
    print(cat,' has an N in name.')

zoe_from_db = Cat.get_or_none(name='Socks')
print(zoe_from_db)

cat_1 = Cat.get_by_id(1)  # sytax is very important here with peewee
print(cat_1)

total = Cat.select().count()
print(total)

total_cat_who_are_5 = Cat.select().where(Cat.age== 3).count()
print(total_cat_who_are_5)

cat_sorted_by_name = Cat.select().order_by(Cat.name.desc(), Cat.age)
print(list(cat_sorted_by_name))

first_3 = Cat.select().order_by(Cat.name).limit(3)
print(list(first_3))
