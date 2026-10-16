import alchemy.transmutation.recipes


def ft_transmutation_0() -> None:
    print("=== Transmutation 0 ===")
    print("Using file alchemy/transmutation/recipes.py directly")
    gold = alchemy.transmutation.recipes.lead_to_gold()
    print(f"Testing lead to gold: {gold}")


ft_transmutation_0()
