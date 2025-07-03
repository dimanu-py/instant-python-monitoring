import random


class CommandPrimitivesMother:
    _AVAILABLE_COMMANDS = ["init", "config"]

    @classmethod
    def any(cls) -> str:
        return random.choice(cls._AVAILABLE_COMMANDS)
