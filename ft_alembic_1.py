import alchemy


def ft_alembic_1() -> None:
    print("=== Alembic 1 ===")
    print("Accessing the alchemy module using 'import alchemy'")
    air = alchemy.create_air()
    print(f"Testing create_air: {air}")
    print("Now show that not all functions can be reached")
    print("This will raise an exception!")
    earth = alchemy.create_earth()
    print(f"Testing create_earth: {earth}")


ft_alembic_1()
