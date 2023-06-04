# Phase 3 Example Project - Hotel CLI

## Introduction

This is an example Phase 3 Project that uses the SQLAlchemy ORM with 1 table in the database. This Hotel CLI allows you to Create new hotels, Read information about existing hotels, Update the name of an existing hotel, and Delete existing hotels from the database.

## Setup

1. Fork and then Clone this repository.
2. Make sure that you are in the correct directory (folder) that contains a `Pipfile`, then run `pipenv install` in your terminal to install the required libraries.
3. Now that your `pipenv` virtual environment is ready to use, enter `pipenv shell` to enter the virtual environment.
4. Enter the command `cd lib` in the terminal to move into the lib directory.
5. Enter the command `python cli.py` in the terminal to start running my Python CLI.

## While running my Python CLI:

Follow the instructions presented in the terminal. Choose from the following options:
- Enter ‘c’ and press the ‘return’ key to create a new hotel
- Enter ‘r’ and press the ‘return’ key to get / read info about hotels
- Enter ‘u’ and press the ‘return’ key to update existing hotels
- Enter ‘d’ and press the ‘return’ key to delete hotels

If you enter a character other than those 4 characters, you will see an invalid input message display and you will be prompted to enter input into the terminal again. It must be either ‘c’, ‘r’, ‘u’, or ‘d’.

Create —> ‘c’:
- If you entered the value of ‘c’ in the terminal, you will then be prompted to enter the name for the hotel you would like to create. Enter the name for the hotel that you would like to create and then press the ‘return’ key.
- The new hotel will then be created and a message will display saying that the new hotel has been created along with the name of the new hotel.

Read —> ‘r’:
- If you entered the value of ‘r’ in the terminal, you will be able to see the information for all hotels from the hotels table.

Update —> ‘u’:
- If you entered the value of ‘u’ in the terminal, you will be able to see the information for all hotels from the hotels table, and you will then be prompted to enter the integer value for the id of the hotel that you would like to update. Enter an integer value for an id for a hotel that currently exists. Entering any other value that is not a whole number / integer will result in an error, so please be careful. Entering an integer value for an id for a hotel that does not exist will also result in an error.
- After entering the integer value for the id for the hotel that you want to update, you will then be prompted to enter the name that you would like to update that hotel to.
- The name of the hotel will then be updated to be the name that you entered and a message will display saying that the hotel has been updated to have the name that you updated it to.

Delete —> ‘d’:
- If you entered the value of ‘d’ in the terminal, you will be able to see the information for all hotels from the hotels table, and you will then be prompted to enter the integer value for the id of the hotel that you would like to delete.
- If you enter the ‘a’ character in the terminal and press the ‘return’ key, this will result in all hotels being deleted from the database and a message will display saying that all hotels have been deleted from the database.
- If you choose to enter an integer instead, you must enter an integer value for an id for a hotel that currently exists. Entering any other value that is not a whole number / integer will result in an error, so please be careful. Entering an integer value for an id for a hotel that does not exist will also result in an error.
- After entering the integer value for the id of the hotel that you want to delete, that hotel will then be deleted from the database and a message will display saying that the hotel has been deleted from the database.
