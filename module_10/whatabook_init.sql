-- drop test user if exists 
DROP USER IF EXISTS 'whatabook_user'@'localhost';

-- create whatabook_user and grant them all privileges to the whatabook database 
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

-- grant all privileges to the whatabook database to user whatabook_user on localhost 
GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

-- drop contstraints if they exist
-- ALTER TABLE wishlist DROP FOREIGN KEY fk_book;
-- ALTER TABLE wishlist DROP FOREIGN KEY fk_user;

-- drop tables if they exist
DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS user;

/*
    Create table(s)
*/
CREATE TABLE store (
    store_id    INT             NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
);

CREATE TABLE book (
    book_id     INT             NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    author      VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    PRIMARY KEY(book_id)
);

CREATE TABLE user (
    user_id         INT         NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75) NOT NULL,
    last_name       VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id) 
);

CREATE TABLE wishlist (
    wishlist_id     INT         NOT NULL    AUTO_INCREMENT,
    user_id         INT         NOT NULL,
    book_id         INT         NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_Id)
);

/*
    insert store record 
*/
INSERT INTO store(locale)
    VALUES('123 Main Street, Anytown USA');

/*
    insert book records 
*/
INSERT INTO book(book_name, author, details)
    VALUES('The Alchemist', 'Paulo Coelho', 'A novel about following your dreams.');

INSERT INTO book(book_name, author, details)
    VALUES('1984', 'George Orwell', 'A dystopian novel about a totalitarian society.');

INSERT INTO book(book_name, author, details)
    VALUES('To Kill a Mockingbird', 'Harper Lee', 'A novel about racism and injustice in the American South.');

INSERT INTO book(book_name, author, details)
    VALUES('Pride and Prejudice', 'Jane Austen', 'A classic novel about love and society.');

INSERT INTO book(book_name, author)
    VALUES('The Cat in the Hat', 'Dr. Seuss');

INSERT INTO book(book_name, author)
    VALUES('Harry Potter', 'J.K. Rowling');

INSERT INTO book(book_name, author)
    VALUES('The Picture of Dorian Gray', 'Oscar Wilde');

/*
    insert user
*/ 
INSERT INTO user(first_name, last_name) 
    VALUES('Alice', 'Smith');

INSERT INTO user(first_name, last_name)
    VALUES('Bob', 'Johnson');

INSERT INTO user(first_name, last_name)
    VALUES('Charlie', 'Garcia');

/*
    insert wishlist records 
*/
INSERT INTO wishlist(user_id, book_id)
VALUES (
(SELECT user_id FROM user WHERE first_name = 'Alice'),
(SELECT book_id FROM book WHERE book_name = 'The Alchemist')
);
INSERT INTO wishlist(user_id, book_id)
VALUES (
(SELECT user_id FROM user WHERE first_name = 'Bob'),
(SELECT book_id FROM book WHERE book_name = '1984')
);
INSERT INTO wishlist(user_id, book_id)
VALUES (
(SELECT user_id FROM user WHERE first_name = 'Charlie'),
(SELECT book_id FROM book WHERE book_name = 'The Picture of Dorian Gray')
);
