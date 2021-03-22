## PROJECT OVERVIEW 
Wayfarer is an exciting travel blog that allows users to experience the world without ever having to leave their home. 

### PREVIEW 
![Screen Shot 2021-03-21 at 11 23 31 PM](https://user-images.githubusercontent.com/74464186/111948572-9ab4bf00-8a9c-11eb-9894-33d3f4c7507e.png)

![Screen Shot 2021-03-21 at 11 32 32 PM](https://user-images.githubusercontent.com/74464186/111949343-c4bab100-8a9d-11eb-8ce2-093d36a7edfd.png)

# Wayfarer
([click here for the link to our project hosted on Heroku!](https://the-wayfarer.herokuapp.com/))


### ORIGINAL WIREFRAMES
* As a user, I want to see a splash page with the name of the website and links to log in or sign up
* As a user, I want to see a profile page with my name, current city and join date
* As a user, I want to update my profile information 
* As a user, I want to see all of the posts I've created
* As a user, I want to click the title of a post to see the full view with title, author and content

* As a user, I want to view a city page with a photo and related posts, sorted by newest first
* As a user, I want to add a new post to a city's page
* As a user, I want to edit or delete my own post

#### Languages and Framework
* Python
* Django
* SQL
* Materialize
* HTML
* CSS

#### User Model

| Column Name | Data Type | Notes |
| --------------- | ------------- | ------------------------------ |
| id | Integer | Serial Primary Key, Auto-generated |
| username | CharField | Must be provided |
| password | CharField | Stored as a hash |


#### City Model

| Column Name | Data Type | Notes |
| --------------- | ------------- | ------------------------------ |
| id | IntegerField | Serial Primary Key, Auto-generated |
| name | CharField | Must be provided |
| photo_url | CharField | Must be provided |
| slug | SlugField | Auto-generated |


#### Post Model

| Column Name | Data Type | Notes |
| --------------- | ------------- | ------------------------------ |
| id | IntegerField | Serial Primary Key, Auto-generated |
| title | CharField | Must be provided |
| body | TextField | Must be provided |
| created_at | DateTimeField | Auto-generated |
| city | IntegerField | ForeignKey, Pulled from City DB |
| user | IntegerField | ForeignKey, Pulled from User DB |


#### Comment Model 

Column Name | Data Type | Notes |
| ---------------- | ------------- | -------------- |
| id | Integer | Serial Primary Key, Auto-generated |
| post | IntegerField | Foreign Key, Pulled from Post DB |
| user | IntegerField | Foreign Key, Pulled from User DB |
| created_at | DateTimeField | Auto-generated |
| content | TextField | Must be provided |
| reply | Integer | Foreign Key, Self-referencing |

#### Profile Model (Extends User Model) 

Column Name | Data Type | Notes |
| ---------------- | ------------- | -------------- |
| id | Integer | Serial Primary Key, Auto-generated |
| user | OneToOneField | Foreign Key, Pulled from User DB |
| current_city | CharField | Must be provided |
| first_name | CharField | Must be provided |
| last_name | CharField | Must be provided |
| photo_url | CharField | Must be provided |


### INSTALLATION INSTRUCTIONS

##### 1. FORK AND CLONE RESPOSITORY TO YOUR GITHUB AND LOCAL REPOSITORY

##### 2. OPEN REPOSITORY AND CREATE A VIRTUAL ENVIRONMENT
RUN THE FOLLOWING CODE:

```
source .env/bin/activate
```

##### 3. INSTALL DEPENDENCIES
RUN THE FOLLOWING CODE:

```
pip3 install -r requirements.txt
```

##### 3. CREATE NEW DATABASE NAMED: wayfarer
RUN THE FOLLOWING CODE:

```
createdb: wayfarer
```

##### 4. RUN THE MIGRATIONS
RUN THE FOLLOWING CODE:

```
python3 manage.py db:migrate
```

#### Contributor Githubs
* https://github.com/r-mckeith
* https://github.com/richardkentng
