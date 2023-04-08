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

```python
mathieu@ubuntu:~/AirBnB_v2$ python3 -m web_flask.0-hello_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```

In another tab:

<details>
<summary>File Test</summary>
<br>

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

```python
mathieu@ubuntu:~$ curl 0.0.0.0:5000/hbnb ; echo "" | cat -e
HBNB$
```
</details>

--------------------------
