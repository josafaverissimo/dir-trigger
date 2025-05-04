import typing
from pathlib import Path

from watchdog.events import FileSystemEvent, FileSystemEventHandler


class MyEventHandler(FileSystemEventHandler):
    @typing.override
    def on_created(self, event: FileSystemEvent):
        print(event)
