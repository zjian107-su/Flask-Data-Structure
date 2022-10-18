# Data Structures (w/ Flask)

## Porject Description
This project uses LinkedList to implement binary search tree, queue, stack, linked list, hashtable with RestFul API. 

## Requirements
PostMan, DB Browser for SQLite, Python, Flask, sqlite3, sqlalchemy.

## Screenshots
1. delete_last_10.png

<img width="393" alt="delete_last_10" src="https://user-images.githubusercontent.com/35544956/125099693-4a428b00-e0a6-11eb-94ad-ac6d2c753c3b.png">

2. get_certain_post.png


<img width="393" alt="get_certain_post" src="https://user-images.githubusercontent.com/35544956/125099997-9f7e9c80-e0a6-11eb-8846-fc85e7b20ea2.png">

3. get_all_users.png

<img width="393" alt="get_all_users" src="https://user-images.githubusercontent.com/35544956/125100054-adccb880-e0a6-11eb-9ade-1f0725235e55.png">

3. terminal.png

<img width="438" alt="terminal" src="https://user-images.githubusercontent.com/35544956/125100994-b4a7fb00-e0a7-11eb-98f4-72feedd879f4.png">


## Others - Dev Notes
- Generate env: 
    `conda create env -n flask`
    `conda activate flask`
    `conda install alchemy flask flask_sqlalchemy`
    `conda install -c conda-forge flask-sqlalchemy`
- Generate db file: 
    `from server import db`
    `db.create_all()`
    `exit()`

