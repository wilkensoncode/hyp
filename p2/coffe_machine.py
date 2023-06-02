class CoffeeMachine:
	# region Constants
	STATUS_STARTING = "starting"
	STATUS_GRINDING = "grinding"
	STATUS_BOILING = "boiling"
	STATUS_MIXING = "mixing"
	STATUS_POURING_WATER = "pouring_water"
	STATUS_POURING_MILK = "pouring_milk"
	STATUS_READY = "ready"

	ALL_STATUSES = [STATUS_STARTING, STATUS_GRINDING, STATUS_BOILING, STATUS_MIXING,
	                STATUS_POURING_WATER, STATUS_POURING_MILK, STATUS_READY]

	repr_status = {
		"starting": "Starting to make a coffee",
		"grinding": "Grinding coffee beans",
		"boiling": "Boiling water",
		"mixing": "Mixing boiled water with crushed coffee beans",
		"pouring_water": "Pouring coffee into the cup",
		"pouring_milk": "Pouring some milk into the cup",
		"ready": "Coffee is ready!"
	}

	# endregion

	def __init__(self):
		pass

	def show_statuses(self):
		for i in CoffeeMachine.ALL_STATUSES:
			print(CoffeeMachine.repr_status[i])


machine = CoffeeMachine()
machine.show_statuses()
