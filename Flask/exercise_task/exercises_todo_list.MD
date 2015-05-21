# ToDo List

- Register (Email address, Username, Password; Method POST)
- Login (Email address/username, Password; Method POST)
- Logout (Method POST)
- Get Tasks (Method GET)
- Get Task (Method GET, based on task ID)
- Post new task (Method POST)
- Update task (Method PUT, based on task ID)
- Update task status (Method PUT, based on task ID)
- Delete tasks (Method DELETE, based on task IDs)
- Delete task (Method DELETE, based on task ID)
- Search tasks (Method GET, based on keyword)

# Requirements:
- Flask micro-framework
- Blueprint (route, error_handlings)
- Json (Jsonify)
- MySQLdb
- Access Token (Flask-login)

# Definition:

## Email address
- Valid email address
- Jika valid => return 200, jika tidak valid => return 400 Bad Request

Contoh invalid return:

``` python
data = {
            'status': 400,
            'message': 'Email address is not valid, please try again'
        }
```

## Username
- Minimal 3 karakter
- Maksimal 35 karakter
- Hanya terdiri dari a-zA-Z0-9_ (optional)
- Jika valid => return 200, jika tidak valid => return 400 Bad Request

``` python
data = {
            'status': 400,
            'message': 'Username is not valid, please try again'
        }
```

## Password
- Minimal 6 karakter
- Jika valid => return 200, jika tidak valid => return 400 Bad Request

``` python
data = {
            'status': 400,
            'message': 'Password is not valid, please try again'
        }
```

## Task
- Task description (DB: varchar)
- Due date (timestamp, DB: int)
- Priorities (Highest, High, Medium, Low, Lowest)
- Status (Open, Close/Done)

## Status Done
- Update status task dari Open menjadi Done.

## Login
- Generate access_token if authentication process success

## Logout
- Remove access_token