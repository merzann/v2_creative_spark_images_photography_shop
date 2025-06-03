document.addEventListener("DOMContentLoaded", function () {
    // READ MORE TOGGLE
    const readMoreBtns = document.querySelectorAll(".read-more-btn");
    if (readMoreBtns.length > 0) {
        readMoreBtns.forEach((btn) => {
            btn.addEventListener("click", function () {
                const cardBody = this.parentElement;
                const shortText = cardBody.querySelector(".short-text");
                const fullText = cardBody.querySelector(".full-text");

                if (shortText && fullText) {
                    const isHidden = fullText.classList.contains("d-none");

                    fullText.classList.toggle("d-none", !isHidden);
                    shortText.classList.toggle("d-none", isHidden);
                    this.textContent = isHidden ? "Read Less" : "Read More";
                }
            });
        });
    }

    // BACK TO TOP & GALLERY BUTTONS
    const backToTopBtn = document.getElementById("backToTop");
    const backToGalleryBtn = document.getElementById("backToGallery");

    if (backToTopBtn || backToGalleryBtn) {
        window.addEventListener("scroll", function () {
            const show = window.scrollY > 200;

            if (backToTopBtn) {
                backToTopBtn.style.opacity = show ? "1" : "0";
                backToTopBtn.style.visibility = show ? "visible" : "hidden";
            }

            if (backToGalleryBtn) {
                backToGalleryBtn.style.opacity = show ? "1" : "0";
                backToGalleryBtn.style.visibility = show ? "visible" : "hidden";
            }
        });
    }

    if (backToTopBtn) {
        backToTopBtn.addEventListener("click", function () {
            window.scrollTo({ top: 0, behavior: "smooth" });
        });
    }
});
