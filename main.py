import typer
from db import init_db, add_expense, get_expenses, get_budgets
from rich.console import Console
from rich.table import Table
from datetime import datetime

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

@app.command("list")
def show():
  rows = get_expenses()

  if(len(rows) == 0):
    console.print("[red]Belum ada pengeluaran[/red]")
    return

  table = Table()
  table.add_column("Tanggal", style="dim")
  table.add_column("Kategori")
  table.add_column("Nominal", justify="right")
  table.add_column("Note")

  for row in rows:
    date = row["date"]
    category = row["category"]
    amount = row["amount"]
    note = row["note"] or ""

    table.add_row(date, category, f"{amount:,.0f}".replace(",", "."), note)

  console.print(table)

budget_app = typer.Typer()
app.add_typer(budget_app, name="budget")

@budget_app.command("set")
def budget_set():
  pass

@budget_app.command("show")
def budget_show():
  month_now = datetime.now().strftime("%Y-%m")
  rows = get_budgets(month_now)

  if(len(rows) == 0):
    console.print("[red]Belum ada budget[/red]")
    return
  
  table = Table()
  table.add_column("Kategori")
  table.add_column("Nominal Budget")

  for row in rows:
    category = row["category"]
    budget = row["amount"]
    table.add_row(category, f"Rp {budget:,.0f}".replace(",", "."))

  console.print(table)

if __name__ == "__main__":
    app()