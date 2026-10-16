import elements as fire_and_water
from alchemy import elements as earth_and_air


def healing_potion() -> str:

    return f"Healing potion brewed with '{earth_and_air.create_earth()}' " \
        f"and '{earth_and_air.create_air()}'"


def strength_potion() -> str:
    return f"Strength potion brewed with '{fire_and_water.create_fire()}' " \
        f"and '{fire_and_water.create_water()}'"
