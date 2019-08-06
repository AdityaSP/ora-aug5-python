# accept comma seperated numbers and then the program should return their sum
# 1,2,3
# 6

ui = input("Enter comma seperated numbers: ").split(',')
total = 0
for i in ui:
    total += int(i)
print("The sum is ", total)    