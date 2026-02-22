# Write program to check password strength rules Input a string s (assume lowercase/uppercase/digits may appear) Now check: 
# if the string contains full fills all these and print final output: valid (STRONG) or Invalid password (WEAK)
# 1. length >= 8
# 2. has at least 1 digit
# 3. has at least 1 uppercase
# 4. has at least 1 lowercase Print “STRONG” else “WEAK”


s = input("Enter your password: ")

has_digit = False
has_upper = False
has_lower = False

# Check length first
if len(s) >= 8:

    for ch in s:
        if ch >= '0' and ch <= '9':
            has_digit = True
        elif ch >= 'A' and ch <= 'Z':
            has_upper = True
        elif ch >= 'a' and ch <= 'z':
            has_lower = True

    if has_digit and has_upper and has_lower:
        print("STRONG")
    else:
        print("WEAK")

else:
    print("WEAK")