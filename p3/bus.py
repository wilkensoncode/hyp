import json


def bus_info():
	data = json.loads(input())

	entries_by_bus = {}
	for d in data:
		entries_by_bus.setdefault(d["bus_id"], [])
		entries_by_bus[d["bus_id"]].append(d)

	for bus, entries in entries_by_bus.items():
		start_stops, end_stops = 0, 0
		for e in entries:
			if e["stop_type"] == "S":
				start_stops += 1
			elif e["stop_type"] == "F":
				end_stops += 1
		if start_stops != 1 or end_stops != 1:
			return print(f"There is no start or end stop for the line: {bus}.")

	all_stops, start_stops, transfer_stops, finish_stops = [], [], [], []
	for d in data:
		all_stops.append(d["stop_name"])
		if d["stop_type"] == "S":
			start_stops.append(d["stop_name"])
		elif d["stop_type"] == "F":
			finish_stops.append(d["stop_name"])

	for name in set(all_stops):
		if all_stops.count(name) > 1:
			transfer_stops.append(name)

	transfer_stops.sort()
	arrive_time(entries_by_bus, transfer_stops, start_stops, finish_stops)


def arrive_time(entries_by_bus, transfer_stops, start_stops, finish_stops):
	print("Arrival time test:")
	incorrect_arrivals = []
	for bus, entries in entries_by_bus.items():
		prev_time = None
		for i in range(len(entries)):
			curr_time = entries[i]["a_time"]
			if prev_time and curr_time <= prev_time:
				incorrect_arrivals.append(f"bus_id line {bus}: wrong time on station {entries[i]['stop_name']}")
				break
			prev_time = curr_time

	if len(incorrect_arrivals) == 0:
		print("OK")
	else:
		for arrival in incorrect_arrivals:
			print(arrival)


bus_info()
