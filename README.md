# OpenGameEngine
A coding language for all your coding language needs.
=
# Installation Steps
For people who just want to use the program:
Install the binary in the releases page: 
https://github.com/3DGameMaker/OpenGameEngine/releases/latest

Then, follow the instructions in the installer
This is only for win 64 but it might work on 32

Now, open the command prompt and run "oge", then your path to your code,
e.g if you have a file in your C drive you might put 
"oge C:\funnyfile.oge"
of course without the brackets.
here is a test one for you to try (form.oge)

create window

set title to "TEST"

set size to 400x300

set background to #f0f8ff

add text "hallo this is a text"

add input "name_field"

add checkbox "I agree to terms"

add button "Submit"

on close "Thank you for participating!"

Limitations:
=
1. You can't run it from a folder,
e.g you cant go into your C drive and run "oge form", 
you have to go "oge C:\form.oge"
2. Its limited, e.g no varibles or anything like that. will work on that in the future..
All the commands:
=
Window Commands:
create window - Creates a new window (destroys any existing window)

set title to "title text" - Sets the window title

set size to WxH - Sets the window size (e.g., 400x300)

set background to "color" - Sets the window background color

Widget Commands:
add text "text content" - Adds a text label to the window

add button "button text" - Adds a button to the window

add input "name" - Adds an input field (optionally with a name for reference)

add checkbox "label text" - Adds a checkbox with the given label

Action Commands:
show message "message text" - Shows a message box with the given text

on close "message text" - Sets a message to show when the window is closed

Notes:
All string arguments can be enclosed in either single or double quotes

Commands are case-insensitive (processed in lowercase)

Empty lines and lines starting with # are ignored

The script must be provided as a command-line argument when running the program
