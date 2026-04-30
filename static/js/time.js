


// Navbar Clock 
function liveClock() {
    const d = new Date();

    const dayClock = d.getDay();   
    const dateClock = d.getDate(); 
    const monthClock = d.getMonth();      
    const yearClock = d.getFullYear();  
    const hoursClock = d.getHours();
    const minutesClock = d.getMinutes();
    const secondsClock = d.getSeconds().toString().padStart(2, '0');

    dayArray = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'];
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
