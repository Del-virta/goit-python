import json


def write_object(customer):
    byted = json.dumps(customer)
    return byted


def write_to_file(customer, path):
    with open(path, 'w') as fh:
        byted_file = json.dump(customer,fh)