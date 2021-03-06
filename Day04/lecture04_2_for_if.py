# # 반복문과 제어문의 조합
# # 1 ~ 50 사이의 3의 배수만 출력하세요.
# # (1)
# for i in range(1, 51):
#     if i % 3 == 0:
#         print(i, end=" ")
# print()
# # (2)
# for i in range(3, 51, 3):  # 위와 출력은 같으나 값만 같을뿐... 의미없는 과정
#     print(i, end=" ")
# print()


# # 1 ~ 100 사이의 7의 배수 개수를 구하세요.
# count = 0
# for i in range(1, 101):
#     if i % 7 == 0:
#         count += 1

# print("7의 배수의 개수", count)


# # for문 예제 04(for&if 조합)
# list_score = [90, 25, 67, 45, 80]
# no = 0
# for a in list_score :
#     no += 1
#     if a >= 60 :
#         print("{}번 학생 {}점으로 합격입니다".format(no, a))
#     else :
#         print("{}번 학생 {}점으로 불합격입니다".format(no, a))


# # for문 예제 05(약수 구하기)
# number = int(input("수를 입력하세요:"))   # 24
# for i in range(1, number + 1):
#     if number % i == 0:
#         print(i, end=" ")


# # continue문 기본 이해01
# for num in range(1,11) : 
#     if num == 4 :
#         continue
#     print(f"숫자 {num}")
# print("프로그램을 종료합니다.")


# # continue문 기본 이해02
# for num in range(1,11) : 
#     print(f"숫자 {num}")
#     continue
#     # break
#     print("컨티뉴 다음 문장입니다")
# print("프로그램을 종료합니다.")
    
    
# # break문 기본 이해
# for num in range(1,11) : 
#     if num == 4 :
#         print(f"숫자 {num}가 나와 종료합니다.")
#         break
#     print(f"숫자 {num}")
# print("프로그램을 종료합니다.")


# # for문과 continue
# list_num = [90, 25, 67, 45, 80]
# no = 0
# for a in list_num:
#     no += 1
#     if a < 60:
#         continue
#     print("%s번 학생 %s점으로 합격입니다." %(no,a))


# # 60점 이상인 학생들의 합격 문구 출력 예시(continue)
# score = [66, 72, 45, 89, 31]
# for i in range(len(score)) :
#     if score[i] < 60 :
#         continue
#     print(f"{i+1}번 학생 {score[i]}점으로 합격입니다.")


# # for문 예제 07(break) 가장 먼저 뽑힌 a형 고객을 선착순 1명만 찾는다고 한다고 할 때
# list_blood_type = ['b', 'b', 'ab', 'a', 'b', 'b']
# seq = 0
# for blood in list_blood_type :
#     seq += 1
#     if blood == 'a' :
#         print("{}번 고객님 {}형이시군요. 당첨되셨습니다.".format(seq, blood))
#         break
#     else :
#         print("{}번 고객님{}형이시군요. 불발입니다.".format(seq, blood))


# # 3부터 50까지 3의 배수의 합을 출력하세요.
# sum = 0
# for i in range(3, 51): # 3 4 5 6 .... 50
#     if i % 3 != 0:
#         continue   # 아래 코드 수행하지 않고 조건을 보러 간다.

#     # 3의 배수
#     sum += i
# print(sum)


# # 리스트 내포 변형 전
# # 1~100까지의 숫자중에 3의 배수를 리스트에 담은 후 해당 리스트를 print 하여라.
# list_result = []
# for num in range(1, 101) :
#     if num % 3 == 0 :
#         list_result.append(num)
# print(list_result)


# # for문 예제 08(리스트 내포)
# # 1~100까지의 숫자중에 3의 배수를 리스트에 담은 후 해당 리스트를 print 하여라
# list_result = [num for num in range(1, 101) if num % 3 == 0]
# print(list_result)




# ===============================================================================
# # 연습문제 dict 활용 : '메모의 마법' 책의 저자가 누구인지 출력하세요.
# books_dict = {'자기계발':{'말 그릇':'김윤나', '메모의 마법':'마에다 유지'},
#               '소설':{'아몬드':'손원평', '나미야 잡화점의 기적':'히가시노 게이고', '어린왕자':'생텍쥐페리'},
#               '과학':{'마음의 미래':'미치오 카쿠', '시간은 흐르지 않는다':'카를로 로벨리',
#                     '평행우주':'미치오 카쿠'}}

# for genre in books_dict:    # 3
#     books_of_genre = books_dict.get(genre)
#     if '메모의 마법' in books_of_genre:
#         print(books_of_genre.get('메모의 마법'))
# ===============================================================================