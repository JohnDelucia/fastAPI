# package specific (everything in package will have access to this)

from app.config import Settings
from fastapi.testclient import TestClient
from app.main import app
from app import schemas
from app.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.database import get_db
from app.database import Base
import pytest
from app.Oauth2 import create_access_token
from app import models


SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}_test'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

# create session or instance of DB (need test DB for testing)
TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)

# create a session used with Object Relational Model (ORM)

# runs before every function dependent on the fixture


@pytest.fixture()
def session():
    # drop tables: allows us to run tests with same email multiple times thus avoiding 'email exists' error
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)  # create tables for us in postgres
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

# allows us to test 'login' without relying on create user test

@pytest.fixture
def test_user2(client):
    user_data = {"email": "jdog123@newemail.com", "password": "password123"}
    res = client.post("/users/", json=user_data)
    new_user = res.json()
    new_user['password'] = user_data['password']
    assert res.status_code == 201
    return new_user

@pytest.fixture
def test_user(client):
    user_data = {"email": "jdog@newemail.com", "password": "password123"}
    res = client.post("/users/", json=user_data)
    new_user = res.json()
    new_user['password'] = user_data['password']
    assert res.status_code == 201
    return new_user


# client (unauthenticated) will use new test database

@pytest.fixture()
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)


@pytest.fixture
def token(test_user):
    return create_access_token({"user_id": test_user['id']})


@pytest.fixture
def authorized_client(client, token):
    client.headers = {
        **client.headers,
        "Authorization": f"Bearer {token}"
    }
    return client


#create three posts 
@pytest.fixture
def test_posts(test_user, session, test_user2):
    posts_data = [{
        "title": "first",
        "content": "content1",
        "owner_id": test_user['id']
    }, {
        "title": "second",
        "content": "content2",
        "owner_id": test_user['id']
    }, {
        "title": "third",
        "content": "content3",
        "owner_id": test_user['id']
    }, {
        "title": "fourth",
        "content": "content4",
        "owner_id": test_user2['id']
    }]

    def create_post_model(post):
        return models.Post(**post)

    post_map = map(create_post_model, posts_data)

    posts = list(post_map)

    session.add_all(posts)

    session.commit()

    posts = session.query(models.Post).all()
    return posts
