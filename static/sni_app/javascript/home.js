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

function bottomscrollFunction() {
  if (
    document.documentElement.scrollTop ==
      document.documentElement.scrollHeight - window.innerHeight ||
    document.body.scrollTop == document.body.scrollHeight - window.innerHeight
  ) {
    bottombutton.style.display = "none";
    if (window.innerWidth >= 970) {
      myHeader.style.display = "none";
    }
  } else {
    bottombutton.style.display = "block";
    myHeader.style.display = "block";
  }
}

// When the user clicks on the button, scroll to the top of the document
function bottomFunction() {
  window.scrollTo(
    0,
    document.body.scrollHeight || document.documentElement.scrollHeight
  );
}

// Get the container element
var routeContainer = document.getElementById("myTopnav");

var routes = routeContainer.getElementsByClassName("route");

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
navBar = document.getElementById("navBar");

var observer = new IntersectionObserver(
  function (entries) {
    if (entries[0].isIntersecting === true) {
      if (window.innerWidth < 970) {
        navBar.style.display = "none";
        bottombutton.style.marginTop = "-10rem";
      }
    } else {
      bottombutton.style.marginTop = "0rem";
      navBar.style.display = "block";
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
