import pytest
from app import schemas


def test_get_all_posts(authorized_client, test_posts):
    res = authorized_client.get("/posts/")

    assert len(res.json()) == len(test_posts)
    assert res.status_code == 200


# unauthorized user is allowed to access all posts
def test_unauthorized_user_get_all_posts(client, test_posts):
    res = client.get("/posts/")
    assert res.status_code == 200


def test_user_get_one_post(client, test_posts):
    res = client.get(f"/posts/{test_posts[0].id}")
    post = schemas.PostOut(**res.json())

    assert res.status_code == 200
    assert post.Post.id == test_posts[0].id


def test_get_one_post_not_exist(client, test_posts):
    res = client.get("/posts/888888")
    assert res.status_code == 404


@pytest.mark.parametrize("title, content, published", [
    ("New title", "new content", True),
    ("Newer title", "newer content", True),
    ("Newest title", "newest content", False)
])
def test_create_post(authorized_client, test_user, test_posts, title, content, published):
    res = authorized_client.post(
        "/posts/", json={"title": title, "content": content, "published": published})
    created_post = schemas.Post(**res.json())
    assert res.status_code == 201
    assert created_post.title == title
    assert created_post.content == content
    assert created_post.published == published


def test_create_post_default_published_true(authorized_client, test_user, test_posts):
    res = authorized_client.post(
        "/posts/", json={"title": "title", "content": "content"})
    created_post = schemas.Post(**res.json())
    assert res.status_code == 201
    assert created_post.title == "title"
    assert created_post.content == "content"
    assert created_post.published == True  # default

def test_unauthorized_user_create_post(client, test_posts):
    res = client.post(
        "/posts/", json={"title": "title", "content": "content"})
    assert res.status_code == 401

def test_unauthorized_user_delete_post(client, test_user, test_posts):
    res = client.delete(f"/posts/{test_posts[0].id}")
    assert res.status_code == 401

def test_delete_post_success(authorized_client, test_user, test_posts):
    res = authorized_client.delete(f"/posts/{test_posts[0].id}")
    assert res.status_code == 204

def test_delete_post_not_exist(authorized_client, test_user, test_posts):
    res = authorized_client.delete("/posts/8787876")
    assert res.status_code == 404

def test_delete_other_users_post(authorized_client, test_user, test_posts):
    res = authorized_client.delete(f"/posts/{test_posts[3].id}")
    assert res.status_code == 403

def test_update_post(authorized_client, test_user, test_posts):
    data = {
        "title": "updated", 
        "content": "updated",
        "id": test_posts[0].id
    }
    res = authorized_client.put(f"/posts/{test_posts[0].id}", json = data)

    updated_post = schemas.Post(**res.json())
    assert res.status_code == 200
    assert updated_post.title == data["title"]
    assert updated_post.content == data["content"]

def test_update_other_users_post(authorized_client, test_user, test_user2, test_posts):
    data = {
        "title": "updated", 
        "content": "updated",
        "id": test_posts[3].id
    }
    res = authorized_client.put(f"/posts/{test_posts[3].id}", json = data)
    assert res.status_code == 403

def test_unauthorized_user_update_post(client, test_user, test_posts):
    res = client.put(f"/posts/{test_posts[0].id}")
    assert res.status_code == 401

def test_update_post_not_exist(authorized_client, test_user, test_posts):
    data = {
        "title": "updated", 
        "content": "updated",
        "id": test_posts[3].id
    }
    res = authorized_client.put("/posts/8787876", json=data)
    assert res.status_code == 404
