import typer
from db import init_db, add_expense
from rich.console import Console

app = typer.Typer()
console = Console()

@app.callback()
def startup():
    init_db()

@app.command()
def add():
  while True:
    try:
      amount = float(typer.prompt("Nominal"))
      break
    except ValueError:
      console.print("[red]Invalid input. Please enter a number[/red]")
  
  category = typer.prompt("Category", default="Eat")
  note = typer.prompt("Note (opsional)", default="")
  
  add_expense(amount, category, note)
  console.print(f"Added: {amount:,.0f} — {category}".replace(",", "."))

if __name__ == "__main__":
    app()