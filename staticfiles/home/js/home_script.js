/**
 * Initializes event listeners for interactive elements on the webpage.
 * Waits for the DOM content to be fully loaded before executing.
 */
document.addEventListener("DOMContentLoaded", function () {
    const gallerySign = document.getElementById("gallery-sign");
    const aboutSign = document.getElementById("about-sign");
    const introSection = document.getElementById("intro");
    const cottageSection = document.getElementById("cottage-animation");
    const animationVideo = document.getElementById("cottage-video");
    const walkingSound = document.getElementById("walking-sound");
    const aboutSection = document.getElementById("about-section");

    /**
     * Handles the click event for the "This way to the gallery" sign.
     * Fades out the intro section, then transitions to the gallery animation
     * before redirecting to the shop page.
     */
    gallerySign.addEventListener("click", function () {
        introSection.style.transition = "opacity 2s ease-out";
        introSection.style.opacity = "0";
    
        setTimeout(() => {
            introSection.style.display = "none";
            cottageSection.classList.remove("hidden");
    
            // Start video and sound
            animationVideo.style.opacity = "1";
            animationVideo.style.visibility = "visible";
            animationVideo.play().catch(error => console.error("Video play error:", error));
            walkingSound.play();
    
            // Overlay text animation
            const overlayText = document.getElementById("video-overlay");
            overlayText.style.visibility = "visible";
            overlayText.style.opacity = "1";
    
            setTimeout(() => {
                overlayText.style.opacity = "0";
            }, 2000);
    
            // Simulate animation duration before redirecting
            setTimeout(() => {
                animationVideo.style.transition = "opacity 2s ease-out";
                animationVideo.style.opacity = "0";
    
                setTimeout(() => {
                    window.location.href = "/shop/gallery/";
                }, 2000);
            }, 4000);
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
    function startCountdown() {
        let countdownElement = document.getElementById("countdown-timer");
    
        // Retrieve expiration date from the HTML element
        let expirationDateString = countdownElement.getAttribute("data-expiry");
    
        // Ensure the expiration date exists
        if (!expirationDateString) {
            countdownElement.innerHTML = "Offer Expired";
            return;
        }
    
        let expirationTime = new Date(expirationDateString).getTime();
    
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
