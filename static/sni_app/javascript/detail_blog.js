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

function replyComment(object) {
    if (
        (object.nextElementSibling.style.display === "none") |
        (object.nextElementSibling.style.display === "")
    ) {
        replyButtons = document.getElementsByClassName("reply-button");
        for (var button = 0; button < replyButtons.length; button++) {
            if (
                replyButtons[button].nextElementSibling.style.display ===
                "block"
            ) {
                replyButtons[button].nextElementSibling.style.display = "none";
                break;
            }
            console.log(replyButtons[button].nextElementSibling);
            console.log(replyButtons[button].nextElementSibling.style.display);
        }
        replyDiv = object.nextElementSibling;
        replyDiv.style.display = "block";
        console.log(typeof replyDiv.style.display);
    } else {
        object.nextElementSibling.style.display = "none";
        console.log("now none");
    }
}
