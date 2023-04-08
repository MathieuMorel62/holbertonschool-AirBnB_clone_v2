# <p align=center>AirBnB clone - Web framework</p>
<img src="https://user-images.githubusercontent.com/113856302/230734893-16f46ef6-19c1-4a70-a320-fcb7f934d779.gif" width="100%">

## Concepts
*For this project, we expect you to look at this concept:*
   
- [AirBnB clone](https://intranet.hbtn.io/concepts/865)

## Resources
### Read Or Watch:
- [What Is a Web Framework?](https://intelegain-technologies.medium.com/what-are-web-frameworks-and-why-you-need-them-c4e8806bd0fb)
- [A Minimal Application](https://flask.palletsprojects.com/en/2.2.x/quickstart/#a-minimal-application)
- [Routing](https://flask.palletsprojects.com/en/2.2.x/quickstart/#routing) (*except “HTTP Methods”*)
- [Rendering Templates](https://flask.palletsprojects.com/en/2.2.x/quickstart/#rendering-templates)
- [Synopsis](https://jinja.palletsprojects.com/en/3.0.x/templates/#synopsis)
- [Variables](https://jinja.palletsprojects.com/en/3.0.x/templates/#variables)
- [Comments](https://jinja.palletsprojects.com/en/3.0.x/templates/#comments)
- [Whitespace Control](https://jinja.palletsprojects.com/en/3.0.x/templates/#whitespace-control)
- [List of Control Structures](https://jinja.palletsprojects.com/en/3.0.x/templates/#list-of-control-structures) (*read up to “Call”*)
- [Flask](https://palletsprojects.com/p/flask/)
- [Jinja](https://jinja.palletsprojects.com/en/3.0.x/templates/)

## General
<details>
<summary>What is a Web Framework</summary>
<br>

>A web framework is a software tool that provides developers with a set of libraries, APIs, and tools to simplify the process of building web applications. Web frameworks often include features such as routing, templating, and database integration, which can help developers create web applications more efficiently.
</details>
<details>
<summary>How to build a web framework with Flask</summary>
<br>

>Flask is a Python web framework that allows developers to build web applications quickly and easily. To build a web framework with Flask, you would typically start by creating a new Flask application object, defining routes to handle incoming requests, and using templates to generate HTML responses.
</details>
<details>
<summary>How to define routes in Flask</summary>
<br>

In Flask, routes are defined using the `@app.route` decorator. For example, the following code defines a route for the URL `/hello`:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'Hello, World!'
```
</details>
<details>
<summary>What is a route</summary>
<br>

>A route is a URL pattern that maps to a specific function in a web application. When a user visits a URL that matches a defined route, the corresponding function is executed to generate a response.
</details>
<details>
<summary>How to handle variables in a route</summary>
<br>

In Flask, variables can be included in routes by using the `<variable>` syntax. For example, the following code defines a route that includes a variable:

```python
@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {username}'
```
  
In this example, the `show_user_profile` function takes a `username` parameter, which is included in the URL pattern.
</details>
<details>
<summary>What is a template</summary>
<br>

>A template is a file that defines the structure and content of a web page. Templates are typically written in HTML and can include placeholders for dynamic content.
</details>
<details>
<summary>How to create a HTML response in Flask by using a template</summary>
<br>

In Flask, templates can be rendered using the `render_template` function. For example, the following code renders a template named `index.html`:

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
```

In this example, the `index` function returns the rendered HTML template.
</details>
<details>
<summary>How to create a dynamic template (loops, conditions…)</summary>
<br>

In Flask, templates can include dynamic content using constructs such as loops and conditions. For example, the following code demonstrates how to use a loop in a template:

```html
<ul>
{% for item in items %}
    <li>{{ item }}</li>
{% endfor %}
</ul>
```

In this example, the `for` loop iterates over a list of items and generates an HTML list.
</details>
<details>
<summary>How to display in HTML data from a MySQL database</summary>
<br>

In Flask, data from a MySQL database can be displayed in HTML by querying the database and passing the results to a template. For example, the following code demonstrates how to query a database and pass the results to a template:

```python
from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)
db = mysql.connector.connect(
    host="localhost",
    user="username",
    password="password",
    database="database"
)

@app.route('/')
def index():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users")
    results = cursor.fetchall()
    return render_template('index.html', users=results)
```

In this example, the `index` function queries a MySQL database for all records in the `users` table, and passes the results to a template as a variable named `users`. The template can then use the `users` variable
</details>

## Requirements
### Python Scripts
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.7.*)
- All your files must be executable
- The length of your files will be tested using wc
- All your modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

### HTML/CSS Files
- Allowed editors: `vi`, `vim`, `emacs`
- All your files should end with a new line
- A `README.md` file at the root of the folder of the project is mandatory
- Your code should be W3C compliant and validate with [W3C-Validator](https://github.com/hs-hq/W3C-Validator) (except for jinja template)
- All your CSS files should be in the `styles` folder
- All your images should be in the `images` folder
- You are not allowed to use `!important` or `id` (`#...` in the CSS file)
- All tags must be in uppercase
- Current screenshots have been done on `Chrome 56.0.2924.87`.
- No cross browsers

## More Info
### MySQL Default Charset Issues
- If you get Flask errors after executing the `curl ...` commands, it might be because of the `DEFAULT CHARSET`. If it’s `DEFAULT CHARSET=latam1`, you might want to change it to `DEFAULT CHARSET=utf8mb4`, either on the server’s config file (/etc/mysql/my.cnf commonly) orm on the CREATE DATABASE statement.

## Install Flask

```python
pip3 install Flask
```

<img src="https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/concepts/74/hbnb_step3.png" width="100%">

----------------

## Tasks

### [0. Hello Flask!](https://github.com/MathieuMorel62/holbertonschool-AirBnB_clone_v2/blob/master/web_flask/0-hello_route.py)
Write a script that starts a Flask web application:
  
- Your web application must be listening on `0.0.0.0`, port `5000`
- Routes:
  - `/`: display “Hello HBNB!”
- You must use the option `strict_slashes=False` in your route definition
  
In another tab:
  
<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/AirBnB_v2$ python3 -m web_flask.0-hello_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```

In another tab:

```python
mathieu@ubuntu:~$ curl 0.0.0.0:5000 ; echo "" | cat -e
Hello HBNB!$
```
</details>

-----------------------------------

### [1. HBNB](https://github.com/MathieuMorel62/holbertonschool-AirBnB_clone_v2/blob/master/web_flask/1-hbnb_route.py)
Write a script that starts a Flask web application:
  
- Your web application must be listening on `0.0.0.0`, port `5000`
- Routes:
  - `/`: display “Hello HBNB!”
  - `/hbnb`: display “HBNB”
- You must use the option `strict_slashes=False` in your route definition

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/AirBnB_v2$ python3 -m web_flask.1-hbnb_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```

In another tab:

```python
mathieu@ubuntu:~$ curl 0.0.0.0:5000/hbnb ; echo "" | cat -e
HBNB$
```
</details>

--------------------------

## [2. C Is Fun!](https://github.com/MathieuMorel62/holbertonschool-AirBnB_clone_v2/blob/master/web_flask/2-c_route.py)
Write a script that starts a Flask web application:

- Your web application must be listening on `0.0.0.0`, port `5000`
- Routes:
  - `/`: display “Hello HBNB!”
  - `/hbnb`: display “HBNB”
  - `/c/<text>`: display “C ” followed by the value of the text variable (replace underscore _ symbols with a space )
- You must use the option `strict_slashes=False` in your route definition

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/AirBnB_v2$ python3 -m web_flask.2-c_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```

In another tab:

```python
mathieu@ubuntu:~$ curl 0.0.0.0:5000/c/is_fun ; echo "" | cat -e
C is fun$

mathieu@ubuntu:~$ curl 0.0.0.0:5000/c/cool ; echo "" | cat -e
C cool$

mathieu@ubuntu:~$ curl 0.0.0.0:5000/c
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
```
</details>

-------------------------

### [3. Python Is Cool!](https://github.com/MathieuMorel62/holbertonschool-AirBnB_clone_v2/blob/master/web_flask/3-python_route.py)
Write a script that starts a Flask web application:
  
- Your web application must be listening on `0.0.0.0`, port `5000`
- Routes:
  - `/`: display “Hello HBNB!”
  - `/hbnb`: display “HBNB”
  - `/c/<text>`: display “C ”, followed by the value of the text variable (replace underscore _ symbols with a space )
  - `/python/<text>`: display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )
    - The default value of `text` is “is cool”
- You must use the option `strict_slashes=False` in your route definition

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/AirBnB_v2$ python3 -m web_flask.3-python_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```

In another tab:

```python
mathieu@ubuntu:~$ curl -Ls 0.0.0.0:5000/python/is_magic ; echo "" | cat -e
Python is magic$

mathieu@ubuntu:~$ curl -Ls 0.0.0.0:5000/python ; echo "" | cat -e
Python is cool$

mathieu@ubuntu:~$ curl -Ls 0.0.0.0:5000/python/ ; echo "" | cat -e
Python is cool$
```
</details>

------------------

### [4. Is It a Number?](https://github.com/MathieuMorel62/holbertonschool-AirBnB_clone_v2/blob/master/web_flask/4-number_route.py)
Write a script that starts a Flask web application:
  
- Your web application must be listening on `0.0.0.0`, port `5000`
- Routes:
  - `/`: display “Hello HBNB!”
  - `/hbnb`: display “HBNB”
  - `/c/<text>`: display “C ”, followed by the value of the text variable (replace underscore _ symbols with a space )
  - `/python/<text>`: display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )
    - The default value of `text` is “is cool”
  - `/number/<n>`: display “n is a number” only if n is an integer
- You must use the option `strict_slashes=False` in your route definition

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/AirBnB_v2$ python3 -m web_flask.4-number_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```

In another tab:

```html
mathieu@ubuntu:~$ curl 0.0.0.0:5000/number/89 ; echo "" | cat -e
89 is a number$

mathieu@ubuntu:~$ curl 0.0.0.0:5000/number/8.9 
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>

mathieu@ubuntu:~$ curl 0.0.0.0:5000/number/python 
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
```
</details>

------------------------

## [5. Number Template](https://github.com/MathieuMorel62/holbertonschool-AirBnB_clone_v2/blob/master/web_flask/5-number_template.py)
Write a script that starts a Flask web application:

- Your web application must be listening on `0.0.0.0`, port `5000`
- Routes:
  - `/`: display “Hello HBNB!”
  - `/hbnb`: display “HBNB”
  - `/c/<text>`: display “C ”, followed by the value of the text variable (replace underscore _ symbols with a space )
  - `/python/<text>`: display “Python ”, followed by the value of the `text` variable (replace underscore `_` symbols with a space )
    - The default value of `text` is “is cool”
  - `/number/<n>`: display “n is a number” **only** if n is an integer
  - `/number_template/<n>`: display a HTML page **only** if `n` is an integer:
    - `H1` tag: “Number: `n`” inside the tag `BODY`
- You must use the option `strict_slashes=False` in your route definition

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/AirBnB_v2$ python3 -m web_flask.5-number_template
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```

In another tab:

```html
mathieu@ubuntu:~$ curl 0.0.0.0:5000/number_template/89 ; echo ""
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>
        <H1>Number: 89</H1>
    </BODY>
</HTML>

mathieu@ubuntu:~$ curl 0.0.0.0:5000/number_template/8.9 
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>

mathieu@ubuntu:~$ curl 0.0.0.0:5000/number_template/python 
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
```
</details>

-------------------------

## [6. Odd Or Even?](https://github.com/MathieuMorel62/holbertonschool-AirBnB_clone_v2/blob/master/web_flask/6-number_odd_or_even.py)
Write a script that starts a Flask web application:

- Your web application must be listening on 0.0.0.0, port 5000
- Routes:
  - `/`: display “Hello HBNB!”
  - `/hbnb`: display “HBNB”
  - `/c/<text>`: display “C ”, followed by the value of the text variable (replace underscore _ symbols with a space )
  - `/python/<text>`: display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )
    - The default value of `text` is “is cool”
  - `/number/<n>`: display “n is a number” **only** if n is an integer
  - `/number_template/<n>`: display a HTML page **only** if n is an integer:
    - `H1` tag: “Number: `n`” inside the tag `BODY`
  - `/number_odd_or_even/<n>`: display a HTML page **only** if `n` is an integer:
    - `H1` tag: “Number: `n` is `even|odd`” inside the tag `BODY`
- You must use the option `strict_slashes=False` in your route definition

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/AirBnB_v2$ python3 -m web_flask.6-number_odd_or_even
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```

In another tab:

```html
mathieu@ubuntu:~$ curl 0.0.0.0:5000/number_odd_or_even/89 ; echo ""
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>
        <H1>Number: 89 is odd</H1>
    </BODY>
</HTML>

mathieu@ubuntu:~$ curl 0.0.0.0:5000/number_odd_or_even/32 ; echo ""
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>
        <H1>Number: 32 is even</H1>
    </BODY>
</HTML>

mathieu@ubuntu:~$ curl 0.0.0.0:5000/number_odd_or_even/python 
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
```
</details>

---------------------

## [7. Improve Engines](https://github.com/MathieuMorel62/holbertonschool-AirBnB_clone_v2/blob/master/web_flask/7-states_list.py)
Before using Flask to display our HBNB data, you will need to update some part of our engine:
  
Update `FileStorage`: (`models/engine/file_storage.py`)
  
- Add a public method `def close(self):`: call `reload()` method for deserializing the JSON file to objects
  
Update `DBStorage`: (`models/engine/db_storage.py`)
  
- Add a public method `def close(self):`: call `remove()` method on the private session attribute (`self.__session`) [tips](https://docs.sqlalchemy.org/en/13/orm/contextual.html) or `close()` on the class `Session` [tips](https://docs.sqlalchemy.org/en/13/orm/session_api.html)
  
Update `State`: (`models/state.py`) - If it’s not already present
  
- If your storage engine is not `DBStorage`, add a public getter method `cities` to return the list of `City` objects from `storage` linked to the current `State`

<details>
<summary>File Test</summary>
<br>

```sql
mathieu@ubuntu:~/AirBnB_v2$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 
>>> from models import storage
>>> from models.state import State
>>> len(storage.all(State))
5
>>> len(storage.all(State))
5
>>> # Time to insert new data!
```

At this moment, in another tab:

```sql
mathieu@ubuntu:~/AirBnB_v2$ echo 'INSERT INTO `states` VALUES ("421a55f1-7d82-45d9-b54c-a76916479545","2017-03-25 19:42:40","2017-03-25 19:42:40","Alabama");' | mysql -uroot -p hbnb_dev_db
Enter password: 
```

And let’s go back the Python console:

```python
>>> # Time to insert new data!
>>> len(storage.all(State))
5
>>> # normal: the SQLAlchemy didn't reload his `Session`
>>> # to force it, you must remove the current session to create a new one:
>>> storage.close()
>>> len(storage.all(State))
6
>>> # perfect!
```

And for the getter cities in the State model:

```python
mathieu@ubuntu:~/AirBnB_v2$ cat main.py
#!/usr/bin/python3
"""
 Test cities access from a state
"""
from models import storage
from models.state import State
from models.city import City

"""
 Objects creations
"""
state_1 = State(name="California")
print("New state: {}".format(state_1))
state_1.save()
state_2 = State(name="Arizona")
print("New state: {}".format(state_2))
state_2.save()

city_1_1 = City(state_id=state_1.id, name="Napa")
print("New city: {} in the state: {}".format(city_1_1, state_1))
city_1_1.save()
city_1_2 = City(state_id=state_1.id, name="Sonoma")
print("New city: {} in the state: {}".format(city_1_2, state_1))
city_1_2.save()
city_2_1 = City(state_id=state_2.id, name="Page")
print("New city: {} in the state: {}".format(city_2_1, state_2))
city_2_1.save()


"""
 Verification
"""
print("")
all_states = storage.all(State)
for state_id, state in all_states.items():
    for city in state.cities:
        print("Find the city {} in the state {}".format(city, state))


mathieu@ubuntu:~/AirBnB_v2$ rm file.json ; HBNB_TYPE_STORAGE=fs ./main.py 
New state: [State] (5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45) {'name': 'California', 'id': '5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 509954), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 509950)}
New state: [State] (a5e5311a-3c19-4995-9485-32c74411b416) {'name': 'Arizona', 'id': 'a5e5311a-3c19-4995-9485-32c74411b416', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510256), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510252)}
New city: [City] (e3e36ded-fe56-44f5-bf08-8a27e2b30672) {'name': 'Napa', 'id': 'e3e36ded-fe56-44f5-bf08-8a27e2b30672', 'state_id': '5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510797), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510791)} in the state: [State] (5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45) {'name': 'California', 'id': '5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510038), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 509950)}
New city: [City] (12a58d70-e255-4c1e-8a68-7d5fb924d2d2) {'name': 'Sonoma', 'id': '12a58d70-e255-4c1e-8a68-7d5fb924d2d2', 'state_id': '5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 511437), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 511432)} in the state: [State] (5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45) {'name': 'California', 'id': '5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510038), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 509950)}
New city: [City] (a693bdb9-e0ca-4521-adfd-e1a93c093b4b) {'name': 'Page', 'id': 'a693bdb9-e0ca-4521-adfd-e1a93c093b4b', 'state_id': 'a5e5311a-3c19-4995-9485-32c74411b416', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 511873), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 511869)} in the state: [State] (a5e5311a-3c19-4995-9485-32c74411b416) {'name': 'Arizona', 'id': 'a5e5311a-3c19-4995-9485-32c74411b416', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510373), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510252)}
   
Find the city [City] (e3e36ded-fe56-44f5-bf08-8a27e2b30672) {'name': 'Napa', 'id': 'e3e36ded-fe56-44f5-bf08-8a27e2b30672', 'state_id': '5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510953), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510791)} in the state [State] (5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45) {'name': 'California', 'id': '5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510038), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 509950)}
Find the city [City] (12a58d70-e255-4c1e-8a68-7d5fb924d2d2) {'name': 'Sonoma', 'id': '12a58d70-e255-4c1e-8a68-7d5fb924d2d2', 'state_id': '5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 511513), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 511432)} in the state [State] (5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45) {'name': 'California', 'id': '5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510038), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 509950)}
Find the city [City] (a693bdb9-e0ca-4521-adfd-e1a93c093b4b) {'name': 'Page', 'id': 'a693bdb9-e0ca-4521-adfd-e1a93c093b4b', 'state_id': 'a5e5311a-3c19-4995-9485-32c74411b416', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 512073), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 511869)} in the state [State] (a5e5311a-3c19-4995-9485-32c74411b416) {'name': 'Arizona', 'id': 'a5e5311a-3c19-4995-9485-32c74411b416', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510373), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510252)}
```
</details>

-----------------------

## [8. List Of States](https://github.com/MathieuMorel62/holbertonschool-AirBnB_clone_v2/blob/master/web_flask/8-cities_by_states.py)
Write a script that starts a Flask web application:

- Your web application must be listening on `0.0.0.0`, port `5000`
- You must use `storage` for fetching data from the storage engine (`FileStorage` or `DBStorage`) => `from models import storage` and `storage.all(...)`
- After each request you must remove the current SQLAlchemy Session:
  - Declare a method to handle `@app.teardown_appcontext`
  - Call in this method `storage.close()`
- Routes:
  - `/states_list`: display a HTML page: (inside the tag `BODY`)
    - `H1` tag: “States”
    - `UL` tag: with the list of all `State` objects present in `DBStorage` **sorted by `name`** (A->Z) [tip](https://jinja.palletsprojects.com/en/2.9.x/templates/)
      - `LI` tag: description of one `State`: `<state.id>: <B><state.name></B>`
- Import this [7-dump](https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/290/7-states_list.sql) to have some data
- You must use the option `strict_slashes=False` in your route definition
  
**IMPORTANT**
  
- Make sure you have a running and valid `setup_mysql_dev.sql` in your `AirBnB_clone_v2` repository ([Task](https://intranet.hbtn.io/rltoken/gIfF4l2eWBO13bfNduSG4w))
- Make sure all tables are created when you run `echo "quit" | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py`

<details>
<summary>File Test</summary>
<br>

```sql
mathieu@ubuntu:~/AirBnB_v2$ curl -o 7-dump.sql "https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/290/7-states_list.sql"

