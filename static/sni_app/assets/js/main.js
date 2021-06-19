/**
 * Template Name: Mentor - v4.2.0
 * Template URL: https://bootstrapmade.com/mentor-free-education-bootstrap-theme/
 * Author: BootstrapMade.com
 * License: https://bootstrapmade.com/license/
 */
(function () {
    "use strict";

    /**
     * Easy selector helper function
     */
    const select = (el, all = false) => {
        el = el.trim();
        if (all) {
            return [...document.querySelectorAll(el)];
        } else {
            return document.querySelector(el);
        }
    };

    /**
     * Easy event listener function
     */
    const on = (type, el, listener, all = false) => {
        let selectEl = select(el, all);
        if (selectEl) {
            if (all) {
                selectEl.forEach((e) => e.addEventListener(type, listener));
            } else {
                selectEl.addEventListener(type, listener);
            }
        }
    };

    /**
     * Easy on scroll event listener
     */
    const onscroll = (el, listener) => {
        el.addEventListener("scroll", listener);
    };

    /**
     * Mobile nav toggle
     */
    on("click", ".mobile-nav-toggle", function (e) {
        select("#navbar").classList.toggle("navbar-mobile");
        this.classList.toggle("bi-list");
        this.classList.toggle("bi-x");
    });

    /**
     * Mobile nav dropdowns activate
     */
    on(
        "click",
        ".navbar .dropdown > a",
        function (e) {
            if (select("#navbar").classList.contains("navbar-mobile")) {
                e.preventDefault();
                this.nextElementSibling.classList.toggle("dropdown-active");
            }
        },
        true
    );

    /**
     * Preloader
     */
    let preloader = select("#preloader");
    if (preloader) {
        window.addEventListener("load", () => {
            preloader.remove();
        });
    }

    //Hide header on footer apperance
    var observer = new IntersectionObserver(
        function (entries) {
            if (
                document.documentElement.scrollHeight -
                    select("#footer").scrollHeight >
                window.innerHeight
            ) {
                if (entries[0].isIntersecting === true) {
                    // select("#header").style.display = "none";
                    select("#header").style.top = "-100px";
                } else {
                    // select("#header").style.display = "block";
                    select("#header").style.top = "0";
                }
            }
        },
        { threshold: [0] }
    );

    observer.observe(select("#footer"));

    // Show acitve route (nav link)
    var routes = select(".route", true);

    var navLinks = {
        Home: "",
        blog: ["blog"],
        about: ["about"],
        services: ["synergyhub", "schedule"],
        authentication: ["login", "register"],
        speakers: ["speakers"],
        organizer: ["organizer"],
        venue: ["venue"],
        sponsors: ["sponsors"],
        events: ["about"],
        "My Account": ["account"],
    };
    var url = window.location.href;

    if (
        url == "http://127.0.0.1:8000/" ||
        url == "http://localhost:8000/" ||
        url == "https://sni.world/" ||
        url == "https://www.sni.world/"
    ) {
        routes[0].className += " active";
    } else {
        var breakParent = false;
        for (navLink in navLinks) {
            console.log(navLinks[navLink]);
            for (var pos = 0; pos < navLinks[navLink].length; ) {
                console.log(navLinks[navLink][pos]);
                if (url.includes(navLinks[navLink][pos])) {
                    console.log(routes[i]);
                    routes[i].className += " active";
                    breakParent = true;
                    break;
                }

                pos += 1;
            }

            i += 1;
            if (breakParent) {
                break;
            }
        }
    }

    window.onscroll = function () {
        bottomScrollFunction();
    };

    function bottomScrollFunction() {
        if (
            document.documentElement.scrollHeight -
                select("#footer").scrollHeight <
            window.innerHeight
        ) {
            if (parseInt(select("#footer").getBoundingClientRect().y) <= 130) {
                select("#header").style.top = "-100px";
            } else {
                select("#header").style.top = "0";
            }
        }
    }

    /**
     * Animation on scroll
     */
    window.addEventListener("load", () => {
        AOS.init({
            duration: 1000,
            easing: "ease-in-out",
            once: true,
            mirror: false,
        });
    });
})();
