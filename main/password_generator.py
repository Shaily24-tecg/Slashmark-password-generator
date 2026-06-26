import random

def generatePassword(pwlength):

    alphabet = "abcdefghijklmnopqrstuvwxyz!@#$%^&*"
    passwords = []

    for i in pwlength:

        password = ""

        for j in range(i):
            next_letter_index = random.randrange(len(alphabet))
            password += alphabet[next_letter_index]

        password = replaceWithNumber(password)
        password = replaceWithUppercaseLetter(password)

        if password not in passwords:
            passwords.append(password)

    return passwords


def replaceWithNumber(pword):
    for i in range(random.randrange(1, 3)):
        replace_index = random.randrange(len(pword) // 2)
        pword = pword[:replace_index] + str(random.randrange(10)) + pword[replace_index + 1:]
    return pword


def replaceWithUppercaseLetter(pword):
    for i in range(random.randrange(1, 3)):
        replace_index = random.randrange(len(pword) // 2, len(pword))
        pword = pword[:replace_index] + pword[replace_index].upper() + pword[replace_index + 1:]
    return pword


def check_strength(password):
    if len(password) >= 10:
        return "Strong"
    elif len(password) >= 7:
        return "Medium"
    else:
        return "Weak"


def main():

    print("\n=== PASSWORD GENERATOR SYSTEM ===\n")

    while True:
        try:
            numPasswords = int(input("How many passwords do you want to generate? "))
            if numPasswords <= 0:
                print("Enter a number greater than 0")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a number.")

    print("Generating " + str(numPasswords) + " passwords\n")

    passwordLengths = []

    print("Minimum length of password should be 6")

    for i in range(numPasswords):
        length = int(input(f"Enter the length of Password #{i+1}: "))
        if length < 6:
            length = 6
        passwordLengths.append(length)

    Password = generatePassword(passwordLengths)

    for i, pwd in enumerate(Password, start=1):
        strength = check_strength(pwd)
        print(f"Generated Password #{i}: {pwd} | Strength: {strength}")

    with open("passwords.txt", "w") as file:
        for i, pwd in enumerate(Password, start=1):
            file.write(f"Generated Password #{i}: {pwd}\n")

    print("\nPasswords saved to passwords.txt")
    print("All passwords generated successfully!")


main()