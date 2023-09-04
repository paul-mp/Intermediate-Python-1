def count_letters(string):
    letter_count = {}

    for char in string:
        if char.islower():
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1

    return letter_count

#Im not sure why but on canvas the output is wrong. This actually counts the lowercase letters

user_input = input("Enter a string: ")

result = count_letters(user_input)

print(result)
