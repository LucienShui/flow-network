from __future__ import absolute_import, print_function
import ctypes


def c_type_transfer(data: [int, float, list]) -> [ctypes.c_int, ctypes.c_double]:
    """
    将 Python 类型转换为 C++ 可接受的类型
    :param data: Python 数据实体
    :return: C++ 数据实体
    """
    ctypes_dict = {
        int: ctypes.c_int,
        float: ctypes.c_double
    }

    data_type = type(data)

    if data_type in ctypes_dict:
        return ctypes_dict[data_type](data)

    if data_type is list:
        element_type = type(data[0])
        if element_type is not list:
            length: int = len(data)

            result = (ctypes_dict[element_type] * length)()

            for i in range(length):
                result[i] = c_type_transfer(data[i])

            return result

    raise RuntimeError('Unsupported type')
