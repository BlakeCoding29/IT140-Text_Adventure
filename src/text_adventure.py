rooms = {
    "Visitor Center": {
        "south": "General Store",
        "east": "Coffee Shop"
    },

    "General Store": {
        "north": "Visitor Center",
        "east": "Outdoor Outfitter",
        "item": "Trail Map"
    },

    "Outdoor Outfitter": {
        "west": "General Store",
        "east": "Marina",
        "item": "Bear Spray"
    },

    "Coffee Shop": {
        "north": "Motel",
        "west": "Visitor Center",
        "east": "Gift Shop",
        "item": "Flashlight"
    },

    "Motel": {
        "south": "Coffee Shop",
        "item": "First Aid Kit"
    },

    "Gift Shop": {
        "west": "Coffee Shop",
        "south": "Marina",
        "item": "Park Pass"
    },

    "Marina": {
        "north": "Gift Shop",
        "south": "Ranger Station",
        "west": "Outdoor Outfitter",
        "item": "Two-Way Radio"
    },

    "Ranger Station": {
        "north": "Marina",
        "villain": "Grizzly Bear"
    }
}

current_room = "Visitor Center"

while current_room != "Ranger Station":
    print("\nCurrent room:", current_room)

    direction = input("Enter a direction: ").lower()

    if direction in rooms[current_room] and direction in [
        "north", "south", "east", "west"
    ]:
        current_room = rooms[current_room][direction]
    else:
        print("You cannot go that way.")

print("\nYou entered the Ranger Station.")
print("The grizzly bear ends your adventure.")
    