mathieu@ubuntu:~/AirBnB_v2$ cat 7-dump.sql | mysql -uroot -p
Enter password: 

mathieu@ubuntu:~/AirBnB_v2$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 -m web_flask.7-states_list
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```

In another tab:

```html
mathieu@ubuntu:~$ curl 0.0.0.0:5000/states_list ; echo ""
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>
        <H1>States</H1>
        <UL>

            <LI>421a55f4-7d82-47d9-b54c-a76916479545: <B>Alabama</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479546: <B>Arizona</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479547: <B>California</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479548: <B>Colorado</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479549: <B>Florida</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479550: <B>Georgia</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479551: <B>Hawaii</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479552: <B>Illinois</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479553: <B>Indiana</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479554: <B>Louisiana</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479555: <B>Minnesota</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479556: <B>Mississippi</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479557: <B>Oregon</B></LI>

        </UL>
    </BODY>
</HTML>
```
</details>

-----------------------

## [9. Cities By States](https://github.com/MathieuMorel62/holbertonschool-AirBnB_clone_v2/blob/master/web_flask/9-states.py)
Write a script that starts a Flask web application:
  
- Your web application must be listening on `0.0.0.0`, port `5000`
- You must use `storage` for fetching data from the storage engine (`FileStorage` or `DBStorage`) => `from models import storage` and `storage.all(...)`
- To load all cities of a `State`:
  - If your storage engine is `DBStorage`, you must use `cities` relationship
  - Otherwise, use the public getter method `cities`
- After each request you must remove the current SQLAlchemy Session:
  - Declare a method to handle `@app.teardown_appcontext`
  - Call in this method `storage.close()`
- Routes:
  - `/cities_by_states`: display a HTML page: (inside the tag `BODY`)
    - `H1` tag: “States”
    - `UL` tag: with the list of all `State` objects present in `DBStorage` **sorted by `name`** (A->Z) [tip](https://jinja.palletsprojects.com/en/2.9.x/templates/)
      - `LI` tag: description of one `State`: `<state.id>: <B><state.name></B>` + `UL` tag: with the list of `City` objects linked to the `State` **sorted by `name`** (A->Z)
        - `LI` tag: description of one `City`: `<city.id>: <B><city.name></B>`
- Import this [7-dump](https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/290/7-states_list.sql) to have some data
- You must use the option `strict_slashes=False` in your route definition
  
**IMPORTANT**
  
- Make sure you have a running and valid `setup_mysql_dev.sql` in your `AirBnB_clone_v2` repository ([Task](https://intranet.hbtn.io/rltoken/gIfF4l2eWBO13bfNduSG4w))
- Make sure all tables are created when you run `echo "quit" | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py`

<details>
<summary>File Test</summary>
<br>

```sql
mathieu@ubuntu:~/AirBnB_v2$ curl -o 7-dump.sql "https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/290/7-states_list.sql"

