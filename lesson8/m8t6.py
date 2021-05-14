import collections


def count_activity(clients_activity):
    new_list = []
    for each_list in clients_activity:
        new_list.extend(each_list)
    result = collections.Counter(new_list).most_common(1)
    return result

print(count_activity([['Edvardson', 'Damriel', 'Mbape','Columb'], ['Edvardson', 'Mbape', 'Mbape']]))
