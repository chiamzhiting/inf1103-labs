import pytest

from supplier import Supplier


@pytest.fixture
def supplier():
    return Supplier("S001", "TechSource Pte Ltd", "sales@techsource.com")