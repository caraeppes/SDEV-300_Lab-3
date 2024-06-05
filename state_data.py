"""
Cara Eppes
6/4/2024
SDEV 300
Lab 3

This is a program that provides the user with information about
the U.S. states including their capitals, populations, and state
flowers.  The user is presented with a menu where the can choose
to get data for all the states, get data and an image of the state
flower for a specific state, display a bar graph of the top 5 most
populated states, update a state's population, or exit the program.
"""

from PIL import Image
import matplotlib.pyplot as plt


def get_capital(state):
    """Gets the capital of a state from the STATE_DATA dictionary"""
    return STATE_DATA.get(state).get("capital")


def get_population(state):
    """Gets the population of a state from the STATE_DATA dictionary"""
    return STATE_DATA.get(state).get("population")


def get_flower(state):
    """Gets the state flower of a state from the STATE_DATA dictionary"""
    return STATE_DATA.get(state).get("flower")


def display_state_data(state):
    """Formats and displays the capital, population, and flower for a specific state"""
    formatted_population = f"{get_population(state):,}"
    print(f"{state : <20}{get_capital(state) : <20}{formatted_population : <20}"
          f"{get_flower(state) : <20}")


def display_all_states_data():
    """Formats and displays the capital, population, and flower for all the U.S. states"""
    print_headers()
    for state in STATE_DATA:
        display_state_data(state)


def find_and_display_state_by_name():
    """Allows user to select a state and displays that state's data and an image of its flower"""
    state = get_and_validate_state_input()
    print_headers()
    display_state_data(state)
    display_flower_image(state)


def display_flower_image(state):
    """Displays an image of a specific state's flower"""
    img = Image.open('./Flower Images/' + STATE_DATA.get(state).get('flower') + '.jpeg')
    plt.imshow(img)
    plt.axis('off')
    plt.show()


def sort_by_population():
    """Sorts the states by population from least to most populated.
    Returns a sorted list of tuples.  Each tuple contains the state's population
     at the first index and its name at the second index"""
    return sorted([(get_population(state), state) for (state, data) in STATE_DATA.items()])


def create_most_populated_states_graph():
    """Sorts the states by population and displays a bar graph of the
    5 most populated states"""
    most_populated_states = sort_by_population()[-5:]
    state_names = []
    populations = []
    for state in most_populated_states:
        state_names.append(state[1])
        populations.append(state[0])

    plt.bar(state_names, populations)
    plt.ylabel("Population (in Millions)")
    plt.title("Most Populated U.S. States")
    plt.show()


def update_population():
    """Allows a user to select a state and update its population"""
    print("\nUpdate State's Population")
    state = get_and_validate_state_input()
    population = get_and_validate_population()
    STATE_DATA.get(state).update({'population': population})
    print(f"Updated {state}'s population to {population:,}.")


def get_and_validate_state_input():
    """Gets state name as user input, validates it is a U.S. state,
    and returns the valid state name"""
    while True:
        state_input = input("\nEnter a state: ").title()
        for state in STATE_DATA:
            if state_input == state:
                return state
        print("State not found.  Please enter a valid U.S. state.")


def get_and_validate_population():
    """Gets population as user input, validates it is a positive integer,
    and returns the population as an int"""
    while True:
        population = input("Enter population: ")
        if population.isdigit():
            return int(population)
        print("Invalid response.  Population must be a positive integer.  Please try again.\n")


def print_headers():
    """Prints headers for state data"""
    print(f"\n\033[1m{'State' : <20}{'Capital' : <20}{'Population' : <20}{'Flower' : <20}\033[0m")


def display_menu():
    """Prints the menu options to the console"""
    menu = """
    Please select an option:
        a. Display all U.S. states in alphabetical order with their capital, population, and flower
        b. Search for a U.S. state and display its capital, population, and an image of its flower
        c. Display a bar graph of the top 5 most populated U.S. states
        d. Update a state's population
        e. Exit Program 
        """
    print(menu)


def run():
    """Displays menu to user and runs the program until the user chooses to exit"""
    print("Welcome to the U.S. States Data Application!")
    while True:
        display_menu()
        selection = input("Enter selection: ")
        if selection == "a":
            display_all_states_data()
        elif selection == "b":
            find_and_display_state_by_name()
        elif selection == "c":
            create_most_populated_states_graph()
        elif selection == "d":
            update_population()
        elif selection == "e":
            print("Exiting program.  Thanks for using the U.S. State Data Application.")
            break
        else:
            print("Invalid menu selection.  Please enter a valid option (a - e).")


