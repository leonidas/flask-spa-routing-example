# Flask SPA routing example

1. Serve API views from `/api/v1` only for logged in users
2. Serve static files in development only for logged in users
3. Serve `index.html` for everything else in development for logged in users
4. Redirect to `/login` (`static/login.html`) for everything else

## Getting started

    virtualenv venv-flask-spa-routing-example
    source venv-flask-spa-routing-example/bin/activate

    git clone https://github.com/leonidas/flask-spa-routing-example
    cd flask-spa-routing-example
    pip install -r requirements.txt

    python main.py
    open http://localhost:5000