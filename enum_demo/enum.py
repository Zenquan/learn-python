from enum import Enum

Colors = Enum('Colors',('red', 'yellow'))

for name, member in Colors.__members__.items():
    print(name, '=>', member, ',', member.value)