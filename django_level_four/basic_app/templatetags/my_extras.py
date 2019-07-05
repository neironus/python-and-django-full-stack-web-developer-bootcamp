from django import template


register = template.Library()

# First Way
@register.filter(name='cut')
def cut(value, arg):
    """
    This cuts out string
    """
    return value.replace(arg, '')

# # Second Way
# def cut(value, arg):
#     """
#     This cuts out string
#     """
#     return value.replace(arg, '')
# register.filter('cur', cut)
