from pathlib import Path
from sys import argv

from src.core.constants import MIN_ARGS_LEN
from src.core.enums.args import ArgsEnum
from src.observers.manager import ObserverManager
from src.utils import MyLogger


def main():
    logger = MyLogger.get_logger(__name__)

    args = argv[1:]

    if len(args) < MIN_ARGS_LEN:
        logger.error(f"Args is less than {MIN_ARGS_LEN}")

        return

    manager = ObserverManager()

    command_arg = args[ArgsEnum.COMMAND_INDEX.value]
    path_arg = args[ArgsEnum.PATH_INDEX.value]
    path = Path(path_arg)

    observer_result = manager.create_observer(path, command_arg)

    if observer_result.error:
        logger.error(observer_result.error)

        return

    assert observer_result.value is not None

    observer = observer_result.value

    observer.start()

    try:
        while observer.is_alive():
            observer.join(1)

    finally:
        observer.stop()
        observer.join()


if __name__ == "__main__":
    main()
