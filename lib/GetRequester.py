import requests
import json

class GetRequester:


    def get_response_body(self):
        url = 'https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json'
        response = requests.get(url)
        return response.content

    def load_json(self):
        all_data = []
        data = json.loads(self.get_response_body())
        for d in data:
            all_data.append(d)

        return all_data
my_data = GetRequester()

print(my_data.load_json())

