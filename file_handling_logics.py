# Day 5: File Reading with Error Handling
# Goal: Open a file safely

filename = input("Enter the filename you want to read: ")

try:
    with open(filename, "r") as f:
        data = f.read()
        print("--- File Content ---")
        print(data)
        print("--------------------")

except FileNotFoundError:
    print("Error: The file", filename, "was not found.")

except Exception:
    print("An unexpected error occurred.")

finally:
    print("Operation attempt finished.")



# Day 5: Saving User Data to a File
# Goal: Store a dictionary into a permanent text file

user_dict = {}

# Collecting Data
name = input("Enter your name: ")
lang = input("Favorite language: ")

user_dict["name"] = name
user_dict["language"] = lang

# Saving to file ('a' means Append - adds to the end of the file)
try:
    with open("users.txt", "a") as f:
        # Convert dictionary to string so it can be saved
        f.write(str(user_dict) + "\n")
    print("Success! Data for", name, "has been saved.")

except:
    print("Something went wrong while saving the file.")
