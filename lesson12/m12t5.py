class Customer:
    def __init__(self, surname, id):
        self.surname = surname
        self.id = id

    def __eq__(self, other):
        if self.surname == other.surname and self.id == other.id:
            return True
        return False

    def __getstate__(self):
        attributes = self.__dict__.copy()
        attributes['id'] *= 4
        return attributes

    def __setstate__(self, state):
        self.__dict__ = state
        self.id/=4