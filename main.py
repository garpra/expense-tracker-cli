import typer
from db import init_db, add_expense, get_expenses, get_budgets, set_budget, get_summary
from rich.console import Console
from rich.table import Table
from datetime import datetime

app = typer.Typer()
console = Console()
budget_app = typer.Typer()
app.add_typer(budget_app, name="budget")

def format_currency(amount: float) -> str:
  return f"Rp {amount:,.0f}".replace(",", ".")

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
  console.print(f"Added: {format_currency(amount)} — {category}")

@app.command("list")
def show():
  rows = get_expenses()

  if(len(rows) == 0):
    console.print("[red]No expenses yet[/red]")
    return

  table = Table()
  table.add_column("Date", style="dim")
  table.add_column("Category")
  table.add_column("Nominal", justify="right")
  table.add_column("Note")

  for row in rows:
    date = row["date"]
    category = row["category"]
    amount = row["amount"]
    note = row["note"] or ""

    table.add_row(date, category, format_currency(amount), note)

  console.print(table)

@app.command()
def summary():
  month_now = datetime.now().strftime("%Y-%m")
  total_spent = 0
  budgets = get_budgets(month_now)
  budget_map = {row["category"]: row["amount"] for row in budgets}

  rows = get_summary(month_now)
  if(len(rows) == 0):
    console.print("[red]No expenses this month[/red]")
    return

  table = Table()
  table.add_column("Category")
  table.add_column("Spent")
  table.add_column("Budget")
  table.add_column("Status")

  for row in rows:
    category = row["category"]
    budget = budget_map.get(category, None)
    spent = row["total"]
    total_spent += spent

    if budget is None:
      table.add_row(category, format_currency(spent), "-", "-")
    else:
      if spent > budget:
        table.add_row(category, format_currency(spent), format_currency(budget), "[red]⚠[/red]")
      else:
        table.add_row(category, format_currency(spent), format_currency(budget), "[green]✓[/green]")

  console.print(table)
  console.print(f"Total: {format_currency(total_spent)}")

@budget_app.command("set")
def budget_set():
  category = typer.prompt("Category", default="Eat")
  while True:
    try:
      amount = float(typer.prompt("Nominal"))
      break
    except ValueError:
      console.print("[red]Invalid input. Please enter a number[/red]")
  
  month_now = datetime.now().strftime("%Y-%m")
  set_budget(category, month_now, amount)
  console.print(f"Added: {format_currency(amount)} — {category} - {month_now}")

@budget_app.command("show")
def budget_show():
  month_now = datetime.now().strftime("%Y-%m")
  rows = get_budgets(month_now)

  if(len(rows) == 0):
    console.print("[red]No budget yet[/red]")
    return
  
  table = Table()
  table.add_column("Category")
  table.add_column("Budget Amount")

  for row in rows:
    category = row["category"]
    budget = row["amount"]
    table.add_row(category, format_currency(budget))

  console.print(table)

if __name__ == "__main__":
    app()