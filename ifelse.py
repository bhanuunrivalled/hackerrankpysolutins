def is_inclusive(number, num1, num2):
    return num1 <= number <= num2


if __name__ == '__main__':
    number = int(input())
    is_odd = number % 2
    iseven = not is_odd
    if is_odd:
        print('Weird')
    elif iseven and is_inclusive(number,2,5):
        print("Not Weird")
    elif iseven and is_inclusive(number, 6, 20):
         print("Weird")
    else:
        print("Not Weird")
