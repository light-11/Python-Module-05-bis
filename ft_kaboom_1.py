def ft_kaboom_1() -> None:
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
    spell_name = "Fantasy"
    ingredients = "Earth, wind and fire"
    from alchemy.grimoire import dark_spellbook
    msg = dark_spellbook.dark_spell_record(spell_name, ingredients)
    print(f"Testing record dark spell: {msg}")


ft_kaboom_1()
