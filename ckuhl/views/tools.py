from flask import Blueprint, render_template


utilities = Blueprint('tools', __name__)

@utilities.route('/')
def index(blog_n=999):
    """return a listing of tools"""
    return render_template('tools/index.html')

@utilities.route('/<string:tool>/')
def tool(tool):
    """return a specific tool page"""
    return render_template('tools/tool.html')

