import pickle


class Customer:
    def __init__(self, surname, id):
        self.surname = surname
        self.id = id

    def __eq__(self, other):
        if self.surname == other.surname and self.id == other.id:
            return True
        return False


def write_object(customer):
    byte_string = pickle.dumps(customer)
    return byte_string


def write_to_file(customer, path):
    with open(path, "wb") as fh:
        packed = pickle.dump(customer, fh)