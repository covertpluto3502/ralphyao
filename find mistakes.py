# Try to spot problems and fix
# - typos
# - syntax

digits = [0, 1, 4, 2, 4, 6, 5, 5, 3]

while True:
    print("What item of the list do you want(or press Ctrl+C to exit)")
    user_input = input()
    index = int(user_input)
    print("Getting the item at", index)
    print ("Item at", index, "is", digits[index])
