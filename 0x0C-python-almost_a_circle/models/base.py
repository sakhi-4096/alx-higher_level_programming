#!/usr/bin/python3

import json
import csv


class Base:
    """
    Base class for models.

    Attributes:
        __nb_objects (int): Private class attribute to keep track of
                            object IDs.

    Methods:
        __init__(self, id=None): Initialize a Base instance.
        to_json_string(list_dictionaries): Convert a list of dictionaries
                                           to a JSON string.
        from_json_string(json_string): Convert a JSON string to a list
                                       of dictionaries.
        save_to_file(cls, list_objs): Save a list of objects to a JSON file.
        load_from_file(cls): Load a list of objects from a JSON file.
        save_to_file_csv(cls, list_objs): Save a list of objects to a CSV file.
        load_from_file_csv(cls): Load a list of objects from a CSV file.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a Base instance.

        Args:
            id (int, optional): ID of the instance. If not provided,
            it will be automatically assigned based on the number of
            existing objects.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries to a JSON string.

        Args:
            list_dictionaries (list): A list of dictionaries representing
                                      object attributes.

        Returns:
            str: A JSON string representation of the list of dictionaries.
        """
        return json.dumps(list_dictionaries or [])

    @staticmethod
    def from_json_string(json_string):
        """
        Convert a JSON string to a list of dictionaries.

        Args:
            json_string (str): A JSON string.

        Returns:
            list: A list of dictionaries containing object attributes.
        """
        return json.loads(json_string) if json_string else []

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save a list of objects to a JSON file.

        Args:
            list_objs (list): A list of object instances to be saved.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            json_data = [obj.to_dictionary()
                         for obj in list_objs] if list_objs else []
            file.write(cls.to_json_string(json_data))

    @classmethod
    def load_from_file(cls):
        """
        Load a list of objects from a JSON file.

        Returns:
            list: A list of object instances.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_data = cls.from_json_string(file.read())
            return [cls.create(**data) for data in json_data]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Save a list of objects to a CSV file.

        Args:
            list_objs (list): A list of object instances to be saved.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for obj in list_objs:
                if isinstance(obj, Rectangle):
                    writer.writerow(
                        [obj.id, obj.width, obj.height, obj.x, obj.y])
                elif isinstance(obj, Square):
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """
        Load a list of objects from a CSV file.

        Returns:
            list: A list of object instances.
        """
        filename = cls.__name__ + ".csv"
        objs = []
        with open(filename, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                data = {
                    "id": int(row[0]),
                    "width": int(row[1]),
                    "height": int(row[2]),
                    "x": int(row[3]),
                    "y": int(row[4]),
                } if cls.__name__ == "Rectangle" else {
                    "id": int(row[0]),
                    "size": int(row[1]),
                    "x": int(row[2]),
                    "y": int(row[3]),
                }
                objs.append(cls.create(**data))
        return objs

    @classmethod
    def create(cls, **dictionary):
        """
        Return an instance with all attributes set.

        Args:
            **dictionary: Double pointer to a dictionary representing the
                          attributes of the instance.
        Returns:
            instance: An instance with all attributes set based on the
                      provided dictionary.
        """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            raise ValueError("Invalid class name")

        dummy_instance.update(**dictionary)
        return dummy_instance
