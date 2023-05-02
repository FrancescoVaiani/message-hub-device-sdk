from __future__ import annotations

import json
from pathlib import Path

from astarte.messagehub.interface import Interface


class Introspection:
    """
    Class that represent the introspection of a device.

    The introspection is the list od interfaces that the device declares to the server it is
    compatible with.

    In any given time a device can have a single interface with a given name, multiple interfaces
    with the same name but different major/minor are not supported.
    """

    def __init__(self):
        self.__interfaces_list: dict[str, Interface] = {}
        self.__interface_bytearray_list: list[bytes] = []

    def add_interface(self, interface_path: Path) -> None:
        """
        Adds an Interface to the Introspection.

        This will add an Interface definition to the Device. It has to be called before
        :py:func:`connect`, as it will be used for building the Device Introspection.

        Parameters
        ----------
        interface_path : Path
            Path to an Astarte Interface definition in the form of a Python dictionary. Usually
            obtained by using json.loads() on an Interface file.
        """
        with open(interface_path, "r", encoding="utf-8") as interface_fp:
            interface_raw = interface_fp.read()
            interface_dict: dict = json.loads(interface_raw)
            interface = Interface(interface_dict)
            self.__interfaces_list[interface.name] = interface
            self.__interface_bytearray_list.append(bytes(interface_raw))

    def get_interface(self, interface_name: str) -> Interface | None:
        """
        Retrieve an Interface definition from the Introspection

        Parameters
        ----------
        interface_name : str
            The name of an Interface previously added with :py:func:`add_interface`.

        Returns
        -------
        Interface or None
            the Interface definition if found in the Introspection, None otherwise.
        """
        if interface_name in self.__interfaces_list:
            return self.__interfaces_list[interface_name]

        return None

    def get_raw(self) -> list[bytes]:
        """
        Retrieve the content of the .json interface files as a list of bytearrays.

        Returns
        -------
        list
            The content of the .json interface files as raw bytes. One file per element.
        """
        return self.__interface_bytearray_list
