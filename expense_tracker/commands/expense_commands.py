from datetime import datetime
from decimal import Decimal
from typing import Optional
import typer
from rich.console import Console
from rich.table import Table
from ..models.expense import Expense
from ..utils.storage import Storage

console = Console()
storage = Storage()

def add_expense(
    description: str = typer.Option(..., "--description", "-d", help="Expense description"),
    amount: float = typer.Option(..., "--amount", "-a", help="Expense amount"),
    category: str = typer.Option("General", "--category", "-c", help="Expense category")
) -> None:
    """Add a new expense"""
    try:
        expense = Expense(
            description=description,
            amount=Decimal(str(amount)),
            category=category
        )
        saved_expense = storage.add_expense(expense)
        console.print(f"[green]Expense added successfully (ID: {saved_expense.id})[/green]")
    except ValueError as e:
        console.print(f"[red]Error: {str(e)}[/red]")
        raise typer.Exit(1)

def list_expenses() -> None:
    """List all expenses"""
    expenses = storage.load_expenses()
    
    if not expenses:
        console.print("[yellow]No expenses found[/yellow]")
        return

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("ID")
    table.add_column("Date")
    table.add_column("Description")
    table.add_column("Category")
    table.add_column("Amount")

    for expense in expenses:
        table.add_row(
            str(expense.id),
            expense.date.strftime("%Y-%m-%d"),
            expense.description,
            expense.category,
            f"${expense.amount:,.2f}"
        )

    console.print(table)

def delete_expense(
    expense_id: int = typer.Argument(..., help="ID of the expense to delete")
) -> None:
    """Delete an expense by ID"""
    if storage.delete_expense(expense_id):
        console.print(f"[green]Expense deleted successfully[/green]")
    else:
        console.print(f"[red]Expense with ID {expense_id} not found[/red]")
        raise typer.Exit(1)

def show_summary(
    month: Optional[int] = typer.Option(None, "--month", "-m", help="Month number (1-12)")
) -> None:
    """Show expense summary"""
    expenses = storage.load_expenses()
    
    if month:
        current_year = datetime.now().year
        expenses = [
            e for e in expenses 
            if e.date.month == month and e.date.year == current_year
        ]
        total = sum(e.amount for e in expenses)
        console.print(f"Total expenses for {datetime(2000, month, 1).strftime('%B')}: ${total:,.2f}")
    else:
        total = sum(e.amount for e in expenses)
        console.print(f"Total expenses: ${total:,.2f}") 