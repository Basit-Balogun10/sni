//Get the button:
topbutton = document.getElementById("toTop-btn");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function () {
  topscrollFunction(), bottomscrollFunction();
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

function bottomscrollFunction() {
  if (
    document.documentElement.scrollTop ==
    document.documentElement.scrollHeight - window.innerHeight
  ) {
    bottombutton.style.display = "none";
  } else {
    bottombutton.style.display = "block";
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
var routeContainer = document.getElementById("navigation");

// Get all buttons with class="route" inside the container
var routes = routeContainer.getElementsByClassName("route");

// Loop through the buttons and add the active class to the current/clicked button
for (var i = 0; i < routes.length; i++) {
  routes[i].addEventListener("click", function () {
    var current = document.getElementsByClassName("active");
    current[0].className = current[0].className.replace(" active", "");
    this.className += " active";
  });
}
