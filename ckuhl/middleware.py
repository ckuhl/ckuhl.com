import datetime
import dateutil
import logging

from flask import current_app, request, render_template


logger = logging.getLogger(__name__)


@current_app.template_filter()
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


@current_app.template_filter()
def teaser_para(content):
    """
    Given a block of HTML, return only the first paragraph (the teaser)

    :param str content: Entire HTML block
    :returns str: First paragraph of html
    """
    return content.split('</p>')[0] + '</p>'


@current_app.template_filter()
def teaser_sentence(content, n=3):
    """
    Given a block of HTML, return only the first n sentences.

    :param str content: Entire HTML block
    :returns str: First n sentences of html
    """
    # TODO: Yes this is a hack
    return '.'.join(content.split('</p>')[0].split('.')[:n]) + '.' + '</p>'


@current_app.errorhandler(404)
def page_404(e):
    """Page not found"""
    return render_template('errors/404.j2'), 404


@current_app.errorhandler(403)
def page_403(e):
    """Forbidden"""
    return render_template('errors/403.j2'), 403


@current_app.before_request
def log_request():
    """
    Log all visiting user agents
    """
    logger.info("%s # %s # %s # %s",
            request.user_agent,
            request.accept_languages,
            request.url,
            datetime.datetime.now())


@current_app.context_processor
def inject_dnt():
    """
    inject a Do Not Track header var for all contexts
    """
    dnt = False
    try:
        dnt = request.headers['dnt']
    except KeyError:
        pass
    try:
        dnt = request.headers['DNT']
    except KeyError:
        pass
    return {'do_not_track': dnt}

