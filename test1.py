import random
# a=random.randint(1,4)
# b=input("1~3까지의 숫자를 입력하세요(1:바위, 2:가위, 3:보):")
#
# if a==1:
#     print("컴퓨터가 바위를 냈습니다.")
#     if b==1:
#         print("비겼습니다.")
#     elif b==2:
#         print("졌습니다.")
#     else:
#         print("이겼습니다.")
#
# elif a==2:
#     print("컴퓨터가 가위를 냈습니다.")
#     if b==1:
#         print("이겼습니다.")
#     elif b==2:
#         print("비겼습니다.")
#     else:
#         print("졌습니다.")
#
# elif a==3:
#     print("컴퓨터가 보를 냈습니다.")
#     if b == 1:
#       print("졌습니다.")
#     elif b == 2:
#         print("이겼습니다.")
#     else:
#         print("비겼습니다.")
#
#
#
# #1.
#
# num_Tshirt=int(input("티셔츠의 개수를 입력해주세요:"))
# num_sweater=int(input("스웨터의 개수를 입력해주세요:"))
#
# price=num_sweater*10000+num_sweater*30000
#
# if price > 100000:
#     price=price*0.85
#     print(price)
# else:
#     price=price*0.95
#     print(price)

#2
#
# a=random.randint(1,101)
# i=0
# while True:
#     i += 1
#     print(i, "회 시도")
#     b = int(input("숫자를 입력하세요:"))
#     if a>b:
#         print("업")
#     elif a<b:
#         print("다운")
#     else:
#         print("정답")
#         break

#
# # 비밀번호 문제
# def pw(x):
#     len_pw=len(x)
#     return len_pw
#
# pwrd=input("비밀번호를 입력하세요:")
#
# if pw(pwrd)>=9:
#     print("good")
# elif pw(pwrd)<5:
#     print("bad")
# else:
#     print("normal")


#할인 제도

#계약금액(contractPrice), 사용 개월 수(period), 카드 코드(cardCode)

contractPrice=int(input("계약 금액을 입력하세요:"))
period=int(input("사용 개월 수:"))
cardCode=int(input("카드 코드:"))

period_dis=1
cardCode_dis=1
if period>12:
    period_dis=0.2
elif period<6:
    period_dis=0
else:
    period_dis=0.1

if cardCode==11:
    cardCode_dis=0.05
elif cardCode==12:
    cardCode_dis=0.08
elif cardCode==13:
    cardCode_dis=0.12

price=contractPrice-(contractPrice*period_dis)-(contractPrice*cardCode_dis)

print(price)




