class letter_number:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return str(self.a) + str(self.b)


test = letter_number(1,2)

print(test)