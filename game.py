import json
from pathlib import Path
from typing import List
from characters import BaseCharacter, Ninja, Mage, Warrior
from items import EnchantedSword, ShinyStaff, Pole, MagicCauldron, SolidRock
from utils import Stats


def read_data(team_assignment: Path) -> List[BaseCharacter]:
    print(team_assignment.resolve())

    with team_assignment.open() as open_file:
        file_data = json.load(open_file)

    character_list = []
    for character_data in file_data:
        stats_dict = character_data['character']['stats']
        stats_dict['current_hp'] = stats_dict['total_hp'] = float(stats_dict.pop('hp'))

        # Makes sure everything is a float, doesn't change its values though
        stats_dict = {character_attribute: float(value) for character_attribute, value in stats_dict.items()}

        base_stats = Stats(**stats_dict)
        if character_data['character']['name'] == 'ninja':
            character = Ninja(base_stats=base_stats)
        elif character_data['character']['name'] == 'mage':
            character = Mage(base_stats=base_stats)
        elif character_data['character']['name'] == 'warrior':
            character = Warrior(base_stats=base_stats)
        else:
            raise ValueError(f"Unknown character type: {character_data['name']}")

        if 'items' in character_data:
            for item_data in character_data['items']:
                item_stats_dict = item_data['stats']

                if item_data['name'] == 'magic_cauldron':
                    item_stats_dict['current_hp'] = item_stats_dict['total_hp'] = float(item_stats_dict.pop('hp', 0))

                # Makes sure everything is a float, doesn't change its values though
                item_stats_dict = {item_attribute: float(value) for item_attribute, value in item_stats_dict.items()}

                item_base_stats = Stats(**item_stats_dict)

                if item_data['name'] == 'enchanted_sword':
                    item = EnchantedSword(base_item_stats=item_base_stats)
                elif item_data['name'] == 'shiny_staff':
                    item = ShinyStaff(base_item_stats=item_base_stats)
                elif item_data['name'] == 'pole':
                    item = Pole(base_item_stats=item_base_stats)
                elif item_data['name'] == 'magic_cauldron':
                    item = MagicCauldron(base_item_stats=item_base_stats)
                elif item_data['name'] == 'solid_rock':
                    item = SolidRock(base_item_stats=item_base_stats)
                else:
                    raise ValueError(f"Unknown item type: {item_data['name']}")

                character.add_item(item)

        character_list.append(character)
    print_character_list(character_list)

    return character_list


def print_character_list(character_list):
    for character in character_list:
        print(f"Character Name: {character.name()}")
        print(f"Current HP: {character.effective_stats.current_hp}")
        print(f"Total HP: {character.effective_stats.total_hp}")
        print(f"Armor: {character.effective_stats.armor}")
        print(f"Magic Resistance: {character.effective_stats.magic_resistance}")
        print(f"Physical Power: {character.effective_stats.physical_power}")
        print(f"Magic Power: {character.effective_stats.magic_power}")
        print(f"Special Trigger Chance: {character.effective_stats.special_trigger_chance}")
        print("\n")


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument("--team_assignment",
                        type=str,
                        help="The location of the team assignment file to read",
                        default="./team_assignments/assignment_6.json",
                        required=False)
    args = parser.parse_args()
    team_assignment = Path(args.team_assignment)
    read_data(team_assignment=team_assignment)
