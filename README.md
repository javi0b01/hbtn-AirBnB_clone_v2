# HBNB

This is the console /command interpreter for the Holberton Airbnb clone project. The console can be used to store objects in and retrieve objects from a JSON.

### Supported classes:
* BaseModel
* User
* State
* City
* Amenity
* Place
* Review

### Commands:
* create - create an object
* show - show an object (based on id)
* destroy - destroy an object
* all - show all objects, of one type or all types
* quit/EOF - quit the console
* help - see descriptions of commands

To start, navigate to the project folder and enter `./console.py` in the shell.

#### Create
`create <class name>`
Ex:
`create BaseModel`

#### Show
`show <class name> <object id>`
Ex:
`show User my_id`

#### Destroy
`destroy <class name> <object id>`
Ex:
`destroy Place my_place_id`

#### All
`all` or `all <class name>`
Ex:
`all` or `all State`

#### Quit
`quit` or `EOF`

#### Help
`help` or `help <command>`
Ex:
`help` or `help quit`

Additionally, the console supports `<class name>.<command>(<parameters>)` syntax.
Ex:
`City.show(my_city_id)`

-- -- -- --

# 0x02. AirBnB clone - MySQL
Foundations - Higher-level programming ― AirBnB clone

###### :copyright: **[Holberton School](https://www.holbertonschool.com/)**
by _Guillaume_

## Learning Objectives
###### Background Context
Environment variables will be your best friend for this project!

- ```HBNB_ENV```: running environment. It can be “dev” or “test” for the moment (“production” soon!)
- ```HBNB_MYSQL_USER```: the username of your MySQL
- ```HBNB_MYSQL_PWD```: the password of your MySQL
- ```HBNB_MYSQL_HOST```: the hostname of your MySQL
- ```HBNB_MYSQL_DB```: the database name of your MySQL
- ```HBNB_TYPE_STORAGE```: the type of storage used. It can be “file” (using ```FileStorage```) or ```db``` (using DBStorage)
###### General
* Fourth teamwork
* What is Unit testing and how to implement it in a large project
* What is ```*args``` and how to use it
* What is ```**kwargs``` and how to use it
* How to handle named arguments in a function
* How to create a MySQL database
* How to create a MySQL user and grant it privileges
* What ORM means
* How to map a Python Class to a MySQL table
* How to handle 2 different storage engines with the same codebase
* How to use environment variables

