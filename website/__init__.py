from flask import Flask

def create_app():
  app = Flask(__name__)
  app.config['SECRET_KEY'] = 'qwertyuiopasdfghjklzxcvbnm'
  
  from .views import views
  from .auth import auth
  
  return app