from typing import NamedTuple, Any
import abc


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
		updated_armor = max((self.armor + changes.armor),0)
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


class BaseItem(abc.ABC):
	"""
	BaseItem is an abstract base class the represents a generic
	item in a game. Specific items should inherit from this class
	and customize the 'name', 'passive_name', and 'calculate_effective_stats'
	methods to match their individual behaviors.

	The class serves as a contract for what each item should include
	"""

	def __init__(self, base_item_stats: Stats, is_passive_active: bool) -> None:
		"""
		Initialize an instance of the BaseItem class

		Args:
			base_item_stats (Stats): The base statistics associated with the item.
			is_passive_active (bool): The state indicating if the passive is active.
		"""
		self.base_item_stats = base_item_stats
		self.is_passive_active = is_passive_active

	@property
	@abc.abstractmethod
	def name(self) -> str:
		"""
		Abstract method representing a 'name' property.

		This method is intended to be overridden in subclasses to
		return the name of the item as a string.

		Returns:
			str: The name of the item
		"""
		pass

	@property
	@abc.abstractmethod
	def passive_name(self) -> str:
		"""
		Abstract method representing a 'passive_name' property

		This property is intended to be overridden in subclasses to
		return the passive name of the item as a string.

		Returns:
			str: The name and passive effect of the item.
		"""
		pass

	@abc.abstractmethod
	def calculate_effective_stats(self, base_character_stats: Stats) -> Stats:
		"""
		Abstract method to calculate effective statistics.

		This method should be overridden by subclasses to provide
		functionality that takes base character stats
		and calculates some effective stats.

		Args:
			base_character_stats (Stats): The original statistics of a
			character before applying the item effect.

		Returns:
			Stats: The calculated statistics after applying the item effect.
		"""
		pass

	def __eq__(self, other: Any) -> bool:
		"""
		Overrides the default implementation of the equality operator.
		Two objects of class BaseItem are considered equal if the 'name'
		properties are the same.

		Args:
			other (Any): The other object that this BaseItem will be compared to.

		Returns:
			bool: True if the other object is an instance of BaseItem and its
			name property is the same as this BaseItem's. False otherwise
		"""

		if isinstance(other, BaseItem):
			return self.name == other.name
		return False
