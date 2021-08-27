# Task Manager on Flask

## Initialize

Complete these steps one time in order to run an app:

1. Enter virtual environment
```
$ virtualenv env --python=python3
$ source env/bin/activate
```

2. Install requirements:
```
(env) $ pip3 install -r requirements.txt
```

3. Initialize database:

```
(env) $ python3
(env) $ from project.server import db
(env) $ db.create_all()
```

4. Exit virtual environment
```
(env) $ deactivate
```

## Running
After initialization, you can run app using the command below:
```
$ chmod +x start.sh
$ ./start.sh
```

Open in browser on localhost via port 5000
```
http://localhost:5000/
```

## Testing
To run testing, use the command below:
```
$ chmod +x runtests.sh
$ ./runtests.sh
```