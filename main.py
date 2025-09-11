import typer
from db import init_db

app = typer.Typer()

@app.callback()
def startup():
    init_db()

if __name__ == "__main__":
    app()