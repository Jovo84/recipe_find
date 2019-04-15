from setup_app.server import app

from setup_app.api.api_controller import api
from setup_app.web.web_controller import web

# Register blueprints

app.register_blueprint(web)
app.register_blueprint(api, url_prefix='/api')

if __name__ == "__main__":
    app.run(threaded=True)
