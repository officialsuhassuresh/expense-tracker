# Expense Tracker CLI

A command-line expense tracking application built with Python and Typer that helps you manage your personal expenses efficiently.

Created as part of the specification provided in https://roadmap.sh/projects/expense-tracker

## Introduction

Expense Tracker CLI is a simple yet powerful tool that allows you to:
- Add, update, and delete expenses
- View all expenses in a formatted table
- Get monthly and overall expense summaries
- Categorize expenses and track spending patterns
- Export expenses to CSV (coming soon)

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/expense-tracker
cd expense-tracker
```

2. Create a virtual environment:
```bash
python -m venv .venv
```

3. Activate the virtual environment:

On Unix or MacOS:
```bash
source .venv/bin/activate
```

On Windows:
```bash
.\.venv\Scripts\activate
```

4. Install the package in development mode:
```bash
pip install -e .
```

## Usage

After installation, you can use the following commands:

### Add an expense
```bash
expense-tracker add --description "Lunch" --amount 20 --category "Food"
```

### List all expenses
```bash
expense-tracker list
```

### View expense summary
```bash
# View total expenses
expense-tracker summary

# View expenses for a specific month
expense-tracker summary --month 8
```

### Delete an expense
```bash
expense-tracker delete 1  # Replace 1 with the expense ID
```

## Data Storage

All expenses are stored locally in a JSON file located at `~/.expense_tracker.json`.

## Testing

Run the tests with:
```bash
pytest
```

For coverage report:
```bash
pytest --cov=expense_tracker --cov-report=html
```

## Cleanup

When you're done working with the expense tracker, you can:

1. Deactivate the virtual environment:
```bash
deactivate
```

2. Remove the virtual environment directory:

On Unix or MacOS:
```bash
rm -rf .venv
```

On Windows:
```bash
rmdir /s /q .venv
```

3. Optionally, remove the expense data file:

On Unix or MacOS:
```bash
rm ~/.expense_tracker.json
```

On Windows:
```bash
del %USERPROFILE%\.expense_tracker.json
```

Note: Removing the data file will permanently delete all your expense records.

