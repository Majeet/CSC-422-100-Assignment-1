# https://mycourses.csp.edu/content/enforced/9016-35437.202430/csfiles/home_dir/courses/CSC422_OL_TER_PRIMARY/CSC422_OL_TER_PRIMARY/READ_ONLY/question/_6297317_1/embedded/CSC%20422%20Assignment%201%20Part%202Rev(1).pdf

class Pet:
    # pet class with name and age as the attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

class PetDatabase:
    # list of pets
    def __init__(self):
        self.pets = []

    def add_pets(self):
        # to add pets to the list
        while True:
            pet_info = input("Add pet (name, age): ")
            if pet_info.lower() == "done":
                break
            try:
                # splitting the input into name and age
                name, age = pet_info.split()
                age = int(age)
                self.pets.append(Pet(name, age)) #creating pet and adding to the list from user input
            except ValueError:
                # non integer age or invalid format error
                print("Invalid input. Please enter a name and an integer age.")

    def view_pets(self):
        # displaying pets in a table
        print("+--------------------------+")
        print("| ID | NAME      | AGE |")
        print("+--------------------------+")
        for i, pet in enumerate(self.pets):
            print("| {:<2} | {:<10} | {:<3} |".format(i, pet.name, pet.age)) # cell min. character for proper spacing
        print("+----------------------+")
        print("{} rows in set.".format(len(self.pets)))

def main():
    database = PetDatabase() #initialising the database
    while True:
        print("What would you like to do?")
        print("1) View all pets")
        print("2) Add more pets")
        print("7) Exit program")
        choice = input("Your choice: ")

        if choice == '1':
            database.view_pets()
        elif choice == '2':
            database.add_pets()
        elif choice == '7':
            print("Goodbye!")
            break
        else:
            # Handling invalid menu choices
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

# references
# https://www.geeksforgeeks.org/enumerate-in-python/