import complex.complex_example_pb2 as complex_example_pb2


complex_message = complex_example_pb2.ComplexMessage()
complex_message.one_dummy.id = 123
complex_message.one_dummy.name = "Dummy message"
print(complex_message)

# Add repeated fields using an instance.
first_multiple_dummy = complex_message.multiple_dummy.add()
first_multiple_dummy.id = 345
first_multiple_dummy.name = "First element of the array."
# Without instantiating it.
complex_message.multiple_dummy.add(id=111, name="Second element of array.")
print(complex_message)
# Using extend().
# This method is prone to bugs as it makes a copy of the message and the changes wont be reflected in the array.
third_dummy_message = complex_example_pb2.DummyMessage()
third_dummy_message.id = 89
third_dummy_message.name = "Third message."
complex_message.multiple_dummy.extend([third_dummy_message])
third_dummy_message.id = 100  # This line wont change the id's value
print("Extend option: ", complex_message)
