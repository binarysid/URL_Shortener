from flask import Flask
from database import database
from app.views import view_blue_print
from config import Config
from flask_migrate import Migrate

def create_app():  
    app = Flask(__name__)
    app.config.from_object(Config)
    database.init_app(app)
    migrate = Migrate(app, database.db)
    app.register_blueprint(view_blue_print)
    return app

# def set_env(mode):
#     if mode == Env.DEV:  
#         dotenv_file = '.env.dev'
#     elif mode == Env.PROD:
#         dotenv_file = '.env.prod'
#     else:
#         dotenv_file = '.env.dev'
#     load_dotenv(dotenv_file)


if __name__ == "__main__":
    create_app().run(debug=Config.DEBUG,host='0.0.0.0')