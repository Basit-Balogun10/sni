// Get the container element
var routeContainer = document.getElementById("myTopnav");

// var routes = routeContainer.getElementsByClassName("route");

// var navLinks = [
//     "Home",
//     "blog",
//     "schedule",
//     "speakers",
//     "organizer",
//     "venue",
//     "sponsors",
// ];
// url = window.location.href;

// if (
//     url == "http://127.0.0.1:8000/" ||
//     url == "http://localhost:8000/" ||
//     url == "https://sni.world/" ||
//     url == "https://www.sni.world/"
// ) {
//     routes[0].className += " active";
//     // routes[1].addEventListener("click", function () {
//     //   routes[0].className = routes[0].className.replace(" active", "");
//     //   routes[1].className += " active";
//     // });
// } else {
//     for (var i = 1; i < navLinks.length; ) {
//         if (url.includes(navLinks[i])) {
//             routes[i].className += " active";
//             break;
//         }
//         // else if (url == "http://127.0.0.1:8000/blog/trending" || url == "http://localhost:8000/blog/trending" || url == "https://sni.world/blog/trending" || url == "https://www.sni.world/blog/trending") {
//         //             routes[1].className += " active";
//         //           }
//         i += 1;
//     }
// }
myHeader = document.getElementById("header");
navBar = document.getElementById("navBar");

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
