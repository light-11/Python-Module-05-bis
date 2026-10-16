def light_spell_allowed_ingredients() -> list[str]:
    light_elements = ["earth", "air", "fire", "water"]
    return light_elements


def light_spell_record(
        spell_name: str,
        ingredients: str
        ) -> str:
    from . import light_validator
    validate = light_validator.validate_ingredients(ingredients)
    if validate == "VALID":
        return f"Spell recorded: {spell_name} ({ingredients} - VALID)"
    else:
        return f"Spell rejected: {spell_name} ({ingredients} - INVALID)"
