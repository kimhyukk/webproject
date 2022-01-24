import random
a=random.randint(1,4)
b=input("1~3까지의 숫자를 입력하세요(1:바위, 2:가위, 3:보):")

if a==1:
    print("컴퓨터가 바위를 냈습니다.")
    if b==1:
        print("비겼습니다.")
    elif b==2:
        print("졌습니다.")
    else:
        print("이겼습니다.")

elif a==2:
    print("컴퓨터가 가위를 냈습니다.")
    if b==1:
        print("이겼습니다.")
    elif b==2:
        print("비겼습니다.")
    else:
        print("졌습니다.")

elif a==3:
    print("컴퓨터가 보를 냈습니다.")
    if b == 1:
      print("졌습니다.")
    elif b == 2:
        print("이겼습니다.")
    else:
        print("비겼습니다.")



#1.

a=int(input("티셔츠의 개수를 입력해주세요:"))
