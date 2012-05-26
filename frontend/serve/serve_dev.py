import sys, os, os.path
sys.path.append(os.path.join(os.path.normpath(os.path.dirname(__file__)), '../../')) 

print sys.path
from frontend import app

if __name__ == "__main__":
    app.run()
