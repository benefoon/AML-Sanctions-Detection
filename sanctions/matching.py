from fuzzywuzzy import fuzz

def is_name_match(entity_name: str, sanction_list: list, threshold: int = 90) -> bool:
    return any(fuzz.token_sort_ratio(entity_name.lower(), sanctioned.lower()) > threshold for sanctioned in sanction_list)
