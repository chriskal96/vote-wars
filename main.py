from flask import Flask
from flask_restx import Api
from api.routes import ns  # Import the namespace

app = Flask(__name__)

# Create the API and attach Swagger docs
api = Api(app,
          version="1.0",
          title="Star Wars API",
          description="API to access characters, films, and starships stored in DB",
          doc="/docs")

# Add the namespace with a prefix
api.add_namespace(ns, path="/api/v1/vote_wars")

if __name__ == "__main__":
    app.run(debug=True)