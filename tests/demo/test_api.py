import pytest
from rest_framework.test import APIClient

from django.contrib.auth.models import User
from demo.models import Message

from model_bakery import baker


@pytest.fixture
def message_factory():
    def factory(*args, **kwargs):
        return baker.make(Message, *args, **kwargs)
    
    return factory


@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def user():
    return User.objects.create_user('admin')


@pytest.mark.django_db
def test_get_message(client, user, message_factory):
    # Arrange
    messages = message_factory(_quantity= 10)

    # Act
    response = client.get('/messages/')

    # Assert
    assert response.status_code == 200
    data = response.json()
    for i, m in enumerate(data) :
        assert m['text'] == messages[i].text


    assert len(data) == len(messages)


@pytest.mark.django_db
def test_create_message(client, user):
    count = Message.objects.count()
    response = client.post('/messages/', data={'user': user.id, 'text': 'test text'})

    assert response.status_code == 201
    assert Message.objects.count() == count + 1