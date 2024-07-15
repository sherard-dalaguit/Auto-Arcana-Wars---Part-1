from utils import Stats, BaseItem


class EnchantedSword(BaseItem):
	def name(self) -> str:
		return "Enchanted Sword"

	def passive_name(self) -> str:
		return f"{self.name}: Lucky Strike"

	def calculate_effective_stats(self, base_character_stats: Stats) -> Stats:
		new_stats = base_character_stats.add_stat_changes(self.base_item_stats)

		if self.is_passive_active:
			return new_stats._replace(special_trigger_chance=5 + 1.25 * new_stats.special_trigger_chance)

		return new_stats


class ShinyStaff(BaseItem):
	def name(self) -> str:
		return "Shiny Staff"

	def passive_name(self) -> str:
		return f"{self.name}: Blessings of Echo"

	def calculate_effective_stats(self, base_character_stats: Stats) -> Stats:
		new_stats = base_character_stats.add_stat_changes(self.base_item_stats)

		if self.is_passive_active:
			return new_stats._replace(magic_power=1 + 1.5 * new_stats.magic_power)

		return new_stats


class Pole(BaseItem):
	def name(self) -> str:
		return "Pole"

	def passive_name(self) -> str:
		return f"{self.name}: No passive abilities"

	def calculate_effective_stats(self, base_character_stats: Stats) -> Stats:
		new_stats = base_character_stats.add_stat_changes(self.base_item_stats)

		return new_stats


class MagicCauldron(BaseItem):
	def name(self) -> str:
		return "Magic Cauldron"

	def passive_name(self) -> str:
		return f"{self.name}: Potion of Life"

	def calculate_effective_stats(self, base_character_stats: Stats) -> Stats:
		new_stats = base_character_stats.add_stat_changes(self.base_item_stats)

		if self.is_passive_active:
			return new_stats._replace(current_hp=10 + 1.3 * base_character_stats.total_hp,
									  total_hp=10 + 1.3 * base_character_stats.total_hp)

		return new_stats


class SolidRock(BaseItem):
	def name(self) -> str:
		return "Solid Rock"

	def passive_name(self) -> str:
		return f"{self.name}: No passive abilities"

	def calculate_effective_stats(self, base_character_stats: Stats) -> Stats:
		new_stats = base_character_stats.add_stat_changes(self.base_item_stats)

		return new_stats
