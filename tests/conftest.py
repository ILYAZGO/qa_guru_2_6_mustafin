import pytest

@pytest.fixture(scope='function', autouse=True)
def files_into_zip():
    pass
    yield