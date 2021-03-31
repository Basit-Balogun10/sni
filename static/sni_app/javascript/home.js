// Get the container element
var routeContainer = document.getElementById("myTopnav");

var routes = routeContainer.getElementsByClassName("route");

var navLinks = [
  "Home",
  "#about",
  "#schedule",
  "speakers",
  "organizer",
  "venue",
  "sponsors",
];
url = window.location.href;
console.log(url);

if (url == "http://127.0.0.1:8000/") {
  console.log(0 + "Home-->" + routes[0].innerText + " true");
  routes[0].className += " active";
} else {
  for (var i = 1; i < navLinks.length; ) {
    if (url.includes(navLinks[i])) {
      console.log(i + navLinks[i] + "-->" + routes[i].innerText + " true");
      routes[i].className += " active";
      break;
    } else {
      console.log(i + navLinks[i] + "-->" + routes[i].innerText);
    }
    i += 1;
  }
}
myHeader = document.getElementById("header");
navBar = document.getElementById("navBar");

// Loop through the buttons and add the active class to the current/clicked button
for (var i = 0; i < routes.length; i++) {
  routes[i].addEventListener("click", function () {
    var current = document.getElementsByClassName("active");
    current[0].className = current[0].className.replace(" active", "");
    this.className += " active";
  });
}

/* Toggle between adding and removing the "responsive" class to topnav when the user clicks on the icon */
function routesDisplay() {
  var ul = document.getElementById("myTopnav");
  var dropdown = document.getElementById("dropdownIcon");
  if (ul.className === "navigation") {
    ul.className += " responsive";
    dropdown.className += " responsive";
  } else {
    ul.className = "navigation";
    dropdown.className = "icon";
  }
}

footer = document.getElementById("pageFooter");