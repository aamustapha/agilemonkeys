# TheAgileMonekeys MiniCRM
A Mini CRM API for the second phase of TheAgileMonkeys recruitment process!

The key features:
- The   API   should   be   only   accessible   by   a   registered   user   by   providing   an authentication mechanism.
- A User should be able to perform all CRUD operations on a customer.
- Users should be associated with the customers they create and edit.
- Admins should be able to perform CRUD operations on users.
- Admins should be able to make other users admin or reduce their permission.

# How to setup
Fork this repo
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
