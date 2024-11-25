import pytest

from src.services.driver import GwinstekDriverService


@pytest.mark.unit
@pytest.mark.anyio
async def test_correct_commands_used(driver_service: GwinstekDriverService, mock_command_data: dict[str, float| int]):
    """Тест на проверку ответов прибора"""
    await driver_service.enable_channel(**mock_command_data)
    response = await driver_service.get_telemetry()
    target_measure = response[mock_command_data["channel"]-1]
    assert target_measure.get("voltage") == mock_command_data["voltage"]
    assert target_measure.get("channel") == mock_command_data["channel"]
    assert target_measure.get("current") == mock_command_data["current"]
    await driver_service.disable_channel(mock_command_data["channel"])




