# 컴퓨터가 3자리 숫자를 문제로 내도록.

# 1~9로만 사용
# 중복된 숫자는 허용 x


from random import sample


cpu_numbers = sample(range(1, 10), 3)

print(cpu_numbers)