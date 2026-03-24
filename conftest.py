import pytest
from src.calculator import divide

@pytest.fixture
def division_cases():
    """Provides (a, b, expected) tuples."""
    return [(10, 2, 5.0), (9, 3, 3.0)]

@pytest.fixture(scope="module")
def db_connection():
    conn = create_test_db()
    yield conn      # test runs here
    conn.close()    # teardown


