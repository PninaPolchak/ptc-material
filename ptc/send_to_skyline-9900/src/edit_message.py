from azure_operations.azure_container import AzureContainer
from utils.connect_to_Azure import get_container
from utils.const import ColonyConfig, ContainerNames, MessageConst, NavadConst, TelemConst
from utils.connect_to_Azure import connect_to_azure
from utils.azLogger import create_logger

logger = create_logger(__name__)

def edit_message(message: dict, container: AzureContainer) -> dict:
    try:
        logger.info("Create message for send to skyline")

        flight_name = message["flightData"]["flightName"]
        flight_format = message["flightData"]["flightFormat"]
        flight_type = message["flightData"]["flightType"]
        flight_path = message["flightData"]["flightPath"]

        message["action"] = MessageConst.ACTION
        message.pop("flightData")
        message["payload"]["identifier"] = flight_name
        message["payload"]["emails"] = ColonyConfig.EMAIL
        message["payload"]["target"] = create_target(flight_path)

        if flight_format == "ALL":
            message["payload"]["type"] = "c"
            message["payload"]["source"] = create_source_for_all(
                container, flight_path)

        elif flight_type == "NAVAD":
            input_folder = get_navad_input_folder_name(container, flight_path)
            message["payload"]["type"] = which_suffix_url(
                container, flight_path, input_folder, NavadConst.IMAGE_SUFFIX)
            message["payload"]["source"] = create_source(
                input_folder, flight_path)

        elif flight_type == "TELEM":
            input_folder = get_telem_input_folder_name(container, flight_path)
            message["payload"]["type"] = which_suffix_url(
                container, flight_path, input_folder, TelemConst.IMAGE_SUFFIX)
            message["payload"]["source"] = create_source(
                input_folder, flight_path)

        logger.info(f"Message:\n {message} \n ready to send !")

    except Exception as error:
        logger.error(error)
        raise ValueError(f"Error in edit message --> {error}")


def create_target(flight_path: str) -> str:
    try:
        logger.info(f"Create target to {flight_path} ")
        create_folder_in_output_container(flight_path)
        target = get_url(ContainerNames.OUTPUT_CONTAINER, flight_path)
        return target

    except Exception as error:
        logger.error(error)
        raise ValueError(f"Failed in create target --> {error}")


def create_folder_in_output_container(flight_path: str) -> None:
    try:
        logger.info(
            f"Connect to Azure container {ContainerNames.OUTPUT_CONTAINER} ")
        container = get_container(ContainerNames.OUTPUT_CONTAINER)
        logger.info(
            f"Create folder {flight_path} in container {ContainerNames.OUTPUT_CONTAINER}")
        container.create_folder(flight_path)
    except Exception as error:
        logger.error(error)
        raise ValueError(
            f"Failed in create folder in output container --> {error}")


def get_url(container_name: str, flight_path: str) -> str:
    try:
        logger.info("Get url from Azure")
        azure = connect_to_azure()
        url = azure.get_url_container(container_name)
        return url.generate_url(flight_path)

    except Exception as error:
        logger.error(error)
        raise ValueError(f"Failed in get url of {container_name} --> {error}")


def create_source_for_all(container: AzureContainer, flight_path: str) -> list:
    try:
        logger.info("Create list of url for ALL flight")

        sub_folders = container.get_folders_from_external_folder(flight_path)
        source_list = []
        url = get_url(ContainerNames.INPUT_CONTAINER, flight_path)
        for folder in sub_folders:
            path_to_folder = f"{flight_path}/{folder}"
            input_folder = get_navad_input_folder_name(
                container, path_to_folder)
            source = f"{url}/{folder}/{input_folder}"
            source_list.append(source)
        return source_list

    except Exception as error:
        logger.error(error)
        raise ValueError(f"Failed in create source for ALL --> {error}")


def get_navad_input_folder_name(container: AzureContainer, flight_name: str) -> str:
    try:
        logger.info(f"Get correct input folder name of:{flight_name}")
        folder_list = container.get_folders_from_external_folder(flight_name)
        return [folder for folder in folder_list if folder.lower() == "input"][0]

    except Exception as error:
        logger.error(error)
        raise ValueError(f"Failed get input folder name --> {error}")


def get_telem_input_folder_name(container: AzureContainer, flight_name: str) -> str:
    try:
        logger.info(f"Get correct telem folder name of:{flight_name}")
        folders = container.get_folders_ending_with(
            flight_name, TelemConst.JPG)
        return folders[0].split(TelemConst.JPG)[0]

    except Exception as error:
        logger.error(error)
        raise ValueError(f"Failed get telem folder name --> {error}")


def which_suffix_url(container: AzureContainer, flight_path: str, input_folder: str, suffix_file: str) -> str:
    try:
        logger.info("Count images")
        images = container.get_files_by_suffix_from_folder(
            f"{flight_path}/{input_folder}", suffix_file)

        return "c" if len(images) >= 3000 else "a"

    except Exception as error:
        logger.error(error)
        raise ValueError(f"Failed in which suffix url --> {error}")


def create_source(input_folder: str, flight_path: str):
    try:
        logger.info(f"Create url to folder: {flight_path}")
        url = get_url(ContainerNames.INPUT_CONTAINER, flight_path)
        source = f"{url}/{input_folder}"
        logger.info(f"Finish create url to folder: {flight_path}")
        return source

    except Exception as error:
        logger.error(error)
        raise ValueError(f"Failed in create source --> {error}")
