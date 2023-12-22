from mongoengine import *

connect(db="web17", host="mongodb+srv://userweb17:321456@cluster0.r7yz0bl.mongodb.net/?retryWrites=true&w=majority")


class Task(Document):
    completed = BooleanField(default=False)
    consumer = StringField(max_length=150)
