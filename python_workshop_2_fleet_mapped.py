# Python for Work 2 - Practical Intermediate Python
# Story: Fleet maintenance system
# This script maps to the PowerPoint slides and the Jupyter Notebook.

from pathlib import Path
import sys


def section(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


# ---------------------------------------------------------------------
# Slide 1-3: Big picture and roadmap
# ---------------------------------------------------------------------
section("Slides 1-3: Workshop story and roadmap")
print("Goal: move from simple examples to organised, reusable Python programs.")
print("Story: build a small fleet maintenance system.")
print("Topics: try/except, modules, classes, methods, inheritance, project.")


# ---------------------------------------------------------------------
# Slide 4: One consistent story
# ---------------------------------------------------------------------
section("Slide 4: One consistent story - fleet variables")
vehicle_id = "VAN-204"
vehicle_type = "Delivery van"
tyres = 4
fuel_level = 72
current_km = 18600
service_due_km = 20000
route = ["Depot", "Library", "Lab"]

print(vehicle_id, vehicle_type)
print("Tyres:", tyres)
print("Fuel level:", fuel_level)
print("Current km:", current_km)
print("Service due at:", service_due_km)
print("Route:", route)


# ---------------------------------------------------------------------
# Slide 5: Errors and try/except
# ---------------------------------------------------------------------
section("Slide 5: Errors and try/except")
raw_km = "eighteen"

try:
    trip_km = float(raw_km)
    print("Trip distance:", trip_km)
except ValueError:
    print("Please enter a number, e.g. 18")

raw_km = "18"
try:
    trip_km = float(raw_km)
    print("Trip distance:", trip_km)
except ValueError:
    print("Please enter a number, e.g. 18")


# ---------------------------------------------------------------------
# Slide 6: Reusable validation pattern
# ---------------------------------------------------------------------
section("Slide 6: Reusable validation function")

def get_positive_number(value, field_name):
    try:
        number = float(value)
        if number <= 0:
            raise ValueError
        return number
    except ValueError:
        print(f"Invalid {field_name}")
        return 0

trip_km = get_positive_number("18", "trip km")
tyres = get_positive_number("4", "tyres")
bad_fuel = get_positive_number("abc", "fuel level")

print("Validated trip km:", trip_km)
print("Validated tyres:", tyres)
print("Validated bad fuel:", bad_fuel)


# ---------------------------------------------------------------------
# Slide 7: Modules, packages and pip
# ---------------------------------------------------------------------
section("Slide 7: Modules, packages and pip")
from datetime import date
import math

print("Today:", date.today())
print("18.2 rounded up:", math.ceil(18.2))

# Create a tiny custom module for the demo.
# In a real project, this would be a separate file you write yourself.
module_code = """def calculate_service_gap(current_km, service_due_km):
    return service_due_km - current_km
"""
module_path = Path(__file__).with_name("fleet_tools.py")
module_path.write_text(module_code)
if str(module_path.parent) not in sys.path:
    sys.path.insert(0, str(module_path.parent))

from fleet_tools import calculate_service_gap

service_gap = calculate_service_gap(current_km, service_due_km)
print("Km until service:", service_gap)
print("Install packages with: py -m pip install pandas matplotlib")


# ---------------------------------------------------------------------
# Slide 8: Classes and objects
# ---------------------------------------------------------------------
section("Slide 8: Classes and objects")
class Vehicle:
    pass

van = Vehicle()
truck = Vehicle()

print("van type:", type(van))
print("truck type:", type(truck))


# ---------------------------------------------------------------------
# Slide 9: Attributes and __init__
# ---------------------------------------------------------------------
section("Slide 9: Attributes and __init__")
class VehicleWithAttributes:
    def __init__(self, vehicle_id, tyres, fuel_level):
        self.vehicle_id = vehicle_id
        self.tyres = tyres
        self.fuel_level = fuel_level

van = VehicleWithAttributes("VAN-204", 4, 72)
truck = VehicleWithAttributes("TRK-091", 6, 55)

print(van.vehicle_id, van.tyres, van.fuel_level)
print(truck.vehicle_id, truck.tyres, truck.fuel_level)


# ---------------------------------------------------------------------
# Slide 10: Variable scope
# ---------------------------------------------------------------------
section("Slide 10: Variable scope debug with print")
DEPOT_NAME = "CDU Casuarina Depot"  # global variable
print("GLOBAL:", DEPOT_NAME)

class ScopeVehicle:
    fleet_type = "training fleet"  # class variable

    def __init__(self, vehicle_id):
        self.vehicle_id = vehicle_id  # instance attribute
        print("INIT object:", self.vehicle_id)

    def label(self):
        status = "ready"  # local variable inside method
        print("METHOD local:", status)
        print("METHOD global:", DEPOT_NAME)
        print("METHOD class:", ScopeVehicle.fleet_type)
        print("METHOD instance:", self.vehicle_id)
        return f"{self.vehicle_id} is {status}"

def demo_scope():
    local_note = "inside function only"
    print("FUNCTION local:", local_note)

van = ScopeVehicle("VAN-204")
demo_scope()
print(van.label())


# ---------------------------------------------------------------------
# Slide 11: Methods
# ---------------------------------------------------------------------
section("Slide 11: Methods - functions inside objects")
class VehicleWithMethods:
    def __init__(self, vehicle_id, fuel_level):
        self.vehicle_id = vehicle_id
        self.fuel_level = fuel_level
        self.engine_on = False

    def start_engine(self):
        self.engine_on = True
        print(self.vehicle_id, "engine started")

    def drive(self, km):
        if not self.engine_on:
            return "Start the engine first"
        self.fuel_level -= km * 0.08
        return f"{self.vehicle_id} drove {km} km. Fuel: {self.fuel_level:.1f}"

van = VehicleWithMethods("VAN-204", 72)
van.start_engine()
print(van.drive(18))


# ---------------------------------------------------------------------
# Slide 12: Single inheritance
# ---------------------------------------------------------------------
section("Slide 12: Single inheritance")
class BaseVehicle:
    def __init__(self, vehicle_id, tyres):
        self.vehicle_id = vehicle_id
        self.tyres = tyres

    def basic_status(self):
        return f"{self.vehicle_id}: {self.tyres} tyres"

class DeliveryVan(BaseVehicle):
    def __init__(self, vehicle_id, tyres, cargo_capacity):
        super().__init__(vehicle_id, tyres)
        self.cargo_capacity = cargo_capacity

    def load_cargo(self, kg):
        return kg <= self.cargo_capacity

van = DeliveryVan("VAN-204", 4, 900)
print(van.basic_status())
print("Can load 750kg?", van.load_cargo(750))
print("Can load 1200kg?", van.load_cargo(1200))


# ---------------------------------------------------------------------
# Slide 13: *args and **kwargs
# ---------------------------------------------------------------------
section("Slide 13: *args and **kwargs")
def add_trip_stops(*stops):
    for stop in stops:
        print("Stop:", stop)

add_trip_stops("Depot", "Library", "Lab")

def show_vehicle_details(**details):
    for key, value in details.items():
        print(key, "=", value)

show_vehicle_details(driver="Mia", route="North", shift="Morning")


# ---------------------------------------------------------------------
# Slide 14: Multiple inheritance
# ---------------------------------------------------------------------
section("Slide 14: Multiple inheritance")
class ActiveVehicle:
    def basic_status(self):
        print("Vehicle is active")

class ServiceToolMixin:
    def inspect_tyres(self):
        print("Checking tyre pressure")

class ServiceVan(ActiveVehicle, ServiceToolMixin):
    pass

service_van = ServiceVan()
service_van.basic_status()
service_van.inspect_tyres()


# ---------------------------------------------------------------------
# Slide 15: Practical project - fleet readiness report
# ---------------------------------------------------------------------
section("Slide 15: Practical project - fleet readiness report")
class FleetVehicle:
    def __init__(self, vehicle_id, tyres, fuel_level, current_km, service_due_km, *route_stops, **details):
        self.vehicle_id = vehicle_id
        self.tyres = get_positive_number(tyres, "tyres")
        self.fuel_level = get_positive_number(fuel_level, "fuel level")
        self.current_km = get_positive_number(current_km, "current km")
        self.service_due_km = get_positive_number(service_due_km, "service due km")
        self.route_stops = list(route_stops)
        self.details = details
        self.engine_on = False

    def start_engine(self):
        self.engine_on = True

    def drive(self, km):
        km = get_positive_number(km, "trip km")
        self.current_km += km
        self.fuel_level -= km * 0.08

    def needs_service(self):
        return self.current_km >= self.service_due_km or self.fuel_level < 15

    def status(self):
        service_text = "SERVICE REQUIRED" if self.needs_service() else "Ready"
        return f"{self.vehicle_id}: {service_text} | km={self.current_km:.0f} | fuel={self.fuel_level:.1f}"

class ProjectDeliveryVan(FleetVehicle):
    def __init__(self, vehicle_id, tyres, fuel_level, current_km, service_due_km, cargo_capacity, *route_stops, **details):
        super().__init__(vehicle_id, tyres, fuel_level, current_km, service_due_km, *route_stops, **details)
        self.cargo_capacity = cargo_capacity

    def load_cargo(self, kg):
        return kg <= self.cargo_capacity

class ProjectServiceTruck(FleetVehicle):
    def __init__(self, vehicle_id, tyres, fuel_level, current_km, service_due_km, tools_count, *route_stops, **details):
        super().__init__(vehicle_id, tyres, fuel_level, current_km, service_due_km, *route_stops, **details)
        self.tools_count = tools_count

    def has_tools(self):
        return self.tools_count > 0

project_van = ProjectDeliveryVan(
    "VAN-204", 4, 72, 18600, 20000, 900,
    "Depot", "Library", "Lab",
    driver="Mia", shift="Morning"
)

project_truck = ProjectServiceTruck(
    "TRK-091", 6, 20, 24100, 24000, 12,
    "Depot", "Workshop",
    driver="Noah", shift="Afternoon"
)

project_van.start_engine()
project_truck.start_engine()
project_van.drive(18)
project_truck.drive(12)

vehicles = [project_van, project_truck]
total_km = 0

for vehicle in vehicles:
    print(vehicle.status())
    print("Route:", " -> ".join(vehicle.route_stops))
    print("Details:", vehicle.details)
    total_km += vehicle.current_km
    if vehicle.needs_service():
        print("Service required:", vehicle.vehicle_id)
    print("---")

print("Fleet mileage:", total_km)


# ---------------------------------------------------------------------
# Slide 16-17: File map and recap
# ---------------------------------------------------------------------
section("Slides 16-17: File map and recap")
print("PowerPoint: concept and mental model")
print("Notebook: guided practice")
print("Python script: runnable program")
print("You practised try/except, modules, classes, methods, inheritance, *args, **kwargs and multiple inheritance.")
