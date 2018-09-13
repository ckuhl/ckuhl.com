from flask import Blueprint, render_template, redirect, url_for


s = Blueprint('shortlinks', __name__)

@s.route('/')
def main():
    return redirect(url_for('core.main'))

@s.route('/ImageBlockX/')
def image_block_x():
    return redirect(url_for('portfolio.project', path='image-block-x'))

