
# TOP BIDDER
By Gary Hird
23rd of June 2026 (Milestone Project 4)
Python / Django / HTML / CSS / JavaScript / PostgreSQL / Stripe
Full Stack Vehicle Auction platform, deployed on Heroku.

## Introduction

I have decided to develop a full stack vehicle auction platform with a countdown timer, which will fully test my knowledge and development ability using all the languages listed above.

As this project is my final project for my 'Level 5 Diploma Web Application Development' course,
it is good to bring everything I have learnt along the journey together within one full stack platform.
Despite Milestone Project 3 introducing me to Python and Django, I have learnt a lot while producing this project and gathered a firmer understanding of the languages and methods used. 
I have enjoyed learning Python and Django and have felt quite comfortable writing and understanding the language. 
I am keen to produce further projects using more of its powerful features.
I especially enjoy the additional complexity and relationship between the buyers and sellers, and how they combine to give the platform different perspectives.


## Design

I designed this site indirectly influenced by platforms which I have used from memory, adding the kind of UX and features which I would expect to find on mainstream top rated platforms.

I started with a dark theme for this new application as I like the black background and the contrast of white text instead of a plain white background.

I didn't include a search bar for this particular project, as I included a search bar for my last project, but I will include it within a 'Future Improvements' section.

While planning this project in the early stages, I was focusing on how I would develop an auction countdown and researching how Django handles dates and times.

For the home page, I wanted to display the items in a vertical list view cascading down, as I used image cards with a horizontal scroll bar for my last project.


## UX

The site is designed for users interested in buying and selling vehicles through an auction, with no fees.
I have used a dark theme which reduces eye strain and keeps focus on the vehicle images and bidding information.

The navigation is easy to follow and use across all of the pages using Django's include feature.

The homepage displays active auctions with countdown timers so users can see what's ending soon.
 I have used JavaScript to calculate the time remaining, without seconds on the homepage due to the amount of listings that could be listed and to reduce the interval frequency. Clicking on the listing's 'Make / Model' title will show a listing detail page with more information and a more precise countdown including seconds.

The JavaScript countdown is only for UX cosmetically, it is only a visual guide and not linked to the auction's bidding. 
The listing's database 'end time and date' is exclusive.
The bidding form is only shown on active auctions and hides automatically when the auction ends.
Lazy style notifications are sent, triggered by user interaction and conditional statements. 
They are not generated automatically in a live environment. Notifications keep users updated on their auction activity without needing to refresh the page, namely 'Outbid', 'Won', 'Sold', and 'Paid'.

When a buyer uses the site after winning an auction, they have an on-screen notification adjacent to the clock under the navbar informing them of a new notification, and also a 'New' label next to the 'Notifications' link on the navigation. 
The 'Won' condition on the notification page presents the buy form which directs them to Stripe payments for secure transactions. 


## Screenshots

Mobile / Tablet / Desktop


## User Stories

### Story 1: Buyer
I want to visit the site and browse vehicles without having to register first. 

### Acceptance Criteria:
-- Display all active listings without having to register
-- Vehicle details show full information

### Story 2: Seller
I want to list my vehicle on a well presented site without paying a fee

### Acceptance Criteria:
-- Listing vehicles is free
-- Site and the listing display is well presented

### Story 3: Bidding
I want a site that's easy to bid on items with a trusted payment system
### Acceptance Criteria:
-- Simple bidding form
-- Countdown timer
-- Use Stripe payments

---------------------

## Site Purpose & Value
TopBidder is a Auction platform for users to view, buy and sell vehicles

-- Account Registration
-- Log in
-- Log out
-- View multiple Vehicle listings
-- Upload own vehicle listings
-- Edit own vehicle listings
-- Delete own vehicle listings
-- Bid on others vehicle listings
-- Buy others vehicles listings
-- Sell own vehicle listings
-- Time and Date Clock

---------------------

## Data Model
The Top Bidder app uses a relational database with the following models.

### Listings
Stores all vehicle data, including:
make, model, year, registration, mileage, fuel, transmission, condition, colour, doors, description, images, starting price, reserve price, current price, end time, status, seller, winner, and final price.

