"""Playing with reCAPTCHA"""
import os
import requests
from urllib.parse import urlparse, parse_qs

from jinja2 import Environment
from jinja2 import FileSystemLoader
from chalice import Chalice, Response, NotFoundError, ChaliceViewError

app = Chalice(app_name='chalice-recaptcha')
app.debug = True

site_key = os.environ["RECAPTCHA_SITE_KEY"]
secret_key = os.environ["RECAPTCHA_SECREY_KEY"]

def _render_template(**kwargs):
    "render jinja template"
    env = Environment(loader=FileSystemLoader(os.path.abspath(os.path.dirname(__file__))))
    template = env.get_template('chalicelib/main.html')
    rendered_template = template.render(kwargs)
    return rendered_template

@app.route('/validate', methods=['POST'], content_types=['application/x-www-form-urlencoded'])
def validate():
    request = app.current_request
    if request.method == 'POST':
        url = "https://www.google.com/recaptcha/api/siteverify"
        parsed = parse_qs(app.current_request.raw_body.decode())
        if "g-recaptcha-response" in parsed:
            recaptcha = parsed["g-recaptcha-response"]
            r = requests.post(url, data = {'secret' : secret_key, 'response' : recaptcha})
            if (r.json()['success']):
                return Response(body=_render_template(message="success"),
                                headers={'Content-Type': 'text/html'},
                                status_code=200)

    return Response(body=_render_template(error_message="not good"),
                    headers={'Content-Type': 'text/html'},
                    status_code=200)

@app.route('/')
def index():
    "homepage route"
    return Response(body=_render_template(site_key=site_key),
                    headers={'Content-Type': 'text/html'},
                    status_code=200)
