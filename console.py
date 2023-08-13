#!/usr/bin/python3
"""Module for HBNBCommand class."""
import cmd
import models


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the HBNB project."""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        print("")
        return True
    
    def emptyline(self):
        """ Handles empty line """
        pass

    def do_create(self, arg):
        """ Creates a new instance of BaseModel, saves it, and prints the id. """
        if not arg:
            print("** class name missing **")
            return
        try:
            new_obj = eval(arg)()
            new_obj.save()
            print(new_obj.id)
        except:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """ Prints the string representation of an instance based on the class name and id. """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in models.storage.classes():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        objs = models.storage.all()
        key = "{}.{}".format(args[0], args[1])
        if key in objs:
            print(objs[key])
        else:
            print("** no instance found **")


    def do_destroy(self, arg):
        """ Deletes an instance based on the class name and id. """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in models.storage.classes():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        objs = models.storage.all()
        key = "{}.{}".format(args[0], args[1])
        if key in objs:
            objs.pop(key)
            models.storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """ Prints all instances based on the class name. """
        objs = models.storage.all()
        if not arg:
            print([str(obj) for obj in objs.values()])
        else:
            args = arg.split()
            if args[0] not in models.storage.classes():
                print("** class doesn't exist **")
                return
            print([str(obj) for key, obj in objs.items() if key.startswith(args[0])])

    def do_update(self, arg):
        """ Updates an instance based on the class name and id. """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in models.storage.classes():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        objs = models.storage.all()
        key = "{}.{}".format(args[0], args[1])
        if key not in objs:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        obj = objs[key]
        attr_name = args[2]
        try:
            attr_value = type(getattr(obj, attr_name))(args[3])
            if hasattr(obj, attr_name):
                setattr(obj, attr_name, attr_value)
                models.storage.save()
        except:
            pass



if __name__ == '__main__':
    HBNBCommand().cmdloop()
