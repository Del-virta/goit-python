def get_favorites(contacts):
    return list(filter(lambda x: x['favorite']==True, contacts))