"""
- Property decorators allows us to give our class attributes - Getter, Setter and Deleters
functionality.
"""


class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        # **********************************************
        # self.email = first + "." + last + "@gmail.com"
        # **********************************************

    def fullname(self):
        return "{}{}".format(self.first, self.last)

    # After running line no : 31, comment line no: 12
    # Defining our email in a class like method but we are able to access like an attribute
    # using property decorator
    @property  # getter
    def email(self):
        return "{}.{}@gmail.com".format(self.first, self.last)


e1 = Employee("TT", "pandey")
print(e1.first)  # TT
print(e1.email)  # TT.pandey@gmail.com
print(e1.fullname())  # TT pandey

e1.first = "jim"
print(e1.first)  # jim
# ****************************************
print(e1.email)  # TT.pandey@gmail.com
# ****************************************
print(e1.fullname())  # jimpandey

e1.fullname = "Test User"