from django import template

register = template.Library()

@register.filter(name = 'cutB')
def cutA(value, arg):
    """
    This cuts out all values of "arg" from the string!
    """
    return value.replace(arg,'')

# register.filter('cutB', cutA)
