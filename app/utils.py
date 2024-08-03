from .models import Conference, User, Booking

from .models import Conference

def add_conference(data):
    #keys in data match those sent from the client
    return Conference(name=data['name'], date=data['date'])

def add_conference(data):
    return Conference(name=data['name'], location=data['location'])

def add_user(data):
    return User(username=data['username'])

def book_conference(data):
    return Booking(user_id=data['user_id'], conference_id=data['conference_id'])
