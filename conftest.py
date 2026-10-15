import os

import pytest
from playwright.sync_api import sync_playwright

# Run without a visible browser by default (needed on CI servers).
# To watch the browser locally, set HEADLESS=false before running pytest.
HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"


@pytest.fixture(scope="session")
def browser():
    # Start Playwright and launch the browser once for the whole test session
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=HEADLESS)
        yield browser
        browser.close()  # cleanup after all tests finish


@pytest.fixture(scope="function")
def page(browser):
    # Create a fresh page (tab) for each individual test
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()  # cleanup after each test