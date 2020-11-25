import simple.simple_pb2 as simple_pb2


simple_message = simple_pb2.SimpleMessage()
simple_message.id = 456
simple_message.is_simple = True
simple_message.name = "ProtoBuff"
sample_list = simple_message.sample_list
sample_list.append(1)
sample_list.append(2)
sample_list.append(3)
# print(sample_list)

print(print("*" * 10, "The created message.", "*" * 10))
print(simple_message)

# Write the message to a binary file.
with open("simple.bin", "wb") as file:
    bites_as_string = simple_message.SerializeToString()
    file.write(bites_as_string)

# Read the message from the binary file.
print("*" * 10, "Reading from file.", "*" * 10)
with open("simple.bin", "rb") as file:
    simple_message_read = simple_pb2.SimpleMessage.FromString(file.read())
    print(simple_message_read)
    print("*" * 10, "Print a single field from the message.", "*" * 10)
    print("The is number: ", simple_message_read.id)
    print("Is simple? ", simple_message_read.is_simple)
    print("the message's name: ", simple_message_read.name)
    print(simple_message_read.sample_list)
    for i in simple_message_read.sample_list:
        print("Sample_list value", i)
