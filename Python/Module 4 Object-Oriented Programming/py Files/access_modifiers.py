class Person:
    def __init__(self, name, age, salary):
        self.name = name           # Public attribute
        self._age = age            # Protected attribute
        self.__salary = salary     # Private attribute

    def show_details(self):
        return f"Name: {self.name}, Age: {self._age}, Salary: {self.__salary}"

# Subclass (Child Class)
class Employee(Person):
    def __init__(self, name, age, salary, role):
        super().__init__(name, age, salary)
        self.role = role

    def access_protected(self):
        return f"Accessing Protected Age: {self._age}"  # Allowed in subclass

    def access_private(self):
        # return f"Accessing Private Salary: {self.__salary}"  # ❌ Will cause an AttributeError
        return "Can't access private attribute directly!"

# Creating an Object
person = Employee("Alice", 30, 50000, "Developer")

# ✅ Public: Accessible anywhere
print(person.name)  # Output: Alice

# 🔸 Protected: Accessible, but should be used cautiously
print(person._age)  # Output: 30 (Warning: Not recommended to access directly)

# 🔒 Private: Not directly accessible
# print(person.__salary)  # ❌ Will cause an AttributeError

# ✅ Accessing private attribute via a public method
print(person.show_details())  # Output: Name: Alice, Age: 30, Salary: 50000

# ✅ Accessing protected in subclass
print(person.access_protected())  # Output: Accessing Protected Age: 30

# ❌ Attempting to access private in subclass
print(person.access_private())  # Output: Can't access private attribute directly!
