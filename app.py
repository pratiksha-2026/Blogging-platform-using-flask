import os
from flaskblog import app

if __name__ == '__main__':
    # Railway/Heroku/Render will provide a 'PORT' environment variable.
    # We default to 5000 if it's not found (for local running).
    port = int(os.environ.get("PORT", 5000))
    
    # We use host='0.0.0.0' to tell the app to listen on all public IPs.
    # We remove debug=True for production safety.
    app.run(host='0.0.0.0', port=port)