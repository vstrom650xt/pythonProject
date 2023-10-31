cat_age = int(input("Enter your cat's age: "))

if cat_age == 1:
    human_age = 15
elif cat_age == 2:
    human_age = 15 + 10
else:
    human_age = 15 + 10 + (cat_age - 2) * 4

print(f"Your cat's age is approximately equivalent to {human_age} human years.")
