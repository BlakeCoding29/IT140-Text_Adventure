# Project Design

## Project Overview

This project is a text-based adventure game created for SNHU IT-140: Introduction to Scripting. The purpose of this project is to apply fundamental Python concepts by designing and developing an interactive game.

The game is currently in the design phase. The project includes the game concept, room layout, pseudocode, and supporting documentation. The final Python implementation will be completed later in the course.

---

## Game Theme

The game takes place in Glacier National Park.

The player begins at the Visitor Center and explores different locations throughout the park to collect six important items. The final destination is the Ranger Station, where a grizzly bear is waiting. The player must collect every required item before entering the Ranger Station. Entering too early results in a loss, while collecting every item first results in a win.

---

## Game Locations

- Visitor Center (Starting Room)
- General Store
- Outdoor Outfitter
- Gift Shop
- Coffee Shop
- Motel
- Marina
- Ranger Station (Grizzly Bear)

---

## Collectible Items

| Location | Item |
|----------|------|
| General Store | Trail Map |
| Outdoor Outfitter | Bear Spray |
| Gift Shop | Park Pass |
| Coffee Shop | Flashlight |
| Motel | First Aid Kit |
| Marina | Two-Way Radio |

---

## Win Condition

Collect all six required items before entering the Ranger Station.

---

## Loss Condition

Enter the Ranger Station before collecting all required items.

---

## Player Commands

The player can use the following commands during gameplay:

- go north
- go south
- go east
- go west
- get item

---

## Game Logic

The game follows these general steps:

1. Start the player in the Visitor Center.
2. Display the player's current location.
3. Display the player's inventory.
4. Accept a movement or item command from the player.
5. Move the player if the requested direction is valid.
6. Allow the player to collect an item if one is available.
7. Check whether the player has entered the Ranger Station.
8. If all required items have been collected, the player wins.
9. Otherwise, the grizzly bear ends the game.
10. Continue until the game ends.

---

## Project Files

- **design/design_document.docx** — Original project planning document for the assignment.
- **design/map.png** — Game map showing room connections.
- **design/pseudocode.txt** — Pseudocode for player movement, item collection, inventory management, and game logic.
- **src/text_adventure.py** — Python source code for the text adventure game.
- **README.md** — Repository overview and project information.
- **.gitignore** — Git configuration for ignoring unnecessary files.

---

## Current Status

- ✔ Game theme selected
- ✔ Rooms and items planned
- ✔ Win and loss conditions planned
- ✔ Pseudocode completed
- ✔ Repository created and documented
- ☐ Map completed
- ✓ Basic player movement implemented
- ☐ Inventory system
- ☐ Win and loss conditions implemented
- ☐ Final testing
- ☐ Testing and debugging
- ☐ Final project submission