import datetime
import dateutil
import logging

from flask import current_app, request, render_template


logger = logging.getLogger(__name__)


@current_app.template_filter()
def format_datetime(date, fmt='%Y-%m-%d'):
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
    FIXME: Replace with with an actual `teaser: ` segment in FlatPages.

    :param str content: Entire HTML block
    :returns str: First paragraph of html
    """
    return content.split('</p>')[0] + '</p>'


@current_app.template_filter()
def teaser_sentence(content, n=3):
    """
    Given a block of HTML, return only the first n sentences.

    :param str content: Entire HTML block
    :param integer n: number of sentences
    :returns str: First n sentences of html
    """
    # FIXME: Yes this is a hack
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

    TODO: Convert this to write to the database.
    """
    logger.info("%s # %s # %s # %s",
                request.user_agent,
                request.accept_languages,
                request.url,
                datetime.datetime.now())


@current_app.context_processor
def inject_dnt():
    """
    Inject a `Do Not Track` header variable for all contexts

    This allows conditionally including tracking scripts, depending on if
    someone doesn't want to be tracked or not.

    Note: They will still be recorded in server logs, as they're interacting
    with the server. However no personal information should be recorded.
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
