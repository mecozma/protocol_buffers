import address_book.address_book_pb2 as address_book_pb2
import sys


def list_people(addressbook):
    for person in addressbook.people:
        print("Person ID: ", person.id)
        print("Name: ", person.name)
        print("E-mail address: ", person.email)
        for phone_number in person.phones:
            if phone_number.type == address_book_pb2.Person.PhoneType.MOBILE:
                print("Mobile phone #: ")
            elif phone_number.type == address_book_pb2.Person.PhoneType.HOME:
                print("Home phone #: ")
            elif phone_number.type == address_book_pb2.Person.PhoneType.WORK:
                print("Work phone #: ")
            print(phone_number.number)


address_book = address_book_pb2.AddressBook()

with open("address_book.bin", "rb") as file:
    address_book.ParseFromString(file.read())
    file.close()

list_people(address_book)
