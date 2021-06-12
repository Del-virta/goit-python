from copy import deepcopy, copy


class Customer:
    def __init__(self, surname, id, attributes):
        self.surname = surname
        self.id = id
        self.attributes = attributes

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
        self.id /= 4

    def __copy__(self):
        copy_customer = Customer('Bob', 29, None)
        copy_customer.id = self.id
        copy_customer.surname = self.surname
        copy_customer.attributes = self.attributes
        return copy_customer

    def __deepcopy__(self):
        deep_copy_customer = Customer('Lacy', 12, None)
        deep_copy_customer.id = copy(self.id)
        deep_copy_customer.surname = copy(self.surname)
        deep_copy_customer.attributes = copy(self.attributes)
        return deep_copy_customer

def create_incremented_customer(customer):
    new_customer = customer.__deepcopy__()
    new_customer.id += 1
    return new_customer