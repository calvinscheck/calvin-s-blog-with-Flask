// Toggling the dark and light mode. This is done using the button in base.html

document.addEventListener("DOMContentLoaded", function () {
    let themeToggle = document.getElementById("theme-toggle");
  
    themeToggle.addEventListener("click", function () {
        document.body.classList.toggle("dark-mode");
    });
});
