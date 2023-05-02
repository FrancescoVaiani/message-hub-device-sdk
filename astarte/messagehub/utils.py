from typing import Any
from astarteplatform.msghub import astarte_type_pb2 as astarte_type


# pylint: disable=no-member
def __value_to_astarte_type(
    data_value: Any, target_type: str
) -> astarte_type.AstarteDataTypeIndividual or None:
    """
    Function that translates from python types to astarte types.

    Parameters
    ----------
    data_value: Any
        Value to translate
    target_type: str
        Target astarte type

    Returns
    -------
    AstarteDataTypeIndividual or None
        The translated Value.
    """
    ret = None
    if target_type == "integer":
        ret = astarte_type.AstarteDataTypeIndividual(astarte_integer=data_value)
    elif target_type == "longinteger":
        ret = astarte_type.AstarteDataTypeIndividual(astarte_long_integer=data_value)
    elif target_type == "double":
        ret = astarte_type.AstarteDataTypeIndividual(astarte_double=data_value)
    elif target_type == "string":
        ret = astarte_type.AstarteDataTypeIndividual(astarte_string=data_value)
    elif target_type == "binaryblob":
        ret = astarte_type.AstarteDataTypeIndividual(astarte_binary_blob=data_value)
    elif target_type == "boolean":
        ret = astarte_type.AstarteDataTypeIndividual(astarte_boolean=data_value)
    elif target_type == "datetime":
        ret = astarte_type.AstarteDataTypeIndividual(astarte_date_time=data_value)
    elif target_type == "integerarray":
        ret = astarte_type.AstarteDataTypeIndividual(astarte_integer_array=data_value)
    elif target_type == "longintegerarray":
        ret = astarte_type.AstarteDataTypeIndividual(astarte_long_integer_array=data_value)
    elif target_type == "doublearray":
        ret = astarte_type.AstarteDataTypeIndividual(astarte_double_array=data_value)
    elif target_type == "stringarray":
        ret = astarte_type.AstarteDataTypeIndividual(astarte_string_array=data_value)
    elif target_type == "binaryblobarray":
        ret = astarte_type.AstarteDataTypeIndividual(astarte_binary_blob_array=data_value)
    elif target_type == "booleanarray":
        ret = astarte_type.AstarteDataTypeIndividual(astarte_boolean_array=data_value)
    elif target_type == "datetimearray":
        ret = astarte_type.AstarteDataTypeIndividual(astarte_date_time_array=data_value)
    return ret


# pylint: enable=no-member
