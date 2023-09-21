# alu-AirBnB_clone - The Console

![image](https://github.com/k-ganda/alu-AirBnB_clone/assets/116561806/582e1bd8-6453-4165-b90d-5c7978433068)

## How to start :

Clone the repository
$ git clone https://github.com/k-ganda/alu-AirBnB_clone.git

Move in to the directory
$ cd AirBnB_clone

Execute the console file
/AirBnB_clone$ ./console.py

## Project Description

This project is aimed at devoloping a simplified version of the hbnb(airbnb) website. A complete web application has the following components: The console, website's frontend interface, database storage, and backend API. The project will be developed step by step with each step focusing on a specific aspect of the application.

\*\* This is the first step and it consists of a custom command line interface for data management, and the base classes for storage of data. \*\*

## Command interpreter Usage :

| **Name**  | **Description**                                                                         |
| --------- | --------------------------------------------------------------------------------------- |
| create    | Creates a new instance of the class passed by argument.                                 |
| show      | Prints the string representation of an instance.                                        |
| \*destroy | Deletes an instance that was already created.                                           |
| all       | Prints string representation of all instances or of all instances of a specified class. |
| \*update  | Updates an instance attribute if exists otherwise create it.                            |
| help      | Show all commands or display information about a specific command.                      |
| quit      | Exit the console.                                                                       |
| EOF       | Exit the console.                                                                       |

\*\*create, destroy and update commands save changes into a JSON file.\*\*

### Console usage with examples :

| Command                                       | Example                                                                                                                        |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| Run the console                               | ./console.py                                                                                                                   |
| Quit the console                              | (hbnb) quit                                                                                                                    |
| Display the help for a command                | (hbnb) help <command>                                                                                                          |
| Create an object                              | (hbnb) create <class>                                                                                                          |
| Show an object                                | (hbnb) show <class> <id> or (hbnb) <class>.show(<id>)                                                                          |
| Destroy an object                             | (hbnb) destroy <class> <id> or (hbnb) <class>.destroy(<id>)                                                                    |
| Show all objects, or all instances of a class | (hbnb) all or (hbnb) all <class>                                                                                               |
| Update an attribute of an object (hbnb)       | update <class> <id> <attribute name> "<attribute value>" or (hbnb) <class>.update(<id>, <attribute name>, "<attribute value>") |

## Models Used

| **File**      | **Description**                                      | **Attributes**                                                                                                                   |
| ------------- | ---------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| base_model.py | BaseModel class for all the other classes            | id, created_at, updated_at                                                                                                       |
| user.py       | User class for future user information               | email, password, first_name, last_name                                                                                           |
| amenity.py    | Amenity class for future amenity information         | name                                                                                                                             |
| city.py       | City class for future location information           | state_id, name                                                                                                                   |
| state.py      | State class for future location information          | name                                                                                                                             |
| place.py      | Place class for future accomodation information      | city_id, user_id, name, description, number_rooms, number_bathrooms, max_guest, price_by_night, latitude, longitude, amenity_ids |
| review.py     | Review class for future user/host review information | place_id, user_id, text                                                                                                          |

**Example 2: Using basic update with an Id and show command:**

(hbnb) update BaseModel 99f01e9a-99c0-42af-8c10-c35cadee1d8f first_name "Betty"
(hbnb) show BaseModel 99f01e9a-99c0-42af-8c10-c35cadee1d8f
[BaseModel] (99f01e9a-99c0-42af-8c10-c35cadee1d8f) {'id': '99f01e9a-99c0-42af-8c10-c35cadee1d8f', 'created_at': datetime.datetime(2020, 7, 1, 11, 36, 30, 773211), 'updated_at': datetime.datetime(2020, 7, 1, 11, 36, 30, 773236), 'first_name': 'Betty'}
(hbnb) Place.update("492f60f3-ff1e-43c7-bb11-f8407b04dd59", "first_name", "John")
(hbnb) show Place 492f60f3-ff1e-43c7-bb11-f8407b04dd59
[Place] (492f60f3-ff1e-43c7-bb11-f8407b04dd59) {'id': '492f60f3-ff1e-43c7-bb11-f8407b04dd59', 'created_at': datetime.datetime(2020, 7, 1, 11, 36, 24, 576486), 'updated_at': datetime.datetime(2020, 7, 1, 11, 36, 24, 576530), 'first_name': 'John'}

### Tests

All the codes will be tested with the unittest module.

# alu-AirBnB_clone - Web Static
This is the front end of the Airbnb project. HTML is used to structure the page, while CSS does the styling.
No Javascript is used.

## How to start
1. Clone the repository
   git clone https://github.com/k-ganda/alu-AirBnB_clone.git

2. Navigate to the repository
   cd alu-AirBnB_clone

3. Navigate to the directory
   cd web_static

4. Execute the HTML files by Opening them with a live server. 

All **CSS files** are in the **styles** folder.
All **images** are in the **images** folder.

There are **8 HTML files**. These each show the steps to acquire the desired outlook of the project.
The 8-index.html is the final one with all changes acquired from each step.

After all the HTML files and CSS files are in place, the frontend should look like this:
![image](https://github.com/k-ganda/alu-AirBnB_clone/assets/116561806/2d595c6d-55a4-40c1-b2a0-2f9c35925b69)


