import requests
import pytest
from rest_framework.reverse import reverse_lazy
from rest_framework.test import APIClient



def test_get_projects(transactional_db):
    client = APIClient()
    response = client.get(path='/api/projects/', format='json')

    assert response.status_code == 200


def test_create_project_with_error_on_package_name(transactional_db,project_incorrect):
    client = APIClient()
    response = client.post(path='/api/projects/', json=project_incorrect,format='json')

    assert response.status_code == 400

def test_create_project_succesfull(transactional_db,project_correct):
    client = APIClient()
    response = client.post(path='/api/projects/', data=project_correct,format='json')
    assert response.status_code == 201