document.addEventListener("DOMContentLoaded", function () {
    const readMoreBtns = document.querySelectorAll(".read-more-btn");

    // Handles Read More toggle
    readMoreBtns.forEach((btn) => {
        btn.addEventListener("click", function () {
            const cardBody = this.parentElement;
            const shortText = cardBody.querySelector(".short-text");
            const fullText = cardBody.querySelector(".full-text");

            if (fullText.classList.contains("d-none")) {
                fullText.classList.remove("d-none");
                shortText.classList.add("d-none");
                this.textContent = "Read Less";
            } else {
                fullText.classList.add("d-none");
                shortText.classList.remove("d-none");
                this.textContent = "Read More";
            }
        });
    });

    // Back to top / gallery buttons
    const backToTopBtn = document.getElementById("backToTop");
    const backToGalleryBtn = document.getElementById("backToGallery");

    // Only attach scroll event if either button exists
    if (backToTopBtn || backToGalleryBtn) {
        window.addEventListener("scroll", function () {
            if (window.scrollY > 200) {
                if (backToTopBtn) {
                    backToTopBtn.style.opacity = "1";
                    backToTopBtn.style.visibility = "visible";
                }
                if (backToGalleryBtn) {
                    backToGalleryBtn.style.opacity = "1";
                    backToGalleryBtn.style.visibility = "visible";
                }
            } else {
                if (backToTopBtn) {
                    backToTopBtn.style.opacity = "0";
                    backToTopBtn.style.visibility = "hidden";
                }
                if (backToGalleryBtn) {
                    backToGalleryBtn.style.opacity = "0";
                    backToGalleryBtn.style.visibility = "hidden";
                }
            }
        });
    }

    // Smooth scroll to top
    if (backToTopBtn) {
        backToTopBtn.addEventListener("click", function () {
            window.scrollTo({
                top: 0,
                behavior: "smooth"
            });
        });
    }
});
