from django import template
register = template.Library()

def myreplace(value, arg):
    return value.replace(arg, "pussy")


register.filter('pucfilter', myreplace)