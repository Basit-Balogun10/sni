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
     * Quick log in
     */
    on("click", "#quick-login-toggle", function () {
        let quickLoginDiv = select("#quick-login");
        let quickLoginShortcut = select("#quick-login-shortcut");
        quickLoginDiv.style.display = "none";
        quickLoginShortcut.style.display = "block";
    });

    on("click", "#expand-quick-login", function () {
        let quickLoginDiv = select("#quick-login");
        quickLoginDiv.style.display = "block";
    });

    /**
     * Preloader
     */
    let preloader = select("#preloader");
    if (preloader) {
        window.addEventListener("load", () => {
            preloader.remove();
        });
    }

    const scrollProgress = document.getElementById("scroll-progress");
    const height =
        document.documentElement.scrollHeight -
        document.documentElement.clientHeight;

    window.addEventListener("scroll", () => {
        const scrollTop =
            document.body.scrollTop || document.documentElement.scrollTop;
        scrollProgress.style.width = `${(scrollTop / height) * 100}%`;
    });

    //Hide header on footer apperance
    var observer = new IntersectionObserver(
        function (entries) {
            if (
                document.documentElement.scrollHeight -
                    select("#footer").scrollHeight >
                window.innerHeight
            ) {
                if (entries[0].isIntersecting === true) {
                    select("#header").style.top = "-100px";
                } else {
                    select("#header").style.top = "0";
                }
            }
        },
        { threshold: [0] }
    );

    observer.observe(select("#footer"));

    var routes = select(".route", true);

    var navLinks = {
        Home: "",
        Blog: ["blog"],
        About: ["about"],
        Schedule: ["schedule"],
        Speakers: ["speakers"],
        Organizer: ["organizer"],
        Venue: ["venue"],
        Sponsors: ["sponsors"],
        Events: ["about"],
        "My Account": ["account", "login", "register"],
    };
    var url = window.location.href;

    var breakParent = false;
    for (var navLink in navLinks) {
        for (var pos = 0; pos < navLinks[navLink].length; ) {
            if (url.includes(navLinks[navLink][pos])) {
                for (var i = 0; i < routes.length; i++) {
                    if (routes[i].innerText.includes(navLink)) {
                        routes[i].className += " active";
                        break;
                    }
                }
                breakParent = true;
                break;
            }

            pos += 1;
        }

        if (breakParent) {
            break;
        }
    }

    if (select(".route.active")) {
    } else {
        routes[0].className = "route active";
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
     * Blog post search
     */
    on("click", "#open-search-div", function () {
        let overlay = select("#search-div");
        overlay.style.display = "block";
    });

    on("mouseover", "#open-search-div", function () {
        this.innerHTML = "Looking for a blog post?";
        this.style.width = "250px";
    });

    on("mouseout", "#open-search-div", function () {
        this.innerHTML = '<i class="fa fa-search"></i>';
        this.style.width = "50px";
    });

    on("click", "#close-search-div", function () {
        let overlay = select("#search-div");
        overlay.style.display = "none";
    });

    /**
     * Animation on scroll
     */
    window.addEventListener("load", () => {
        AOS.init({
            duration: 1000,
            easing: "ease-in-out",
            once: false,
            mirror: true,
        });
    });
})();
