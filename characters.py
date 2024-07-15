from utils import Stats, BaseItem
import abc


class BaseCharacter(abc.ABC):
	"""
    BaseCharacter is an abstract base class for a character entity. It lays the
    foundation for how a character should be structured in the context of this application
    with methods for managing items, accessing character's name and their special attack.

    Attributes:
        base_stats (Stats): initial stats of the character;
        added_item_stats (Stats): stats gained from items;
        effective_stats (Stats): current stats after applying items;
        items (list[BaseItem]): items held by the character
    """

	def __init__(self, base_stats: Stats, added_item_stats: Stats, effective_stats: Stats, items: list[BaseItem]):
		"""
		Initialize BaseCharacter with base stats, added stats, effective stats and items.

		Args:
			base_stats (Stats): initial stats of the character;
			added_item_stats (Stats): stats gained from items;
			effective_stats (Stats): current stats after applying items;
			items (list[BaseItem]): items held by the character
		"""

		self.base_stats = base_stats
		self.added_item_stats = added_item_stats
		self.effective_stats = effective_stats
		self.items = items

	@property
	@abc.abstractmethod
	def name(self) -> str:
		"""
        Abstract property for the character's name.
        """
		pass

	@property
	@abc.abstractmethod
	def special_attack_name(self) -> str:
		"""
		Abstract property for the character's special attack name.
		"""
		pass

	def add_item(self, item: BaseItem) -> None:
		"""
		Adds an item to the character's inventory, updates the effective stats
        with the added item stats. If the character already has 3 items, raises
		an exception.

        Args:
            item (BaseItem): Item to be added.

		Raises:
	        ValueError: If character has already 3 items.
        """

		if len(self.items) > 3:
			raise ValueError('Too many items')
		else:
			self.items.append(item)

		self.effective_stats = self.base_stats  # Reset effective stats to base stats

		# Calculate effective stats for each item
		for item in self.items:
			self.effective_stats = item.calculate_effective_stats(self.base_stats)

	def __str__(self) -> str:
		"""
		Returns a string representation of the character, including, its name,
		base stats, effective stats and items.

		Returns:
			str: String representation of the character.
		"""

		items = ', '.join(item.name for item in self.items)

		return (f"Character: {self.name}, "
				f"Base Stats: {self.base_stats}, "
				f"Effective Stats: {self.effective_stats}, "
				f"Items: {items}")
