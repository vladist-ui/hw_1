def reverse_number(n):
    reversed_number = 0
    negative = n < 0
    n = abs(n)

    while n > 0:
        last_digit = n % 10
        reversed_number = reversed_number * 10 + last_digit
        n //= 10


    return -reversed_number if negative else reversed_number


input_number = int(input("Введите целое число: "))
output_number = reverse_number(input_number)
print(output_number)