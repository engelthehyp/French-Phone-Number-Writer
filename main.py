from csv_utilities import *
from phone_number_format_config import *
from phone_number_operations_two_digit_group import convert_number_group_to_word
from user_ask_question import *


numbers_to_words: dict = prepare_csv_as_dict('numbers-to-words-0-to-100.csv', skip_first_line=True)
def main() -> None:
	# region Initialization - Runs only once
	standard_phone_number_config = PhoneNumberFormatConfig(delimiter='.')
	# endregion

	while True:
		config = standard_phone_number_config
		user_phone_number = config.get_user_input_phone_number()
		number_groups = user_phone_number.split(config.delimiter)

		number_as_words = ', '.join(
			[convert_number_group_to_word(group, numbers_to_words)
			 for group in number_groups])

		print(number_as_words)

		if user_ask_question("Convert another number? (Y/N): "):
			continue

		break  # If we get here, the user chose not to continue.


if __name__ == '__main__':
	main()
