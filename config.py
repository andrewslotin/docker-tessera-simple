import os

GRAPHITE_URL  = os.getenv('GRAPHITE_URL', 'http://localhost:8080')
SECRET_KEY    = os.getenv('SECRET_KEY', 'you might want to change it')
SERVER_PORT   = 80
DEFAULT_THEME = 'snow'
