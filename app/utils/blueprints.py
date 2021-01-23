from app.modules import users, tokens


def register_blueprints(app):
    app.register_blueprint(users.blueprint)
    app.register_blueprint(tokens.blueprint)
