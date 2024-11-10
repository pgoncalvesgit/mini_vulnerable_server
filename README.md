# Mini Vulnerable Server

This is a simple python flask server that has 4 vulnerable xss endpoints. It was created for a class given at the University of Coimbra - Department of Informatics Engeneering.

## Instalation

You can either install this through docker or by simply running it in python.

### Docker

With docker all you need to do is (inside the project root directory):

```bash
docker build . -t <container_name>
docker run -p 8000:5000 <container_name>
```

This will run the container with the container_name used. The part (-p 8000:5000) means that we are forwarding any connections to our port 8000 into the 5000 port of the container.

### Python

With python it should be as simple as running:

```bash
pip install -r requirements.txt
python3 -m flask run
```

## Authentication

It uses basic auth, just to show how probely can deal with it. Credentials are DEI for both the username and the password.