mathieu@ubuntu:~/AirBnB_v2$ cat 7-dump.sql | mysql -uroot -p
Enter password: 

mathieu@ubuntu:~/AirBnB_v2$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 -m web_flask.8-cities_by_states
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```

In another tab:

```html
mathieu@ubuntu:~$ curl 0.0.0.0:5000/cities_by_states ; echo ""
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>
        <H1>States</H1>
        <UL>

            <LI>421a55f4-7d82-47d9-b54c-a76916479545: <B>Alabama</B>
                <UL>

                        <LI>521a55f4-7d82-47d9-b54c-a76916479545: <B>Akron</B></LI>

                        <LI>531a55f4-7d82-47d9-b54c-a76916479545: <B>Babbie</B></LI>

                        <LI>541a55f4-7d82-47d9-b54c-a76916479545: <B>Calera</B></LI>

                        <LI>551a55f4-7d82-47d9-b54c-a76916479545: <B>Fairfield</B></LI>

                </UL>
            </LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479546: <B>Arizona</B>
                <UL>

                        <LI>521a55f4-7d82-47d9-b54c-a76916479546: <B>Douglas</B></LI>

                        <LI>531a55f4-7d82-47d9-b54c-a76916479546: <B>Kearny</B></LI>

                        <LI>541a55f4-7d82-47d9-b54c-a76916479546: <B>Tempe</B></LI>

                </UL>
            </LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479547: <B>California</B>
                <UL>

                        <LI>541a55f4-7d82-47d9-b54c-a76916479547: <B>Fremont</B></LI>

                        <LI>551a55f4-7d82-47d9-b54c-a76916479547: <B>Napa</B></LI>

                        <LI>521a55f4-7d82-47d9-b54c-a76916479547: <B>San Francisco</B></LI>

                        <LI>531a55f4-7d82-47d9-b54c-a76916479547: <B>San Jose</B></LI>

                        <LI>561a55f4-7d82-47d9-b54c-a76916479547: <B>Sonoma</B></LI>

                </UL>
            </LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479548: <B>Colorado</B>
                <UL>

                        <LI>521a55f4-7d82-47d9-b54c-a76916479548: <B>Denver</B></LI>

                </UL>
            </LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479549: <B>Florida</B>
                <UL>

                        <LI>521a55f4-7d82-47d9-b54c-a76916479549: <B>Miami</B></LI>

                        <LI>531a55f4-7d82-47d9-b54c-a76916479549: <B>Orlando</B></LI>

                </UL>
            </LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479550: <B>Georgia</B>
                <UL>

                </UL>
            </LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479551: <B>Hawaii</B>
                <UL>

                        <LI>521a55f4-7d82-47d9-b54c-a76916479551: <B>Honolulu</B></LI>

                        <LI>531a55f4-7d82-47d9-b54c-a76916479551: <B>Kailua</B></LI>

                        <LI>541a55f4-7d82-47d9-b54c-a76916479551: <B>Pearl city</B></LI>

                </UL>
            </LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479552: <B>Illinois</B>
                <UL>

                        <LI>521a55f4-7d82-47d9-b54c-a76916479552: <B>Chicago</B></LI>

                        <LI>561a55f4-7d82-47d9-b54c-a76916479552: <B>Joliet</B></LI>

                        <LI>541a55f4-7d82-47d9-b54c-a76916479552: <B>Naperville</B></LI>

                        <LI>531a55f4-7d82-47d9-b54c-a76916479552: <B>Peoria</B></LI>

                        <LI>551a55f4-7d82-47d9-b54c-a76916479552: <B>Urbana</B></LI>

                </UL>
            </LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479553: <B>Indiana</B>
                <UL>

                </UL>
            </LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479554: <B>Louisiana</B>
                <UL>

                        <LI>531a55f4-7d82-47d9-b54c-a76916479554: <B>Baton rouge</B></LI>

                        <LI>541a55f4-7d82-47d9-b54c-a76916479554: <B>Lafayette</B></LI>

                        <LI>521a55f4-7d82-47d9-b54c-a76916479554: <B>New Orleans</B></LI>

                </UL>
            </LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479555: <B>Minnesota</B>
                <UL>

                        <LI>521a55f4-7d82-47d9-b54c-a76916479555: <B>Saint Paul</B></LI>

                </UL>
            </LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479556: <B>Mississippi</B>
                <UL>

                        <LI>521a55f4-7d82-47d9-b54c-a76916479556: <B>Jackson</B></LI>

                        <LI>541a55f4-7d82-47d9-b54c-a76916479556: <B>Meridian</B></LI>

                        <LI>531a55f4-7d82-47d9-b54c-a76916479556: <B>Tupelo</B></LI>

                </UL>
            </LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479557: <B>Oregon</B>
                <UL>

                        <LI>531a55f4-7d82-47d9-b54c-a76916479557: <B>Eugene</B></LI>

                        <LI>521a55f4-7d82-47d9-b54c-a76916479557: <B>Portland</B></LI>

                </UL>
            </LI>

        </UL>
    </BODY>
