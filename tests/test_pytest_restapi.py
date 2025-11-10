import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_all_posts():
    response = requests.get(f"{BASE_URL}/posts")
    assert response.status_code == 200
    
    posts = response.json()
    assert isinstance(posts, list)
    assert len(posts) > 0
    
    first_post = posts[0]
    assert "id" in first_post
    assert "title" in first_post
    assert "body" in first_post
    assert "userId" in first_post

def test_get_single_post():
    response = requests.get(f"{BASE_URL}/posts/1")
    assert response.status_code == 200
    
    post = response.json()
    assert post["id"] == 1
    assert post["title"]

def test_create_post():
    new_post = {
        "title": "Мой тестовый пост",
        "body": "Это тело моего тестового поста",
        "userId": 1
    }
    response = requests.post(f"{BASE_URL}/posts", json=new_post)
    assert response.status_code == 201
    
    created_post = response.json()
    assert "id" in created_post
    assert created_post["title"] == new_post["title"]
    assert created_post["body"] == new_post["body"]

def test_update_post():
    updated_data = {
        "title": "Обновленный заголовок",
        "body": "Обновленное тело поста",
        "userId": 1
    }
    response = requests.put(f"{BASE_URL}/posts/1", json=updated_data)
    
    assert response.status_code == 200
    updated_post = response.json()
    assert updated_post["title"] == updated_data["title"]
    assert updated_post["body"] == updated_data["body"]

def test_delete_post():
    response = requests.delete(f"{BASE_URL}/posts/1")
    assert response.status_code == 200