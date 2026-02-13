const toggle = document.getElementById("themeToggle");

if (toggle) {
    toggle.addEventListener("click", () => {
        document.body.classList.toggle("dark-mode");

        localStorage.setItem(
            "theme",
            document.body.classList.contains("dark-mode") ? "dark" : "light"
        );
    });
}

window.onload = () => {
    if (localStorage.getItem("theme") === "dark") {
        document.body.classList.add("dark-mode");
    }
};

function toggleDetails(id) {
    const element = document.getElementById(id);
    if (element) {
        element.style.display =
            element.style.display === "block" ? "none" : "block";
    }
}
