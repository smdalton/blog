from django import template
# this is the dict that maps categories choices names and icons together,
# centralized in the management section
from techblog.management.commands.structures import choices_map
"""
needed for pretty markdown rendering courtesy of
https://www.ignoredbydinosaurs.com/posts/275-easy-markdown-and-syntax-highlighting-django
v v v v v v v v
"""
import mistune
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter


register = template.Library()

# choices map is a tuple of an icon, and it's specified color, the color is appended to text in template


class HighlightRenderer(mistune.Renderer):
    def block_code(self, code, lang):
        if not lang:
            return '\n<pre><code>%s</code></pre>\n' % mistune.escape(code)
        lexer = get_lexer_by_name(lang, stripall=True)
        formatter = HtmlFormatter()
        return highlight(code, lexer, formatter)


@register.filter()
def markdown(value):
    markdown = mistune.Markdown()
    return markdown(value)

@register.filter()
def map_category_to_icon(category):

    """
    :param category: A valid category as defined in techblog.models in Post.CATEGORIES
    :return: a snippet of html that is correctly encoded to display
    both relevant colors, and font-awesome icons for the category
    """
    # get the specific dict we need to the rest of the icon operations
    category = choices_map[category]
    icon = category['icon']
    icon_color = category['color']
    long_name = category['long_name']
    # print(f"\n The category at the filter is: {category}")

    result = f"""<a href="#!" class="{icon_color}-text">
                    <h5 class="font-weight-bold mb-3">
                        <i class="fa {icon} pr-2"></i>
                                {long_name}
                    </h5></a>"""
    return result


@register.filter()
def map_category_to_button_color(category):
    """
    :param category: A valid category as defined in techblog.models in Post.CATEGORIES
    :return: the specific color
    """
    return choices_map[category]['color']