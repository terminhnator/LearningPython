# for n in range(1,101):
#     if n % 3 == 0 and n % 5 == 0:
#         print("FizzBuzz")
#     elif n % 5 == 0:
#         print("Buzz")
#     elif n % 3 == 0:
#         print("Fizz")
#     else:
#         print(n)


for n in range(1, 101):
    output = ""

    if n % 3 == 0:
        output += "Fizz"
    if n % 5 == 0:
        output += "Buzz"
    if output == "":
        output = n

    print(output)

print('\n'.join('Fizz' * (i%3==0) + 'Buzz' * (i%5==0) or str(i) for i in range(1,101)))