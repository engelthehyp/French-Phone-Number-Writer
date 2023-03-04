import csv


def prepare_csv_as_dict(path: str, skip_first_line: bool = False) -> dict:
	with open(path) as file:
		reader = csv.reader(file)

		if skip_first_line:
			next(reader)

		return dict(reader)
