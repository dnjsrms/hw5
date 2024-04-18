#사용자 정의 함수
def read_single_digit(digit):
    if digit == 0:
        return "공"
    elif digit == 1:
        return "일"
    elif digit == 2:
        return "이"
    elif digit == 3:
        return "삼"
    elif digit == 4:
        return "사"
    elif digit == 5:
        return "오"
    elif digit == 6:
        return "육"
    elif digit == 7:
        return "칠"
    elif digit == 8:
        return "팔"
    elif digit == 9:
        return "구"

def read_number(number):
    if number < 10:  
        return read_single_digit(number)
    elif number < 100:
        tens = number // 10
        units = number % 10
        return read_single_digit(tens) + read_single_digit(units)
   
    else:  
        hundreds = number // 100
        remainder = number % 100
        if remainder == 0:
            return read_single_digit(hundreds)
        else:
            return read_single_digit(hundreds) + read_number(remainder)

#주 프로그램부


user_input = int(input("세 자리수 이하의 10진 정수를 입력하세요: "))
if user_input < 0 or user_input > 999:
    print("세 자리수 이하의 정수를 입력해주세요.")
else:
    result = read_number(user_input)
    print(result)


