# Sports Group Test Project Automation Framework

Python + Pytest + Selenium WebDriver automation framework for the
Sports Group Test Project.

## Overview

This project provides a maintainable UI automation framework based on:

- Python
- Pytest
- Selenium WebDriver
- Page Object Model (POM)
- Explicit waits
- Environment-based configuration
- Pytest markers

## Application Under Test

The test application is:

https://qae-assignment-tau.vercel.app/

The candidate-specific URL is configured through the `BASE_URL`
environment variable.

Example:

    BASE_URL=https://qae-assignment-tau.vercel.app/?user-id=...

Keeping the URL in configuration prevents test code from becoming
dependent on environment-specific values.

## Project Structure

    SportGroupTestProject/
    │
    ├── README.md
    ├── requirements.txt
    ├── pytest.ini
    ├── .gitignore
    ├── example.env
    ├── .env
    │
    ├── TestingPlan.docx
    │
    ├── config/
    │   └── settings.py
    │
    ├── drivers/
    │   └── driver_factory.py
    │
    ├── pages/
    │   ├── base_page.py
    │   └── main_upcoming_matches.py
    │
    ├── tests/
    │   ├── conftest.py
    │   ├── test_upcoming_matches.py
    │
    ├── utils/
        └── waits.py
    

## Architecture

### Page Object Model

All Selenium interaction belongs in the `pages` package.

Tests should express business behavior and assertions 

For example:

    main_content.load(BASE_URL)
    assert main_content.is_loaded()

instead of:

    driver.find_element(By.ID, "main-content")

This makes the framework easier to maintain when the UI changes.

### BasePage

`BasePage` contains reusable Selenium operations such as:

- waiting for elements
- clicking
- reading text
- checking visibility
- finding elements

### MainContentPage

`UpcomingMatchesPage` represents only:

    #main-content

This is intentional. Authentication and other areas of the website
are outside the requested testing scope.

### Driver Factory

`driver_factory.py` centralizes browser creation.

Currently supported:

- Chrome
- Firefox

Chrome is the default.

## Installation

### 1. Clone the repository

    git clone <repository-url>

    cd SportGroupTestProject

### 2. Create a virtual environment

Linux/macOS:

    python3 -m venv .venv
    source .venv/bin/activate

Windows:

    python -m venv .venv
    .venv\Scripts\activate

### 3. Install dependencies

    pip install -r requirements.txt

## Configuration
    Copy example.env and create the .env file in the root

Then configure the application URL.

Example:

    BASE_URL=https://qae-assignment-tau.vercel.app/?user-id=...
    BROWSER=chrome
    HEADLESS=false
    EXPLICIT_WAIT=10
    PAGE_LOAD_TIMEOUT=30

Do not commit `.env` to source control.

## Running the Tests

Run the complete suite:

    pytest

Run smoke tests:

    pytest -m smoke

Run functional tests:

    pytest -m functional

Run a specific test file:

    pytest tests/test_upcoming_matches.py

## Headless Execution

For CI/CD environments, set:

    HEADLESS=true

Then run:

    pytest

For local debugging:

    HEADLESS=true

## Browser Selection

Chrome:

    BROWSER=chrome pytest

Firefox:

    BROWSER=firefox pytest


## External Documents

The project contains the following external document in the root:

    TestingPlan.docx

The Testing Plan should contain the functional scope, test scenarios, 
priorities and execution considerations for the application.

The automation framework and Testing Plan should be kept aligned.

## CI/CD Considerations

A typical CI command is:

    HEADLESS=true pytest --html=reports/report.html --self-contained-html

Recommended CI stages:

1. Install Python
2. Create virtual environment
3. Install dependencies
4. Start/verify browser
5. Execute smoke tests
6. Execute regression tests
7. Publish the HTML report
8. Preserve screenshots/logs if failure diagnostics are added

## Future Improvements

Potential extensions include:

- automatic screenshots on failure
- structured logging
- Allure reporting
- parallel execution with pytest-xdist
- CI pipeline integration
- test data factories
- API test layer
- environment-specific configuration
- browser matrix execution
- accessibility checks

These should only be introduced when they provide value to the
project rather than increasing framework complexity unnecessarily.
