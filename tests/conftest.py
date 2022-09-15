import pytest
from .packing import clear

@pytest.fixture(scope='module', autouse=True)
def teardown():
    pass
    yield
    clear()