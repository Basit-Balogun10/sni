function toggleVisibility(object) {
    console.log(object);
    input = object.previousElementSibling;
    console.log(input);
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
