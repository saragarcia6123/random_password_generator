import random

special_range = [(33, 33),(35,47),(58, 64),(91, 96),(123, 126)]

def gen_random_password(min_length: int, max_length: int) -> list[str]:
    password = []
    length = random.randint(min_length, max_length)
    for i in range(length):
        char = chr(gen_random_char_ascii())
        password.append(char)
    return password

def gen_random_char_ascii() -> int:
    random_type = random.randint(0,3)
    if random_type == 0:
        return random.randint(65,90) # Uppercase letter
    elif random_type == 1:
        return random.randint(97,122) #Lowercase letter
    elif random_type == 2:
        return random.randint(48,57) #Number
    else:
        global special_range
        start, end = random.choice(special_range)
        return random.randint(start, end) # Special character

def is_valid_password(password: list[str]) -> bool:
    if len(password) < 12:
        return False
    
    has_upper = False
    has_lower = False
    has_num = False
    has_special = False
    
    for index, char in enumerate(password):
        ascii_val = ord(char)
        if 65 <= ascii_val <= 90:
            has_upper = True
        elif 97 <= ascii_val <= 122:
            has_lower = True
        elif 48 <= ascii_val <= 57:
            has_num = True
        else:
            global special_range
            in_range = any(start <= ascii_val <= end for start, end in special_range)
            if in_range:
                has_special = True
                
        if has_num and has_lower and has_upper and has_special:
            return True
    return False

def gen_until_valid(min_length, max_length) -> str:
    password = []
    while not is_valid_password(password):
        password = gen_random_password(min_length, max_length)
    return ''.join(password)

number_of_passwords = int(input("Enter number of passwords to generate: "))
passwords = [gen_until_valid(12, 24) for i in range(number_of_passwords)]

for p in passwords:
    print(p)
