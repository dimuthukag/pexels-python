import re

def validate_page(page:int)->bool:
    """
        Validate the given page value
    """
    if type(page)==int:
        if page >=1:
            return True
        raise Exception(f"ValueError: Unsupported value for page:{type(page)}. Expected 'page' value is >= 1.")
    raise Exception(f"TypeError: Unsupported type for page:{type(page)}. Expected 'page' type is 'int'.")

def validate_per_page(per_page:int)->bool:
    """
        Validate the given per page value
    """
    MAX_PER_PAGE = 80
    if type(per_page)==int:
        if per_page <= MAX_PER_PAGE:
            return True
        raise Exception(f"ValueError: Unsupported value for per_page:{type(per_page)}. Expected 'per_page' value is <= {MAX_PER_PAGE}.")
    raise Exception(f"TypeError: Unsupported type for per_page:{type(per_page)}. Expected 'per_page' type is 'int'.")

def validate_query(query:str)->bool:
    """
        Validate the given query value
    """
    if type(query)==str:
        return True
    raise Exception(f"TypeError: Unsupported type for query:{type(query)}. Expected 'query' type is 'str'.")

def validate_orientation(orientation:str)->bool:
    """
        Validate the given orientation value
    """
    supported_orientations = ['landscape', 'portrait', 'square']
    if type(orientation)==str:
        if orientation.strip().lower() in supported_orientations:
            return True
        raise Exception(f"ValueError: Unsupported value for orientation:{type(orientation)}. Expected 'orientation' value is one out of {supported_orientations.__str__()}.")
    raise Exception(f"TypeError: Unsupported type for orientation:{type(orientation)}. Expected 'orientation' type is 'str'.")

def validate_photo_size(photo_size:str)->bool:
    """
        Validate the given photo size value
    """
    supported_photo_sizes = ['large','medium','small']
    if type(photo_size)==str:
        if photo_size.strip().lower() in supported_photo_sizes:
            return True
        raise Exception(f"ValueError: Unsupported value for photo_size:{type(photo_size)}. Expected 'photo_size' value is one out of {supported_photo_sizes.__str__()}.")
    raise Exception(f"TypeError: Unsupported type for photo_size:{type(photo_size)}. Expected 'photo_size' type is 'str'.")

def validate_locale(locale:str)->bool:
    """
        Validate the given locale value
    """
    supported_locales = ['en-US','pt-BR','es-ES','ca-ES','de-DE','it-IT','fr-FR','sv-SE','id-ID','pl-PL','ja-JP','zh-TW','zh-CN','ko-KR','th-TH','nl-NL','hu-HU','vi-VN','cs-CZ','da-DK','fi-FI','uk-UA','el-GR','ro-RO','nb-NO','sk-SK','tr-TR','ru-RU']
    if type(locale)==str:
        if locale.strip() in supported_locales:
            return True
        raise Exception(f"ValueError: Unsupported value for locale:{type(locale)}. Expected 'locale' value is one out of {supported_locales.__str__()}.")
    raise Exception(f"TypeError: Unsupported type for locale:{type(locale)}. Expected 'locale' type is 'str'.")

def validate_color(color:str)->bool:
    """
        Validate the given color value
    """
    if type(color)==str:
        if re.findall(r'^#[0-9a-fA-F]{6}$',color):
            return True
        raise Exception(f"ValueError: Unsupported value for color:{type(color)}. Expected 'color' value is hex color code (#000000 to #FFFFFF).")
    raise Exception(f"TypeError: Unsupported type for color :{type(color)}. Expected 'color' type is 'str'.")