from django import template
register = template.Library()

@register.
def get_icon(value):

    if value == 'arg':
        print("filter accessed correctly")
    return f"<b>{value}"