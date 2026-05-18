from peewee import SqliteDatabase, CharField, DateField, BooleanField, Model
from datetime import date

db = SqliteDatabase('database/second_db.db')
COMMAND_REGISTRY = {}

def register_table(name):
        """Декоратор"""
        def decorator(func):
            COMMAND_REGISTRY[name] = func
            return func
        return decorator

class BaseModel(Model):
    class Meta:
        database = db

@register_table("Person")
class Person(BaseModel):
    name = CharField()
    birthday = DateField()
    is_relative = BooleanField()


db.connect()

# new = Person(name='Sanya', birthday=date(1901, 5, 8), is_relative=True)
# new.save()
# user = Person.get(Person.id == 2)
# user.delete_instance()
for person in Person.select():
    print(person.name, person.birthday)



# db.create_tables([Person])
# db.drop_tables([Person])
db.close()

