
import logging
from flask.logging import default_handler
from logging.handlers import RotatingFileHandler

from logging.config import dictConfig

'''
dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})
'''
log_file_path = "logs/foo.log"
handler = RotatingFileHandler(log_file_path, maxBytes=10000, backupCount=1)
formatter = logging.Formatter("[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")
handler.setFormatter(formatter)

from chat_app import chat_app as app

app.logger.setLevel(logging.INFO)
app.logger.addHandler(handler)

app.run(host='0.0.0.0', port=8000, debug=True)
