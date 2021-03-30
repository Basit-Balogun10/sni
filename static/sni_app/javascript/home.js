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
//Get the button:
topbutton = document.getElementById("toTop-btn");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function () {
  topscrollFunction(), bottomscrollFunction(), changePos();
};

function topscrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    topbutton.style.display = "block";
  } else {
    topbutton.style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}

bottombutton = document.getElementById("toBottom-btn");
myHeader = document.getElementById("header");
navBar = document.getElementById("navBar");

function bottomscrollFunction() {
  if (
    document.documentElement.scrollTop ==
      document.documentElement.scrollHeight - window.innerHeight ||
    document.body.scrollTop == document.body.scrollHeight - window.innerHeight
  ) {
    bottombutton.style.display = "none";
    if (window.innerWidth >= 970) {
      navBar.style.top = "-100rem";
      //      myHeader.style.display = "none";
    }
  } else {
    bottombutton.style.display = "block";
    navBar.style.top = "0";
    //    myHeader.style.display = "block";
  }
}

// When the user clicks on the button, scroll to the top of the document
function bottomFunction() {
  window.scrollTo(
    0,
    document.body.scrollHeight || document.documentElement.scrollHeight
  );
}

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
    bottombutton.style.display = "none";
  } else {
    ul.className = "navigation";
    dropdown.className = "icon";
  }
}

footer = document.getElementById("pageFooter");

var observer = new IntersectionObserver(
  function (entries) {
    if (entries[0].isIntersecting === true) {
      if (window.innerWidth < 970) {
        navBar.style.display = "none";
        // navBar.style.top = "-100rem";
        bottombutton.style.marginTop = "-10rem";
      }
    } else {
      navBar.style.display = "block";
      bottombutton.style.marginTop = "0rem";
      // navBar.style.top = "0";
    }
  },
  { threshold: [0] }
);

function changePos() {
  if (window.innerHeight < 330) {
    bottombutton.style.marginRight = "40rem";
  } else {
    bottombutton.style.marginRight = "0rem";
  }
}

observer.observe(footer);

// const [x1, x2, x3, x4] = 0;

// function distanceBetweenElements(navBar, footer) {
//   let distance = -1;

//   const x1 = navBar.offset().top;
//   const y1 = navBar.offset().left;
//   const x2 = footer.offset().top;
//   const y2 = footer.offset().left;
//   const xDistance = x1 - x2;
//   const yDistance = y1 - y2;

//   distance = Math.sqrt(xDistance * xDistance + yDistance * yDistance);

//   console.log(distance);
//   return distance;
// }
