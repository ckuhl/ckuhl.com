import dateutil


def prettydate(date, fmt=None):
    """
    Filter to pretty format the date as:
    <month name> <day number>, <year>
    """
    date = dateutil.parser.parse(date)
    native = date.replace(tzinfo=None)
    format='%B %e, %Y'
    return native.strftime(format)

def numericdate(date, fmt=None):
    """
    Filter to format the date as:
    <year>-<month #>-<date of month>
    """
    date = dateutil.parser.parse(date)
    native = date.replace(tzinfo=None)
    format='%Y-%m-%d'
    return native.strftime(format)

