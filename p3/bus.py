from re import fullmatch
import json


def bus_info():
	validation = {
		'bus_id': {'type': int, 're_pattern': r"\d+"},
		'stop_id': {'type': int, 're_pattern': r"\d+"},
		'stop_name': {'type': str, 're_pattern': r"(?:[A-Z][A-Za-z]?[a-z]+ ?)+(Avenue|Street|Road|Boulevard)$"},
		'next_stop': {'type': int, 're_pattern': r"\d+"},
		'stop_type': {'type': str, 're_pattern': r"^(|[SOF])$"},
		'a_time': {'type': str, 're_pattern': r"^(?:[01][0-9]|2[0-3]):[0-5][0-9]$"}
	}

	err_lst = dict.fromkeys(validation, 0)
	roads = json.loads(input())

	bus_id = {}  # map bus id to # stops

	for route in roads:
		for key, val in route.items():
			if not isinstance(val, validation[key]['type']) \
					or fullmatch(validation[key]['re_pattern'], str(val)) is None:
				err_lst[key] += 1
			if isinstance(val, int) and key == 'bus_id':
				bus_id[val] = bus_id.get(val, 0) + 1

	# print(f"Format validation: {sum(err_lst.values())} errors")
	# for k, v in err_lst.items():
	# 	if k == 'stop_name' or k == 'stop_type' or k == 'a_time':
	# 		print(f"{k}: {v}")
	print("Line names and number of stops:")
	for bus in bus_id:
		print(f"bus_id: {bus}, stops: {bus_id[bus]}")


bus_info()
