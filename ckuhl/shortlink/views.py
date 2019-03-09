import logging

from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse

log = logging.getLogger(__name__)


def outbound(request: HttpRequest, outbound_link: str) -> HttpResponse:
    """Track outbound links (for the analytics)"""
    # TODO: Analytics here(?)
    log.info(f'Outbound link followed to {outbound_link}')
    return redirect(outbound_link)


def root(request: HttpRequest) -> HttpResponse:
    """Redirect the root page to the website root"""
    return redirect(reverse('core:home'), permanent=True)


def image_block_x(request: HttpRequest) -> HttpResponse:
    """Link to the Image Block X portfolio page (this link is used on GitHub)"""
    return redirect(reverse('portfolio:project', args=['image-block-x']))


def mips_vm(request: HttpRequest) -> HttpResponse:
    """Link to the MIPS VM portfolio page (this link is used on GitHub)"""
    return redirect(reverse('portfolio:project', args=['mips-vm']))
