def create_table(size=10):
    return [[] for _ in range(size)]  #hash table initialization with empty lists for chaining

def hash_key(key, size):
    return hash(key) % size  # hash key initialization

def insert(table, size, key, value):
    index = hash_key(key, size)
    for pair in table[index]:
        if pair[0] == key:
            pair[1] = value  # updating the value if it is already existed
            return
    table[index].append([key, value])  # new key-value pair added

def search(table, size, key):
    index = hash_key(key, size)
    for pair in table[index]:
        if pair[0] == key:
            return pair[1]  # return value if key is matched
    return None  # not finding the key

def delete(table, size, key):
    index = hash_key(key, size)
    for i, pair in enumerate(table[index]):
        if pair[0] == key:
            del table[index][i]  # Delete the key-value pair if key is matched
            return True
    return False  # not finding the key

def display(table):
    for i, bucket in enumerate(table):
        print(f"Bucket {i}: {bucket}")

size = 10
hash_table = create_table(size)

# insertion of key-value pairs
insert(hash_table, size, 10, "apple")
insert(hash_table, size, 20, "banana")
insert(hash_table, size, "key1", "cherry")

# searching for a value
print("Search result for key 20:", search(hash_table, size, 20))
print("Search result for key 'key1':", search(hash_table, size, "key1"))

# deletion of a key-value pair
delete(hash_table, size, 10)

# displaying the hash table
display(hash_table)
