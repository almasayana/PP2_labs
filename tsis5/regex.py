import re

with open("tsis5/row.txt", "r", encoding="utf-8") as file:
    text = file.read()

# 1
result = re.findall(r"ab*", text)
print("Задание 1:", result)

# 2
result = re.findall(r"ab{2,3}", text)
print("Задание 2:", result)

# 3
result = re.findall(r"[a-z]+_[a-z]+", text)
print("Задание 3:", result)

# 4
result = re.findall(r"[A-Z][a-z]+", text)
print("Задание 4:", result)

# 5
result = re.findall(r'a.*b$', text)
print("Задание 5:", result)

# 6
result = re.sub(r"[ ,.]", ":", text)
print("Задание 6:", result)

# 7
result = re.sub(r'_([a-z])', lambda match: match.group(1).upper(), text)
print("Задание 7:", result)

# 8
result = re.split(r"(?=[A-Z])", text)
print("Задание 8:", result)

# 9
result = re.sub(r"([A-Z])", r" \1", text)
print("Задание 9:", result)

# 10
res = re.sub(r'([a-z])([A-Z])', r'\1_\2', text).lower()
print("Задание 10:", res)


