from .option import Option


class Numeric(Option):
    required: bool
    label: str
    description: str

    def __init__(self, required: bool, label: str, description: str):
        self.required = required
        self.label = label
        self.description = description

    def to_dict(self):
        return {
            'type': 'numeric',
            'required': self.required,
            'label': self.label,
            'description': self.description,
        }
