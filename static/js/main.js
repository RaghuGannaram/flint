console.log("Hello from main.js");

document.getElementById("menu-button")?.addEventListener("click", function () {
    console.log("menu button clicked");
    document.getElementById("mobile-menu").classList.toggle("hidden");
});

document.getElementById("profile-button")?.addEventListener("click", function () {
    console.log("profile button clicked");
    document.getElementById("profile-menu").classList.toggle("hidden");
});

document.getElementById("profile-menu")?.addEventListener("click", function (event) {
    if (!profileButton.contains(event.target) && !profileMenu.contains(event.target)) {
        document.getElementById("profile-menu").classList.add("hidden");
    }
});
