from edit_message import edit_message
from utils.const import ColonyConfig
from send_message import send_message
from utils.connect_to_Azure import get_container
import copy
from utils.azLogger import create_logger

logger = create_logger(__name__)


def send_to_skyline(message: dict) -> None:
    try:
        container_name = message["payload"]["container"]
        flight_name = message["flightData"]["flightName"]

        logger.info(f"Start process send to skyline flight {flight_name}")

        error_message = copy.deepcopy(message)
        container = get_container(container_name)
        edit_message(message, container)
        send_message(message)

    except Exception as error:
        logger.error(f"Failed in main function: send to skyline --> {error}")
        send_error(error_message, error)


def send_error(error_message: dict, error: str) -> None:
    update_message_for_error(error_message, error)
    send_message(error_message)


def update_message_for_error(error_message: dict, error: str) -> dict:
    flight_name = error_message["flightData"]["flightName"]
    error_message["action"] = "VerifyError"
    error_message["payload"]["errorDescription"] = f"{flight_name}: send_to_skyline - {error} "
    error_message["payload"]["mailTo"] = ColonyConfig.EMAIL
    error_message.pop("flightData")
    return error_message
