from core import app
from flask_cors import CORS

CORS(app)

if __name__ == "__main__":
    app.run(port = 3000, debug = True)