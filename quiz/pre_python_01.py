"""1. 아래와 같이 숫자를 두번 물어보게 하고 ★을 출력해서 사각형을 만드시오
가로의 숫자를 입력하시오 : 
세로의 숫자를 입력하시오 :

예시
<입력>
가로의 숫자를 입력하시오 : 5
세로의 숫자를 입력하시오 : 4

<출력>
★★★★★
★★★★★
★★★★★
★★★★★
 """

def makeSquare(Width, Height):
    Square = (('★' * Width + ("\n")) * (Height - 1)) + ('★' * Width)
    return Square

Width = int(input('가로의 숫자를 입력하시오 : '))

Height = int(input('세로의 숫자를 입력하시오 : '))

print(makeSquare(Width, Height))