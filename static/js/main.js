document.addEventListener("DOMContentLoaded", () => {
    console.log("DOM loaded successfully..!");

    // Set current year dynamically
    document.getElementById("current-year").textContent = new Date().getFullYear();

    // Event listeners using delegation
    document.body.addEventListener("click", (event) => {
        const menuButton = document.getElementById("menu-button");
        const profileButton = document.getElementById("profile-button");
        const mobileMenu = document.getElementById("mobile-menu");
        const profileMenu = document.getElementById("profile-menu");

        // Toggle mobile menu
        if (menuButton?.contains(event.target)) {
            toggleClass(mobileMenu, "hidden");
        } else {
            mobileMenu?.classList.add("hidden");
        }

        // Toggle profile menu
        if (profileButton?.contains(event.target)) {
            toggleClass(profileMenu, "hidden");
        } else if (!profileMenu?.contains(event.target)) {
            profileMenu?.classList.add("hidden");
        }
    });
});

// Utility function to toggle a class safely
function toggleClass(element, className) {
    if (element) {
        element.classList.toggle(className);
    }
}
