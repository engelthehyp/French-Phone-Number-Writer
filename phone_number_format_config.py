from dataclasses import dataclass


@dataclass
class PhoneNumberFormatConfig:
	delimiter: str
	digit_group_length: int = 2

	def get_user_input_phone_number(self) -> str:
		return input(f"Enter a French style phone number, with " +
					 f"groups of {self.digit_group_length}, " +
					 f"delimited by '{self.delimiter}'. ")

	def __str__(self):
		return f"Phone Number Configuration - groups of {self.digit_group_length}, delimited by {self.delimiter}."