</HTML>
```
</details>

<img src="https://user-images.githubusercontent.com/113856302/230739582-d1494525-3c5a-409c-9c87-88fb990c9c82.png" width="100%">

--------------------------------------

### [10. States And State](https://github.com/MathieuMorel62/holbertonschool-AirBnB_clone_v2/blob/master/web_flask/10-hbnb_filters.py)
Write a script that starts a Flask web application:
  
- Your web application must be listening on `0.0.0.0`, port `5000`
- You must use `storage` for fetching data from the storage engine (`FileStorage` or `DBStorage`) => `from models import storage` and `storage.all(...)`
- To load all cities of a `State`:
  - If your storage engine is `DBStorage`, you must use `cities` relationship
  - Otherwise, use the public getter method `cities`
- After each request you must remove the current SQLAlchemy Session:
  - Declare a method to handle `@app.teardown_appcontext`
  - Call in this method `storage.close()`
- Routes:
  - `/states`: display a HTML page: (inside the tag BODY)
    - `H1` tag: “States”
    - `UL` tag: with the list of all `State` objects present in `DBStorage` **sorted by `name`** (A->Z) [tip](https://intranet.hbtn.io/rltoken/UVC1Bw_-nfa_0T2gv1MuQg)
      - `LI` tag: description of one State: `<state.id>: <B><state.name></B>`
  - `/states/<id>`: display a HTML page: (inside the tag `BODY`)
    - If a `State` object is found with this `id`:
      - `H1` tag: “State: ”
      - `H3` tag: “Cities:”
      - `UL` tag: with the list of `City` objects linked to the `State` **sorted by `name`** (A->Z)
        - `LI` tag: description of one `City`: `<city.id>: <B><city.name></B>`
    - Otherwise:
      - `H1` tag: “Not found!”
- You must use the option `strict_slashes=False` in your route definition
- Import this [7-dump](https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/290/7-states_list.sql) to have some data
  
**IMPORTANT**
  
- Make sure you have a running and valid `setup_mysql_dev.sql` in your `AirBnB_clone_v2` repository ([Task](https://intranet.hbtn.io/rltoken/gIfF4l2eWBO13bfNduSG4w))
- Make sure all tables are created when you run `echo "quit" | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py`

<details>
<summary>File Test</summary>
<br>

```sql
mathieu@ubuntu:~/AirBnB_v2$ curl -o 7-dump.sql "https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/290/7-states_list.sql"

