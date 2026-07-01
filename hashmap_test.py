class MyHashMap:
    def __init__(self, size=10):
        self.size = size
        # Create a list of empty lists (buckets) to handle collisions
        self.buckets = [[] for _ in range(self.size)]

    def _get_hash(self, key):
        """
        Our internal Hash Function. 
        It converts a key into an index within our array size.
        """
        # hash() is a built-in Python function that turns objects into integers
        return hash(key) % self.size

    def put(self, key, value):
        """Insert or update a key-value pair."""
        bucket_index = self._get_hash(key)
        bucket = self.buckets[bucket_index]

        # Check if the key already exists in the bucket to update it
        for i, kv_pair in enumerate(bucket):
            k, v = kv_pair
            if k == key:
                bucket[i] = (key, value)  # Update existing key
                return

        # If it's a brand new key, append it to the bucket
        bucket.append((key, value))

    def get(self, key):
        """Retrieve a value by its key."""
        bucket_index = self._get_hash(key)
        bucket = self.buckets[bucket_index]

        # Search through the specific bucket
        for k, v in bucket:
            if k == key:
                return v
        
        return None  # Key not found

    def delete(self, key):
        """Remove a key-value pair."""
        bucket_index = self._get_hash(key)
        bucket = self.buckets[bucket_index]

        for i, kv_pair in enumerate(bucket):
            k, v = kv_pair
            if k == key:
                del bucket[i]
                return True
        
        return False  # Key wasn't there to delete
    


# Initialize our hash map with 5 buckets
hash_map = MyHashMap(size=10)

# 1. Insert some data
hash_map.put("apple", 1.50)
hash_map.put("banana", 0.75)
hash_map.put("orange", 1.25)

# 2. Retrieve data
print("Price of banana:", hash_map.get("banana"))  # Output: 0.75
print("Price of grape:", hash_map.get("grape"))    # Output: None

# 3. Update data
hash_map.put("apple", 1.80)
print("New price of apple:", hash_map.get("apple"))  # Output: 1.80

# 4. Peek under the hood to see how the buckets look!
print("\nInternal Buckets Structure:")
for idx, bucket in enumerate(hash_map.buckets):
    print(f"Bucket {idx}: {bucket}")