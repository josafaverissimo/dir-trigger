import typing
from pathlib import Path

from watchdog.observers import Observer
from watchdog.observers.api import BaseObserver

from src.utils import Result, MyLogger
from src.observers.handlers import MyEventHandler


logger = MyLogger.get_logger(__name__)


class ObserverManager:
    @staticmethod
    def create_observer(
        path: Path,
        shell_command: str,
        /,
        recursive: bool = False,
    ) -> Result[BaseObserver | None, str | None]:
        path = path.expanduser()

        if not path.exists():
            return Result(None, f"Path: {str(path)} does not exist")

        path_str = str(path.expanduser().resolve(strict=True))

        handler = MyEventHandler()
        observer = Observer()
        observer.schedule(handler, path_str, recursive=recursive)

        logger.info(f"Watching path: {path_str}")

        return Result(typing.cast(BaseObserver, observer), None)
