import logging

from injector import inject, singleton
from starlette.config import Config

LOGGER = logging.getLogger(__name__)


@singleton
@inject
class ApplicationConfig:

    def __init__(self, config: Config) -> None:
        self.master_database_url: str = config('MASTER_DATABASE_URL',
                                               cast=str,
                                               default='mysql+mysqlconnector://ubuntu:qwerty@123@localhost:3306/tracking')
        self.replica_database_url: str = config('REPLICA_DATABASE_URL',
                                                cast=str,
                                                default='mysql+mysqlconnector://ubuntu:qwerty@123@localhost:3306/tracking')

        self.code_generator_characters: str = config('CODE_GENERATOR_CHARACTERS',
                                                     cast=str,
                                                     default='ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')

        self.code_generator_min_length: str = config('CODE_GENERATOR_MIN_LENGTH',
                                                     cast=int,
                                                     default=6)

        self.code_generator_code_prefix: str = config('CODE_GENERATOR_CODE_PREFIX',
                                                      cast=str,
                                                      default='R')

        LOGGER.debug("Application Configuration Initialized")
