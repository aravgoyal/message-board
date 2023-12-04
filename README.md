# Message Board

## Overview

This is a basic message board web application that utilizes Python, HTML, and the Flask framework. Users can post and view anonymous, time-stamped messages from other users in descending order.

## Components and Interactions

### Flask App (app.py) 
This is the main application file containing the Flask server setup, routes, and message handling logic.

### HTML Template (templates/index.html)
This is the template file that defines the structure and style of the web pages. It includes input forms for posting messages, a button to submit messages, and a section to display messages.

### CSS Styles (within index.html)
This includes simple styles to enhance the visual appearance of the message blocks and form elements.

## Requirements
The application fulfills the specified requirements by providing the following features:
- Users can type a message and post it to the message board.
- Messages are displayed on the board from most to least recent.
- Users on different computers can post to the same board and view each other’s messages.
- Messages have a maximum length of 128 characters.

## How to Start the Application

1. Clone the repository: git clone https://github.com/aravgoyal/message-board.git
2. Navigate to the project directory: cd message-board
3. Run the Flask application in terminal: python app.py
4. Navigate to given address.
