import json
from pathlib import Path
from typing import List, Optional
from decimal import Decimal
from datetime import datetime
from ..models.expense import Expense

class Storage:
    def __init__(self):
        self.data_file = Path.home() / ".expense_tracker.json"
        self.ensure_data_file()

    def ensure_data_file(self):
        if not self.data_file.exists():
            self.data_file.write_text("[]")

    def load_expenses(self) -> List[Expense]:
        data = json.loads(self.data_file.read_text())
        expenses = []
        for item in data:
            item['amount'] = Decimal(item['amount'])
            item['date'] = datetime.fromisoformat(item['date'])
            expenses.append(Expense(**item))
        return expenses

    def save_expenses(self, expenses: List[Expense]):
        data = [expense.model_dump() for expense in expenses]
        self.data_file.write_text(json.dumps(data, default=str))

    def add_expense(self, expense: Expense) -> Expense:
        expenses = self.load_expenses()
        expense.id = len(expenses) + 1
        expenses.append(expense)
        self.save_expenses(expenses)
        return expense

    def get_expense(self, expense_id: int) -> Optional[Expense]:
        expenses = self.load_expenses()
        return next((e for e in expenses if e.id == expense_id), None)

    def update_expense(self, expense_id: int, updated_expense: Expense) -> Optional[Expense]:
        expenses = self.load_expenses()
        for i, expense in enumerate(expenses):
            if expense.id == expense_id:
                updated_expense.id = expense_id
                expenses[i] = updated_expense
                self.save_expenses(expenses)
                return updated_expense
        return None

    def delete_expense(self, expense_id: int) -> bool:
        expenses = self.load_expenses()
        filtered_expenses = [e for e in expenses if e.id != expense_id]
        if len(filtered_expenses) < len(expenses):
            self.save_expenses(filtered_expenses)
            return True
        return False 