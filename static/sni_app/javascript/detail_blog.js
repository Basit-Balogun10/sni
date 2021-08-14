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

function closeConfirmationPopup() {
    let overlay = select("#confirm-report-overlay");
    let popup = select("#confirmation-popup");
    overlay.style.display = "none";
    popup.children[0].classList.toggle("d-none");
    popup.children[1].classList.toggle("d-none");
    popup.style.padding = "50px";
}

function controlAboutDiv(state = null) {
    if (state) {
        let overlay = select("#about-div");
        overlay.style.display = "block";
    } else {
        let overlay = select("#about-div");
        overlay.style.display = "none";
    }
}

function controlReportDiv(object = null) {
    if (object) {
        let objectId = object.id.split("_")[1];
        let reportDiv = document.getElementById("report-div");
        let reportForm = document.getElementById("report-form");
        let reportUl = document.getElementById("rt-ul");
        if (object.id.includes("comment")) {
            reportDiv.id = "comment-report-div" + objectId;
            reportUl.setAttribute("targ", "comment");
        } else if (object.id.includes("reply")) {
            reportDiv.id = "reply-report-div" + objectId;
            reportUl.setAttribute("targ", "reply");
        }
        reportForm.id = "report-form" + objectId;
        reportForm.setAttribute("value", objectId);
        reportUl.setAttribute("data-catid", objectId);
        reportDiv.style.display = "block";
        reportDiv.classList.toggle("active-div");
    } else {
        let reportUl = document.getElementById("rt-ul");
        reportUl.setAttribute("data-catid", "");

        let reportDiv = select(".report-div");
        reportDiv.style.display = "none";
        reportDiv.id = "report-div";

        if (reportDiv.className.split(" ").includes("active-div")) {
            reportDiv.classList.toggle("active-div");
        }

        let reportForm = select(".report-form");
        reportForm.id = "report-form";
        reportForm.setAttribute("value", objectId);
    }
}

function replyComment(object) {
    if (
        document.getElementById("reply-div" + object.id.split("_")[1]).style
            .display === "none"
    ) {
        replyButtons = document.getElementsByClassName("show-reply-form");
        for (var button = 0; button < replyButtons.length; button++) {
            let id = replyButtons[button].id.split("_")[1];
            let replyDiv = document.getElementById("reply-div" + id);
            if (replyDiv.style.display === "block") {
                replyDiv.style.display = "none";
                break;
            }
        }
        let objectId = object.id.split("_")[1];
        let div = (document.getElementById(
            "reply-div" + objectId
        ).style.display = "block");
    } else {
        let objectId = object.id.split("_")[1];
        let div = (document.getElementById(
            "reply-div" + objectId
        ).style.display = "none");
    }
}

function alertMessage() {
    let message =
        "Please refresh this page on your browser to reply to your newly submitted comment.";
    alert(message);
}

function selectThis(object) {
    object.classList.toggle("selected");
}

//Changer heade bg-color on scrolling away from hero section
var observer = new IntersectionObserver(
    function (entries) {
        if (entries[0].isIntersecting === false) {
            select("#header").style.backgroundColor = "#002657";
        } else {
            select("#header").style.backgroundColor = "rgb(255, 255, 255, 0)";
        }
    },
    { threshold: [0] }
);

observer.observe(select("#hero"));
