def user_radius():
    return float(input("Enter the radius of your circle: "))

choice = int(input("What do you want to find out:\n1. Area\n2. Circumference\n: "))

if choice not in [1, 2]:
    print("Invalid choice!")
else:
    radius = user_radius()

    if choice == 1:
        answer = (radius ** 2) * 3.14
        print("Area:", answer)

    elif choice == 2:
        answer = (radius * 2) * 3.14
        print("Circumference:", answer)


