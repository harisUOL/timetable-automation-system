from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    """
    Safe dictionary access for nested template usage.
    Returns None safely if dictionary or key does not exist.
    """
    if not dictionary:
        return None

    if isinstance(dictionary, dict):
        return dictionary.get(key)

    return None
