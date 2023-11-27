# 8bit Cub

## Description
An 8-bit arcade style adventure game

## Installation
Create the virtual environment

    $ source venv/bin/activate
    $ pip install 
    $ python code/main.py
    

## Controls
 - __Arrow Keys__: Move character in respective directions (up, down, left, right).
 - __Spacebar__: Attack.
 - __ALT key__: Use special ability
 - __Q key__: Swap between weapons
 - __W key__: Swap between abilities
 - __P__: Pause the game.

## Abilities
 - __Health Regeneration__: Regenerates 20 health points and drains 20 energy points
 - __Flame Balls__: Deals 5 damage and costs 20 energy points.

## Weapons
**Note each weapon's cooldown time will be denoted by the ending parentheses*

 - __Sword__: Lightweight weapon that inflicts 15 damage (100ms)
 - __Lance__: Long, medium weight weapon that inflicts 30 damage (400ms)
 - __Axe__: Heavy weapon that inflicts 20 damage (300ms)
 - __Rapier__: Very lightweight weapon that inflicts 8 damage (50ms)
 - __Sai__: Another lightweight weapon that inflicts 10 damage (80ms)

## Monsters
 - Squid: A medium-sized monster with a large notice radius
 - Racoon: The largest monster but also the slowest. 
 - Spirit: A small but quick monster. It also has one of the largest notice radius
 - Bamboo: The weakest monster that is easy to sneak by


## Monster Stats
| Monster | Health Points (HP) | Attack Power | Speed | Medals Awarded | Resistance | Attack Type |
|---------|--------------------|--------------|-------|----------------|------------|-------------|
| Racoon  | 300                | 40           | 2     | 250            | 3          | Claw        |
| Spirit  | 100                | 8            | 4     | 110            | 3          | Thunder     |
| Bamboo  | 70                 | 6            | 3     | 70             | 3          | Leaf Attack |
| Squid   | 100                | 20           | 3     | 100            | 3          | Slash       |

## Notes:

- **Health Points (HP):** Represents the monster's overall health. When it reaches 0, the monster is defeated.
- **Attack Power:** Indicates the damage the monster inflicts with each attack.
- **Medals Awarded:** Indicates the medals you will be awarded with upon defeating the monster. These can be spent in the marketplace in the main menu (P key)

