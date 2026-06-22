




// Auction multiple countdown for index.html 

function indexCountdowns() {
    const timers = document.querySelectorAll('.auction-timer');

    timers.forEach(timer => {
        const deadline = parseInt(timer.getAttribute('data-deadline-ms'));

        const interval = setInterval(function() {
            const now = new Date().getTime();
            const gap = deadline - now;

            
            if (gap <= 0) {
                clearInterval(interval);
                timer.innerHTML = "Ended";
                timer.classList.remove('text-danger');
                return;
            }

            const days = Math.floor(gap / 86400000);
            const hours = Math.floor((gap % 86400000) / 3600000);
            const minutes = Math.floor((gap % 3600000) / 60000);
            const seconds = Math.floor((gap % 60000) / 1000);
            
            let displayText = "";

            
            if (days >=1) {
                // more than 1 day 
                displayText = days + "d " + hours + "h " + minutes + "m";
            } 
            else if (hours >= 1) {
                // less than 1 day but more than 1 hour 
                displayText = hours + "h " + minutes + "m"
            }
            else {
                // less than 1 day, less than 1 hour
                displayText = minutes + "m " + seconds + "s";
                timer.classList.add('text-danger');
            }

            timer.innerHTML = displayText;

        }, 1000);
    });
}

window.onload = indexCountdowns;
