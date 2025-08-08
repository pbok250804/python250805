# 자료형별 예시 데이터
example_data = [1, 2, 3, 2, 1]

# List
list_data = list(example_data)
print("List:", list_data)
print("List supports indexing:", list_data[0])
print("List allows duplicates:", list_data.count(2), "times 2 appears")
print("List is mutable: changing first element to 100")
list_data[0] = 100
print("Modified List:", list_data)
print()

# Set
set_data = set(example_data)
print("Set:", set_data)
print("Set does not allow duplicates.")
print("Set is unordered, indexing not supported.")
print("Set is mutable: adding 4")
set_data.add(4)
print("Modified Set:", set_data)
print()

# Tuple
tuple_data = tuple(example_data)
print("Tuple:", tuple_data)
print("Tuple supports indexing:", tuple_data[0])
print("Tuple allows duplicates:", tuple_data.count(2), "times 2 appears")
print("Tuple is immutable. Attempting modification raises an error.")
try:
    tuple_data[0] = 100
except TypeError as e:
    print("Error:", e)
print()

# Dictionary
dict_data = {1: 'a', 2: 'b', 3: 'c'}
print("Dict:", dict_data)
print("Dict keys must be unique.")
print("Dict supports key access:", dict_data[2])
print("Dict is mutable: changing key 1's value to 'z'")
dict_data[1] = 'z'
print("Modified Dict:", dict_data)
print()

# 요약 비교표 출력
print(f"{'Type':<10}{'Ordered':<10}{'Mutable':<10}{'Duplicates':<15}{'Indexing':<10}")
print(f"{'-'*55}")
print(f"{'List':<10}{'Yes':<10}{'Yes':<10}{'Allowed':<15}{'Yes':<10}")
print(f"{'Set':<10}{'No':<10}{'Yes':<10}{'Not Allowed':<15}{'No':<10}")
print(f"{'Tuple':<10}{'Yes':<10}{'No':<10}{'Allowed':<15}{'Yes':<10}")
print(f"{'Dict':<10}{'Yes (3.7+)':<10}{'Yes':<10}{'Keys Unique':<15}{'By Key':<10}")
