from flask import Flask


chat_app = Flask(__name__)


from chat_app import data_routers
from chat_app import page_routers






