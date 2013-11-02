import time
import md5
import os
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from IPython import embed
from flask import render_template_string

PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))


app = Flask(__name__.split('.')[0])
app.config.from_object('wedding.envvar')

def validate_token(token, time):
    return md5.md5(secret_key+time).hexdigest() == token

def gen_token():
    ts = str(time.time())
    return ts, md5.md5(secret_key+ts).hexdigest()

def render(template_name, context={}):
    context['page'] = template_name
    return render_template(template_name, **context)

@app.route("/", methods=["GET"])
def index():
    return render("index.html")

@app.route("/templated/<path:filename>", methods=["GET"])
def templated(filename):
	staticfile = os.sep.join([PROJECT_ROOT,"static",filename])
	if not os.path.exists(staticfile):
		return None

	content = file(staticfile).read()

	return render_template_string(content)
