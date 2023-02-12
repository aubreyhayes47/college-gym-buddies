# College Gym Buddies
## Inspiration
One of the biggest challenges I have faced while losing weight over the last two years, (75 pounds as of February 2023), has been holding myself accountable for exercise. My wife is wonderful, supportive, and the best cheerleader I have. Unfortunately, she's less than half my size. Finding someone who I connect with, that pushes me, and that also has access to the Temple University gym has proven to be a challenge.

## What it does
College Gym Buddies addresses one of the biggest issues people face while embarking on or continuing their fitness journey, finding someone to be fit with. After registering with an email address ending in ".edu", users are able to connect with other students, faculty, and staff at their university. 

Profile pictures and editable bios allow students to share their favorite exercise, potential gym schedule, or any other information they might find relevant. The private message system allows users to connect and discuss the specifics of what they might do together, when they might do it, and how they can contact each other. Of course, users can also block others if they no longer want to see or message with them.

## How I built it
The backend of the website is built with Python using the Flask micro-framework. Python's sqlite3 module connects with a database holding user profiles, messages, universities, and all other data for the app. Jinja templates dynamically render HTML webpages and the Bootstrap framework cleans it all up.

## Challenges I ran into
Some of the SQL queries ended up being a little more complicated than I planned, but dynamically saving picture files to a directory named after the user was really the biggest challenge. It took a quite awhile, but I eventually was able to allow users to upload and update profile pictures and their user profile displays the most recent upload.

## Accomplishments that I'm proud of
I will say it was quite fun to architect and build a messaging system. There are some tweaks I could make from it, but being able to send, receive, and reply to messages while filtering based on your conversation partner, really brought the site up to the next level.

## What I learned
I really dived deep into Bootstrap this time around. Flex containers, rows, and navbars are all tools I've used before without understanding as well as I do now. The "card" container is really the main feature of the site and ended up being perfect for what I was looking for. (After an hour or two of tweaking)

## What's next for College Gym Buddies
Improving the user experience when sending and receiving messages, email notifications, and potential deployment could all be in the future. First up will definitely be email verification. Right now, a registration success email is sent, but it doesn't actually verify the user's account.
