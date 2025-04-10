from .news_routes import news_bp
from .general_routes import general_bp
from .utility_routes import utility_bp

def register_routes(app):
    app.register_blueprint(news_bp, url_prefix='/api')
    app.register_blueprint(general_bp, url_prefix='/api')
    app.register_blueprint(utility_bp, url_prefix='/api')