# Dictionary containing the 50 U.S. states in alphabetical order
# with their capitals, populations, and flowers
STATE_DATA = {
    "Alabama": {
        "capital": "Montgomery",
        "population": 5143033,
        "flower": "Camellia"
    },
    "Alaska": {
        "capital": "Juneau",
        "population": 733536,
        "flower": "Alpine Forget-me-not"
    },
    "Arizona": {
        "capital": "Phoenix",
        "population": 7497004,
        "flower": "Saguaro Cactus Blossom"
    },
    "Arkansas": {
        "capital": "Little Rock",
        "population": 3089060,
        "flower": "Apple Blossom"
    },
    "California": {
        "capital": "Sacramento",
        "population": 38889770,
        "flower": "California Poppy"
    },
    "Colorado": {
        "capital": "Denver",
        "population": 5914181,
        "flower": "Rocky Mountain Columbine"
    },
    "Connecticut": {
        "capital": "Hartford",
        "population": 3625646,
        "flower": "Mountain Laurel"
    },
    "Delaware": {
        "capital": "Dover",
        "population": 1044321,
        "flower": "Peach Blossom"
    },
    "Florida": {
        "capital": "Tallahassee",
        "population": 22975931,
        "flower": "Orange Blossom"
    },
    "Georgia": {
        "capital": "Atlanta",
        "population": 11145304,
        "flower": "Cherokee Rose"
    },
    "Hawaii": {
        "capital": "Honolulu",
        "population": 1430877,
        "flower": "Pua Aloalo"
    },
    "Idaho": {
        "capital": "Boise",
        "population": 1990456,
        "flower": "Syringa"
    },
    "Illinois": {
        "capital": "Springfield",
        "population": 12516863,
        "flower": "Violet"
    },
    "Indiana": {
        "capital": "Indianapolis",
        "population": 6892124,
        "flower": "Peony"
    },
    "Iowa": {
        "capital": "Des Moines",
        "population": 3214315,
        "flower": "Wild Rose"
    },
    "Kansas": {
        "capital": "Topeka",
        "population": 2944376,
        "flower": "Wild Native Sunflower"
    },
    "Kentucky": {
        "capital": "Frankfort",
        "population": 4540745,
        "flower": "Goldenrod"
    },
    "Louisiana": {
        "capital": "Baton Rouge",
        "population": 4559475,
        "flower": "Magnolia"
    },
    "Maine": {
        "capital": "Augusta",
        "population": 1402106,
        "flower": "White Pine Cone and Tassel"
    },
    "Maryland": {
        "capital": "Annapolis",
        "population": 6196525,
        "flower": "Black-Eyed Susan"
    },
    "Massachusetts": {
        "capital": "Boston",
        "population": 7020058,
        "flower": "Mayflower"
    },
    "Michigan": {
        "capital": "Lansing",
        "population": 10041241,
        "flower": "Apple Blossom"
    },
    "Minnesota": {
        "capital": "St. Paul",
        "population": 5761530,
        "flower": "Lady Slipper"
    },
    "Mississippi": {
        "capital": "Jackson",
        "population": 2940452,
        "flower": "Magnolia"
    },
    "Missouri": {
        "capital": "Jefferson City",
        "population": 6215144,
        "flower": "White Hawthorn Blossom"
    },
    "Montana": {
        "capital": "Helena",
        "population": 1142746,
        "flower": "Bitterroot"
    },
    "Nebraska": {
        "capital": "Lincoln",
        "population": 1988698,
        "flower": "Goldenrod"
    },
    "Nevada": {
        "capital": "Carson City",
        "population": 3210931,
        "flower": "Sagebrush"
    },
    "New Hampshire": {
        "capital": "Concord",
        "population": 1405105,
        "flower": "Purple Lilac"
    },
    "New Jersey": {
        "capital": "Trenton",
        "population": 9320865,
        "flower": "Violet"
    },
    "New Mexico": {
        "capital": "Santa Fe",
        "population": 2115266,
        "flower": "Yucca"
    },
    "New York": {
        "capital": "Albany",
        "population": 19469232,
        "flower": "Rose"
    },
    "North Carolina": {
        "capital": "Raleigh",
        "population": 10975017,
        "flower": "Dogwood"
    },
    "North Dakota": {
        "capital": "Bismarck",
        "population": 788940,
        "flower": "Wild Prairie Rose"
    },
    "Ohio": {
        "capital": "Columbus",
        "population": 11812173,
        "flower": "Red Carnation"
    },
    "Oklahoma": {
        "capital": "Oklahoma City",
        "population": 4088377,
        "flower": "Mistletoe"
    },
    "Oregon": {
        "capital": "Salem",
        "population": 4227337,
        "flower": "Oregon Grape"
    },
    "Pennsylvania": {
        "capital": "Harrisburg",
        "population": 12951275,
        "flower": "Mountain Laurel"
    },
    "Rhode Island": {
        "capital": "Providence",
        "population": 1098082,
        "flower": "Violet"
    },
    "South Carolina": {
        "capital": "Columbia",
        "population": 5464155,
        "flower": "Yellow Jessamine"
    },
    "South Dakota": {
        "capital": "Pierre",
        "population": 928767,
        "flower": "American Pasque"
    },
    "Tennessee": {
        "capital": "Nashville",
        "population": 7204002,
        "flower": "Iris"
    },
    "Texas": {
        "capital": "Austin",
        "population": 30976754,
        "flower": "Bluebonnet"
    },
    "Utah": {
        "capital": "Salt Lake City",
        "population": 3454232,
        "flower": "Sego Lily"
    },
    "Vermont": {
        "capital": "Montpelier",
        "population": 647818,
        "flower": "Red Clover"
    },
    "Virginia": {
        "capital": "Richmond",
        "population": 8752297,
        "flower": "American Dogwood"
    },
    "Washington": {
        "capital": "Olympia",
        "population": 7841283,
        "flower": "Coast Rhododendron"
    },
    "West Virginia": {
        "capital": "Charleston",
        "population": 1766107,
        "flower": "Rhododendron"
    },
    "Wisconsin": {
        "capital": "Madison",
        "population": 5931367,
        "flower": "Wood Violet"
    },
    "Wyoming": {
        "capital": "Cheyenne",
        "population": 586485,
        "flower": "Indian Paintbrush"
    }
}


def main():
    """Main function"""
    run()


main()
