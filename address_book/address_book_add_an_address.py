import address_book.address_book_pb2 as address_book_pb2
import sys


def prompt_for_record(person):
    """
    This function prompts for person details.
    :param person: Proto buffer message.
    :return:
    """
    person.name = input("Please enter the person's name:  ")
    person.id = int(input("Enter person ID number:  "))
    email = input("Please enter your email (Leave blank for none):  ")
    # If the email is not empty string assign the string to email.
    if email != "":
        person.email = email
    while True:
        number = input("Please enter your phone number (leave blank to finish):  ")
        if number == "":
            break
        phone_number = person.phones.add()
        phone_number.number = number
        phone_type = input("Is it a mobile, home or work phone?  ")
        if phone_type == "mobile":
            phone_number.type = person.PhoneType.MOBILE
        elif phone_type == "home":
            phone_number.type = person.PhoneType.HOME
        elif phone_type == "work":
            phone_number.type = person.PhoneType.WORK
        else:
            print("Unknown phone number; leave as default value")
    print(person)


address_book = address_book_pb2.AddressBook()
# Read the existing address book.
try:
    with open("address_book.bin", "rb") as file:
        address_book.ParseFromString(file.read())
        file.close()
except IOError:
    print(sys.argv[1] + "Could not open the file. Creating a new one.")

# Add an address.
prompt_for_record(address_book.people.add())

# Write the new address book back to disk.
with open("address_book.bin", "wb") as file:
    file.write(address_book.SerializeToString())
    file.close()
