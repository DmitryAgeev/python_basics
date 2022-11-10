import random

print("Pick a number between 0 and 100. The computer will try to guess your number.")
start = 0
end = 100
try_count = 0
ask = None

while ask not in {"Yes", "yes"}:
    try_count += 1
    number = random.randint(start, end)
    ask = input(f"{number}, right? ")
    if ask in {"Less", "less"}:
        end = number - 1
    elif ask in {"More", "more"}:
        start = number + 1
print(f"Computer guess on {try_count} tries")
