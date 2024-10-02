# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Order(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: int=None, pet_id: int=None, quantity: int=None, ship_date: datetime=None, status: str=None, complete: bool=None):  # noqa: E501
        """Order - a model defined in Swagger

        :param id: The id of this Order.  # noqa: E501
        :type id: int
        :param pet_id: The pet_id of this Order.  # noqa: E501
        :type pet_id: int
        :param quantity: The quantity of this Order.  # noqa: E501
        :type quantity: int
        :param ship_date: The ship_date of this Order.  # noqa: E501
        :type ship_date: datetime
        :param status: The status of this Order.  # noqa: E501
        :type status: str
        :param complete: The complete of this Order.  # noqa: E501
        :type complete: bool
        """
        self.swagger_types = {
            'id': int,
            'pet_id': int,
            'quantity': int,
            'ship_date': datetime,
            'status': str,
            'complete': bool
        }

        self.attribute_map = {
            'id': 'id',
            'pet_id': 'petId',
            'quantity': 'quantity',
            'ship_date': 'shipDate',
            'status': 'status',
            'complete': 'complete'
        }

        self._id = id
        self._pet_id = pet_id
        self._quantity = quantity
        self._ship_date = ship_date
        self._status = status
        self._complete = complete

    @classmethod
    def from_dict(cls, dikt) -> 'Order':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Order of this Order.  # noqa: E501
        :rtype: Order
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this Order.


        :return: The id of this Order.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this Order.


        :param id: The id of this Order.
        :type id: int
        """

        self._id = id

    @property
    def pet_id(self) -> int:
        """Gets the pet_id of this Order.


        :return: The pet_id of this Order.
        :rtype: int
        """
        return self._pet_id

    @pet_id.setter
    def pet_id(self, pet_id: int):
        """Sets the pet_id of this Order.


        :param pet_id: The pet_id of this Order.
        :type pet_id: int
        """

        self._pet_id = pet_id

    @property
    def quantity(self) -> int:
        """Gets the quantity of this Order.


        :return: The quantity of this Order.
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity: int):
        """Sets the quantity of this Order.


        :param quantity: The quantity of this Order.
        :type quantity: int
        """

        self._quantity = quantity

    @property
    def ship_date(self) -> datetime:
        """Gets the ship_date of this Order.


        :return: The ship_date of this Order.
        :rtype: datetime
        """
        return self._ship_date

    @ship_date.setter
    def ship_date(self, ship_date: datetime):
        """Sets the ship_date of this Order.


        :param ship_date: The ship_date of this Order.
        :type ship_date: datetime
        """

        self._ship_date = ship_date

    @property
    def status(self) -> str:
        """Gets the status of this Order.

        Order Status  # noqa: E501

        :return: The status of this Order.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status: str):
        """Sets the status of this Order.

        Order Status  # noqa: E501

        :param status: The status of this Order.
        :type status: str
        """
        allowed_values = ["placed", "approved", "delivered"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def complete(self) -> bool:
        """Gets the complete of this Order.


        :return: The complete of this Order.
        :rtype: bool
        """
        return self._complete

    @complete.setter
    def complete(self, complete: bool):
        """Sets the complete of this Order.


        :param complete: The complete of this Order.
        :type complete: bool
        """

        self._complete = complete
