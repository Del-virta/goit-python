from collections import deque


def form_deque(clients_id, max_len):
    queue = deque(maxlen=max_len)
    new_list = clients_id[::-1]
    for aidi in new_list:
        if not aidi%2:
            queue.appendleft(aidi)
        else:
            queue.append(aidi)
    return queue
print(form_deque([1233, 4566, 1234, 7877, 2], 5))