import pytest
from decimal import Decimal
from expense_tracker.utils.storage import Storage
from expense_tracker.models.expense import Expense

@pytest.fixture
def storage(tmp_path):
    # Mock storage with temporary file
    storage = Storage()
    storage.data_file = tmp_path / ".expense_tracker.json"
    storage.ensure_data_file()
    return storage

def test_add_expense(storage):
    expense = Expense(description="Test", amount=Decimal("10.00"))
    saved = storage.add_expense(expense)
    assert saved.id == 1
    
    expenses = storage.load_expenses()
    assert len(expenses) == 1
    assert expenses[0].description == "Test"

def test_delete_expense(storage):
    # Add and then delete expense
    expense = Expense(description="Test", amount=Decimal("10.00"))
    saved = storage.add_expense(expense)
    
    assert storage.delete_expense(saved.id) == True
    assert len(storage.load_expenses()) == 0 