mathieu@ubuntu:~/AirBnB_v2$ cat 7-dump.sql | mysql -uroot -p
Enter password: 

mathieu@ubuntu:~/AirBnB_v2$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 -m web_flask.9-states
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```

In another tab:

```html
mathieu@ubuntu:~$ curl 0.0.0.0:5000/states ; echo ""
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>

        <H1>States</H1>
        <UL>

            <LI>421a55f4-7d82-47d9-b54c-a76916479545: <B>Alabama</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479546: <B>Arizona</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479547: <B>California</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479548: <B>Colorado</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479549: <B>Florida</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479550: <B>Georgia</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479551: <B>Hawaii</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479552: <B>Illinois</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479553: <B>Indiana</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479554: <B>Louisiana</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479555: <B>Minnesota</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479556: <B>Mississippi</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479557: <B>Oregon</B></LI>

        </UL>

    </BODY>
</HTML>

mathieu@ubuntu:~$ curl 0.0.0.0:5000/states/421a55f4-7d82-47d9-b54c-a76916479552 ; echo ""
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>

        <H1>State: Illinois</H1>
        <H3>Cities:</H3>
        <UL>
                <LI>521a55f4-7d82-47d9-b54c-a76916479552: <B>Chicago</B></LI>

                <LI>561a55f4-7d82-47d9-b54c-a76916479552: <B>Joliet</B></LI>

                <LI>541a55f4-7d82-47d9-b54c-a76916479552: <B>Naperville</B></LI>

                <LI>531a55f4-7d82-47d9-b54c-a76916479552: <B>Peoria</B></LI>

                <LI>551a55f4-7d82-47d9-b54c-a76916479552: <B>Urbana</B></LI>
        </UL>

    </BODY>
