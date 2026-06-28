
// countdown timer (vehicle.html))

// milliseconds

// Day = 86,400,000
// Hour = 3,600,000
// Minute = 60,000
// Second = 1,000


function auctionCountdown() {

const countdownDiv = document.getElementById('countdown');
const deadlineMs = parseInt(countdownDiv.getAttribute('data-deadline-ms'));

const interval = setInterval(function() {
    const now = new Date().getTime();
    const difference = deadlineMs - now;

    if (difference <= 0) {
            clearInterval(interval);
            countdownDiv.innerHTML = "Ended";
            countdownDiv.classList.remove('text-danger');

            const bidForm = document.getElementById('bidding-form');
            if (bidForm) {
                bidForm.style.display = 'none';
            }

            return;
        }


        // divide millseconds into days, hours, mins and seconds
        const days = Math.floor(difference / (86400000));
        const hours = Math.floor((difference % (86400000)) / (3600000));
        const minutes = Math.floor((difference % (3600000)) / (60000));
        const seconds = Math.floor((difference % (60000)) / 1000);

        countdownDiv.innerHTML = days + "d " + hours + "h " + minutes + "m " + seconds + "s ";

        if (days >= 1) {
            // more than 1 day
            displayText = days + "d " + hours + "h " + minutes + "m";
        } 
        else if (hours >= 1) {
            // less than 1 day but more than 1 hour
            displayText = hours + "h " + minutes + "m";
        } 
        else {
            // less than 1 day, less than 1 hour
            displayText = minutes + "m " + seconds + "s";
            countdownDiv.classList.add('text-danger');
        }

        // Output the structured text to your div
        countdownDiv.innerHTML = displayText;
    

    }, 1000);

}

window.onload = auctionCountdown;

