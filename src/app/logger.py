import logging

import colorlog

colored_handler = logging.StreamHandler()
colored_handler.setFormatter(
    colorlog.ColoredFormatter(
        fmt="%(asctime)s - %(purple)s%(name)s%(reset)s - %(log_color)s%(levelname)s%(reset)s - %(message)s",
    ),
)


def init_logging(log_level: int | str = logging.INFO,
                 handler: logging.Handler = colored_handler,
                 custom_loggers: list[str] | None = None) -> None:
    """Инициализация формата логирования.

    Args:
        log_level (int | str, optional): Уровень логирования. По умолчанию logging.INFO.
        handler (logging.Handler, optional): Хендлер для логирования. По умолчанию colored_handler.
        custom_loggers (list[str] | None, optional): Список логгеров, которые самостоятельно устанавливают формат.
            У них будет обновлен handler и log_level, чтобы логи соответствовали единому стилю.
    """
    logging.basicConfig(level=log_level, handlers=[handler])

    if custom_loggers is None:
        custom_loggers = []

    loggers = [
        *logging.root.manager.loggerDict.keys(),
        *custom_loggers,
    ]
    for logger_name in loggers:
        logger = logging.getLogger(logger_name)
        logger.handlers.clear()
        logger.addHandler(handler)
        logger.propagate = False
        logger.setLevel(log_level)