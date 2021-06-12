class Employees:
    def __init__(self, surnames, group):
        self.employees_dict = {}
        self.surnames = surnames
        for i in surnames:
            self.employees_dict[i] = self.surnames.index(i)
        self.group = group

    def __setitem__(self, key, value):
        self.employees_dict[key] = value

    def __getitem__(self, item):
        return self.employees_dict[item]