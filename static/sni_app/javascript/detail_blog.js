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
        console.log(reportDiv);
        reportDiv.style.display = "block";
        reportDiv.classList.toggle("active-div");
        console.log(reportDiv.classList);
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
    // if (object) {
    //     var reportDiv;
    //     let objectId = object.id.split("_")[1];
    //     if (object.id.includes("comment")) {
    //         reportDiv = document.getElementById(
    //             "comment-report-div" + objectId
    //         );
    //     } else if (object.id.includes("reply")) {
    //         reportDiv = document.getElementById("reply-report-div" + objectId);
    //     }
    //     console.log(reportDiv);
    //     reportDiv.style.display = "block";
    //     reportDiv.classList.toggle("active-div");
    //     console.log(reportDiv.classList);
    // } else {
    //     let reportDivs = select(".report-div", true);
    //     reportDivs.forEach((reportDiv) => {
    //         reportDiv.style.display = "none";
    //         if (reportDiv.className.split(" ").includes("active-div")) {
    //             reportDiv.classList.toggle("active-div");
    //         }
    //     });
    // }
    // if (reportDiv.className.split(" ").includes("active-div")) {
    //     reportDiv.style.display = "none";
    // } else {
    //     reportDiv.classList.toggle("active-div");
    // }
}

function replyComment(object) {
    // rd = document.getElementById()
    // object.insertAdjacentHTML('')
    if (
        document.getElementById("reply-div" + object.id.split("_")[1]).style
            .display === "none"
    ) {
        // console.log("it's none");
        replyButtons = document.getElementsByClassName("show-reply-form");
        for (var button = 0; button < replyButtons.length; button++) {
            let id = replyButtons[button].id.split("_")[1];
            let replyDiv = document.getElementById("reply-div" + id);
            // console.log(button);
            // console.log(replyButtons[button].nextElementSibling);
            // console.log(replyButtons[button].nextElementSibling.style.display);
            if (replyDiv.style.display === "block") {
                console.log("one is block");

                replyDiv.style.display = "none";
                break;
            }
            // console.log(replyButtons[button].nextElementSibling);
            // console.log(replyButtons[button].nextElementSibling.style.display);
        }
        let objectId = object.id.split("_")[1];
        let div = (document.getElementById(
            "reply-div" + objectId
        ).style.display = "block");
        // console.log("now block");
        // console.log(typeof replyDiv.style.display);
    } else {
        let objectId = object.id.split("_")[1];
        let div = (document.getElementById(
            "reply-div" + objectId
        ).style.display = "none");
        // console.log("now none");
    }
}

function alertMessage() {
    let message =
        "Please refresh this page on your browser to reply to your newly submitted comment.";
    alert(message);
}

function selectThis(object) {
    object.classList.toggle("selected");
    console.log(object);
    console.log(object.classList);
}