#### Relationships:
-- All listings belong to one user (the seller) with a ForeignKey
-- All listings can have multiple bids using a related_name
-- All listings can have multiple notifications using a related_name
-- When a user account is deleted, their connected listings are also deleted

### Bids
Stores bid amounts placed by users on listings.
Records the user, listing, bid amount, and timestamp.

#### Relationships:
-- Each bid belongs to one listing through a ForeignKey
-- Each bid belongs to one user (the bidder) through a ForeignKey

### Notifications
Stores messages sent to users about auction activity.
Types include: Outbid, Won, Sold, Ended with no bids.

#### Relationships:
-- Each notification belongs to one user through a ForeignKey
-- Each notification links to one listing through a ForeignKey

---------------------

## Accessibility
HTML5 elements used (main, nav, section)
All images include descriptive 'alt' attributes
Keyboard function for forms and buttons
ARIA labels for all buttons
Dark Background to avoid eye strain
Good contrast used

---------------------

## Technologies Used
HTML5 - Structure and content
CSS3 - Styling and responsive design
JavaScript - smart interaction
Bootstrap 5.2.3 - CSS framework
Font Awesome - Icons
Python - Backend logic
Django -Web Framework
PostgreSQL - Database use
Cloudinary - Image Hosting
White Noise - Loading Staid Files
Heroku - Live Database Deployment
Stripe - Secure Payments

---------------------

## DB Development

### Accounts

Users can view this site without an account but will need to 'Register and login' to upload an item for Auction or to bid on / buy an item. 

Firstly i am developing only the navbar, which once complete i will save separately as a template for future projects.
I am also planning on including the Time and Date on this Navbar using JavaScript, as later i will need to use the Javascript to help with the Auction countdown timer aspect of this Application. 
I have not used the Javascript 'Date Time Model' since 2023 so it will be good to refresh my knowledge ahead of the more complicated method of dividing milliseconds into days, hours. minutes and seconds and also using setInterval for refreshing a section of the page once every second. 


### Listings
I have added a app called 'listings' which will handle both the auction items and 'buy now' items for the website.
The upload form will only be available for 'logged in' users.
i will design the upload form first before building the backend end, as the form is the first step in the data journey to the database. 

i have decided to keep this an Auctions site for vehicles only, i was considering other categories for example 'Household', 'Electrical' and 'Garden' but after considering the table design and all additional category specific data columns,  i will just keep it as one single category and add this 'Multiple category' idea to the applications future development section.

---------------------

## Testing
I tested the site manually by checking each feature worked while developing and also checked that the developed version matched the deployed.

### Functionality Testing:
-- Registration creates a new user
-- Login and logout redirect correctly
-- Upload form validates empty fields
-- Edit form updates existing records
-- Delete removes listing from database
-- Bidding updates current price and notifies outbid user
-- Auction expiry changes status and sets winner
-- Stripe payment processes test card successfully
-- Notifications appear with correct type and message
### Automated Testing:
-- I wrote three basic automated tests using Django's TestCase framework:
-- Creating a listing saves to the database
-- Editing a listing updates the record
-- Deleting a listing removes it from the database

### Usability Testing:
-- Navigation is correct on all pages
-- Forms are easy to complete
-- Countdown timers are visible and accurate
-- Payment flow is clear and secure
### Responsiveness Testing:
-- Site tested on mobile, tablet, and desktop using Chrome DevTools
-- Bootstrap grid stacks layout correctly
-- Data Management Testing:
-- Creating a listing adds it to the database
-- Editing updates the existing record
-- Deleting removes it from the database
-- Bids link to correct listing and user
-- Notifications link to correct user and listing

---------------------

