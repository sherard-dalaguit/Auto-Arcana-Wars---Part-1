from typing import NamedTuple

class Stats(NamedTuple):
	"""
	all values are floats with default 0.
	current_hp
	total_hp
	armo
	magic_resistance
	physical_power
	magic_power
	special_trigger_chance
	"""

	def add_stat_changes(self, changes: "Stats") -> "Stats":
