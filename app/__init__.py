import quart
import hypercorn
import os
from app.utils import blueprints

app = quart.Quart(__name__)
app.config["SECRET_KEY"] = os.urandom(32)
blueprints.register_blueprints(app)
