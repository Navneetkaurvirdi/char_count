try:
    print("***Welcome to this project***")
    a = input("Enter the sentence or paragraph: ")

    if not a.strip(): 
        raise ValueError("Input is empty")

    count = 0
    for i in a:
        count += 1
    print("The count is:", count)

except ValueError as ve:
    print(f"Error: {ve}")
except TypeError:
    print("Invalid entry")
