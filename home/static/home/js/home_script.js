document.addEventListener("DOMContentLoaded", function () {
    const gallerySign = document.getElementById("gallery-sign");
    const aboutSign = document.getElementById("about-sign");
    const introSection = document.getElementById("intro");
    const cottageSection = document.getElementById("cottage-animation");
    const aboutSection = document.getElementById("about-section");
    const walkingSound = document.getElementById("walking-sound");

    // Handle clicking "This way to the gallery"
    gallerySign.addEventListener("click", function () {
        introSection.classList.add("fade-out");

        setTimeout(() => {
            introSection.style.display = "none";
            cottageSection.style.display = "block";
            walkingSound.play();

            // Simulate walking animation
            setTimeout(() => {
                window.location.href = "/shop/";
            }, 5000);
        }, 2000);
    });

    // Handle clicking "About Us"
    aboutSign.addEventListener("click", function () {
        window.scrollTo({
            top: document.getElementById("about-section").offsetTop,
            behavior: "smooth"
        });
    });
});
