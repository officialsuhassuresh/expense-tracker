import typer
from .commands import expense_commands

app = typer.Typer(help="Expense Tracker CLI")

app.command(name="add")(expense_commands.add_expense)
app.command(name="list")(expense_commands.list_expenses)
app.command(name="delete")(expense_commands.delete_expense)
app.command(name="summary")(expense_commands.show_summary)

if __name__ == "__main__":
    app() 