## Code Validation
- HTML validated with W3C Markup Validator (https://validator.w3.org/)
  checked using a rendered page source to not get imbedded python flags 
- CSS validated with W3C CSS Validator (https://jigsaw.w3.org/css-validator/)
- JavaScript checked with Chrome DevTools console
- Python checked with PEP8 style guid

---------------------

## Security Features
-- Secret Key: Hidden in environment variables, not in code
-- Database URL: Hidden in environment variables
-- Stripe Keys: Hidden in environment variables
-- Debug Mode: Set to False for deployment
-- CSRF Protection: Django's built-in middleware used
-- Allowed Hosts: Limited to Heroku and local development
-- Password Validation: Django's default validators used
-- WhiteNoise: Serves static files securely in production

---------------------

## Bugs & Errors

### Issue 1: CSS / Static not loading

This issue kept coming up occasionally. I found using WhiteNoise with CompressedManifestStaticFilesStorage solved this issue for production.
### Issue 2: Auction timer calculating wrong

The JavaScript countdown was showing incorrect times due to timezone parsing. I fixed this by passing Unix timestamps from Django to JavaScript instead of date strings, avoiding any timezone conversion issues.
### Issue 3: Stripe payment redirect 404

Stripe was redirecting to /payment/success/ but my URLs were prefixed with /listings/. I fixed this by moving all listings URLs to the root prefix in top_bidder/urls.py.
### Issue 4: Winner not set on auction end

The notification was telling users they won, but the database winner field was not being populated. I fixed this by adding listing.winner = winning_bid.user and listing.final_price = winning_bid.bid to the check_and_close_auctions function in utils.py.

### Issue 5: Listing status

Small issue with the listing status column not auto changing from 'Active' to 'Ended' 
i will have to trigger this when a user clicks to view its details and secondary if a user try's to bid on a listing that has already ended 

When a vehicle detail is requested. i have place a check 'is_expired' in vehicle details function / views.py and then a conditional statement in the html to show or hide the bidding box depending on the end time not the status column as planned. 

Final if_expired check made as bids are submitted 

### Issue 6: static files clash for Heroku

I believe having a folder called Static and also Staticfiles caused a conflict with Django.
This has been a small issue throughout the project and made it more challenging to compare Development and Deployment. 
I solved this by adding / copying static files manually through my terminal. 
xcopy static\* staticfiles\ /s /e /y


---------------------

## Version Control
I used GitHub throughout the project. 
Each section of development progress was committed regularly with descriptive comments. 
The repository contains the full project history,
between the 30th of April and the 23rd of June 2026


Git Repository: https://github.com/gazhird/milestone-project-4

---------------------

## Local Development

1. Clone this repository
git clone https://github.com/gazhird/milestone-project-4.git
2. Create a virtual environment
python -m venv venv
3. Activate an environment
venv\Scripts\activate
4. Install all dependencies
pip install -r requirements.txt
5. create a .env file with the following included within:
-- SECRET_KEY
-- DATABASE_URL
-- CLOUDINARY_CLOUD_NAME
-- CLOUDINARY_API_KEY
-- CLOUDINARY_API_SECRET
-- STRIPE_SECRET_KEY
-- STRIPE_PUBLISHABLE_KEY
6. Run the migrations
python manage.py migrate
7. Create a superuser
python manage.py createsuperuser
8.  Run Server
python manage.py runserver

---------------------

## Deployment (Heroku)
1. Create Heroku app: 
heroku create
2. Add PostgreSQL: 
heroku addons:create heroku-postgresql
3. Set config vars:
-- heroku config:set SECRET_KEY=...
-- heroku config:set DATABASE_URL=...
-- heroku config:set CLOUDINARY_CLOUD_NAME=...
-- heroku config:set CLOUDINARY_API_KEY=...
-- heroku config:set CLOUDINARY_API_SECRET=...
-- heroku config:set STRIPE_SECRET_KEY=...
-- heroku config:set STRIPE_PUBLISHABLE_KEY=...
4. Push code: 
git push heroku main
5. Migrate: 
heroku run python manage.py migrate
6. Collect static: 
heroku run python manage.py collectstatic
7. Open: heroku open
Live site: https://top-bidder.herokuapp.com/

---------------------

## Resources

### Documentation & Tools
W3Schools
W3C HTML Validator
W3C CSS Validator
Django Documentation
Stripe Documentation

### Reference Books
Django for Beginners - William S Vincent
Pro Django - Marty Alchin

### Additional Resources
Code Institute (walkthrough Blog Project)
YouTube Django tutorials