## Resources
* [AirBnB clone](https://intranet.hbtn.io/concepts/74)
* [cmd module](https://docs.python.org/3.4/library/cmd.html)
* [packages](https://intranet.hbtn.io/concepts/66)
* [unittest module](https://docs.python.org/3.4/library/unittest.html#module-unittest)
* [args/kwargs](https://pythontips.com/2013/08/04/args-and-kwargs-in-python-explained/)
* [SQLAlchemy tutorial](https://docs.sqlalchemy.org/en/13/orm/tutorial.html)
* [How To Create a New User and Grant Permissions in MySQL](https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql)
* [Jimmy’s (My)SQL Cheat Sheet](https://gist.githubusercontent.com/MasterProgrammer200/771e877ff56a4e75f32d/raw/a66990e0935dc95029a1bba05db07c57cf231d9f/mySQLCheatSheet.SQL)
* [Python3 and environment variables](https://docs.python.org/3/library/os.html?highlight=env#os.getenv)
* [Object Relational Mapping with Python’s SQL Alchemy](https://medium.com/@eightlimbed/object-relational-mapping-with-pythons-sql-alchemy-1af658b02679)
* [SQLAlchemy](https://docs.sqlalchemy.org/en/13/)
* [MySQL 5.7 SQL Statement Syntax](https://dev.mysql.com/doc/refman/5.7/en/sql-syntax.html)
* [AirBnB clone - ORM](https://www.youtube.com/watch?v=jeJwRB33YNg&feature=youtu.be)

## Tasks
* [x] 0. Fork me if you can!
* [ ] 1. Bug free!
* [x] 2. Console improvements
* [x] 3. MySQL setup development
* [x] 4. MySQL setup test
* [x] 5. Delete object
* [x] 6. DBStorage - States and Cities
* [x] 7. DBStorage - User
* [x] 8. DBStorage - Place
* [x] 9. DBStorage - Review
* [ ] 10. DBStorage - Amenity... and BOOM!

## Developers in 0x02. AirBnB clone - MySQL
Juan Camilo Esquivel, Javier Andrés Garzón Patarroyo

-- -- -- --

# 0x03. AirBnB clone - Deploy static
Foundations - Higher-level programming ― AirBnB clone

###### :copyright: **[Holberton School](https://www.holbertonschool.com/)**
by _Guillaume_

## Learning Objectives
###### Background Context
Ever since you completed project 0x0F. Load balancer of the SysAdmin track, you’ve had 2 web servers + 1 load balancer but nothing to distribute with them.

It’s time to make your work public!

In this first deployment project, you will be deploying your web_static work. You will use Fabric (for Python3). Fabric is a Python library and command-line tool for streamlining the use of SSH for application deployment or systems administration tasks. It provides a basic suite of operations for executing local or remote shell commands (normally or via sudo) and uploading/downloading files, as well as auxiliary functionality such as prompting the running user for input, or aborting execution. This concept is important: execute commands locally or remotely. Locally means in your laptop (physical laptop or inside your Vagrant), and Remotely means on your server(s). Fabric is taking care of all network connections (SSH, SCP etc.), it’s an easy tool for transferring, executing, etc. commands from locale to a remote server.
###### General
* What is Fabric
* How to deploy code to a server easily
* What is a ```tgz``` archive
* How to execute Fabric command locally
* How to execute Fabric command remotely
* How to transfer files with Fabric
* How to manage Nginx configuration
* What is the difference between ```root``` and ```alias``` in a Nginx configuration

## Resources
* [How to use Fabric](https://www.digitalocean.com/community/tutorials/how-to-use-fabric-to-automate-administration-tasks-and-deployments)
* [How to use Fabric in Python](https://www.pythonforbeginners.com/systems-programming/how-to-use-fabric-in-python)
* [Fabric and command line options](http://docs.fabfile.org/en/1.13/usage/fab.html#command-line-options)
* [CI/CD concept page](https://intranet.hbtn.io/concepts/43)
  - [Twelve Principles of Agile Software](http://agilemanifesto.org/principles.html)
  - [CI/CD](https://resources.collab.net/blogs/walk-before-you-run-understanding-ci-in-cd)
* [Nginx configuration for beginners](http://nginx.org/en/docs/beginners_guide.html)
* [Difference between root and alias on NGINX](https://blog.heitorsilva.com/en/nginx/diferenca-entre-root-e-alias-do-nginx/)
* [Fabric for Python 3](https://github.com/mathiasertl/fabric)
* [Fabric Documentation](http://www.fabfile.org/)
* [Tip](https://stackoverflow.com/questions/10631933/nginx-static-file-serving-confusion-with-root-alias)
* [.tgz](https://en.wikipedia.org/wiki/Tar_%28computing%29)
* [AirBnB clone](https://intranet.hbtn.io/concepts/74)

## Task
* [x] 0. Prepare your web servers
* [x] 1. Compress before sending
* [x] 2. Deploy archive!
* [x] 3. Full deployment
* [x] 4. Keep it clean!
* [x] 5. Puppet for setup

## Developer in 0x03. AirBnB clone - Deploy static
Javier Andrés Garzón Patarroyo
- [website](https://tecnoayuda.co/)

:man_technologist: :books: :computer: :globe_with_meridians:

-- -- -- --

# 0x04. AirBnB clone - Web framework
Foundations - Higher-level programming ― AirBnB clone

###### :copyright: **[Holberton School](https://www.holbertonschool.com/)**
by _Guillaume_

## Learning Objectives
###### General
* What is a Web Framework
* How to build a web framework with Flask
* How to define routes in Flask
* What is a route
* How to handle variables in a route
* What is a template
* How to create a HTML response in Flask by using a template
* How to create a dynamic template (loops, conditions…)
* How to display in HTML data from a MySQL database

## Resources
* [AirBnB clone](https://intranet.hbtn.io/concepts/74)
  - [AirBnB website](https://www.airbnb.com/)
  - [Video here](https://www.youtube.com/watch?v=m-cfupVumos)
  - [here the playlist](https://www.youtube.com/playlist?list=PLlLHfkTcnvmPOp6jv_89tRpJUMFrP-Wbi)
  - [Overview](https://www.youtube.com/watch?v=QTwmCB_AWqI&feature=youtu.be)
  - [The Console](https://www.youtube.com/watch?v=jeJwRB33YNg&feature=youtu.be)
  - [ORM](https://www.youtube.com/watch?v=ZwCD8cNZk9U&feature=youtu.be)
  - [RESTful API](https://www.youtube.com/watch?v=LrQhULlFJdU&feature=youtu.be)
  - [Unittest](https://docs.python.org/3.4/library/unittest.html#module-unittest)
  - [Python packages](https://intranet.hbtn.io/concepts/66)
    - [Packages](https://docs.python.org/3.4/tutorial/modules.html#packages)
  - [How To Use them](https://www.digitalocean.com/community/tutorials/how-to-use-args-and-kwargs-in-python-3)
  - [strftime](https://strftime.org/)
* [What is a Web Framework?]()
* [A Minimal Application](https://flask.palletsprojects.com/en/1.0.x/quickstart/#a-minimal-application)
* [Routing](https://flask.palletsprojects.com/en/1.0.x/quickstart/#routing)
* [Rendering Templates](https://flask.palletsprojects.com/en/1.0.x/quickstart/#rendering-templates)
* [Synopsis](https://jinja.palletsprojects.com/en/2.9.x/templates/#synopsis)
* [Variables](https://jinja.palletsprojects.com/en/2.9.x/templates/#variables)
* [Comments](https://jinja.palletsprojects.com/en/2.9.x/templates/#comments)
* [Whitespace Control](https://jinja.palletsprojects.com/en/2.9.x/templates/#whitespace-control)
* [List of Control Structures](https://jinja.palletsprojects.com/en/2.9.x/templates/#list-of-control-structures)
* [Flask](https://palletsprojects.com/p/flask/)
* [Jinja](https://jinja.palletsprojects.com/en/2.9.x/templates/)
* [W3C-Validator ](https://github.com/holbertonschool/W3C-Validator)
* [tips](https://docs.sqlalchemy.org/en/13/orm/contextual.html)
* [tips](https://docs.sqlalchemy.org/en/13/orm/session_api.html)
* [tip](https://jinja.palletsprojects.com/en/2.9.x/templates/)
* [7-dump](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/7-states_list.sql)
* [10-dump](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/10-hbnb_filters.sql)
* [100-dump](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/100-hbnb.sql)

## Tasks
* [ ] 0. Hello Flask!
* [ ] 1. HBNB
* [ ] 2. C is fun!
* [ ] 3. Python is cool!
* [ ] 4. Is it a number?
* [ ] 5. Number template
* [ ] 6. Odd or even?
* [ ] 7. Improve engines
* [ ] 8. List of states
* [ ] 9. Cities by states
* [ ] 10. States and State
* [ ] 11. HBNB filters
* [ ] 12. HBNB is alive!

## Developer in 0x04. AirBnB clone - Web framework
Javier Andrés Garzón Patarroyo
- [website](https://tecnoayuda.co/)

:man_technologist: :books: :computer: :globe_with_meridians:
