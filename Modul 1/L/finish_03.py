from dataclasses import dataclass


class Notification:
    def notify(self, message):
        raise NotImplementedError

# class Contact:
#     def __init__(self, name, email, phone):
#         self.name = name
#         self.email = email
#         self.phone = phone


@dataclass
class Contact:
    name: str
    email: str
    phone: str


class Email(Notification):
    def __init__(self, email):
        self.email = email

    def notify(self, message):
        print(f'Send {message} to email: {self.email}')


class SMS(Notification):
    def __init__(self, phone):
        self.phone = phone

    def notify(self, message):
        print(f'Send {message} to phone: {self.phone}')


class NotificationService:
    def __init__(self, notification: Notification):
        self.notification = notification

    def send(self, message):
        self.notification.notify(message)


if __name__ == '__main__':
    person = Contact('John', 'hzdkv@example.com', '077777')
    service_SMS = NotificationService(SMS(person.phone))
    service_email = NotificationService(Email(person.email))
    service_SMS.send('Hello bro!')
    service_email.send('Hello bro!')