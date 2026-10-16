from . import light_spellbook


def validate_ingredients(ingredients: str) -> str:
    light_elements_list = light_spellbook.light_spell_allowed_ingredients()
    if any(
        element.upper() in ingredients.upper()
        for element in light_elements_list
    ):
        return "VALID"
    else:
        return "INVALID"
