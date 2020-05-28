'''
9. Write a Python class which has two methods get_String and print_String.
get_String accept a string from the user and
print_String print the string in upper case.
'''

class HandleUserInput:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def get_String(self):
        self.input = input("Napisz cos: ")
        return input

    def print_String(self, input):
        string = self.input.upper()
        print(string)

object1 = HandleUserInput("Ana", "Kot")
object1.print_String(object1.get_String())