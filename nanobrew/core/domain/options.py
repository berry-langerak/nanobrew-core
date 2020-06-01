from .option import Option
from .option_type.decimal import Decimal
from .option_type.enum import Enum
from .option_type.numeric import Numeric
from .option_type.text import Text


class Options:
    _options: dict = {}

    def __init__(self, options: dict):
        self._options = options

    @classmethod
    def from_dict(cls, options_dict: dict):
        option_types = {
            'decimal': Decimal,
            'enum': Enum,
            'text': Text,
            'numeric': Numeric,
        }

        options = {}
        for (key, option) in options_dict.items():
            options[key] = option_types[option['type']].from_dict(option)

        return Options(options)

    def validate(self, parameters: dict) -> (bool, dict):
        option_errors = {}
        for (key, option) in self._options.items():
            value = parameters[key] if key in parameters else None

            (success, errors) = option.validate(value)
            if success is False:
                option_errors[key] = errors

        return (len(option_errors) == 0, option_errors)

    def filter(self, parameters: dict) -> dict:
        return {key: parameters[key] for key in self._options.keys()}

    def to_dict(self) -> dict:
        return {key: option.to_dict() for key, option in self._options.items()}
