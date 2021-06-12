import csv


def write_customers_to_csv(customers, file_name):
    with open(file_name, 'w', newline='') as fh:
        field_names = ['id','name']
        writer = csv.DictWriter(fh,fieldnames = field_names)
        writer.writeheader()
        for customer in customers:     
            writer.writerow(customer)