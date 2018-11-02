import logging
import re

from django import template
from django.template.defaultfilters import stringfilter


register = template.Library()

log = logging.getLogger(__name__)


@register.filter('truncateparas_html')
@stringfilter
def first_paragraph_html(html: str) -> str:
    """
    Use a regex way to get the first paragraph from HTML.

    Not going to work _all_ of the time, but it should work most of the time.
    """
    try:
        return re.search(r'^<p>[\S\s]*?</p>', html).group(0)
    except AttributeError:
        return ''
