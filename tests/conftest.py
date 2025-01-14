import pytest
from pathlib import Path
from expense_tracker.utils.storage import Storage

@pytest.fixture
def temp_storage(tmp_path):
    storage = Storage()
    storage.data_file = tmp_path / ".expense_tracker.json"
    storage.ensure_data_file()
    return storage

@pytest.fixture
def clean_storage():
    """Provides a clean storage for each test"""
    yield Storage()
    # Cleanup after test
    if Path(".expense_tracker.json").exists():
        Path(".expense_tracker.json").unlink() 