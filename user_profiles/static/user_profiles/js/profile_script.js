// Prevent auto sliding
// Allows continuous looping when clicking next/prev
document.addEventListener("DOMContentLoaded", function () {
    // controls profile card carousel behaviour
    var profileCarousel = document.getElementById("profileCarousel");
    var carouselInstance = new bootstrap.Carousel(profileCarousel, {
        interval: false,
        wrap: true
    });

    // Handles preview display for profile picture 
    const fileInput = document.getElementById("id_profile_picture");
    const previewImg = document.querySelector(".profile-picture");

    if (fileInput && previewImg) {
        fileInput.addEventListener("change", function () {
            const file = fileInput.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = function (e) {
                    previewImg.src = e.target.result;
                };
                reader.readAsDataURL(file);
            }
        });
    }

    // Auto uppercase in postal code
    const postcodeInput = document.getElementById("id_default_postcode");
    if (postcodeInput) {
        postcodeInput.addEventListener("input", function () {
            this.value = this.value.toUpperCase();
        });
    }

    /** 
     * Triggers second modal during process for account deletion request
     * Request second confirmation from user
    */
    const confirmDeleteBtn = document.getElementById("confirmDeleteBtn");
    const finalDeleteBtn = document.getElementById("finalDeleteBtn");
    const deleteAccountForm = document.getElementById("deleteAccountForm");

    if (confirmDeleteBtn && finalDeleteBtn && deleteAccountForm) {
        confirmDeleteBtn.addEventListener("click", function () {
            var confirmModal = new bootstrap.Modal(document.getElementById("confirmDeleteModal"));
            confirmModal.show();
        });

        finalDeleteBtn.addEventListener("click", function () {
            deleteAccountForm.submit();
        });
    }

    // Handler for Order History and Wishlist entry in navbar profile dropdown
    const carouselEl = document.querySelector("#profileCarousel");
    const urlSlide = new URLSearchParams(window.location.search).get("slide");

    if (carouselEl && urlSlide) {
        const carousel = $(carouselEl).carousel();

        if (urlSlide === "history") {
            $(carouselEl).carousel(1);
        } else if (urlSlide === "wishlist") {
            $(carouselEl).carousel(2);
        }
    }
});
