import enums.enum_example_pb2 as enum_example_pb2

enum_message = enum_example_pb2.EnumMessage()
enum_message.id = 212
enum_message.day_of_the_week = enum_example_pb2.SUNDAY
print(print("*" * 10, "The created message.", "*" * 10))
print(enum_message)
print(print("*" * 10, "Print the day of the week.", "*" * 10))
# It will print the integer assigned to the day.
print(enum_message.day_of_the_week)
# Use this to find out if the day of the week printed is what you expect.
print(enum_message.day_of_the_week == enum_example_pb2.SUNDAY)

# Write the message to a binary file.
with open("enum.bin", "wb") as file:
    bites_as_string = enum_message.SerializeToString()
    file.write(bites_as_string)

print(print("*" * 10, "Read the message from a binary file.", "*" * 10))
with open("enum.bin", "rb") as file:
    enum_message_read = enum_example_pb2.EnumMessage.FromString(file.read())
    print(enum_message_read.id)
    print(enum_message_read.day_of_the_week)
