# d1 = {"name":"메가스터디", "address":"강남", "floor":4}
# # print(type(d1), d1)
# # 조회
# print(d1["name"])
# print(d1["address"])
# # 추가
# print("추가 전 :", d1)
# d1["phone"] = "010-1111-2222"
# print("추가 후 :", d1)
# # 수정 : 중복 키값 추가
# d1["floor"] = 45
# print("2차 추가 후 :", d1)
# # 삭제 1 
# del d1["floor"]
# print("삭제 후 :", d1)
# # 삭제 2
# print(d1.pop("phone"))
# print("2차 삭제 후 :", d1)
# # 모두 삭제
# d1.clear()
# print("전체 삭제 후 :", d1)


# d1 = {"a":1, "b":2}
# d2 = {"a":11, "c":3}
# #확장
# # d1.update(d2)
# # print(d1)
# d2.update(d1)
# print(d2)

# d1 = {"a":1, "b":2, "c":22}
# 조회
# print(d1["a"])
# print(d1["z"])
# print("프로그램 실행중")

# # print(d1.get("z", "찾고자 하는 키값은 존재 하지 않습니다."))
# print(d1.get("z"))
# print("프로그램 실행중")

# #키 출력
# d1 = {"a":1, "z":2, "k":3}
# d1_keys = d1.keys() # dict_keys(['a', 'b', 'c'])
# print(type(d1_keys), d1_keys)
# # 리스트로 형변환
# dtoL = list(d1_keys)
# dtoL.sort()
# print(dtoL)
# # 값 출력
# print(d1.values())
# # 키와 값 출력
# print(d1.items())




