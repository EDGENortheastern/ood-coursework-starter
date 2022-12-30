# The following code should properly,
# but it fails:
# person = Person('Katia', 'Punter', 50)
# print(person.full_name)
# print(person.age)

# fix the bug


class Person():

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name