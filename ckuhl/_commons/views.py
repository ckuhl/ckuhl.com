from django.shortcuts import render


def page_not_found(request, exception, template_name='error/404.html'):
    """Override of the default 404 page"""
    return render(request, template_name, status=404)
