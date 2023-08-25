#!/usr/bin/python3
"""Module for HBNBCommand class."""
import cmd
import models
import re
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def do_create(self, arg):
        'Create a new instance of BaseModel'
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(args[0])()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        'Print the string representation of an instance'
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            instances = storage.all()
            if key not in instances:
                print("** no instance found **")
            else:
                print(instances[key])

    def do_destroy(self, arg):
        'Delete an instance based on the class name and id'
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            instances = storage.all()
            if key not in instances:
                print("** no instance found **")
            else:
                del instances[key]
                storage.save()

    def do_all(self, arg):
        'Print all string representation of all instances'
        args = arg.split()
        if len(args) > 0 and args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            instances = storage.all()
            result = []
            for key in instances:
                if len(args) == 0 or key.split('.')[0] == args[0]:
                    result.append(str(instances[key]))
            print(result)

    def do_update(self, arg):
        'Update an instance based on the class name and id'
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            instances = storage.all()
            if key not in instances:
                print("** no instance found **")
            elif len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 3:
                print("** value missing **")
            else:
                setattr(instances[key], args[2], eval(args[3]))
                storage.save()

    def default(self, line):
        'Custom default command to handle <class name>.all()" synatx.'
        parts = line.split('.')
        if len(parts) == 2 and parts[1] == 'all()':
            class_name = parts[0]
            if parts[1] == 'all()':
                self.do_all(class_name)
            elif parts[1] == 'count':
                print(eval(class_name).count())
            if class_name in self.classes:
                self.do_all(class_name)
        else:
            print("** Unkown syntax: {}".format(line))

    def do_count(self, arg):
        """Usage: <class name>.count()
        Retrieve the number of instances of a given class."""
        class_name = arg.split('.')[0]
        count = 0
        for obj in storage.all().values():
            if class_name == obj.__class__.__name__:
                count += 1
        print(count)

    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        args = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            class_name = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", class_name[1])
            if match is not None:
                command = [class_name[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in args.keys():
                    call = "{} {}".format(class_name[0], command[1])
                    return args[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False


    def do_quit(self, arg):
        'Quit command to exit the program'
        return True

    def do_EOF(self, arg):
        'EOF command to exit the program'
        return True

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
