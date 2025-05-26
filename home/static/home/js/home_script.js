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
        console.log("About sign clicked!");
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
        const countdownElement = document.getElementById("countdown-timer");

        // Exit if the countdown element is missing
        if (!countdownElement) return;

        const expirationDateString = countdownElement.getAttribute("data-expiry");

        // If the date is missing or invalid
        if (!expirationDateString) {
            countdownElement.textContent = "Offer Expired";
            return;
        }

        const expirationTime = new Date(expirationDateString).getTime();

        function updateCountdown() {
            const now = new Date().getTime();
            const timeRemaining = expirationTime - now;

            if (timeRemaining <= 0) {
                countdownElement.textContent = "Offer Expired";
                return;
            }

            const days = Math.floor(timeRemaining / (1000 * 60 * 60 * 24));
            const hours = Math.floor((timeRemaining % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            const minutes = Math.floor((timeRemaining % (1000 * 60 * 60)) / (1000 * 60));
            const seconds = Math.floor((timeRemaining % (1000 * 60)) / 1000);

            countdownElement.textContent = `${days}d ${hours}h ${minutes}m ${seconds}s`;
        }

        // Start the countdown loop
        updateCountdown();
        setInterval(updateCountdown, 1000);
    }

    // Call countdown only after DOM is ready
    startCountdown();

    /**
     * Handles the removal of message alerts and their container.
     * Ensures that the container is removed only when no alerts remain.
     */
    function removeMessageContainerIfEmpty() {
        const container = document.getElementById("message-container");
        const remainingAlerts = document.querySelectorAll("#message-container .alert");
        if (container && remainingAlerts.length === 0) {
            container.remove();
        }
    }

    /**
     * Handles Bootstrap alert dismissals and auto-hide functionality.
     * Ensures clean DOM removal and avoids spacing issues.
     */
    document.querySelectorAll(".alert .btn-close").forEach(function (button) {
        button.addEventListener("click", function () {
            // Wait for Bootstrap's fade animation to complete
            setTimeout(removeMessageContainerIfEmpty, 500);
        });
    });

    setTimeout(function () {
        document.querySelectorAll("#message-container .alert").forEach(function (alertDiv) {
            alertDiv.remove();
        });
        removeMessageContainerIfEmpty();
    }, 5000);

    /**
     * Closes the navbar when clicking outside of it.
     */
    document.addEventListener("click", function (event) {
        var navbarToggler = document.querySelector(".navbar-toggler");
        var navbarCollapse = document.querySelector(".navbar-collapse");

        if (navbarCollapse && navbarToggler) {
            if (
                !navbarCollapse.contains(event.target) &&
                !navbarToggler.contains(event.target) &&
                navbarCollapse.classList.contains("show")
            ) {
                bootstrap.Collapse.getInstance(navbarCollapse).hide();
            }
        }
    });

    // Mute toggle logic
    const audioToggleBtn = document.getElementById("toggle-audio");

    if (audioToggleBtn && walkingSound) {
        audioToggleBtn.addEventListener("click", () => {
            walkingSound.muted = !walkingSound.muted;
            audioToggleBtn.textContent = walkingSound.muted ? "🔇" : "🔊";
        });
    }
});
