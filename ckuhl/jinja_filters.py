import dateutil


def datetimeformat(date, fmt='%Y-%m-%d'):
    """
    Format a datetime object according to an arbitrary format string

    :param Date date: Date to format
    :param str fmt: Formatting string to use
    :returns string: Formatted date
    """
    date = dateutil.parser.parse(date)
    native = date.replace(tzinfo=None)
    return native.strftime(fmt)

