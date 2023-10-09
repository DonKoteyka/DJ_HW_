import pytest
from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Course


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def one_course():
    return Course.objects.create(name='Pytest course')


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory


@pytest.mark.django_db
# def test_get_first_course(client):
#     Course.objects.create(name = 'Pytest course')
#     response = client.get('/api/v1/courses/')
#     assert response.status_code == 200
def test_get_one_course(client, course_factory):
    course = course_factory(_quantity=1)
    response = client.get('/api/v1/courses/')
    data = response.json()
    assert response.status_code == 200
    for index, c in enumerate(data):
        assert c['name'] == course[index].name


def test_get_all_courses(client, course_factory):
    courses = course_factory(_quantity=3)
    response = client.get('/api/v1/courses/')
    data = response.json()
    assert response.status_code == 200
    for index, c in enumerate(data):
        assert c['name'] == courses[index].name
# def test_example():
#     assert True, "Just test example"
