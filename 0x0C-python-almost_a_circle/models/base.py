#!/usr/bin/python3
"""
A class module that wil be the base of other classes
"""
import json
import os
import csv


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
            with open(filepath, "r", encoding="UTF-8") as file:
                file_read = file.read()
                read_list = Base.from_json_string(file_read)

                file_dict = []
                for att in read_list:
                    rect = cls.create(**att)
                    file_dict.append(rect)
                return (file_dict)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serializes objects using COMMA SEPARATED VALUES(CSV)
        """

        filename = cls.__name__ + ".csv"

        if cls.__name__ == "Rectangle":
            header = ["id", "width", "height", "x", "y"]
        elif cls.__name__ == "Square":
            header = ["id", "size", "x", "y"]

        with open(filename, mode="w", newline="") as file:
            csv_file = csv.DictWriter(file, fieldnames=header)
            for row in list_objs:
                csv_file.writerow(row.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        deserializes objects from files with COMMA SEPARATED VALUES(CSV)
        """

        filename = cls.__name__ + ".csv"

        if not os.path.isfile(filename):
            return []

        list_objs = []
        if cls.__name__ == "Rectangle":
            header = ["id", "width", "height", "x", "y"]
        elif cls.__name__ == "Square":
            header = ["id", "size", "x", "y"]

        with open(filename, mode="r") as file:
            csv_file = csv.DictReader(file, fieldnames=header)
            for row in csv_file:
                list_objs.append(cls.create(**row))
        return list_objs
