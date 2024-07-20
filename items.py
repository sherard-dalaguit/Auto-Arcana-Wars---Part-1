from utils import Stats, BaseItem


class EnchantedSword(BaseItem):
	def name(self) -> str:
		"""Returns the name of the item."""
		return "Enchanted Sword"

	def passive_name(self) -> str:
		"""Returns the name of the item and its special ability."""
		return f"{self.name}: Lucky Strike"

	def is_unique_passive(self) -> bool:
		"""Returns whether an item has a unique passive effect."""
		return True

	def calculate_effective_stats(self, base_character_stats: Stats) -> Stats:
		"""
		Calculates the effective stats after equipping the item.

		The new stats will be based on the base character stats and
		the passive ability effects if the passive is active.

		Args:
			base_character_stats (Stats): The basic character stats before equipping the item

		Returns:
			Stats: The new character stats after equipping the item.
		"""

		if self.is_passive_active:
			return self.base_item_stats._replace(special_trigger_chance=5 + 0.25 * base_character_stats.special_trigger_chance)
		return self.base_item_stats


class ShinyStaff(BaseItem):
	def name(self) -> str:
		"""Returns the name of the item."""
		return "Shiny Staff"

	def passive_name(self) -> str:
		"""Returns the name of the item and its special ability."""
		return f"{self.name}: Blessings of Echo"

	def is_unique_passive(self) -> bool:
		"""Returns whether an item has a unique passive effect."""
		return False

	def calculate_effective_stats(self, base_character_stats: Stats) -> Stats:
		"""
		Calculates the effective stats after equipping the item.

		The new stats will be based on the base character stats and
		the passive ability effects if the passive is active.

		Args:
			base_character_stats (Stats): The basic character stats before equipping the item

		Returns:
			Stats: The new character stats after equipping the item.
		"""

		effective_stats = self.base_item_stats

		if self.is_passive_active:
			added_effect = Stats(magic_power=1 + 0.5 * base_character_stats.magic_power)
			effective_stats = effective_stats.add_stat_changes(added_effect)

		return effective_stats


class Pole(BaseItem):
	def name(self) -> str:
		"""Returns the name of the item."""
		return "Pole"

	def passive_name(self) -> str:
		"""Returns the name of the item and its special ability."""
		return f"{self.name}: No passive abilities"

	def is_unique_passive(self) -> bool:
		"""Returns whether an item has a unique passive effect."""
		return False

	def calculate_effective_stats(self, base_character_stats: Stats) -> Stats:
		"""
		Calculates the effective stats after equipping the item.

		The new stats will be based on the base character stats and
		the passive ability effects if the passive is active.

		Args:
			base_character_stats (Stats): The basic character stats before equipping the item

		Returns:
			Stats: The new character stats after equipping the item.
		"""

		return self.base_item_stats


class MagicCauldron(BaseItem):
	def name(self) -> str:
		"""Returns the name of the item."""
		return "Magic Cauldron"

	def passive_name(self) -> str:
		"""Returns the name of the item and its special ability."""
		return f"{self.name}: Potion of Life"

	def is_unique_passive(self) -> bool:
		"""Returns whether an item has a unique passive effect."""
		return True

	def calculate_effective_stats(self, base_character_stats: Stats) -> Stats:
		"""
		Calculates the effective stats after equipping the item.

		The new stats will be based on the base character stats and
		the passive ability effects if the passive is active.

		Args:
			base_character_stats (Stats): The basic character stats before equipping the item

		Returns:
			Stats: The new character stats after equipping the item.
		"""

		effective_stats = self.base_item_stats

		if self.is_passive_active:
			added_effect = Stats(current_hp=10 + 0.3 * base_character_stats.total_hp,
								 total_hp=10 + 0.3 * base_character_stats.total_hp)
			effective_stats = effective_stats.add_stat_changes(added_effect)

		return effective_stats


class SolidRock(BaseItem):
	def name(self) -> str:
		"""Returns the name of the item."""
		return "Solid Rock"

	def passive_name(self) -> str:
		"""Returns the name of the item and its special ability."""
		return f"{self.name}: No passive abilities"

	def is_unique_passive(self) -> bool:
		"""Returns whether an item has a unique passive effect."""
		return False

	def calculate_effective_stats(self, base_character_stats: Stats) -> Stats:
		"""
		Calculates the effective stats after equipping the item.

		The new stats will be based on the base character stats and
		the passive ability effects if the passive is active.

		Args:
			base_character_stats (Stats): The basic character stats before equipping the item

		Returns:
			Stats: The new character stats after equipping the item.
		"""
		return self.base_item_stats
