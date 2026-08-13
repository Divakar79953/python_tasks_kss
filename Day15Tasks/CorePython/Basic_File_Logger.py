#Basic File Logger


try:
    n = int(input("How many logs do you want to enter? "))

    with open("user_logs.txt", "a") as file:

        for i in range(n):
            log = input("Enter user action: ")
            file.write(log + "\n")

    print("Logs saved successfully.")

except ValueError:
    print("Invalid input! Please enter a number.")

except FileNotFoundError:
    print("File not found.")

except PermissionError:
    print("Permission denied. Cannot write to the file.")
