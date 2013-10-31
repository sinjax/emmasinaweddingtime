import time
import md5
import os
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect


PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
app = Flask(
    __name__, 
    static_folder=os.path.join(PROJECT_ROOT, 'public'),
    static_url_path='/public'
)

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

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
