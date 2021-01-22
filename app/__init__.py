import quart
import hypercorn
import os

app = quart.Quart(__name__)
app.config["SECRET_KEY"] = os.urandom(32)
