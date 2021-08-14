function toggleVisibility(object) {
    var input = object.previousElementSibling;
    if (input.getAttribute("type") === "password") {
        input.setAttribute("type", "text");
        object.classList.toggle("fa-eye-slash");
        object.classList.toggle("fa-eye");
    } else {
        input.setAttribute("type", "password");
        object.classList.toggle("fa-eye");
        object.classList.toggle("fa-eye-slash");
    }
}

window.addEventListener("load", function () {
    let inputs = document.getElementsByTagName("input");
    for (let input = 0; input < inputs.length; input++) {
        if (inputs[input].getAttribute("type") === "password") {
            inputs[input].insertAdjacentHTML(
                "afterEnd",
                '<span toggle="#password" class="cursor-pointer fa fa-fw fa-eye field-icon toggle-password" onclick="javascript: toggleVisibility(this);"></span>'
            );
        }
    }
});
