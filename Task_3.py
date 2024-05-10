import re
def password_strength_checker(password):
    length_score = len(password) * 4
    uppercase_count = len(re.findall(r'[A-Z]', password))
    lowercase_count = len(re.findall(r'[a-z]',password))
    digit_count = len(re.findall(r'\d', password))
    special_char_count = len(re.findall(r'[!@#$%^&*()-_+=:;"\|?/]', password))

    score = 0
    score += length_score
    score =+ uppercase_count * 5
    score =+ lowercase_count * 5
    score =+ digit_count * 5
    score += special_char_count * 5

    if score < 30:
        resp = "Weak Password"
    elif score < 60:
        resp = "Moderate Password"
    elif score < 90:
        resp = "Strong Password"
    else:
        resp = "Very Strong Password"
    
    print (f"Password Strength: {resp} with score of {score}/100")

def main():
    password = input("Enter Your password: ")
    password_strength_checker(password)

if __name__== "__main__":
    main()