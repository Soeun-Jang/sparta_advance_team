text = "Hello, World!"
my_list = ["apple", "orange", "cherry"]
my_dict = {"apple" : 1, "orange" : 2, "cherry" : 3}

# 문자열 메서드 예시 코드 
# 1. count : 문자열 내에서 특정 문자가 몇 개나 있는지 세는 메서드
count = text.count("H")
print(count) # 1 

# 2. find : 문자열 내에서 특정 문자열이 처음 나오는 위치를 찾아주는 메서드
position = text.find("World")
print(position)

# 3. index : 문자열 내에서 특정 문자열이 처음 나오는 위치를 찾아주는 메서드
try:
  position = text.index("World")
  print(position)
except ValueError:
  print("찾는 문자열이 없습니다.")
  
# 4. join : 특정 문자열을 기준으로 다른 문자열들을 합쳐주는 메서드
joined_list = " ".join(my_list)
print(joined_list) 

# 5. upper : 문자열 내 모든 소문자를 대문자로 변환
uppercase_text = text.upper()
print(uppercase_text)

# 6. lower : 문자열 내 모든 대문자를 소문자로 변환
lowercase_text =text.lower()
print(lowercase_text)

# 7. replace : 문자열 내에서 특정 문자열을 다른 문자열로 바꾸는 메서드
replaced_text = text.replace("World", "Python")
print(replaced_text)

# 8. split : 문자열을 특정 문자 기준 나누어 리스트 형태로 반환하는 메서드 
splited_text = text.split(",")
print(splited_text)


#리스트 메서드 예시 코드
# 1. len : 리스트의 길이를 반환하는 메서드
print(len(my_list))

# 2. del : 리스트 내 특정 요소 삭제
del my_list[2]
print(my_list)

# 3. append : 리스트의 맨 뒤에 새로운 요소를 추가하는 메서드
my_list.append("melon")
print(my_list)

# 4. sort : 리스트를 오름차순으로 정렬하는 메서드
my_list.sort()
print(my_list)

# 5. reverse : 리스트의 요소 순서를 반대로 뒤집는 메서드
my_list.reverse()
print(my_list)

# 6. index : 리스트 특정 요소 인덱스를 반환하는 메서드
print(my_list.index("orange"))

# 7. insert : 리스트 특정 위치에 요소를 삽입하는 메서드
my_list.insert(2, "cherry")
print(my_list)

# 8. pop : 리스트의 마지막 요소를 빼낸 뒤 삭제하는 메서드
my_list.pop(3)
print(my_list)

# 9. count : 리스트의 특정 요소 개수를 세는 메서드
print(my_list.count("cherry"))
list_num = [1,1,2,3,4,5]
print(list_num.count(1))

# 10. extend : 리스트를 확장하여 새로운 요소들을 추가하는 메서드
my_list.extend(["apple", "grape", "mango"])
print(my_list)

# 11. += 연산자를 이용한 리스트 확장
numbers = [1,2,3]
numbers += [7,8,9]
print(numbers)


# 딕셔너리 메서드
# 1. 딕셔너리에 데이터 쌍 추가
my_dict["grape"] = 4
print(my_dict)

# 2. del : 딕셔너리에서 특정 요소를 삭제
del my_dict["grape"]
print(my_dict)

# 3. items : 딕셔너리의 모든 키와 값을 튜플 형태의 리스트로 반환
print(my_dict.items())

# 4. get : 딕셔너리에서 지정한 키에 대응 값을 반환
friut = my_dict.get("apple")
print(friut)

# 5. in : 해당 키가 딕셔너리 안에 있는 지 확인
if "apple" in my_dict:
  print("애플이다")
else:
  print("애플이 없다")
  
# 6. clear : 딕셔너리 모든 요소 삭제
my_dict.clear()
print(my_dict)