from flask import Blueprint, redirect, url_for


short_links = Blueprint('short_links', __name__)


@short_links.route('/')
def main():
    return redirect(url_for('core.main'))


@short_links.route('/ImageBlockX/')
def image_block_x():
    return redirect(url_for('portfolio.project', path='image-block-x'))
