from app import create_app
app = create_app()

from flask_migrate import Migrate
from app.models import db

# Initialize database migration support
migrate = Migrate(app, db)

# Import Blueprints (if using any)
from app.routes import main

# Register Blueprints
app.register_blueprint(main)

if __name__ == '__main__':
    # Running the Flask app
    app.run(debug=True)
