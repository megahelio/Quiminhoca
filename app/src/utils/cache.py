def get_cache_key(formula: str, source: str) -> str:
    import hashlib
    hash_key = hashlib.sha256(f"{formula}_{source}".encode()).hexdigest()
    return f"chem_cache:{hash_key}"