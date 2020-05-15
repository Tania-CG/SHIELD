from django import template
from django.utils.safestring import mark_safe

register = template.Library()


def danger_level(level):
    if level < 30:
        color = "green"
        label = "Bajo"
    elif level < 65:
        color = "orange"
        label = "Medio"
    else:
        color = "red"
        label = "Alto"
    return mark_safe(f"<span style='color: {color};'>{label}</span>")

register.filter("danger_level", danger_level)

# usando un decorador sería así:
# from django import template
# register = template.Library()

# @register.filter
# def danger_level(level):
#     if level < 30:
#         return "Bajo"
#     elif level < 66:
#         return "Medio"
#     else:
#         return "Alto"
