# 컴퓨터가 3자리 숫자를 문제로 내도록.

# 1~9로만 사용
# 중복된 숫자는 허용 x


from random import sample


cpu_numbers = sample(range(1, 10), 3)

print(cpu_numbers)

# 사람이 3자리 숫자를 입력 > 맞출때 까지 계속 입력
# 한칸한칸 비교해야해서 list로 진행

while True :
    user_number = list()

    # 3자리 숫자를 입력하면 > 3칸의 목록으로 분리 
    input_num = int(input('3자리 숫자 입력 : '))

    #ex. 123 => [1, 2, 3]으로 분리.
    # 3자리 정수가 들어왔다고 전제.

    # 제일 먼저 추가 : 100의 자리
    # 그 다음 : 10의 자리
    # 그 다음 : 1의 자리

    user_number.append(input_num // 100) # 100의 자리
    user_number.append(input_num // 10 % 10) # 10의 자리
    user_number.append(input_num % 10) # 1의 자리

    print(user_number)