def main():
    full_name = input("Please enter in a full name: ").split()
    total = 0
    for x in full_name:
        total += len(x)
    print(total)

