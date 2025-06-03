import random
import string

def meaningful_password(name, dob, address, nickname, pin):
    # Step 1: Extract meaningful parts
    name_part = name[:2].capitalize()           # First 2 letters of name
    nick_part = nickname[-2:].capitalize()      # Last 2 letters of nickname
    city_part = address[:3].lower()             # First 3 letters of city
    dob_part = ''.join(dob.split('/'))[-4:]     # Last 4 of DOB (usually year)
    pin_part = pin[-2:]                         # Last 2 digits of PIN

    # Step 2: Combine with symbols and mix
    symbols = random.choice('!@#$%&*')
    mid_digit = random.choice(string.digits)
    
    # Password format example: Roxydel2000#8
    password = f"{name_part}{nick_part}{city_part}{dob_part}{symbols}{mid_digit}{pin_part}"
    
    # Final random capitalization for spice
    password = ''.join(c.upper() if random.random() > 0.7 else c for c in password)

    return password

def evaluate_strength(password):
    length_score = min(len(password), 20) * 2  # Max 40
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)

    complexity_score = sum([has_upper, has_lower, has_digit, has_symbol]) * 15  # Max 60
    total_score = length_score + complexity_score

    if total_score >= 90:
        strength = "Very Strong"
    elif total_score >= 75:
        strength = "Strong"
    elif total_score >= 50:
        strength = "Moderate"
    else:
        strength = "Weak"

    return total_score, strength

# ---- Main Program ----
print("🔐 Meaningful Password Generator\n")

name = input("Enter your name: ")
dob = input("Enter your DOB (DD/MM/YYYY): ")
address = input("Enter your address/city: ")
nickname = input("Enter your nickname: ")
pin = input("Enter your PIN code: ")

password = meaningful_password(name, dob, address, nickname, pin)
score, rating = evaluate_strength(password)

print("\n✅ Generated Password:", password)
print(f"🔎 Strength Score: {score}% - {rating}")