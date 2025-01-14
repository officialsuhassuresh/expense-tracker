from typer.testing import CliRunner
from expense_tracker.cli import app

runner = CliRunner()

def test_add_expense():
    result = runner.invoke(app, [
        "add",
        "--description", "Test Expense",
        "--amount", "50.00",
        "--category", "Test"
    ])
    assert result.exit_code == 0
    assert "Expense added successfully" in result.stdout

def test_invalid_amount():
    result = runner.invoke(app, [
        "add",
        "--description", "Test Expense",
        "--amount", "-50.00",
        "--category", "Test"
    ])
    assert result.exit_code == 1
    assert "Error" in result.stdout 