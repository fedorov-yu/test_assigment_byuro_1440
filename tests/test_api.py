

from http import HTTPStatus

import pytest
from fastapi.testclient import TestClient


@pytest.mark.usefixtures("mock_driver")
@pytest.mark.e2e
def test_ping(client: TestClient):
    """Тест пинга"""
    response = client.get(url="/service/ping")
    assert response.status_code == HTTPStatus.OK

@pytest.mark.usefixtures("mock_driver")
@pytest.mark.e2e
def test_enable(client: TestClient):
    """Тест включения драйвера"""
    response = client.post(
        url="/driver/turnOn",
        json={
            "channel": 1,
            "current": 1.0,
            "voltage": 1.0,
            })
    assert response.status_code == HTTPStatus.OK

@pytest.mark.usefixtures("mock_driver")
@pytest.mark.e2e
def test_disable(client: TestClient):
    """Тест выключения драйвера"""
    response = client.post(
        url="/driver/turnOff",
        json={
            "channel": 1,
            })
    assert response.status_code == HTTPStatus.OK

@pytest.mark.usefixtures("mock_driver")
@pytest.mark.e2e
def test_telemetry(client: TestClient):
    """Тест измерений"""
    response = client.get(url="/driver/healthCheck")
    res_json = response.json()
    assert isinstance(res_json, list)
    for i in res_json:
        assert i.get("channel")
        assert i.get("current")
        assert i.get("voltage")
        assert i.get("measured_dt")
