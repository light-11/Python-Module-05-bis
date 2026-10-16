from alchemy.grimoire import light_spellbook


def ft_kaboom_0() -> None:
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    spell_name = "Fantasy"
    ingredients = "Earth, wind and fire"
    msg = light_spellbook.light_spell_record(spell_name, ingredients)
    print(f"Testing record light spell: {msg}")


ft_kaboom_0()
