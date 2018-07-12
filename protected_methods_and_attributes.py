class Protected:
    __name = "Security"

    # the __ makes the method unaccessible outside of the class
    def __method(self):
        return self.__name