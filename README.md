Python symple server to simulate configurations through REST api

It will repond to any GET request with a message. Updating the message is possible by giving a new value in the body through a POST request. It will throw an error if the message is longer than 100 characters.

Serves at port 8080

# Building the container

    docker build -t hw-python .

# Running the container

    docker run --rm -it -p 8080:8080 hw-python
