# Homework
# A program that asks for a base and a power.
# For example:
# x? 2
# n? 3
# Then the program should print the answer LIKE THIS: 2x2x2=8
x = int(input("Please give me base number x: "))
n = int(input("Please give me power number n: "))

message = ""

for n in range(1, n+1):
    message += str(x) + "x"

answer = x**n
message += "=" + str(answer)
message = message.replace("x=","=")

print(message)

quit()