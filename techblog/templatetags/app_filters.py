from django import template
register = template.Library()

@register.filter()
def map_category_to_icon(category):
    # make a piece of html for each category

    print(f"\n The category at the filter is: {category}")

    if category == 'arg':
        print("filter accessed correctly")
        return f"<b>{category}</b>"

