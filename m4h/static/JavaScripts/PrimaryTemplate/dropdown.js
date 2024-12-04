function toggleDropdown() {
    var menu = document.getElementById("dropdown-menu");
    menu.style.display = menu.style.display === "block" ? "none" : "block";
}

// Închide meniul dropdown când faci clic în afara acestuia
window.onclick = function(event) {
    if (!event.target.closest(".user-profile")) {
        document.getElementById("dropdown-menu").style.display = "none";
    }
}
