import json
from pathlib import Path
from typing import List
from characters import BaseCharacter, Ninja, Mage, Warrior
from items import EnchantedSword, ShinyStaff, Pole, MagicCauldron, SolidRock


def read_data(team_assignment: Path) -> List[BaseCharacter]:
    print(team_assignment.resolve())

    with team_assignment.open() as open_file:
        file_data = json.load(open_file)

    character_list = []
    for entry in file_data:
        character_data = entry['character']
        item_data_list = entry.get('items', [])

        if character_data['name'] == 'mage':
            character = Mage(base_stats=character_data['stats'])
        elif character_data['name'] == 'warrior':
            character = Warrior(base_stats=character_data['stats'])
        elif character_data['name'] == 'ninja':
            character = Ninja(base_stats=character_data['stats'])
        else:
            raise ValueError(f"Unknown character type: {character_data['name']}")

        for item_data in item_data_list:
            if item_data['name'] == 'enchanted_sword':
                item = EnchantedSword(base_item_stats=item_data['stats'])
            elif item_data['name'] == 'shiny_staff':
                item = ShinyStaff(base_item_stats=item_data['stats'])
            elif item_data['name'] == 'pole':
                item = Pole(base_item_stats=item_data['stats'])
            elif item_data['name'] == 'magic_cauldron':
                item = MagicCauldron(base_item_stats=item_data['stats'])
            elif item_data['name'] == 'solid_rock':
                item = SolidRock(base_item_stats=item_data['stats'])
            else:
                raise ValueError(f"Unknown item type: {item_data['name']}")

            character.add_item(item)

        character_list.append(character)

    return character_list


if __name__ == "__main__":
    from argparse import ArgumentParser
    
    parser = ArgumentParser()
    parser.add_argument("--team_assignment", 
                        type=str, 
                        help="The location of the team assignment file to read",
                        default="./team_assignments/assignment_1.json",
                        required=False)
    args = parser.parse_args()
    team_assignment = Path(args.team_assignment)
    read_data(team_assignment=team_assignment)
