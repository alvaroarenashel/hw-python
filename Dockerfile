from python:latest
copy server.py /
expose 8080
cmd python server.py
