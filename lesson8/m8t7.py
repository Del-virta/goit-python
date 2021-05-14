from collections import defaultdict


def group_clients(clients):
    clients_dict = defaultdict(list)

    for aidi in clients:
        region = aidi[0]+aidi[1]
        clients_dict[region].append(aidi)
    return clients_dict

print(group_clients(['34345', '76788', '34654']))