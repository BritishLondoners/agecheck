def check_age():
    try:
        # Ask user for age
        age = int(input("Enter your age: "))

        # Validate age range (0–100)
        if age < 0 or age > 100:
            print("Error: Age entered is not realistic.")
        else:
            print(f"Age entered: {age}")

            # Check even or odd
            if age % 2 == 0:
                print("Your age is even.")
            else:
                print("Your age is odd.")

    except ValueError:
        # Handle non-integer input
        print("Error: Please enter a valid integer for age.")

# Run the function
check_age()
