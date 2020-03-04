# TheAgileMonekeys MiniCRM
### Challenge
A Mini CRM API for the second phase of TheAgileMonkeys recruitment process!

The key features:
- The   API   should   be   only   accessible   by   a   registered   user   by   providing   an authentication mechanism.
- A User should be able to perform all CRUD operations on a customer.
- Users should be associated with the customers they create and edit.
- Admins should be able to perform CRUD operations on users.
- Admins should be able to make other users admin or reduce their permission.

### Approach
By using django's packed in features for basic CRUD applications. The following are all operations that can be performed
#### Without Authentication
 - Create new user account by sending a `POST` request to `auth/users/`. Fields are: username, password, email
 - Login by sending a `POST` request to `auth/token/login`. Fields are username, password.

#### Authentication Required
After login, add `Authorization: Token {token}` to all subsequent request headers.
 - Customers can be created by sending a `POST` request to `customers/`. Fields are name, surname, picture
 - Customers can be listed by sending a `GET` request to `customers/`
 - Customer details can be viewed by sending `GET` request to `customers/{id}/`.
 - Customer details can be updated by sending `PUT` or `PATCH` request to `customers/{id}/`.
 - Customer can be deleted by sending `DELETE` request to `customers/{id}/`
 - I can delete my account by sending `DELETE` request to `auth/users/{my_id}/`.

#### Admin Account required
This activities requires Authentication with elevated permissions
 - Users can be listed by sending `GET` request to `auth/users/`.
 - User can be created by sending `POST` request to `auth/users/`. Fields are: username, password, email
 - User details can be viewed by sending `GET` request to `auth/users/{id}/`.
 - User details can be updated by sending `PUT` or `PATCH`  request to `auth/users/{id}/`.
 - User details can be deleted by sending `DELETE` request to `auth/users/{id}/`.
 - User can be made admin by sending `GET` request to `custom-auth/{id}/upgrade/`.
 - User can be stripped of admin privileges by sending `GET` request to `custom-auth/{id}/downgrade/`.

# How to setup
Fork this repo.

In a terminal window, run the following command
```bash
# clone your forked repo
git clone git@github.com:<username>/agilemonkeys.git

# enter projectt director
cd agilemonkeys

# run setup command
make install

# start server
make start
```

# Running code
```bash
# start server
make start
```

# Development
```bash
# run database migrations
make migrations

# run test
make test
```

# Enterr docker environment
```bash
# Make sure docker container is running

docker exec -it agilemonkeys sh

# Or as root
docker exec -it -u root agilemonkeys sh
```
