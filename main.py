from flask import appcontext_popped
from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run()
