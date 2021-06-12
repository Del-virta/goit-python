class Customer:

    def __init__(self, surname, id=1):
        self.id = id
        self.surname = surname

    def __add__(self, customer_2):
        return self.id + customer_2.id