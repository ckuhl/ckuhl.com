from typing import Dict

from django.http import HttpRequest


def do_not_track(request: HttpRequest) -> Dict[str, bool]:
    """
    Insert whether or not Do Not Track is enabled into every context.
    For more information, see: https://en.wikipedia.org/wiki/Do_Not_Track

    Value can be 1, 0, or unset. For now, assuming unset means the visitor is
    okay with tracking.
    """
    return {'do_not_track': bool(request.META.get('HTTP_DNT', 0))}
