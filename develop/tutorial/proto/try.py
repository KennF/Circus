import addressbook_pb2

person  = addressbook_pb2.Person()
person.id = 1
person.name = "John Doe"
person.email = "test@test.com"
phone = person.phone.add()
phone.number = "123-4333"
phone.type = addressbook_pb2.Person.HOME

print(person.SerializeToString())
print(person)