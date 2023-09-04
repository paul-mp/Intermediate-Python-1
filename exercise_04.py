counter = 5
sum = 0

#utilized this for try catch block information: https://stackoverflow.com/questions/2083987/how-to-retry-after-exception
while True: 
    try:
        while counter > 0:
            user_input = int(input("Enter a string: "))
            sum += user_input
            counter -= 1
    except:
        print("Please enter an int.")
        continue
    break

print("Your sum is", sum)