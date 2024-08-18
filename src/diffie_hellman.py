def key_exchange(g, n, private_key):
    public_key = pow(g, private_key, n)
    return public_key

def generate_shared_key(public_key, private_key, n):
    shared_key = pow(public_key, private_key, n)
    return shared_key