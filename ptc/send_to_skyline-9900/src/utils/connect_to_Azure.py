from azure_operations.azure_connection import AzureConnection, AzureContainer
from utils.const import AzureConfig
from utils.azLogger import create_logger

logger = create_logger(__name__)


def get_container(container_name: str) -> AzureContainer:
    try:
        azure_connection = connect_to_azure()
        container = azure_connection.get_azure_container(container_name)
        logger.info(f"Success connect to container {container_name}")
        return container

    except Exception as error:
        logger.error(error)
        raise ValueError(f"Failed connect to container {container_name} - {error}")


def connect_to_azure() -> AzureConnection:
    try:
        azure_connection = AzureConnection(AzureConfig.CONNECTION_STRING)
        logger.info("Success connect to Azure")
        return azure_connection

    except Exception as error:
        logger.error(error)
        raise ValueError(f"Failed connect to azure - {error}")
