document.addEventListener("DOMContentLoaded", function () {
    const readMoreButtons = document.querySelectorAll(".read-more-btn");

    readMoreButtons.forEach((button) => {
        button.addEventListener("click", function () {
            const cardBody = this.closest(".card-body");
            
            const shortText = cardBody.querySelector(".short-text");
            const fullText = cardBody.querySelector(".full-text");
            const card = cardBody.closest(".card");

            // Expand: Hide short text, show full text, and let card grow
            if (fullText.classList.contains("d-none")) {
                shortText.classList.add("d-none");
                fullText.classList.remove("d-none");
                this.textContent = "Read Less";

                card.style.minHeight = "auto";
            } else {
                shortText.classList.remove("d-none");
                fullText.classList.add("d-none");
                this.textContent = "Read More";

                card.style.minHeight = ""; 
            }
        });
    });
});
