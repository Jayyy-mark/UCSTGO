import os
from app import create_app

# Load environment config (default to 'dev')
env = os.environ.get('FLASK_ENV', 'dev')
app = create_app(config_name=env)

if __name__ == '__main__':

    app.run(debug=True, host='0.0.0.0', port=5000)