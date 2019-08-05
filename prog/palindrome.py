ui = input("Enter your string: ").strip().upper()

if ui == ui[::-1]:
    print("You have entered a palindrome")
else:
    print("Not a palindrome")
    