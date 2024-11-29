from flask import Blueprint, abort, render_template
from jinja2 import TemplateNotFound

simple_page = Blueprint('simple_page', __name__, template_folder='templates')


@simple_page.route('/', defaults={'page': 'index'})
@simple_page.route('/<page>')
def show(page):
    try:
        return render_template(f'{page}.html')
    except TemplateNotFound:
        abort(404)
