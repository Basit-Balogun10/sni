function toggleVisibility(object) {
    input = object.previousElementSibling;
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
