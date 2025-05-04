import typing
import logging

T = typing.TypeVar("T")
K = typing.TypeVar("K")


class Result(typing.NamedTuple, typing.Generic[T, K]):
    value: T
    error: K


class MyLogger:
    logger_instances: dict[str, logging.Logger] = {}

    @classmethod
    def get_logger(cls, name: str) -> logging.Logger:
        if cls.logger_instances.get(name):
            return cls.logger_instances[name]

        formater = logging.Formatter(
            "[%(asctime)s - %(name)s - line %(lineno)s]: "
            + "%(levelname)s - %(message)s"
        )

        handler = logging.StreamHandler()
        handler.setFormatter(formater)
        handler.setLevel(logging.INFO)

        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)
        logger.addHandler(handler)

        cls.logger_instances[name] = logger

        return logger
