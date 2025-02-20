"""
    review/custom_filters.py
"""

from django import template
from django.utils.timesince import timesince

register = template.Library()


@register.filter
def compact_timesince(value):
    """compact_timesince filter
    Returns a compact version of the timesince value.
    """
    time_str = timesince(value).split(",")[0]
    time_parts = time_str.split()
    if len(time_parts) == 2:
        return f"{time_parts[0]}{time_parts[1][0]}"
    return time_str
