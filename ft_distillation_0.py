from alchemy import potions


def ft_distillation_0() -> None:
    print("=== Distillation 0 ===")
    print("Direct access to alchemy/potions.py")
    strength_potion = potions.strength_potion()
    healing_potion = potions.healing_potion()
    print(f"Testing strength_potion: {strength_potion}")
    print(f"Testing healing_potion: {healing_potion}")


ft_distillation_0()
