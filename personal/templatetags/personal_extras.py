# from django import template
# from datetime import datetime, timezone
# from urllib.parse import quote, quote_plus, unquote

# register = template.Library()

# @register.filter
# def get_value(arg):
#     categories_readable = {"history": "history", "politics-and-international-relations": "POLITICS & INTERNATIONAL RELATIONS",
#                "society-and-culture": "SOCIETY & CULTURE", "science-and-technology": "SCIENCE & TECHNOLOGY",
#                "art-and-literature": "ART & LITERATURE", "business-and-economics": "BUSINESS & ECONOMICS"}
#     return categories_readable[arg]