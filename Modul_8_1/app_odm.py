import argparse

from bson.objectid import ObjectId
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from mongoengine import connect, Document, StringField, IntField, ListField, DoesNotExist

connect(db="web17", host="mongodb+srv://userweb17:<password>@cluster0.r7yz0bl.mongodb.net/?retryWrites=true&w=majority")


parser = argparse.ArgumentParser(description='Server Cats Enterprice')
parser.add_argument('--action', help='create, read, update, delete')  # CRUD action
parser.add_argument('--id')
parser.add_argument('--name')
parser.add_argument('--age')
parser.add_argument('--features', nargs='+')

arg = vars(parser.parse_args())

action = arg.get('action')
pk = arg.get('id')
name = arg.get('name')
age = arg.get('age')
features = arg.get('features')


class Cat(Document):
    name = StringField(max_length=120, required=True)
    age = IntField(min_value=1, max_value=30)
    features = ListField(StringField(max_length=150))
    meta = {"collections": 'cats'}


def find():
    return Cat.objects.all()


def create(name, age, features):
    r = Cat(name=name, age=age, features=features)
    r.save()
    return r


def update(pk, name, age, features):
    cat = Cat.objects(id=pk).first()        # Якщо не знайде, поверне None
    if cat:
        cat.update(name=name, age=age, features=features)
        cat.reload()
    return cat


def delete(pk):
    try:
        cat = Cat.objects.get(id=pk)            # Якщо не знайде, поверне помилку DoesNotExist
        cat.delete()
        return cat
    except DoesNotExist:
        return None


def main():
    match action:
        case 'create':
            r = create(name, age, features)
            print(r.to_mongo().to_dict())
        case 'read':
            r = find()
            print([e.to_mongo().to_dict() for e in r])
        case 'update':
            r = update(pk, name, age, features)
            if r:
                print(r.to_mongo().to_dict())
        case 'delete':
            r = delete(pk)
            if r:
                print(r.to_mongo().to_dict())
        case _:
            print("Unknown command")


if __name__ == '__main__':
    main()
