# Playwright + Pytest Framework (in progress)

A framework skeleton built with Python and Playwright, being developed step by step as a learning project. Tests are being added.

## Status

**Built so far**
- One page object (`pages/login_page.py`)
- Shared pytest fixtures (`conftest.py`)
- A GitHub Actions workflow file
- A test plan (`docs/test-plan.md`)

**Planned**
- UI tests using the page objects
- API tests with pytest and `requests`
- JSON-driven test data
- Markers for smoke and regression runs
- HTML and Allure reports
- Cross-browser runs

## Tech Stack
- Python 3.x
- Playwright (Python)
- Pytest
- Page Object Model (POM)
- GitHub Actions

## Project Structure

```
playwright-automation-framework/
  .github/workflows/   CI workflow
  docs/                test plan
  pages/               page objects (login_page.py)
  test-data/           test data (empty for now)
  tests/
    api/               API tests (planned)
    ui/                UI tests (planned)
  conftest.py          shared pytest fixtures
  requirements.txt
  .gitignore
```

## How to Run

```bash
pip install -r requirements.txt
playwright install
pytest tests/ -v
```

Tests run without a visible browser by default. To watch the browser on Windows PowerShell:

```powershell
$env:HEADLESS="false"; pytest tests/ -v
```

## Author
Varun Deshpande