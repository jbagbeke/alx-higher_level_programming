#!/usr/bin/python3
"""
A class module that wil be the base of other classes
"""
import json


class Base:
    """
    Base class of other classes in this project
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialises id of a class if not None

        Args:
            Arg1: (id) An int representing the id of the instance/object
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries
        """

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return str([])

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file
        """

        filename = cls.__name__ + '.json'
        with open(filename, "w", encoding="UTF-8") as file:
            if list_objs is None:
                json.dump("[]", file)
            elif list_objs is not None:
                my_list = []
                for obj in list_objs:
                    tmp_obj = obj.to_dictionary()
                    my_list.append(tmp_obj)
                json.dump(Base.to_json_string(my_list), file)
