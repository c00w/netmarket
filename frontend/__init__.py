import logging, flask, traceback, random

app = flask.Flask('frontend', template_folder='.', 
            static_folder = 'static')
app.Debug = False

# Set a secret key. Mainly used for CSRF. Should be random otherwise 
# no protection since no one is going to remember to change this
ascii_uppercase = 'ABCDEFHIJKLMNOPQRXTUVWXYZ'
digits = '0123456789'
app.secret_key = ''.join(random.choice(ascii_uppercase + digits) for x in range(20))

@app.teardown_request
def teardown_request_wrap(exception):
    """
    Prints tracebacks and handles bugs
    """
    if exception:
        logging.error(traceback.format_exc()) 

import frontend.user         
import frontend.upload
import frontend.search
import frontend.homepage
import frontend.settings
import frontend.files
