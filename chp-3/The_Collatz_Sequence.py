def collatz(number):
    print(number)
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1
    
n = int(input("Enter a number: "))
value = collatz(n)
while value != 1:
    value = collatz(value)
print(1)


