const timer = document.getElementById('timer');
const r = document.querySelector(':root');
const mode = document.getElementById('mode');
var hr = 0;
var min = 0;
var sec = 0;
var stoptime = true;

function startTime() {
  if (stoptime == true) {
        stoptime = false;
        timeCycle();
    }
}
function stopTime() {
  if (stoptime == false) {
    stoptime = true;
  }
}

function timeCycle() {
    if (stoptime == false) {
    sec = parseInt(sec);
    min = parseInt(min);
    hr = parseInt(hr);

    sec = sec + 1;

    if (sec == 60) {
      min = min + 1;
      sec = 0;
    }
    if (min == 60) {
      hr = hr + 1;
      min = 0;
      sec = 0;
    }

    if (sec < 10 || sec == 0) {
      sec = '0' + sec;
    }
    if (min < 10 || min == 0) {
      min = '0' + min;
    }
    if (hr < 10 || hr == 0) {
      hr = '0' + hr;
    }

    timer.innerHTML = hr + ':' + min + ':' + sec;

    setTimeout("timeCycle()", 1000);
  }
}

function reset() {
    sec = 0;
    min = 0;
    hr = 0;
    timer.innerHTML = '00:00:00';
}
// COLOR SECTION
var cc = 0;
var theme = 0;
function changeMode() {
  if (cc == 0) {
    cc = 1;
  } else {
    cc = 0;
  }
  if(theme == 0) {
    if(cc == 0) {
      r.style.setProperty('--main-color', 'black');
      r.style.setProperty('--accent-color', 'yellow');
      mode.innerHTML = "light mode";
    } else if (cc == 1) {
      r.style.setProperty('--main-color', 'yellow');
      r.style.setProperty('--accent-color', 'black');
      mode.innerHTML = "dark mode";
    }
  } else if (theme == 1) {
    if(cc == 0) {
      r.style.setProperty('--main-color', 'blue');
      r.style.setProperty('--accent-color', 'white');
      mode.innerHTML = "light mode";
    } else if (cc == 1) {
      r.style.setProperty('--main-color', 'white');
      r.style.setProperty('--accent-color', 'blue');
      mode.innerHTML = "dark mode";
    }
  } else if (theme == 2) {
    if(cc == 0) {
      r.style.setProperty('--main-color', 'purple');
      r.style.setProperty('--accent-color', 'pink');
      mode.innerHTML = "light mode";
    } else if (cc == 1) {
      r.style.setProperty('--main-color', 'pink');
      r.style.setProperty('--accent-color', 'purple');
      mode.innerHTML = "dark mode";
    }
  }
}

function yb() {
  theme = 0;
  if(cc == 0) {
    r.style.setProperty('--main-color', 'black');
    r.style.setProperty('--accent-color', 'yellow');
    mode.innerHTML = "light mode";
  } else if (cc == 1) {
    r.style.setProperty('--main-color', 'yellow');
    r.style.setProperty('--accent-color', 'black');
    mode.innerHTML = "dark mode";
  }
}

function bw() {
  theme = 1;
  if(cc == 0) {
    r.style.setProperty('--main-color', 'blue');
    r.style.setProperty('--accent-color', 'white');
    mode.innerHTML = "light mode";
  } else if (cc == 1) {
    r.style.setProperty('--main-color', 'white');
    r.style.setProperty('--accent-color', 'blue');
    mode.innerHTML = "dark mode";
  }
}

function pp() {
  theme = 2;
  if(cc == 0) {
    r.style.setProperty('--main-color', 'purple');
    r.style.setProperty('--accent-color', 'pink');
    mode.innerHTML = "light mode";
  } else if (cc == 1) {
    r.style.setProperty('--main-color', 'pink');
    r.style.setProperty('--accent-color', 'purple');
    mode.innerHTML = "dark mode";
  }
}

// DROPDOWN SECTION
function showDropdown() {
  document.getElementById("myDropdown").classList.toggle("show");
}

window.onclick = function(event) {
  if (!event.target.matches('.dropbtn')) {
    var dropdowns = document.getElementsByClassName("dropdown-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
}