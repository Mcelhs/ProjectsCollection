# This is a simple contacts book program. I intend to have it save and print contacts
# through a text file "Contacts.txt" in a ContactsBook folder.

import sys
import os

contactsFile = 'ContactBook/Contacts.txt'

# add contact
def addContact(name, phone, email=''):
    if name != '' and phone != '':
        with open(contactsFile, 'a') as file:
            file.write(f'{name}\n{phone}\n{email}\n\n')
            print('Added a contact.\n')
    else:
        print('You must write at least a name and a phone number.\n')
        print('(automatically created contacts file if not existing)\n')

# print contacts
def printContacts():
    with open(contactsFile, 'r') as file:
        for line in file:
            print(line, end='')

# remove contact
def removeContact():
    pass

# clear whole file
def clearContacts():
    f = open(contactsFile, 'w')
    f.close()
    print('File cleared')
    print('(automatically created contacts file if not existing)\n')
    # print(f.closed) # is file closed? (debugging purposes)

# command variables for os, maybe there is a
# more proper way to do this (?)
posix = 'clear'
nt = 'cls'

os.system(posix)

print('''
CONTACTS BOOK v1
=================
Add, remove, print, or clear contacts:
    1. Add contact
    2. Remove contact
    3. Print contacts
    4. Clear contacts
''')

while True:

    prompt = input("Select an option (or q to exit) >> ")

    if prompt == '1':
        name = input("Contact Name: ")
        phone = input("Phone no. #: ")
        email = input('Email (optional): ')  
        addContact(name, phone, email)
    elif prompt == '2':
        pass
    elif prompt == '3':
        printContacts()
    elif prompt == '4':
        clearContacts()
    elif prompt.lower() == 'q':
        os.system(posix)
        sys.exit()
    else:
        print("Invalid option. \n")
        continue
