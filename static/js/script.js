document.addEventListener("DOMContentLoaded", function () {
    /**
     * Removes the message container if it exists and contains no alerts.
     */
    function removeMessageContainerIfEmpty() {
        const container = document.getElementById("message-container");
        const remainingAlerts = document.querySelectorAll("#message-container .alert");
        if (container && remainingAlerts.length === 0) {
            container.remove();
        }
    }

    // Collapse navbar when clicking on dropdown items
    document.querySelectorAll('.dropdown-menu .dropdown-item').forEach((item) => {
        item.addEventListener('click', function () {
            const navbarCollapse = document.querySelector('.navbar-collapse');
            const instance = bootstrap.Collapse.getInstance(navbarCollapse);
            if (instance) {
                instance.hide();
            }
        });
    });

    /**
     * Handle Bootstrap alert dismissals properly.
     * Removes alert elements and cleans up the container.
     */
    const closeButtons = document.querySelectorAll(".alert .btn-close, .alert .close");
    if (closeButtons.length > 0) {
        closeButtons.forEach(function (button) {
            button.addEventListener("click", function (event) {
                const alertDiv = event.target.closest(".alert");
                if (alertDiv) {
                    alertDiv.remove();
                }
                removeMessageContainerIfEmpty();
            });
        });
    }

    /**
     * Auto-hide messages after 5 seconds and clean up the container.
     */
    setTimeout(function () {
        const alerts = document.querySelectorAll("#message-container .alert");
        if (alerts.length > 0) {
            alerts.forEach(function (alertDiv) {
                alertDiv.remove();
            });
            removeMessageContainerIfEmpty();
        }
    }, 5000);

    /**
     * Close navbar if clicking outside of the toggler and menu.
     */
    document.addEventListener("click", function (event) {
        const navbarToggler = document.querySelector(".navbar-toggler");
        const navbarCollapse = document.querySelector(".navbar-collapse");

        if (navbarCollapse && navbarToggler) {
            const isClickOutside =
                !navbarCollapse.contains(event.target) &&
                !navbarToggler.contains(event.target) &&
                navbarCollapse.classList.contains("show");

            if (isClickOutside) {
                const instance = bootstrap.Collapse.getInstance(navbarCollapse);
                if (instance) {
                    instance.hide();
                }
            }
        }
    });
    
    const translations = {
        en: {
            heading: "Coming Soon",
            message: "This section of our site isn’t quite ready yet.",
            note: "We're working to bring you a refined experience in your language.",
            homeLink: "Back to Creative Spark Images"
        },
        de: {
            heading: "Seite in Vorbereitung",
            message: "Dieser Bereich unserer Website ist noch nicht verfügbar.",
            note: "Wir arbeiten daran, Creative Spark Images bald auch auf Deutsch anzubieten.",
            homeLink: "Zurück zur Startseite"
        },
        fr: {
            heading: "Page en préparation",
            message: "Cette section de notre site n’est pas encore disponible.",
            note: "Nous travaillons à vous proposer Creative Spark Images en français très bientôt.",
            homeLink: "Retour à l’accueil"
        },
        es: {
            heading: "Página en preparación",
            message: "Esta sección de nuestro sitio aún no está disponible.",
            note: "Estamos trabajando para ofrecer Creative Spark Images en español muy pronto.",
            homeLink: "Volver al inicio"
        }
    };
    
    function detectLang() {
        const urlParams = new URLSearchParams(window.location.search);
        const queryLang = urlParams.get('lang');
        if (queryLang && translations[queryLang]) {
            return queryLang;
        }
        const browserLang = navigator.language.slice(0, 2).toLowerCase();
        if (translations[browserLang]) {
            return browserLang;
        }
        return 'en';
    }
    
    const lang = detectLang();
    const t = translations[lang];

    // Update translated text
    const headingEl = document.getElementById('heading');
    if (headingEl) headingEl.textContent = t.heading;

    const messageEl = document.getElementById('message');
    if (messageEl) messageEl.textContent = t.message;

    const noteEl = document.getElementById('note');
    if (noteEl) noteEl.textContent = t.note;

    const homeLinkEl = document.getElementById('home-link');
    if (homeLinkEl) homeLinkEl.textContent = t.homeLink;


    // Update flag icon
    const flagMap = {
        en: {
            src: '/static/images/flags/uk-flag.png',
            alt: 'English'
        },
        de: {
            src: '/static/images/flags/de-flag.png',
            alt: 'Deutsch'
        },
        fr: {
            src: '/static/images/flags/fr-flag.png',
            alt: 'Français'
        },
        es: {
            src: '/static/images/flags/es-flag.png',
            alt: 'Español'
        }
    };

    const flag = flagMap[lang] || flagMap['en'];
    const flagImg = document.getElementById('current-flag');
    if (flagImg) {
        flagImg.src = flag.src;
        flagImg.alt = flag.alt;
    }

    // Check that customer added valid email in contact form
    const emailField = document.getElementById('id_email');
    if (emailField) {
        emailField.addEventListener('input', function () {
            const email = emailField.value;
            const isValid = /^[^\s@]+@[^\s@]+\.[a-zA-Z]{2,}$/i.test(email);

            if (!email) {
                emailField.classList.remove('is-valid', 'is-invalid');
            } else if (isValid) {
                emailField.classList.add('is-valid');
                emailField.classList.remove('is-invalid');
            } else {
                emailField.classList.add('is-invalid');
                emailField.classList.remove('is-valid');
            }
        });
    }
});
