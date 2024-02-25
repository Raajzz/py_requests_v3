import requests

class PyRequests:
    def get_json_data(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
            data = response.json()
            return data
        except Exception as e:
            print(f"An error occurred: {e}")

    def post_json_data(url, data):
        try:
            response = requests.post(url, json=data)
            response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
            data = response.json()
            print(data)
        except Exception as e:
            print(f"An error occurred: {e}")

def main():
    # to call the different requests defined
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = PyRequests().get_json_data(url)
    print(response)

if __name__ == "__main__":
    main()