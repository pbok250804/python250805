# 자료형 정의
my_list = [1, 2, 3, 4, 1]              # 중복 허용, 순서 유지, 변경 가능
my_set = {1, 2, 3, 4, 1}               # 중복 불가, 순서 없음, 변경 가능
my_dict = {'a': 1, 'b': 2, 'c': 3}     # 키-값 쌍, 순서 있음(Python 3.7+), 키 중복 불가
my_tuple = (1, 2, 3, 4, 1)            # 중복 허용, 순서 유지, 변경 불가

# 출력
print("=== List ===")
print("자료:", my_list)
print("타입:", type(my_list))
print("인덱싱:", my_list[0])
print("중복 허용 여부:", "Yes" if len(my_list) != len(set(my_list)) else "No")
print("변경 가능 여부: Yes (예: my_list[0] = 100)")

print("\n=== Set ===")
print("자료:", my_set)
print("타입:", type(my_set))
print("인덱싱 지원 여부: No (예: my_set[0] → 오류)")
print("중복 허용 여부: No")
print("변경 가능 여부: Yes (예: my_set.add(5))")

print("\n=== Dict ===")
print("자료:", my_dict)
print("타입:", type(my_dict))
print("키 접근:", my_dict['a'])
print("중복 키 허용 여부: No")
print("변경 가능 여부: Yes (예: my_dict['a'] = 10)")

print("\n=== Tuple ===")
print("자료:", my_tuple)
print("타입:", type(my_tuple))
print("인덱싱:", my_tuple[0])
print("중복 허용 여부:", "Yes" if len(my_tuple) != len(set(my_tuple)) else "No")
print("변경 가능 여부: No (예: my_tuple[0] = 100 → 오류)")
