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

**Example 2: Using basic update with an Id and show command:**
(hbnb) update BaseModel 99f01e9a-99c0-42af-8c10-c35cadee1d8f first_name "Betty"
(hbnb) show BaseModel 99f01e9a-99c0-42af-8c10-c35cadee1d8f
[BaseModel] (99f01e9a-99c0-42af-8c10-c35cadee1d8f) {'id': '99f01e9a-99c0-42af-8c10-c35cadee1d8f', 'created_at': datetime.datetime(2020, 7, 1, 11, 36, 30, 773211), 'updated_at': datetime.datetime(2020, 7, 1, 11, 36, 30, 773236), 'first_name': 'Betty'}
(hbnb) Place.update("492f60f3-ff1e-43c7-bb11-f8407b04dd59", "first_name", "John")
(hbnb) show Place 492f60f3-ff1e-43c7-bb11-f8407b04dd59
[Place] (492f60f3-ff1e-43c7-bb11-f8407b04dd59) {'id': '492f60f3-ff1e-43c7-bb11-f8407b04dd59', 'created_at': datetime.datetime(2020, 7, 1, 11, 36, 24, 576486), 'updated_at': datetime.datetime(2020, 7, 1, 11, 36, 24, 576530), 'first_name': 'John'}