</HTML>

mathieu@ubuntu:~$ curl 0.0.0.0:5000/states/holberton ; echo ""
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>

        <H1>Not found!</H1>

    </BODY>
</HTML>
```
</details>

-----------------------------

## [11. HBNB filters](https://github.com/MathieuMorel62/holbertonschool-AirBnB_clone_v2/blob/master/web_flask/templates/10-hbnb_filters.html)
Write a script that starts a Flask web application:
  
- Your web application must be listening on `0.0.0.0`, port `5000`
- You must use `storage` for fetching data from the storage engine (`FileStorage` or `DBStorage`) => `from models import storage` and `storage.all(...)`
- To load all cities of a `State`:
  - If your storage engine is `DBStorage`, you must use `cities` relationship
  - Otherwise, use the public getter method `cities`
- After each request you must remove the current SQLAlchemy Session:
  - Declare a method to handle `@app.teardown_appcontext`
  - Call in this method `storage.close()`
- Routes:
  - `/hbnb_filters`: display a HTML page like [6-index.html](https://github.com/MathieuMorel62/holbertonschool-AirBnB_clone_v2/blob/master/web_static/6-index.html), which was done during the project [0x01. AirBnB clone - Web static](https://intranet.hbtn.io/rltoken/LSsy0WYsMdxl-zlZqbAthg)
    - Copy files [3-footer.css](https://github.com/MathieuMorel62/holbertonschool-AirBnB_clone_v2/blob/master/web_flask/static/styles/3-footer.css), [3-header.css](https://github.com/MathieuMorel62/holbertonschool-AirBnB_clone_v2/blob/master/web_flask/static/styles/3-header.css), [4-common.css](https://github.com/MathieuMorel62/holbertonschool-AirBnB_clone_v2/blob/master/web_flask/static/styles/4-common.css) and [6-filters.css](https://github.com/MathieuMorel62/holbertonschool-AirBnB_clone_v2/blob/master/web_flask/static/styles/6-filters.css) from `web_static/styles/` to the folder `web_flask/static/styles`
    - Copy files [icon.png](https://github.com/MathieuMorel62/holbertonschool-AirBnB_clone_v2/blob/master/web_flask/static/images/icon.ico) and [logo.png](https://github.com/MathieuMorel62/holbertonschool-AirBnB_clone_v2/blob/master/web_flask/static/images/logo.png) from `web_static/images/` to the folder `web_flask/static/images`
    - Update `.popover` class in [6-filters.css](https://github.com/MathieuMorel62/holbertonschool-AirBnB_clone_v2/blob/master/web_static/styles/6-filters.css) to allow scrolling in the popover and a max height of 300 pixels.
    - Use [6-index.html](https://github.com/MathieuMorel62/holbertonschool-AirBnB_clone_v2/blob/master/web_static/6-index.html) content as source code for the template [10-hbnb_filters.html](https://github.com/MathieuMorel62/holbertonschool-AirBnB_clone_v2/blob/master/web_flask/templates/10-hbnb_filters.html):
      - Replace the content of the `H4` tag under each filter title (`H3` States and `H3` Amenities) by `&nbsp`;
    - `State`, `City` and `Amenity` objects must be loaded from `DBStorage` and **sorted by `name`** (A->Z)
- You must use the option `strict_slashes=False` in your route definition
- Import this [10-dump](https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/290/10-hbnb_filters.sql) to have some data
  
**IMPORTANT**
  
- Make sure you have a running and valid `setup_mysql_dev.sql` in your `AirBnB_clone_v2` repository ([Task](https://intranet.hbtn.io/rltoken/gIfF4l2eWBO13bfNduSG4w))
- Make sure all tables are created when you run `echo "quit" | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py`

<details>
<summary>File Test</summary>
<br>

```sql
mathieu@ubuntu:~/AirBnB_v2$ curl -o 10-dump.sql "https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/290/10-hbnb_filters.sql"

