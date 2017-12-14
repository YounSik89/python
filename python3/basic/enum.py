from enum import Enum

class Color(Enum):
    red = 1
    green = 2
    blue = 3

Color2 = Enum('Color2','red green blue')

print(Color.blue.name)
print(Color.blue.value)
