# Augustine
# Part 1
MIN_LENGTH = 10
MAX_AGE = 90
DIGITS = "0123456789"
UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
SYMBOLS = "!@#$%&*?"

accounts = [
    ("amina", "Nairobi@2026!Safe", 12),
    ("brian", "password", 240),
    ("cynthia", "Cyn#Tembo77kali", 45),
    ("dan", "dan", 400),
    ("esther", "welcome1", 30),
    ("faith", "Summer2025", 120),
    ("george", "G3orge!Rift*Valley", 5),
    ("hassan", "qwerty", 95),
    ("irene", "Summer2025", 60),
    ("james", "jamesmwangi", 88),
    ("kevin", "K3v!n", 10),
    ("linda", "welcome1", 200),
]

common = ["123456", "password", "qwerty", "admin123", "letmein", "welcome1"]
print("Number of accounts:", len(accounts))
print("First:", accounts[0])
print("Last:", accounts[-1])

# Part 2
short = []

for username, password, days in accounts:
    if len(password) < MIN_LENGTH:
        short.append(username)

print("Too short:", short)
print("How many:", len(short))

# Part 3
for username, password, days in accounts:
    has_digit = False
    has_upper = False
    has_symbol = False

    for ch in password:
        if ch in DIGITS:
            has_digit = True
        if ch in UPPER:
            has_upper = True
        if ch in SYMBOLS:
            has_symbol = True

    print(username, "digit:", has_digit, "upper:", has_upper, "symbol:", has_symbol)

# Part 4
results = []
strong = 0
medium = 0
weak = 0

for username, password, days in accounts:
    score = 0

    if len(password) >= MIN_LENGTH:
        score = score + 1
    if password not in common:
        score = score + 1

    has_digit = False
    has_upper = False
    has_symbol = False

    for ch in password:
        if ch in DIGITS:
            has_digit = True
        if ch in UPPER:
            has_upper = True
        if ch in SYMBOLS:
            has_symbol = True

    if has_digit:
        score = score + 1
    if has_upper:
        score = score + 1
    if has_symbol:
        score = score + 1

    if score == 5:
        rating = "Strong"
        strong = strong + 1
    elif score >= 3:
        rating = "Medium"
        medium = medium + 1
    else:
        rating = "Weak"
        weak = weak + 1

    results.append((score, username, rating))
    print(username, "score:", score, rating)

print("Strong:", strong, "Medium:", medium, "Weak:", weak)

# Part 5
results.sort()

print("Three weakest:")
for score, username, rating in results[:3]:
    print(username, "with", score)

# Part 6
for username, password, days in accounts:
    if password in common:
        print("COMMON PASSWORD:", username)
    if password == username:
        print("SAME AS USERNAME:", username)

# Part 7
seen = []

for username, password, days in accounts:
    if password in seen:
        continue

    shared = []
    for username2, password2, days2 in accounts:
        if password2 == password:
            shared.append(username2)

    if len(shared) > 1:
        print("REUSED:", password, "by", shared)
        seen.append(password)

# Part 8
expired = []
for username, password, days in accounts:
    if days > MAX_AGE:
        expired.append(username)

print("Expired:", expired)

compliant = 0

for username, password, days in accounts:
    for score, name, rating in results:
        if name == username:
            if rating == "Strong" and days <= MAX_AGE:
                compliant = compliant + 1

print("Audited:", len(accounts))
print("Strong:", strong)
print("Medium:", medium)
print("Weak:", weak)
print("Expired:", len(expired))
print("Reused: 2")
print("Compliant:", compliant)
print("Compliance rate: " + f"{compliant / len(accounts) * 100:.1f}" + "%")