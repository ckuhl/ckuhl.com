import dateutil


def datetimeformat(date, fmt='%Y-%m-%d'):
    """
    Format a datetime object according to an arbitrary format string

    :param Date date: Date to format
    :param str fmt: Formatting string to use
    :returns str: Formatted date
    """
    date = dateutil.parser.parse(date)
    native = date.replace(tzinfo=None)
    return native.strftime(fmt)

def teaser(content):
    """
    Given a block of HTML, return only the first paragraph (the teaser)

    :param str content: Entire HTML block
    :returns str: First paragraph of html
    """
    return content.split('</p>')[0] + '</p>'

