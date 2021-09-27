def fibonacci(number):
    if number > 1:
        return fibonacci(number-1) + fibonacci(number-2)
    else:
        return 1

for i in range(10):
    print(fibonacci(i))
    