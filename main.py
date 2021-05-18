from client.client import Client

from dummy_server.server import get_random_request

# Dummy server generates random requests, 
# your goal is to process them as per task requirements (see README.md)

if __name__ == "__main__":
    for _ in range(10):
        request = get_random_request()
        print(request)
        # process request below
        print(Client(request).process_data())