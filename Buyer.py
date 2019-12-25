import json
import requests


class TaxiPassenger:
    def __init__(self):
        self.startPoint = "start point"
        self.endPoint = "end point"
        self.sendFile = {}
        self.jsonFile = None

    # get info from buyer (input)
    def make_package(self):
        self.startPoint = int(input("start point is "))
        self.endPoint = int(input("end point is "))
        return self.startPoint, self.endPoint

    # # change packages to json
    def make_json(self):
        self.sendFile = {"start point is ": self.startPoint, "end point ": self.endPoint}
        self.jsonFile = json.dumps(self.sendFile)
        print(self.jsonFile)
        return self.jsonFile

    # send json to server
    def send_json_to_server(self, url, json):
        requests.post(url, json)
        print("json is send ")
    # w8 to receive from server
    def receive_answer_from_server(self):
        pass

    def main(self):
        self.make_package()
        self.make_json()
        self.send_json_to_server('http://localhost:80', self.jsonFile)

#http://localhost:80 Xampp

#http://httpbin.org/post

if __name__ == '__main__':
    passenger = TaxiPassenger()
    passenger.main()
