import random

# All classes inherit from object
class Character:
    def __init__(self, name, **kwargs):
        self.name = name

        for key, value in kwargs.items():
            setattr(self, key, value)


# Thief class inherits from Character
class Thief(Character):
    # attribute
    sneaky = True

    def __init__(self, name, sneaky=True, **kwargs):
        #set the name and kwargs attributes (inherits from Character)
        super().__init__(name, **kwargs)
        self.sneaky = sneaky

    # methods are functions that belong to a class
    # methods are used by an instance, not the by the actual class
    # because of that methods take at least one parameter, that represents the instance that's using the method
    # self is used by convention
    def pickpocket(self):
        return self.sneaky and bool(random.randint(0, 1))

    def hide(self, light_level):
        return self.sneaky and light_level < 10