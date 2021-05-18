from client.client import Client

from dummy_server.server import get_random_request

# Dummy server generates random requests, 
# your goal is to process them as per task requirements (see README.md)

requeststatisic = {'text': 0, 'sound': 0, 'image': 0, 'video': 0}

if __name__ == "__main__":
    for _ in range(10):
        request = get_random_request()
        print(request)
        # process request below
        requeststatisic[request['type']] += 1
        data = Client(request)
        processeddata = data.process_data()
        # print(data.is_data_processed())
        if data.is_data_processed():
            print(processeddata)
    
    print('\nprocess data statistic')
    for datatype, num in requeststatisic.items():
         print(datatype, num)
