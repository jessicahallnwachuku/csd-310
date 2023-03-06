# Import necessary modules
import sys
import mysql.connector
from mysql.connector import errorcode

# Define main menu function
def show_main_menu():
    # Display menu options
    print("What would you like to do?")
    print("1. View books")
    print("2. View store locations")
    print("3. My account")
    print("4. Create User")
    print("5. Exit program")

    # Prompt user to select an option
    choice = input("Enter your choice: ")

    # Process user's choice
    if choice == "1":
        show_books()
    elif choice == "2":
        show_locations()
    elif choice == "3":
        show_account_menu()
    elif choice == "4":
        create_user()
    elif choice == "5":
        print("Goodbye!")
        exit()
    else:
        print("Invalid choice. Please try again.\n")
        show_main_menu()

# Define account menu function
def show_account_menu():
    # Prompt user to enter their user ID
    user_id = input("Enter your user ID: ")

    # Validate user's ID
    if validate_user(user_id):
        # Display menu options
        print("What would you like to do?")
        print("1. View my Wishlist")
        print("2. Add a book to my Wishlist")
        print("3. Return to main menu")

        # Prompt user to select an option
        choice = input("Enter your choice: ")

        # Process user's choice
        if choice == "1":
            show_wishlist(user_id)
        elif choice == "2":
            show_books_to_add(user_id)
        elif choice == "3":
            show_main_menu()
        else:
            print("Invalid choice. Please try again.\n")
            show_account_menu()
    else:
        print("Invalid user ID. Please try again.\n")
        show_account_menu()

# Define function to display available books
def show_books():
    # Connect to the database
    cnx = mysql.connector.connect(user='root', password='Nathan0821.',
                              host='127.0.0.1',
                              database='whatabook')

    # Create cursor
    cursor = cnx.cursor()

    # Query database for list of all books
    query = ("SELECT book_id, book_name, author, details FROM book")

    cursor.execute(query)

    # Display results
    for (book_id, book_name, author, details) in cursor:
        print("Book ID: {}".format(book_id))
        print("Title: {}".format(book_name))
        print("Author: {}".format(author))
        print("Details: {}".format(details))
        print()

    # Close cursor and connection
    cursor.close()
    cnx.close()

# Define function to display store locations
def show_locations():
    # Connect to the database
    cnx = mysql.connector.connect(user='root', password='Nathan0821.',
                              host='127.0.0.1',
                              database='whatabook')

    # Create cursor
    cursor = cnx.cursor()

    # Query database for list of all locations
    query = ("SELECT store_id, locale FROM Store")

    cursor.execute(query)

    # Display results
    for (location_id, location_name) in cursor:
        print("Location ID: {}".format(location_id))
        print("Name: {}".format(location_name))

        # Close cursor and connection
    cursor.close()
    cnx.close()

# Define function to validate user ID
def validate_user(user_id):
    # Connect to the database
    cnx = mysql.connector.connect(user='root', password='Nathan0821.',
                              host='127.0.0.1',
                              database='whatabook')

    # Create cursor
    cursor = cnx.cursor()

    # Query database for user ID
    query = ("SELECT COUNT(1) FROM user WHERE user_id = {}".format(user_id))

    cursor.execute(query)

    # Get result of query
    result = cursor.fetchone()

    # Close cursor and connection
    cursor.close()
    cnx.close()

    # Check if user ID is valid
    if result[0] == 1:
        return True
    else:
        return False

# Define function to display user's Wishlist
def show_wishlist(user_id):
    # Connect to the database
    cnx = mysql.connector.connect(user='root', password='Nathan0821.',
                              host='127.0.0.1',
                              database='whatabook')

    # Create cursor
    cursor = cnx.cursor()

    # Query database for user's Wishlist
    query = ("SELECT b.book_id, b.book_name, b.author, b.details "
             "FROM book b "
             "INNER JOIN wishlist w ON b.book_id = w.book_id "
             "WHERE w.user_id = {}".format(user_id))

    cursor.execute(query)

    # Display results
    for (book_id, book_name, author, details) in cursor:
        print("Book ID: {}".format(book_id))
        print("Title: {}".format(book_name))
        print("Author: {}".format(author))
        print("Details: {}".format(details))
        print()

    # Close cursor and connection
    cursor.close()
    cnx.close()

# Define function to display books that can be added to user's Wishlist
def show_books_to_add(user_id):
    # Connect to the database
    cnx = mysql.connector.connect(user='root', password='Nathan0821.',
                              host='127.0.0.1',
                              database='whatabook')

    # Create cursor
    cursor = cnx.cursor()

    # Query database for books not in user's Wishlist
    query = ("SELECT book_id, book_name, author, details "
             "FROM book "
             "WHERE book_id NOT IN "
             "(SELECT book_id FROM wishlist WHERE user_id = {})".format(user_id))

    cursor.execute(query)

    # Display results
    for (book_id, book_name, author, details) in cursor:
        print("Book ID: {}".format(book_id))
        print("Title: {}".format(book_name))
        print("Author: {}".format(author))
        print("Details: {}".format(details))
        print()

    # Prompt user to select a book to add to their Wishlist
    book_id = input("Enter the ID of the book you want to add to your Wishlist: ")

    # Add book to user's Wishlist
    add_book_to_wishlist(user_id, book_id)

    # Close cursor and connection
    cursor.close()
    cnx.close()

# Define function to add a book to user's Wishlist
def add_book_to_wishlist(user_id, book_id):
    # Connect to the database
    cnx = mysql.connector.connect(user='root', password='Nathan0821.',
                              host='127.0.0.1',
                              database='whatabook')

    # Create cursor
    cursor = cnx.cursor()

    # Insert book ID and user ID into Wishlist table
    insert = ("INSERT INTO wishlist (user_id, book_id) " "VALUES ({}, {})".format(user_id, book_id))

    cursor.execute(insert)

    cnx.commit()

    print("Book with ID {} added to your Wishlist.\n".format(book_id))

    # Close cursor and connection
    cursor.close()
    cnx.close()
# Define function to create a new user
def create_user():
    # Connect to the database
    cnx = mysql.connector.connect(user='root', password='Nathan0821.',
                              host='127.0.0.1',
                              database='whatabook')

    # Create cursor
    cursor = cnx.cursor()

    # Prompt user for new user's details
    first_name = input("Enter new user's first name: ")
    last_name = input("Enter new user's last name: ")

    # Execute query to create new user
    query = "INSERT INTO user (first_name, last_name) VALUES ('{}', '{}')".format(first_name, last_name)
    cursor.execute(query)

    # Commit changes to the database
    cnx.commit()

    print("New user '{}' '{}' created.".format(first_name, last_name))

    # Close cursor and connection
    cursor.close()
    cnx.close()


# Define main function
def main():
    # Display main menu
    show_main_menu()

# Call main function
main()
