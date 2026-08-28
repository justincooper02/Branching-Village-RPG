# Branching Village RPG - INST326

A text-based, choose-your-own-adventure game built in Python for INST326. Players lead a medieval settlement through choices about raiding, negotiating, and survival, managing four core stats (manpower, food, power, reputation) that shape which of several endings they reach, including an achievement system tied to specific story choices.

My contributions:

- scenario_selection(game, scenario_branches, player) - drives the core game loop, presenting scenarios based on player choices and progressing the branching story (technique: conditional expressions)
- check_achievements(self) - tracks and displays unlocked/locked achievements based on the player's full decision history (technique: set operations)
- inst326_story.py - wrote the branching story content and scenario data (the settlement's raid/negotiate storyline, endings, and Ronald the cat's recurring cameo)

Team: Ryan Andreasen, Justin Cooper, John Wang, Keenan Williamson

Full attribution:

| Function | Author | Technique |
|----------|--------|-----------|
| check_status(game) | Keenan | Key function |
| random_event(game) | Keenan | f-strings with expressions |
| scenario_selection(...) | Justin | Conditional expressions |
| check_achievements(self) | Justin | Set operations |
| main() | Ryan | Regular expressions |
| __str__(self) | Ryan | Magic methods |
| assign_class | John | Optional parameters |
| assign_skills | John | Comprehensions/generator expressions |

How to run: python3 inst326_game.py - no command-line arguments needed.

Files in this repo:

- inst326_game.py - game engine, Game/Player classes, core loop
- inst326_story.py - branching story content and scenario data
- story_events.py - random event definitions
