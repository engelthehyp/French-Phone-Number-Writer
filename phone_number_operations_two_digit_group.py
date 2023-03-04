def convert_string_by_char_to_dictionary_value(char_sequence: str, reference: dict, output_delimiter: str = ' ') -> str:
	"""
	This function, given a string, returns a new string made by joining, with `output_delimiter`, the value of each character in the `char_sequence`, defined by `reference`.

	A general use case: Given a string containing numbers, returns a string of French words - one for each single number.

	Example: "0653284" as `char_sequence`, the included French numbers dictionary as `reference`,
	and " " as `output_delimiter`, this function returns "zéro six cinq trois deux huit quatre".

	Functional purity: **Impure**. Can raise exceptions.

	:param char_sequence: Passed as a string, so we can index them. You have to play nice and make sure that every character is in `reference`.
	:param reference: A dictionary that should map every character you might pass in `char_sequence` on that function call.
	:param output_delimiter: The string placed between each computed value. Space by default because you would almost always want some form of separation.
	:return: A new string made by joining the value of each character in the `char_sequence`, defined by `reference`, with `output_delimiter`.

	:raises: `ValueError` if `char_sequence` contains characters that were not stored as keys in `reference`.
	"""
	fist_number = char_sequence[0]

	if len(char_sequence) == 1:
		return reference[fist_number]

	return reference[fist_number] + \
		output_delimiter + \
		convert_string_by_char_to_dictionary_value(char_sequence[1:], reference, output_delimiter)


def convert_number_group_to_word(number_group: str, reference: dict, output_delimiter: str = ' ') -> str:
	first_number = number_group[0]
	second_number = number_group[1]

	if first_number == '0':
		return reference[first_number] + output_delimiter + reference[second_number]

	return reference[number_group]