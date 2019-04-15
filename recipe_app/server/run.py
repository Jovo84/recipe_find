from recipe_app.server import app

from recipe_app.api.api_controller import api
from recipe_app.web.web_controller import web

# Register blueprints

app.register_blueprint(web)
app.register_blueprint(api, url_prefix='/api')

if __name__ == "__main__":
    app.run(threaded=True)
