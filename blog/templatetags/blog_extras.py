from django import template
from datetime import datetime, timezone
from urllib.parse import quote, quote_plus, unquote
from bs4 import BeautifulSoup


register = template.Library()


@register.simple_tag
def concat_all(*args):
    """concatenate all args"""
    return ''.join(map(str, args))


@register.simple_tag
def get_trending(*args):
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
        return utc_to_local(utc_dt).strftime('%a, %b %d, %Y %X %Z %z')

    local_time = aslocaltimestr(arg)
    return local_time


@register.filter
def full_datetime(arg):
    def utc_to_local(utc_dt):
        return utc_dt.replace(tzinfo=timezone.utc).astimezone(tz=None)

    def aslocaltimestr(utc_dt):
        return utc_to_local(utc_dt).strftime('%a, %B %d, %Y %X %z')

    local_time = aslocaltimestr(arg)
    return local_time


@register.filter
def get_time(arg):
    return datetime.now()


@register.filter
def get_readable(arg):
    categories_readable = {"history": "HISTORY", "politics-and-international-relations": "POLITICS & INTERNATIONAL RELATIONS",
               "society-and-culture": "SOCIETY & CULTURE", "science-and-technology": "SCIENCE & TECHNOLOGY",
               "art-and-literature": "ART & LITERATURE", "business-and-economics": "BUSINESS & ECONOMICS"}
    return categories_readable[arg]

@register.filter
def get_color(arg):
    categories_color = {"history": "deepskyblue", "politics-and-international-relations": "red",
            "society-and-culture": "yellow", "science-and-technology": "lightseagreen",
            "art-and-literature": "blue", "business-and-economics": "deeppink"}
    return categories_color[arg]


@register.filter
def get_text(arg):
    soup = BeautifulSoup(arg, features="lxml")
    return soup.get_text()