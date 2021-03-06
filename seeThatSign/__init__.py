from flask import Flask
app = Flask(__name__)

import seeThatSign.views

def create_app(debug=True):
    app = Flask(__name__)
    app.debug = debug

    # add your modules
    app.register_module(seeThatSign.views)
    
    # other setup tasks

    return app

if __name__ == "__main__":
    app = create_app(debug=True)
    app.run()
