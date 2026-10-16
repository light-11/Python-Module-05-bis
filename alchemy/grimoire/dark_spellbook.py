from alchemy.grimoire.dark_validator import validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    dark_elements = ["bats", "frogs", "arsenic", "eyeball"]
    return dark_elements


def dark_spell_record(
        spell_name: str,
        ingredients: str
        ) -> str:
    validate = validate_ingredients(ingredients)
    if validate == "VALID":
        return f"Spell recorded: {spell_name} ({ingredients} - VALID)"
    else:
        return f"Spell rejected: {spell_name} ({ingredients} - INVALID)"
