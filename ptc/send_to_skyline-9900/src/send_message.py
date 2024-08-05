from utils.rabbitmq_actions import RabbitmqActions
from utils.const import QueueNames
from utils.azLogger import create_logger

logger = create_logger(__name__)

def send_message(edit_message:dict) -> None:
    try:
        logger.info(f"Send message {edit_message} to {QueueNames.COLONY_QUEUE}")
        rabbitmq = RabbitmqActions()
        rabbitmq.publish_to_colony(edit_message)

    except Exception as error:
        logger.error(f"Failed in send message --> {error}")
        raise ValueError(error)
