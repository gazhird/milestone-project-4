


// Navbar Clock 
function liveClock() {
    const d = new Date();

    const dayClock = d.getDay();   
    const dateClock = d.getDate(); 
    const monthClock = d.getMonth();      
    const yearClock = d.getFullYear();  
    const hoursClock = d.getHours();
    const minutesClock = d.getMinutes().toString().padStart(2, '0');
    const secondsClock = d.getSeconds().toString().padStart(2, '0');

    dayArray = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
    monthArray = ['Jan','Feb','March','April','May','June','July','August','Sep','Oct','Nov','Dec'];

    function dateDressing(dateClock) {
    if (dateClock === 1 || dateClock === 21 || dateClock === 31) {
     return dateClock + "st";
    }
    if (dateClock === 2 || dateClock === 22) {
     return dateClock + "nd";
    }
    if (dateClock === 3 || dateClock === 23) {
     return dateClock + "rd";
    }
    return dateClock + "th";
    }

    let clockString = dayArray[dayClock] + ' ' + dateDressing(dateClock) + ' ' + monthArray[monthClock] + ' ' + yearClock + ' ' + hoursClock + ':' + minutesClock + ':' + secondsClock;

    document.getElementById("clock").innerHTML = clockString;
    }

    liveClock();
    setInterval(liveClock, 1000);




// Auction multiple countdown for index.html 

function indexCountdowns() {
    const timers = document.querySelectorAll('.auction-timer');

    timers.forEach(timer => {
        const deadline = new Date(timer.getAttribute('data-deadline')).getTime();

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
            
            let displayTime = "";

            
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
