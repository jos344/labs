from sqlalchemy import Column, Integer, UnicodeText
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import select

import sys
import datetime

# Sqlite3 will be used as database engine. Database will be saved in file guestbook.db
engine = create_engine('sqlite:///guestbook.db', echo=False)
Base = declarative_base(bind=engine)

# Sqlalchemy translates class to sqlite3 table and creates database
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(UnicodeText)
    message = Column(UnicodeText)
    date = Column(UnicodeText)

    def __init__(self, name, message, date):
        self.name = name
        self.message = message
        self.date = date

Base.metadata.create_all()

# Create connection to database for all crud operations
Session = sessionmaker(bind=engine)
s = Session()

def add_to_gb(name, message):
    '''Add user name and message to database'''
    q = s.query(User.id).filter(User.name==name)
    if s.query(q.exists()).scalar() == True: 
        print('Name already exists in gb')
        return

    date = datetime.datetime.now()
    user = User(name, message, date)
    s.add(user)
    s.commit()
    print('Your message has been saved to gb')

def delete_from_gb(name):
    '''Delete user message from database'''
    q = s.query(User.id).filter(User.name==name)
    if s.query(q.exists()).scalar() == False: 
        print('No user with that name in gb')
        return

    query = s.query(User).filter(User.name == name)
    row = query.delete()
    s.commit()
    print('Your message has been deleted from gb')

def update_gb(name, message):
    '''Update user message in database'''    
    q = s.query(User.name).filter(User.name==name)
    if s.query(q.exists()).scalar() == False: 
        print('No user with that name in gb')   
        return

    query = s.execute(select(User).filter_by(name=name)).scalar_one()
    query.message = message
    date = datetime.datetime.now()
    query.date = date 
    print('Your message has been updated to gb')

def show_gb():
    '''Print all entries in database'''
    print('\n******* Guestbook *******')
    query = s.query(User).order_by(User.id)
    if query.count() == 0:
        print('Guestbook is empty')
    for row in query.all():
        print(f'Name: {row.name} - Message: {row.message} - Signed: {row.date}')
    print('**************************\n')

def check_input():
    '''Check that user enter name and message'''
    try: 
        name = input('Please enter your name: ')
        if not name:
            print('You have to enter a name')
            raise ValueError            
        message = input('Please enter your message: ')
        if not message:
            print('You have to enter a message')
            raise ValueError 
        return name, message    
    except:
        return None 

def show_menu():
    '''Show program menu'''
    print('************************************')
    print('*    Welcome to Guestbook          *')   
    print('*    1. List all messages          *')
    print('*    2. Enter your message         *')
    print('*    3. Delete your message        *')
    print('*    4. Update your message        *')
    print('*    5. Quit                       *')
    print('************************************')

while True: 
    show_menu()
    try:
        choice = int(input('Please make your selection 1 - 5: '))
    except ValueError:
        print('Please enter number 1 - 5. Exited')
        sys.exit()
    if choice == 1:
        show_gb()
    if choice == 2:
        try:
            name, message = check_input()
        except TypeError:
            continue
        add_to_gb(name, message)       
    if choice == 3:
        name = input('Please enter name to delete: ')
        if not name:
            print('You have to enter a name')
            continue
        delete_from_gb(name)
    if choice == 4:
        try:
            name, message = check_input()
        except TypeError:
            continue 
        update_gb(name, message)  
    if choice == 5:
        print('Bye') 
        sys.exit()