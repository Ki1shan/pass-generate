import random
import string

def meaningful_random_password(name, dob, address, nickname, pin):
    # Extract parts from input
    parts = [
        name[:2].capitalize(),
        nickname[-2:].capitalize(),
        address[:3].lower(),
        ''.join(dob.split('/'))[-4:],  # Year from DOB
        pin[-2:]
    ]

    # Shuffle parts to make each password unique
    random.shuffle(parts)

    # Add random symbols and digits in random positions
    symbols = random.choices('!@#$%^&*?', k=2)
    digits = random.choices(string.digits, k=2)

    combined = parts + symbols + digits
    random.shuffle(combined)

    # Join and apply random casing
    password = ''.join(combined)
    password = ''.join(
        c.upper() if random.random() > 0.5 else c.lower()
        for c in password
    )

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
print("🔐 Meaningful Random Password Generator\n")

name = input("Enter your name: ")
dob = input("Enter your DOB (DD/MM/YYYY): ")
address = input("Enter your address/city: ")
nickname = input("Enter your nickname: ")
pin = input("Enter your PIN code: ")

password = meaningful_random_password(name, dob, address, nickname, pin)
score, rating = evaluate_strength(password)

print("\n✅ Generated Password:", password)
print(f"🔎 Strength Score: {score}% - {rating}")
