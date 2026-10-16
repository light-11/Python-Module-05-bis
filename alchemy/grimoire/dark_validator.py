from alchemy.grimoire.dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    dark_elements_list = dark_spell_allowed_ingredients()
    if any(
        element.upper() in ingredients.upper()
        for element in dark_elements_list
    ):
        return "VALID"
    else:
        return "INVALID"
