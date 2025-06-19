import base64
import string
import re
import itertools

# Cleaned ASCII string from decrypted binary
data = "ZLlHrKsJcrzUGmXYtTA1p54DU9ufdodOHT08ArrRh6S7mwPCQAIp"

# 1. Try base64 decoding on chunks
print("🔍 Base64 Decoding Attempts:")
for i in range(len(data) - 7):
    chunk = data[i:i+8]
    try:
        decoded = base64.b64decode(chunk + "==").decode('utf-8')
        print(f"{chunk} ➜ {decoded}")
    except:
        pass

# 2. Pull words using regex
print("\n🔎 Searching for words (3+ letters):")
words = re.findall(r'[A-Za-z]{3,}', data)
for w in words:
    print(f"  - {w}")

# 3. Generate permutations of shorter words for pattern clues
print("\n🧠 Exploring anagram-like combos:")
for combo in itertools.combinations(words, 2):
    combined = ''.join(combo)
    print(f"Trying: {combined}")

# 4. Extract all printable and alphanumeric characters
print("\n🧽 Printable ASCII:")
print(''.join([c if c in string.printable else '.' for c in data]))

print("\n🔠 Letters/Numbers Only:")
print(''.join(filter(str.isalnum, data)))

# Optional: Check entropy or frequency if next phase is needed
