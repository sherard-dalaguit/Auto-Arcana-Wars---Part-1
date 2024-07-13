from typing import NamedTuple


class Stats(NamedTuple):
	"""all values are floats with default 0."""
	current_hp: float = 0.0
	total_hp: float = 0.0
	armor: float = 0.0
	magic_resistance: float = 0.0
	physical_power: float = 0.0
	magic_power: float = 0.0
	special_trigger_chance: float = 0.0

	def add_stat_changes(self, changes: "Stats") -> "Stats":
		"""
		Updates the stats based on the provided changes while ensuring
		that the values remain within their appropriate ranges.

		Args:
			changes (Stats): The stat changes to be applied.

		Returns:
			Stats: The updated stats after the changes have been applied.

		Note:
			The current HP cannot exceed total HP and is ensured to be at least 0.
			The special trigger chance is capped at 100.
		"""

		updated_current_hp = min(self.current_hp + changes.current_hp, self.total_hp + changes.total_hp)
		updated_total_hp = self.total_hp + changes.total_hp
		updated_armor = self.armor + changes.armor
		updated_magic_resistance = self.magic_resistance + changes.magic_resistance
		updated_physical_power = self.physical_power + changes.physical_power
		updated_magic_power = self.magic_power + changes.magic_power
		updated_special_trigger_chance = min(self.special_trigger_chance + changes.special_trigger_chance, 100)

		return Stats(
			current_hp=max(updated_current_hp, 0),  # max() is used to ensure current_hp can't go below 0
			total_hp=updated_total_hp,
			armor=updated_armor,
			magic_resistance=updated_magic_resistance,
			physical_power=updated_physical_power,
			magic_power=updated_magic_power,
			special_trigger_chance=updated_special_trigger_chance
		)

	def __str__(self) -> str:
		"""
		Returns a formatted string providing detailed information about the object's attributes.
		"""
		return f"""current_hp = {self.current_hp},
		total_hp = {self.total_hp},
		armor = {self.armor},
		magic_resistance = {self.magic_resistance},
		physical_power = {self.physical_power},
		magic_power = {self.magic_power},
		special_trigger_chance = {self.special_trigger_chance}
		"""
