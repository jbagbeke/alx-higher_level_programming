#!/usr/bin/python3
"""
A class module that wil be the base of other classes
"""
import json
import os


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
                file.write("[]")
            elif list_objs is not None:
                my_list = []
                for obj in list_objs:
                    tmp_obj = obj.to_dictionary()
                    my_list.append(tmp_obj)
                file.write(Base.to_json_string(my_list))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation json_string
        """

        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set
        """

        if dictionary is not None and len(dictionary) != 0:
            if cls.__name__ == 'Square':
                rect = cls(2)
            else:
                rect = cls(2, 5)
            rect.update(**dictionary)
            return rect

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances
        """

        filepath = cls.__name__ + ".json"

        if not os.path.isfile(filepath):
            return []
        else:
            if len(filepath) == 0:
                return []

            with fopen(filepath, "r", encoding="UTF-8") as file:
                file_read = file.read()
                read_list = Base.from_json_string(file_read)
                instances = Base.create(read_list)
            return read_list
