// Prevent auto sliding
// Allows continuous looping when clicking next/prev
document.addEventListener("DOMContentLoaded", function () {
    var profileCarousel = document.getElementById("profileCarousel");
    var carouselInstance = new bootstrap.Carousel(profileCarousel, {
        interval: false,
        wrap: true
    });
});
