// Handles click event for Read More button
document.addEventListener("DOMContentLoaded", function () {
    const readMoreBtns = document.querySelectorAll(".read-more-btn");

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

    // Handles click event for Back-to-top button
    const backToTopBtn = document.getElementById("backToTop");
    const backToGalleryBtn = document.getElementById("backToGallery");

    window.addEventListener("scroll", function () {
        if (window.scrollY > 200) {
            backToTopBtn.style.opacity = "1";
            backToTopBtn.style.visibility = "visible";
            backToGalleryBtn.style.opacity = "1";
            backToGalleryBtn.style.visibility = "visible";
        } else {
            backToTopBtn.style.opacity = "0";
            backToTopBtn.style.visibility = "hidden";
            backToGalleryBtn.style.opacity = "0";
            backToGalleryBtn.style.visibility = "hidden";
        }
    });

    // Scroll to top when the Back to Top button is clicked
    backToTopBtn.addEventListener("click", function () {
        window.scrollTo({
            top: 0,
            behavior: "smooth"
        });
    });
});
