# ROBOT RESCUE DATABASE - STARTER CODE
# Your task: complete the binary search and menu system.
# Data structure robots[ID,"name","sector", "battery", "status" ]

robots = [
    [101, "Scout-1", "Sector A", 92, "AVAILABLE"],
    [108, "Medic-2", "Sector B", 67, "BUSY"],
    [115, "Rover-3", "Sector A", 45, "CHARGING"],
    [121, "Drone-4", "Sector C", 88, "AVAILABLE"],
    [128, "Carrier-5", "Sector B", 73, "BUSY"],
    [134, "Scout-6", "Sector D", 56, "AVAILABLE"],
    [142, "Atlas-7", "Sector D", 81, "AVAILABLE"],
    [149, "Medic-8", "Sector A", 39, "CHARGING"],
    [157, "Drone-9", "Sector C", 95, "AVAILABLE"],
    [164, "Rover-10", "Sector B", 62, "BUSY"],
    [172, "Atlas-11", "Sector E", 76, "AVAILABLE"],
    [181, "Scout-12", "Sector E", 51, "CHARGING"],
    [193, "Carrier-13", "Sector C", 84, "AVAILABLE"],
    [205, "Medic-14", "Sector D", 69, "BUSY"],
    [218, "Drone-15", "Sector A", 97, "AVAILABLE"],
    [231, "Atlas-16", "Sector E", 42, "CHARGING"]
]

def show_all_robots():
    print("\n--- ROBOT DATABASE ---")


def linear_search_robot(target_id):
    

    # TODO: use a for loop to match each entry with a target_ID.
    # TODO: add +1 to the counter of comparisons.
    
    return None
def binary_search_robot(target_id):
    low = 0
    high = len(robots) - 1
    

    # TODO: Use a while loop that continues while low <= high
    # TODO: Calculate the middle index
    # TODO: Read the robot ID at the middle index
    # TODO: Increase the comparisons counter
    # TODO: Print which ID is being checked
    # TODO: If target_id == middle ID, return the robot and comparison count
    # TODO: If target_id > middle ID, move low above middle
    # TODO: If target_id < middle ID, move high below middle

    return None


def show_robot(robot):
    print("\n-----------------------------")
    print("ROBOT FOUND")
    print("-----------------------------")
    print("ID:      ", robot[0])
    print("Name:    ", robot[1])
    print("Location:", robot[2])
    print("Battery: ", str(robot[3]) + "%")
    print("Status:  ", robot[4])

    # TODO CHALLENGE: classify battery as GOOD / LOW / CRITICAL
    # TODO CHALLENGE: say whether the robot is ready to deploy


def search_robot():
    target_id = int(input("Enter Robot ID: "))
    
    robot = binary_search_robot(target_id)

    if robot is not None:
        show_robot(robot)
    else:
        print("Robot", target_id, "was not found.")
        


def show_ready_robots():
    print("\n--- READY FOR EMERGENCY DEPLOYMENT ---")
    # TODO: Use a for loop to display robots that are AVAILABLE
    #       and have a battery level of at least 70%


running = True
while running:
    print("\n=================================")
    print("   RESCUE ROBOT CONTROL SYSTEM")
    print("=================================")
    print("1 - Search robot using binary search")
    print("2 - Display robot database")
    print("3 - Show robots ready for deployment")
    print("4 - deploy first available robot")
    print("5 - deplay robot by ID")
    print("6 - Exit")
    choice = input("select option:")

    if choice == 1:
    
