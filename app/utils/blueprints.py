from app.modules import users


def register_blueprints(app):
    app.register_blueprints(users.bluerprint)
