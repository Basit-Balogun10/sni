from django import template
from datetime import datetime, timezone
from urllib.parse import quote, quote_plus, unquote

register = template.Library()


@register.simple_tag
def concat_all(*args):
    """concatenate all args"""
    return ''.join(map(str, args))


# @register.simple_tag
# def sum_up(*args):
#     return sum(args)


@register.simple_tag
def assign(string):
    assignment = string
    return string


@register.filter
def myfunc(arg):
    def utc_to_local(utc_dt):
        return utc_dt.replace(tzinfo=timezone.utc).astimezone(tz=None)

    def aslocaltimestr(utc_dt):
        return utc_to_local(utc_dt).strftime('%a, %B %d, %Y %X %Z %z')

    local_time = aslocaltimestr(arg)
    return local_time


@register.filter
def get_time(arg):
    print(datetime.now())

    print(myfunc(datetime.now()))
    return datetime.now()
