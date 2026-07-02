import user_pb2

# 1. Create a new User object
user = user_pb2.User()
user.name = "Alice Smith"
user.id = 101
user.email = "alice@example.com"
user.roles.extend(["admin", "user"])

# 2. Serialize the object to a compact binary byte stream
binary_data = user.SerializeToString()
print(f"Serialized binary size: {len(binary_data)} bytes")

# 3. Deserialize the binary byte stream back into an object
parsed_user = user_pb2.User()
parsed_user.ParseFromString(binary_data)

# 4. Read the parsed fields
print(f"Parsed User: {parsed_user.name} (ID: {parsed_user.id})")
