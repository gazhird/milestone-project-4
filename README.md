


#### New Project 'Top Bidder Auctions'

Milestone Project 4 
Auction site 

By Gary Hird
20th of April 2026


### Under construction 

I am currently developing this site

## Design

I am using a Dark Theme for this new application as i like the blackbackground and the contrast of white text.



## Development

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

### Bids

Despite planning without this table i have decided to include a database which handles the bids
with a foreign keys to link to listing, the buyer and seller.

## Notifications

The 4th table design to update users with information such as:
- "You the top bidder"
- "Sorry, you was outbid"
- "Your listing sold"
- "Your listing did not sell"



### Development Notes

## Listing status

Small issue with the listing status column not auto changing from 'Active' to 'Ended' 
i will have to trigger this when a user clicks to view its details and secondary if a user try's to bid on a listing that has already ended 

When a vehicle detail is requested. i have place a check 'is_expired' in vehicle details function / views.py and then a conditional statement in the html to show or hide the bidding box depending on the end time not the status column as planned. 

Final if_expired check made as bids are submitted 



### Heroku 


Migrate
- python manage.py makemigrations 
- python manage.py migrate

CSS 
- python manage.py collectstatic

Commit 
- heroku login
- git push heroku main
- heroku open


Errors
 - heroku logs --tail