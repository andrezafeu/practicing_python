class ReversedStr(str):
    # new is a class method, therefore it doesn't take self as argument
    def __new__(*args, **kwargs):
        # since strings are immutable, the ony place we should change them is at creation time
        # it's safer and easier to use the new method of the class you are extending directly
        self = str.__new__(*args, **kwargs)
        self = self[::-1]
        return self