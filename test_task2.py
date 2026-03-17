import requests
import time
import csv

url = "https://jsonplaceholder.typicode.com/posts/1"

post_payload = {
    "title": "New Post",
    "body": "This is a test post",
    "userId": 1
}

put_payload = {
    "title": "Updated Title",
    "body": "Updated content",
    "userId": 1
}

patch_payload = {
    "title": "Partially Updated Title"
}


# GET API
def test_get_api():

    start = time.time()

    response = requests.get(url)

    end = time.time()

    print("Time taken:", end - start)

    assert response.status_code == 200

    data = response.json()

    with open("output.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(data.keys())
        writer.writerow(data.values())


# POST API
def test_post_api():

    response = requests.post(
        "https://jsonplaceholder.typicode.com/posts",
        json=post_payload
    )

    assert response.status_code == 201


# PUT API
def test_put_api():

    response = requests.put(url, json=put_payload)

    assert response.status_code == 200


# PATCH API
def test_patch_api():

    response = requests.patch(url, json=patch_payload)

    assert response.status_code == 200


# DELETE API
def test_delete_api():

    response = requests.delete(url)

    assert response.status_code == 200

    
    # PATCH REQUEST
 
    def test_patch_api(self):

        response = requests.patch(url, json=patch_payload)

        print(response.json())

        assert response.status_code == 200


   
    # DELETE REQUEST
    
    def test_delete_api(self):

        response = requests.delete(url)

        print(response.text)

        assert response.status_code == 200