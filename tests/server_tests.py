import pytest
from app import app
import asyncio


pytest_plugins = ('pytest_asyncio',)


@pytest.fixture
def client():
    # Тестовий клієнт Flask-додатка
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_home_page(client):
    """Тест для домашньої сторінки."""
    response = client.get('/')
    assert response.status_code == 200
    assert "Система контролю вентиляцією" in response.get_data(as_text=True)


def test_api_generate(client):
    """Тест для ендпоінта /api/generate."""
    response = client.get('/api/generate')
    assert response.status_code == 200
    data = response.get_json()
    assert "temperature" in data
    assert "humidity" in data
    assert "pollution" in data
    assert isinstance(data["temperature"], (int, float))
    assert isinstance(data["humidity"], (int, float))
    assert isinstance(data["pollution"], (int, float))


def test_api_get_data(client):
    """Тест для ендпоінта /api/get_data."""
    response = client.get('/api/get_data')
    assert response.status_code == 200
    data = response.get_json()
    assert "temperature" in data
    assert "humidity" in data
    assert "pollution" in data
    assert isinstance(data["temperature"], (int, float))
    assert isinstance(data["humidity"], (int, float))
    assert isinstance(data["pollution"], (int, float))
