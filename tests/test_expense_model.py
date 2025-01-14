import pytest
from decimal import Decimal
from datetime import datetime
from expense_tracker.models.expense import Expense

def test_valid_expense_creation():
    expense = Expense(
        description="Lunch",
        amount=Decimal("20.50"),
        category="Food"
    )
    assert expense.description == "Lunch"
    assert expense.amount == Decimal("20.50")
    assert expense.category == "Food"
    assert isinstance(expense.date, datetime)

def test_invalid_amount():
    with pytest.raises(ValueError):
        Expense(
            description="Lunch",
            amount=Decimal("-20.50"),
            category="Food"
        ) 