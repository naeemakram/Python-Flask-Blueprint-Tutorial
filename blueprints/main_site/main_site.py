from flask import Blueprint, abort, render_template
from jinja2 import TemplateNotFound
from blueprints.blog_pages import blog_pages

main_site = Blueprint('main_site', __name__, template_folder='templates')
main_site.register_blueprint(blog_pages.blog_pages)


@main_site.route('/', defaults={'page': 'index'})
@main_site.route('/<page>')
def show(page):
    try:
        return render_template(f'{page}.html')
    except TemplateNotFound:
        abort(404)
