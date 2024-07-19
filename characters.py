from utils import BaseCharacter


class Ninja(BaseCharacter):
	def name(self) -> str:
		"""Returns the name of the character."""
		return "Ninja"

	def special_attack_name(self) -> str:
		"""Returns the name of the character and its special attack."""
		return f"{self.name}: Blessings of Echo"


class Mage(BaseCharacter):
	pass


class Warrior(BaseCharacter):
	pass
