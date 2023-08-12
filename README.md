Airbnb Clone Project 🏠

Welcome to the Airbnb Clone project, a comprehensive web application that brings together database storage, a powerful back-end API, and an intuitive front-end interface, all inspired by the renowned Airbnb platform.

As of now, the project primarily focuses on the implementation of the dynamic back-end console.

Class Structure 🆑

The Airbnb Clone leverages a well-structured class hierarchy to organize its functionalities:
* BaseModel 📦
* FileStorage 🗄️
* User 👤
* State 🌆
* City 🏙️
* Amenity ⚙️
* Place 🏡
* Review 📝

Data Storage Mechanism 🛄

Our project harrness the power of the FileStorage class to manage the data storage operations. Upon each launch of the backend, an instance of FileStorage named `Storage` is initialized. This instance dynamically loads/reloads data from class instance stored in the `file.json` JSON file. Subsequently, as new class instance are created, updated, or removed, the `storage` object meticulously maintains these changes in the `file.json` file.


Interactive Console 💻

Our command-line console serves as a gateway to the Airbnb Clone's backend management. You can effortlessly manage and manipulate the various classes integral to our application by making method calls on the storage object.

Getting Started with the Console 🚀

 1. Clone the repository to your local machine.
 2. Navigate to the project directory.
 3. Open a terminal or command prompt.

Utilizing the Console 🛠️
 1. Execute the console script: `python console.py`
 2. You will be greeted by the command prompt: `(hbnb)`

Available Commands 📝

  * `create <class>`: Generate a fresh instance of the specified class.
  * show `<class> <id>`: Display comprehensive information about a specific instance.
  * `destroy <class> <id>`: Eradicate an instance.
  * `all` or `all <class>`: Showcase all instances of the chosen class.
  * `count <class>`: Obtain the count of instances of a particular class.
  * update `<class> <id> <attribute> "<value>"` or `update <class> <id> <dictionary>`: Modify the attributes of an instance.


  Usage Examples 🌟

  * Creating a new user: `create User`
  * Displaying user information: `show User <id>`
  * Deleting a user: `destroy User <id>`
  * Listing all users: `all User`
  * Counting instances of a class: `count Place`
  * Updating user information: `update User <id> email "newemail@example.com"`



  Execution
  shell should work like this in interactive mode:

  $ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$

also in non-interactive mode:

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$



  Contributors 👥

  This repository is diligently maintained by me:

  * Ismael Abdulahi (ismaelabdulahi1@gmailcom) ✨

  For a complete roster of dedicated contributors, please consult the AUTHORS file.


  Rigorous Testing 🧪
  
  Our commitment to quality is evident through rigorous unit testing. The tests folder encompasses a suite of unittests for the Airbnb Clone project. To execute the entire test suite concurrently, kindly execute the following command:

  $ python3 -m unittest discover tests

Alternatively, if desired, you can choose to run individual test files:

$ python3 -m unittest tests/test_console.py
