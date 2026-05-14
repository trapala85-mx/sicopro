# apps/core/utils/str_to_bool.py

def str_to_bool(value:str, default=False) -> bool:
    """
    Convierte un string a booleano.
    
    Args:
        value: String a convertir (ej: 'true', 'false', None)
        default: Valor por defecto si value es None o vacío
    
    Returns:
        bool
    """
    if value is None:
        return default
    
    return value.lower() == 'true'