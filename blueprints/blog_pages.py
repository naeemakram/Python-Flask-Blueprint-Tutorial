from flask import Blueprint, abort, render_template
from jinja2 import TemplateNotFound

blog_pages = Blueprint('blog_pages', __name__, template_folder='templates/blog')

@blog_pages.route('/blog', defaults={'page': '/index'})
@blog_pages.route('/blog/<page>')
def blog_page(page):
    try:
        return render_template(f'/blog/{page}.html')
    except TemplateNotFound:
        abort(404)