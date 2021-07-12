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

function activateDiv(postContainer) {
    postSummaryContainer = postContainer.children[1];
    postTime = postSummaryContainer.children[0].children[1];

    postSummaryContainer.style.background = "#002657";
    postTime.style.color = "#c582eb";
}

function deactivateDiv(postContainer) {
    let postSummaryContainer = postContainer.children[1];
    let postTime = postSummaryContainer.children[0].children[1];

    postSummaryContainer.style.background = "none";
    postTime.style.color = "#002657";
}

// on(
//     "click",
//     ".rt a",
//     (confirmReport = function (state) {
//         /* state can be 1 or 0 */
//         var containerElement = document.getElementById("main-doc");
//         var overlayEle = document.getElementById("confirm-report-overlay");

//         if (state) {
//             overlayEle.style.display = "block";
//             containerElement.setAttribute("class", "blur");
//         } else {
//             overlayEle.style.display = "none";
//             containerElement.setAttribute("class", null);
//         }
//     }),
//     true
// );

function confirmReport(state) {
    /* state can be 1 or 0 */
    var overlayEle = document.getElementById("confirm-report-overlay");
    console.log(overlayEle);

    if (state) {
        reportDivs = select(".report-div", true);
        reportDivs.forEach((reportDiv) => {
            reportDiv.style.display = "none";
            reportDiv.classList.toggle("active-div");
        });
        overlayEle.style.display = "block";
    } else {
        let popup = select("#confirmation-popup");
        popup.setAttribute("data-value", "cancel");
        overlayEle.style.display = "none";
    }
}

function makeReport(object) {
    let popup = select("#confirmation-popup");
    popup.setAttribute("data-value", "submit");
    popup.style.padding = "30px";
    popup.innerHTML =
        '<h5 class=""><i class="bi text-success bi-check-circle"></i>Your report have been successfully submitted. Our team will review this comment as soon as possible and will take the necessary actions afterwards. Thank you for trying to keep this community safe for everyone!</h5><button class="btn btn-lg btn-success" onclick="closeConfirmationPopup()">Close</button>';
}

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
        var reportDiv;
        let objectId = object.id.split("_")[1];
        if (object.id.includes("comment")) {
            reportDiv = document.getElementById(
                "comment-report-div" + objectId
            );
        } else if (object.id.includes("reply")) {
            reportDiv = document.getElementById("reply-report-div" + objectId);
        }
        console.log(reportDiv);
        reportDiv.style.display = "block";
        reportDiv.classList.toggle("active-div");
        console.log(reportDiv.classList);
    } else {
        let reportDivs = select(".report-div", true);
        reportDivs.forEach((reportDiv) => {
            reportDiv.style.display = "none";
            if (reportDiv.className.split(" ").includes("active-div")) {
                reportDiv.classList.toggle("active-div");
            }
        });
    }
    // if (reportDiv.className.split(" ").includes("active-div")) {
    //     reportDiv.style.display = "none";
    // } else {
    //     reportDiv.classList.toggle("active-div");
    // }
}

function hideReportDiv(object) {
    console.log(object);
    object.classList.toggle("d-none");
    object.classList.toggle("active-div");
    console.log(object.classList);
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
