from rapidfuzz import fuzz

def fuzzy_name_match(name: str, sanctions_list: list[str], threshold: int = 85) -> bool:
    """
    Returns True if name has high similarity to any entry in sanctions_list
    """
    name = name.lower().strip()
    return any(fuzz.partial_ratio(name, s.lower().strip()) >= threshold for s in sanctions_list)
