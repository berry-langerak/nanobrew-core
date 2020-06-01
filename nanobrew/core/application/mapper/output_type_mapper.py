from ...domain.output_type import OutputType


class OutputTypeMapper:
    def output_type_to_dict(self, output_type: OutputType):
        return output_type.to_dict()
