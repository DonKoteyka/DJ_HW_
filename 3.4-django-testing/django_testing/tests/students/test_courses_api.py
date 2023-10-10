import pytest
import random
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
def test_get_one_course(client, course_factory):
    course = course_factory(_quantity=1)
    response = client.get('/api/v1/courses/')
    data = response.json()
    assert response.status_code == 200
    assert data[0]['name'] == course[0].name


@pytest.mark.django_db
def test_get_all_courses(client, course_factory):
    courses = course_factory(_quantity=3)
    response = client.get('/api/v1/courses/')
    data = response.json()
    assert response.status_code == 200
    for index, c in enumerate(data):
        assert c['name'] == courses[index].name


@pytest.mark.django_db
def test_filter_id(client, course_factory):
    max_id = 100
    random_number = random.randint(50, max_id)
    courses = course_factory(_quantity=max_id)
    response = client.get(f'/api/v1/courses/?id={random_number}')
    data = response.json()[0]
    assert response.status_code == 200
    assert data['id'] == courses[random_number - 5].id
    # assert data['id'] == courses[random_number - 1].id

@pytest.mark.django_db
def test_filter_name(client, course_factory):
    max_id = 20
    random_number = random.randint(5, max_id)
    courses = course_factory(_quantity=max_id)
    random_name = courses[random_number - 1].name
    response = client.get(f'/api/v1/courses/?name={random_name}')
    data = response.json()[0]
    assert response.status_code == 200
    assert data['name'] == courses[random_number - 1].name

@pytest.mark.django_db
def test_create_course(client, one_course):
    pre_course_count = Course.objects.count()
    response = client.post('/api/v1/courses/', data={'name': 'Python for beginners'})
    course_count = Course.objects.count()
    assert response.status_code == 201
    assert pre_course_count+1 == course_count
