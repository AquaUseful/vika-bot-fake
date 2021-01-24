from app.modules import users, tokens, chats


def register_blueprints(app):
    app.register_blueprint(users.blueprint)
    app.register_blueprint(tokens.blueprint)
    app.register_blueprint(chats.blueprint)
