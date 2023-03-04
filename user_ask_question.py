from __future__ import annotations

from typing import Callable


def user_ask_question(prompt: str,
					  transform_function: Callable[[str], str] = lambda s: s.upper(),
					  accept_values: tuple | list = ('Y', 'YES'),
					  reject_values: tuple | list = ('N', 'NO')) -> bool:
	"""
	This function returns `True` if the user answers in the affirmative to the prompt. Otherwise, it returns `False`.
	If the user enters an invalid answer, they are shown the acceptable answers and asked again until they respond satisfactorily.
	"""
	answer = transform_function(input(prompt))

	while True:
		if answer in accept_values or answer in reject_values:
			return answer in accept_values

		print(f"Invalid answer. Must be:")
		print(f"{' or '.join(accept_values)} to accept, or")
		print(f"{' or '.join(reject_values)} to reject.")
