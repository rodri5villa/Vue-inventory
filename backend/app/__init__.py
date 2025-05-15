from flask import Flask
from flask_graphql import GraphQLView
from .process import schema
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.add_url_rule(
    '/',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True
    )
)
