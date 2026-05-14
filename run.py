import os
from app import create_app

# Load environment config (default to 'dev')
env = os.environ.get('FLASK_ENV', 'dev')
app = create_app(config_name=env)

if __name__ == '__main__':
    # Create tables if they don't exist
    with app.app_context():
        # Import db HERE, inside the context, to ensure it binds correctly
        from app.models import db

        db.create_all()
        print("Database tables created/verified successfully!")

    app.run(debug=True, host='0.0.0.0', port=5000)