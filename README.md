# Social Media API

This program is a social media API created in Python which uses FastAPI. The front end shown below is provided by FastAPI. 
This API has nine seperate functions under four categories: Users, Authentication, Posts, Vote.
More than 30 unit and integration tests are used to ensure funtionality of this API.

**Users:** (1) Create a user by giving an email and password. (2) Look up a user by their user ID, returns email, id, and 'created at' time stamp.

https://user-images.githubusercontent.com/96018567/189568812-cc39c992-b284-4652-bedb-2d89de8c658e.mov

**Authentication:** In order to have access to all API request options, a user must log in using their email and password. 

https://user-images.githubusercontent.com/96018567/189569618-834752f6-e809-450c-8291-87facf22292c.mov

**Posts:** (1) Get all posts on platform, will return post content, title, id, and 'created at' time.(2) Get one post on the platform by giving post ID. 
(3) Create post by providing title and content. (4) Update post by providing post ID, and then title and/or content. (5) Delete post by providing post ID.
Options (3), (4), and (5) require a user to be signed in to make these requests. 

https://user-images.githubusercontent.com/96018567/189570279-4b9b12f5-c7ed-428d-bfbb-09aadbfff600.mov

**Vote:** (1) Vote on a post by providing the post ID. Similar to likes on other social media platforms. 
I did not provide a video example of this instance as it is very similar to previous examples. 


