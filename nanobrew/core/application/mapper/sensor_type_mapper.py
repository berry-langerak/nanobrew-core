from ...domain.sensor_type import SensorType


class SensorTypeMapper:
    def sensor_type_to_dict(self, sensor_type: SensorType):
        return sensor_type.to_dict()
