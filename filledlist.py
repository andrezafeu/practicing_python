import copy


class FilledList(list):
    def __init__(self, count, value, *args, **kwargs):
        super().__init__()
        for _ in range(count):
            # if we weren't using copy.copy and the function received someting mutable, 
            # like another list, each member of that list or each member of our list that 
            # was a copy of of that list would be the same member.
            # If one of them is changed, all the others too would be changed too, because we are 
            # just putting in references to that list.
            # With copy.copy we are getting brand new versions of those lists 
            self.append(copy.copy(value))