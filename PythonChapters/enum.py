from enum import Enum
class State1(Enum):
    INACTIVE = 0
    ACTIVE = 1
    
print(State1.INACTIVE.value)
    
class Season(Enum):
    SPRING = 1
    SUMMER = 2
    AUTUMN = 3
    WINTER = 4
print(Season.SPRING)
print(Season.SPRING.name)
print(Season.SPRING.value)
print(type(Season.SPRING))
print(repr(Season.SPRING))
print(list(Season))    