import hashlib
input_string = "23f3004056@ds.study.iitm.ac.in 2025"
hash_result = hashlib.sha256(input_string.encode()).hexdigest()
session_code = hash_result[-5:]
print(session_code)