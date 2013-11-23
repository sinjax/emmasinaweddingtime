import rsvp
from wedding import app
from helpers import *

@app.route("/place", methods=["GET"])
def place(): return render("place.html")

@app.route("/", methods=["GET"])
def plan(): return render("plan.html")

@app.route("/dinner", methods=["GET"])
def dinner(): return render("dinner.html")

@app.route("/templated/<path:filename>", methods=["GET"])
def templated(filename):
	staticfile = os.sep.join([PROJECT_ROOT,"static",filename])
	if not os.path.exists(staticfile):
		return None

	content = file(staticfile).read()

	return render_template_string(content)
