from .option_type.decimal import Decimal
from .option_type.enum import Enum
from .option_type.numeric import Numeric
from .option_type.text import Text


class Options:
    '''This class is a facade over options.'''
    _options: dict = {}

    def __init__(self):
        self._options = {}

    def add_enum_option(self, required: bool, name: str, label: str, description: str, options: dict):
        self._options[name] = Enum(required, label, description, options)

    def add_decimal_option(self, required: bool, name: str, label: str, description: str):
        self._options[name] = Decimal(required, label, description)

    def add_text_option(self, required: bool, name: str, label: str, description: str):
        self._options[name] = Text(required, label, description)

    def add_numeric_option(self, required: bool, name: str, label: str, description: str):
        self._options[name] = Numeric(required, label, description)

    def to_dict(self) -> dict:
        return {key: option.to_dict() for key, option in self._options.items()}
