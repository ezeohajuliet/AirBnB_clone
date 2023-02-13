#!/usr/bin/python3
"""Entry point of the command interpreter for the AirBnb clone"""

import cmd
from models import storage


class HBNBCommand(cmd.Cmd):
    """Defines the HBNB command line interpreter
    This class inherits from cmd's ``Cmd`` class
    Attributes:
        prompt (str): the prefix prompt
            to be displayed during cmdloop's runtime
    """

    prompt = "(hbnb) "
    # intro = "--Welcome to hbnb!--\nEnter \"help\" or \"?\" to get started."

    __valid_classes = ["BaseModel", "User", "Place", "State", "City",
                       "Amenity", "Review"]

    __valid_commands = {"create": "create", "count": "count",
                        "all": "all", "show": "show",
                        "destroy": "destroy", "update": "update"}

    __no_args_cmds = {"create()": "create", "all()": "all", "count()": "count"}

    def do_EOF(self, line):
        """End Of File"""
        return True

    def do_quit(self, line):
        """Exits the program"""
        return True

    def emptyline(self):
        """Does nothing when an empty line + ENTER is passed"""
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file), and prints the id
        """

        if not line:
            print("** class name missing **")
        elif line not in HBNBCommand.__valid_classes:
            # print(line, type(line))
            print("** class doesn't exist **")
        else:
            new_obj = storage.classes[line]()
            new_obj.save()
            print(new_obj.id)

    def help_create(self):
        """Prints the usage of the show method"""

        print("syntax: create <class name> or <class name.create>")
        print("Creates a new instance of BaseModel,",
              "saves it (to the JSON file), and prints the id")

    def do_show(self, line):
        """Prints the string representation of
        an instance based on the class name and id
        """

        if not line:
            print("** class name missing **")
            return

        args = line.split(" ")
        if args[0] not in HBNBCommand.__valid_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        for key, value in storage.all().items():
            if args[1] == value.id:
                if args[0] == key.split(".")[0]:
                    print(str(value))
                    return
        print("** no instance found **")

    def help_show(self):
        """Prints the usage of the show method"""

        print("syntax: show <class name> <id> or <class name>.show(<id>)")
        print("Prints the string representation of",
              "an instance based on the class name and id")

    def do_destroy(self, line):
        """Deletes an instance based on the class name
        and id (save the change into the JSON file)
        """

        if not line:
            print("** class name missing **")
            return

        args = line.split(" ")
        if args[0] not in HBNBCommand.__valid_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        dict_repr = storage.all()
        for key, value in dict_repr.items():
            if args[0] == key.split(".")[0]:
                if args[1] == value.id:
                    del dict_repr[key]
                    storage.save()
                    return
        print("** no instance found **")

    def help_destroy(self):
        """Prints the usage of the destroy method"""

        print("syntax: destroy <class name> <id>",
              "or <class name>.destroy(<id>)")
        print("Deletes an instance based on the class name",
              "and id (save the change into the JSON file)")

    def do_all(self, line):
        """Prints all string representation of all instances
        based on the class name or not
        """

        args = line.split()
        if not line:
            print([str(value) for value in storage.all().values()])
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        else:
            print([str(value) for value in storage.all().values()
                  if type(value).__name__ == args[0]])

    def help_all(self):
        """Prints the usage of the all method"""
        print("syntax: all or all <class name> or <class name>.all()")
        print("Prints all string representations of all instances",
              "based on the class name or not")

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        """

        if not line:
            print("** class name missing **")
            return

        args = line.split(" ")
        if args[0] not in HBNBCommand.__valid_classes:
            print("** class doesn't exist **")
            return

        args_len = len(args)
        if args_len < 2:
            print("** instance id missing **")
            return

        found = False
        for key, value in storage.all().items():
            if args[1] == value.id:
                found = True
                dict_key = key
                break

        if not found:
            print("** no instance found **")
            return

        if args_len < 3:
            print("** attribute name missing **")
            return

        if args_len < 4:
            print(args_len)
            print("** value missing **")
            return

        obj_repr = storage.all()
        attribute = args[2]
        if args[3][0] == '"':
            value = args[3].split('"')[1]
            i = 3
            while args[i] and args[i][-1] != '"':
                value += " " + args[i]
                i += 1
                value += " " + args[i].split('"')[0]
        else:
            value = args[3]

        obj = obj_repr[dict_key]
        try:
            obj_attr = getattr(obj, attribute)
        except AttributeError:
            obj_attr = attribute  # we don't reject any attributes
            # print("*** {} has not attribute {} ***".format(
            #     obj.__class__.__name__, attribute))
            # return
            #

        dict_of_types = {"str": str, "int": int, "float": float}
        obj_attr_type = type(obj_attr).__name__
        try:
            value = dict_of_types[obj_attr_type](value)
        except (KeyError, ValueError):
            print("*** type of {} not supported ***".format(obj_attr))
            return

        # value = eval(obj_attr_type(value))
        setattr(obj, attribute, value)
        obj.save()

    def help_update(self):
        """prints the usage of the update method"""

        print("syntax: update <class name> <id>",
              "<attribute name> \"<attribute value>\" or",
              "<class name>.update(<id>, <attribute name>, <attribute value>)")
        print("Updates an instance based on the class name and id by adding",
              "or updating attribute (save the change into the JSON file).",
              'Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"')

    def do_count(self, line):
        """Retrieves the number of instances of a class"""
        count = 0
        for key in storage.all():
            if key.split(".")[0] == line:
                count += 1
        print(count)

    def help_count(self):
        """prints the usage of the count method"""

        print("syntax: <class name>.count()")
        print("Retrieves the number of instances of a class")

    def precmd(self, line: str) -> str:
        """Runs before the command line is evaluated
        This implementation prepares the line to pass to appriopriate commands
        """

        args = line.split(".")
        if len(args) < 2:
            return super().precmd(line)

        class_name, command = args[0], args[1].split("(")[0]
        if class_name not in HBNBCommand.__valid_classes:
            return super().precmd(line)

        if command not in HBNBCommand.__valid_commands:
            return super().precmd(line)

        command = args[1]
        if command in HBNBCommand.__no_args_cmds:
            new_line = HBNBCommand.__no_args_cmds[command] + " " + class_name
            return super().precmd(new_line)

        line_list = args[1].split("(")
        if not line_list:
            return super().precmd(line)

        command = line_list[0]
        new_line = command + " " + class_name
        if len(line_list) >= 2:
            line_list = line_list[1].strip(")")
            args_list = line_list.split(",")
            if len(args_list) <= 1:
                id_arg = line_list.strip('"')
                new_line += " " + id_arg
            else:
                for arg in args_list:
                    new_line += " " + arg.strip(' "')

        return super().precmd(new_line)
