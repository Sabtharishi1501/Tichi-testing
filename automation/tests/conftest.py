import pytest

from utilities.driver_factory import get_driver
from utilities.config import BASE_URL


@pytest.fixture
def driver():

    driver = get_driver()

    driver.get(BASE_URL)

    yield driver

    driver.quit()