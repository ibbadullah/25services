document.querySelector(".done").addEventListener("click", function() {
  document.querySelector(".wrap").style.visibility = "visible";
  document.querySelector(".jar").style.display = "none";
  const update = function() {
    let bday = document.querySelector(".start").value,
      bdays = new Date(bday),
      done = bdays.getTime(),
      d = new Date(),
      mili = d.getTime(),
      tim = mili - done,
      year = Math.floor(tim / 31536000000),
      mon = Math.floor(tim / 2592000000),
      week = Math.floor(tim / 604800000),
      day = Math.floor(tim / 86400000),
      hour = Math.floor(tim / 3600000),
      min = Math.floor(tim / 60000),
      sec = Math.floor(tim / 1000);
    let fill = function(time1, time2) {
      document.querySelector(time1).innerHTML = time2;
    }
    fill(".year", year);
    fill(".mon", mon);
    fill(".week", week);
    fill(".day", day);
    fill(".hour", hour);
    fill(".min", min);
    fill(".sec", sec);
  }
  let run = setInterval(update, 1000)
})