from datetime import datetime

import pytest

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    print("This is Pytest config file")
    report_dir="reports"
    now=datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    config.option.htmlpath=f"{report_dir}/reports_{now}.html"
    
@pytest.fixture(scope='session',autouse=True)
def setup_teardown():
    print("This is setup and teardown method")
    print("Starting the test")
    yield
    print("Ending the test")