mathieu@ubuntu:~/AirBnB_v2$ cat 10-dump.sql | mysql -uroot -p
Enter password: 

mathieu@ubuntu:~/AirBnB_v2$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 -m web_flask.10-hbnb_filters
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```
</details>

In the browser:

<img src="https://user-images.githubusercontent.com/113856302/230739635-25f2d574-a8c8-4802-b885-9452a0ec4fb0.png" width="100%">

<img src="https://user-images.githubusercontent.com/113856302/230739648-fbb48499-a0b8-4f84-a624-8824a617801d.png" width="100%">

<img src="https://user-images.githubusercontent.com/113856302/230739659-ffdbc8cd-2602-463e-9c9c-fe392c906a6a.png" width="100%">

<img src="https://user-images.githubusercontent.com/113856302/230739672-e560f97a-ab05-42fa-9638-fd25c7d4e436.png" width="100%">

----------------------------

## [12. HBNB Is Alive!]()
Write a script that starts a Flask web application:
  
- Your web application must be listening on `0.0.0.0`, port `5000`
- You must use `storage` for fetching data from the storage engine (`FileStorage` or `DBStorage`) => `from models import storage` and `storage.all(...)`
- To load all cities of a `State`:
  - If your storage engine is `DBStorage`, you must use `cities` relationship
  - Otherwise, use the public getter method `cities`
- After each request you must remove the current SQLAlchemy Session:
  - Declare a method to handle `@app.teardown_appcontext`
  - Call in this method `storage.close()`
- Routes:
  - `/hbnb`: display a HTML page like [8-index.html](https://github.com/MathieuMorel62/holbertonschool-AirBnB_clone_v2/blob/master/web_static/8-index.html), done during the [0x01. AirBnB clone - Web static](https://intranet.hbtn.io/rltoken/LSsy0WYsMdxl-zlZqbAthg) project
    - Copy files [3-footer.css](https://github.com/MathieuMorel62/holbertonschool-AirBnB_clone_v2/blob/master/web_static/styles/3-footer.css), [3-header.css](https://github.com/MathieuMorel62/holbertonschool-AirBnB_clone_v2/blob/master/web_static/styles/3-header.css), [4-common.css](https://github.com/MathieuMorel62/holbertonschool-AirBnB_clone_v2/blob/master/web_static/styles/4-common.css), [6-filters.css](https://github.com/MathieuMorel62/holbertonschool-AirBnB_clone_v2/blob/master/web_static/styles/6-filters.css) and [8-places.css](https://github.com/MathieuMorel62/holbertonschool-AirBnB_clone_v2/blob/master/web_static/styles/8-places.css) from `web_static/styles/` to the folder `web_flask/static/styles`
    - Copy all files from `web_static/images/` to the folder `web_flask/static/images`
    - Update `.popover` class in [6-filters.css](https://github.com/MathieuMorel62/holbertonschool-AirBnB_clone_v2/blob/master/web_static/styles/6-filters.css) to enable scrolling in the popover and set max height to 300 pixels.
    - Update [8-places.css](https://github.com/MathieuMorel62/holbertonschool-AirBnB_clone_v2/blob/master/web_static/styles/8-places.css) to always have the price by night on the top right of each place element, and the name correctly aligned and visible (i.e. screenshots below)
    - Use [8-index.html](https://github.com/MathieuMorel62/holbertonschool-AirBnB_clone_v2/blob/master/web_static/8-index.html) content as source code for the template [100-hbnb.html]():
      - Replace the content of the `H4` tag under each filter title (`H3` States and `H3` Amenities) by `&nbsp;`
      - Make sure all HTML tags from objects are correctly used (example: `<BR />` must generate a new line)
    - `State`, `City`, `Amenity` and `Place` objects must be loaded from `DBStorage` and **sorted by `name`** (A->Z)
- You must use the option `strict_slashes=False` in your route definition
- Import this [100-dump](https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/290/100-hbnb.sql) to have some data
  
**IMPORTANT**
  
- Make sure you have a running and valid `setup_mysql_dev.sql` in your `AirBnB_clone_v2` repository ([Task](https://intranet.hbtn.io/rltoken/gIfF4l2eWBO13bfNduSG4w))
- Make sure all tables are created when you run `echo "quit" | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py`

<details>
<summary>File Test</summary>
<br>

```sql
mathieu@ubuntu:~/AirBnB_v2$ curl -o 100-dump.sql "https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/290/100-hbnb.sql"

mathieu@ubuntu:~/AirBnB_v2$ cat 100-dump.sql | mysql -uroot -p
Enter password: 

mathieu@ubuntu:~/AirBnB_v2$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 -m web_flask.100-hbnb
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```
</details>

<img src="https://user-images.githubusercontent.com/113856302/230739711-31ed91f2-f423-4629-9155-fe171a9746f8.png" width="100%">

<img src="https://user-images.githubusercontent.com/113856302/230739724-2d3954a4-e24c-4b9d-b9b6-0815d9358c01.png" width="100%">

<img src="https://user-images.githubusercontent.com/113856302/230739735-94b3ed48-519a-497b-8f8d-d0adc74def72.png" width="100%">

<img src="https://user-images.githubusercontent.com/113856302/230739743-d86a78a9-bb88-4c97-8338-0afe51e3990b.png" width="100%">

<img src="https://user-images.githubusercontent.com/113856302/230739757-f6bffe06-9866-468e-9846-08c7b49de737.png" width="100%">

-------------------

## Author

- Mathieu Morel
