import pytest


@pytest.fixture
def project_incorrect():
    return {
        "name": "incorrect-project",
        "packages": [
            {"name": "12312312312312312"},
            {"name": "Django", "version": "2.2.24"},
            {"name": "psycopg2-binary", "version": "2.9.1"}
        ]
    }

@pytest.fixture
def project_correct():
    return {
        "name": "Zeus",
        "packages": [
            {"name": "Django", "version": "2.2.24"},
            {"name": "psycopg2-binary", "version": "2.9.1"}
        ]
    }