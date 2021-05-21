from django import template
from datetime import datetime, timezone

register = template.Library()


@register.simple_tag
def concat_all(*args):
    """concatenate all args"""
    return ''.join(map(str, args))


@register.simple_tag
def assign(string):
    assignment = string
    return string


@register.filter
def myfunc(arg):
    def utc_to_local(utc_dt):
        return utc_dt.replace(tzinfo=timezone.utc).astimezone(tz=None)

    def aslocaltimestr(utc_dt):
        return utc_to_local(utc_dt).strftime('%m %d, %Y, %H:%M:%S - %Z %z')

    local_time = aslocaltimestr(arg)
    my_dict = {
        "01": "January",
        "02": "February",
        "03": "March",
        "04": "April",
        "05": "May",
        "06": "June",
        "07": "July",
        "08": "August",
        "09": "September",
        "10": "October",
        "11": "November",
        "12": "December",
    }

    tp = local_time.split(' ')
    month = tp[0]
    for key, values in my_dict.items():
        if month == key:
            tp[0] = values
            tp
            break
    local_time = ' '.join(tp)
    return local_time
