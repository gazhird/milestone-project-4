



// countdown timer (vehicle.html))

// milliseconds

// Day = 86,400,000
// Hour = 3,600,000
// Minute = 60,000
// Second = 1,000

function auctionCountdown() {

const countdownElement = document.getElementById('countdown');
const deadlineString = countdownElement.getAttribute('data-deadline');

const deadlineTime = new Date(deadlineString).getTime()

const interval = setInterval(function() {
    const now = new Date().getTime();
    const difference = deadlineTime - now;

    // divide millseconds into days, hours, mins and seconds
    // then divide the modules / remainder
    const days = Math.floor(difference / (86400000));
    const hours = Math.floor((difference % (86400000)) / (3600000));
    const minutes = Math.floor((difference % (3600000)) / (60000));
    const seconds = Math.floor((difference % (60000)) / 1000);

    countdownElement.innerHTML = days + "d " + hours + "h " + minutes + "m " + seconds + "s ";


    if (difference <= 0) {
        clearInterval(interval);
        countdownElement.innerHTML = "Ended";
        return;
    }

    }, 1000);

}

window.onload = auctionCountdown;
