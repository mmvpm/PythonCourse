# ~itertools.zip_longest
def my_zip_longest(*collections, fillvalue=None):
    max_len = max(map(len, collections))

    for collection in collections:
        if len(collection) < max_len:
            collection += [fillvalue] * (max_len - len(collection))
    
    for i in range(max_len):
        yield tuple(map(lambda a: a[i], collections))