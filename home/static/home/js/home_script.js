/**
 * Initializes event listeners for interactive elements on the webpage.
 * Waits for the DOM content to be fully loaded before executing.
 */
document.addEventListener("DOMContentLoaded", function () {
    const gallerySign = document.getElementById("gallery-sign");
    const aboutSign = document.getElementById("about-sign");
    const introSection = document.getElementById("intro");
    const cottageSection = document.getElementById("cottage-animation");
    const aboutSection = document.getElementById("about-section");
    const walkingSound = document.getElementById("walking-sound");

    /**
     * Handles the click event for the "This way to the gallery" sign.
     * Fades out the intro section, then transitions to the gallery animation
     * before redirecting to the shop page.
     */
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

    /**
     * Handles the click event for the "About Us" sign.
     * Scrolls smoothly to the "About" section of the webpage.
     */
    aboutSign.addEventListener("click", function () {
        window.scrollTo({
            top: document.getElementById("about-section").offsetTop,
            behavior: "smooth"
        });
    });


    /**
     * Starts a countdown timer that updates the countdown display every second
     * until the specified expiration time.
     *
     * @param {number} expirationTime - The expiration timestamp in milliseconds (UTC time).
     */
    function startCountdown(expirationTime) {
        let countdownElement = document.getElementById("countdown-timer");

        /**
         * Updates the countdown timer by calculating the remaining time
         * and updating the DOM element accordingly.
         */
        function updateCountdown() {
            let now = new Date().getTime();
            let timeRemaining = expirationTime - now;

            if (timeRemaining <= 0) {
                countdownElement.innerHTML = "Offer Expired";
                return;
            }

            let days = Math.floor(timeRemaining / (1000 * 60 * 60 * 24));
            let hours = Math.floor((timeRemaining % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            let minutes = Math.floor((timeRemaining % (1000 * 60 * 60)) / (1000 * 60));
            let seconds = Math.floor((timeRemaining % (1000 * 60)) / 1000);

            countdownElement.innerHTML = `${days}d ${hours}h ${minutes}m ${seconds}s`;
        }

        // Initialize and update the countdown every second
        updateCountdown();
        setInterval(updateCountdown, 1000);
    }

    // Initialize countdown with an expiration date retrieved dynamically
    let expirationDate = new Date("{{ special_offer.expiry_date|date:'Y-m-d H:i:s' }}").getTime();
    startCountdown(expirationDate);
});
