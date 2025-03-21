// Prevent auto sliding
// Allows continuous looping when clicking next/prev
document.addEventListener("DOMContentLoaded", function () {

    // controls profile card carousel behaviour
    var profileCarousel = document.getElementById("profileCarousel");
    var carouselInstance = new bootstrap.Carousel(profileCarousel, {
        interval: false,
        wrap: true
    });

    // Triggers second modal during process for account deletion request
    // requesting second confirmation from user
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
});
