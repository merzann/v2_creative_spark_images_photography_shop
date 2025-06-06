// Prevent auto sliding
// Allows continuous looping when clicking next/prev
document.addEventListener("DOMContentLoaded", function () {

    // controls profile card carousel behaviour
    var profileCarousel = document.getElementById("profileCarousel");
    var carouselInstance = new bootstrap.Carousel(profileCarousel, {
        interval: false,
        wrap: true
    });

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

    // Handler for My-Order_history navbar dropdown
    const carouselEl = document.querySelector("#profileCarousel");
    const urlSlide = new URLSearchParams(window.location.search).get("slide");

    if (urlSlide === "history" && carouselEl) {
    
    const carousel = $(carouselEl).carousel();
    $(carouselEl).carousel(1);  
    }
});
