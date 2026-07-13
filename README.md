# IT-140 Text Adventure Game

This repository contains my text-based adventure game project for SNHU IT-140: Introduction to Scripting. The project is currently in the design stage, and the pseudocode for player movement, item collection, inventory, and the win and loss conditions has been completed.

## Game Theme

The game takes place in Glacier National Park. The player starts at the Visitor Center and must explore different locations throughout the park to collect six required items. The Ranger Station contains a grizzly bear, which acts as the villain. If the player enters the Ranger Station before collecting every item, the game ends. If all required items are collected first, the player wins.

## Locations

- Visitor Center
- General Store
- Outdoor Outfitter
- Gift Shop
- Coffee Shop
- Ranger Station
- Motel
- Marina

## Current Progress

- [x] Choose the game theme
- [x] Plan the rooms and villain
- [x] Create movement pseudocode
- [x] Create item collection pseudocode
- [ ] Complete the storyboard and map
- [ ] Build the room dictionary
- [ ] Add player movement
- [ ] Add the inventory system
- [ ] Add win and loss conditions
- [ ] Test and finish the game

## Repository Structure

```text
IT140_TEXT_ADVENTURE/
├── design/
│   ├── design_document.docx
│   ├── map.png
│   └── pseudocode.txt
├── src/
│   └── text_adventure.py
├── .gitignore
└── README.md

## Project Design

The design documents for this project are located in the `design` folder.

Contents include:
- `design_document.docx` — Original project planning document
- `map.png` — Map of the game world and room connections
- `pseudocode.txt` — Pseudocode for player movement, inventory management, and game logic