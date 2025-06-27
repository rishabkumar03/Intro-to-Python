# PASSWORD STRENGTH CHECKER
    # Check if a password is 'Weak', 'Medium', 'Strong'. Criteria: <6 chars(Weak), 6-10 chars(Medium), >10 chars(Strong).

pasword = "505byArcticMonkeys"

if len(pasword) < 6:
    Strength = "Weak"
elif len(pasword) <= 10:
    Strength = "Medium"
else:
    Strength = "Strong"

print("Your password strength is:", Strength)