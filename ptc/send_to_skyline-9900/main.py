from utils.rabbitmq_actions import RabbitmqActions
from send_to_skyline import send_to_skyline
from utils.const import QueueNames


def main():
    rabbitmq = RabbitmqActions()
    rabbitmq.consume(send_to_skyline, QueueNames.SEND_TO_SKYLINE_QUEUE)


if __name__ == "__main__":
    main()
