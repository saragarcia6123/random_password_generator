import random

def gen_random_password() -> list[str]:
    password = []
    length = random.randint(12,24)
    for i in range(length):
        char = chr(gen_random_char_ascii())
        password.append(char)
    return password

def gen_random_char_ascii() -> int:
    random_type = random.randint(0,3)
    if random_type == 0:
        return random.randint(65,90) #uppercase letter ascii
    elif random_type == 1:
        return random.randint(97,122) #lowercase letter ascii
    elif random_type == 2:
        return random.randint(48,57) #number
    else:
        special_range = [(33, 33),(35,47),(58, 64),(91, 96),(123, 126)]
        start, end = random.choice(special_range)
        return random.randint(start, end) #special char ascii

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
            special_range = [(33, 33),(35,47),(58, 64),(91, 96),(123, 126)]
            in_range = any(start <= ascii_val <= end for start, end in special_range)
            if in_range:
                has_special = True
                
        if has_num and has_lower and has_upper and has_special:
            return True
    return False

def gen_until_valid():
    password = []
    while not is_valid_password(password):
        password = gen_random_password()
    return ''.join(password)

passwords = [gen_until_valid() for i in range(10)]

for p in passwords:
    print(p)