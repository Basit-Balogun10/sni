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
        objectId = object.id.split("_")[1];
        div = document.getElementById("reply-div" + objectId).style.display =
            "block";
        // console.log("now block");
        // console.log(typeof replyDiv.style.display);
    } else {
        objectId = object.id.split("_")[1];
        div = document.getElementById("reply-div" + objectId).style.display =
            "none";
        // console.log("now none");
    }
}


function alertMessage(){
    let message = 'Please refresh this page on your browser to reply to your newly submitted comment.'
    alert(message)
}