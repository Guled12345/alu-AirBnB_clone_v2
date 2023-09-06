**How to start:**
Clone the repository
$ git clone https://github.com/JoseR98/AirBnB_clone.git

Move in to the directory
$ cd AirBnB_clone

Execute the console file
/AirBnB_clone$ ./console.py

**command interpreter are:**

Name	Description
*create	Creates a new instance of the class passed by argument.
show	Prints the string representation of an instance.
*destroy	Deletes an instance that was already created.
all	Prints string representation of all instances or of all instances of a specified class.
*update	Updates an instance attribute if exists otherwise create it.
help	Show all commands or display information about a specific command.
quit	Exit the console.
EOF	Exit the console.
*create, destroy and update commands save changes into a JSON file.

Commands usage:
Command	Usage
create	create <class_name>
show	show <class_name> <object_id> ; <class_name>.show(<object_id>)()
destroy	destroy <class_name> <object_id ; <class_name>.destroy(<object_id>)()
all	all <class_name> ; <class_name>.all()
update	update <class_name> <object_id> <attribute name> “<attribute value>” ; <class name>.update(<object_id>, <attribute name>, <attribute value>) ; <class name>.update(<object_id>, <dictionary representation>)
help	help ; help <command_name>
quit	quit
EOF	EOF ; (ctrl + d)
