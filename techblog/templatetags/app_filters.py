from django import template
register = template.Library()

POST_CHOICES = (
        ('DJBE', 'Django Backend'),
        ('DJFE', 'Django Frontend'),
        ('DJU', 'Django Utility'),
        ('T', 'Technology'),
        ('A', 'Algorithms'),
        ('MAKE', 'Arduino and Raspberry Pi'),
        ('CS', 'Computer Science Fundamentals'),
        ('PHYS', 'Physics'),
        ('MAT', 'Math')
    )

choices_map = {
    'DJBE': '',
    'DJFE': '',
    'DJU':  '',
    'T':    '',
    'A':    '',
    'MAKE': '',
    'CS':   '',
    'PHYS': '',
    'MAT':  '',
}


@register.filter()
def map_category_to_icon(category):
    # make a piece of html for each category

    print(f"\n The category at the filter is: {category}")

    if category == 'arg':
        print("filter accessed correctly")
        return f"<b>{category}</b>"
    else:
        return f"no match for category {category}"


@register.filter()
def map_category_to_color(category):

    print(f"\n The category at the filter is: {category}")