document.addEventListener('DOMContentLoaded', () => {
    // ==========================================================================
    // 0. Hero Background Slider
    // ==========================================================================
    const heroSlides = document.querySelectorAll('.hero-bg-slide');
    const heroDotsContainer = document.getElementById('heroDots');
    
    if (heroSlides.length > 1) {
        let currentHeroIdx = 0;
        const slideInterval = 5000; // transition every 5 seconds
        let autoPlayTimer = null;
        
        // Generate dots dynamically
        if (heroDotsContainer) {
            heroSlides.forEach((_, idx) => {
                const dot = document.createElement('button');
                dot.classList.add('hero-dot');
                if (idx === 0) dot.classList.add('active');
                dot.setAttribute('aria-label', `Slide ${idx + 1}`);
                
                dot.addEventListener('click', () => {
                    goToSlide(idx);
                    resetTimer();
                });
                
                heroDotsContainer.appendChild(dot);
            });
        }
        
        const dots = heroDotsContainer ? heroDotsContainer.querySelectorAll('.hero-dot') : [];
        
        function goToSlide(idx) {
            heroSlides[currentHeroIdx].classList.remove('active');
            if (dots.length > 0) dots[currentHeroIdx].classList.remove('active');
            
            currentHeroIdx = idx;
            
            heroSlides[currentHeroIdx].classList.add('active');
            if (dots.length > 0) dots[currentHeroIdx].classList.add('active');
        }
        
        function nextSlide() {
            const nextIdx = (currentHeroIdx + 1) % heroSlides.length;
            goToSlide(nextIdx);
        }
        
        function startAutoPlay() {
            autoPlayTimer = setInterval(nextSlide, slideInterval);
        }
        
        function stopAutoPlay() {
            if (autoPlayTimer) {
                clearInterval(autoPlayTimer);
            }
        }
        
        function resetTimer() {
            stopAutoPlay();
            startAutoPlay();
        }
        
        // Start playing
        startAutoPlay();
    }

    // ==========================================================================
    // 1. Mobile Menu Toggle
    // ==========================================================================
    const menuToggle = document.getElementById('menuToggle');
    const navMenu = document.getElementById('navMenu');
    
    if (menuToggle && navMenu) {
        menuToggle.addEventListener('click', () => {
            navMenu.classList.toggle('show');
            menuToggle.classList.toggle('active');
            
            // Toggle hamburger icon animation
            const bars = menuToggle.querySelectorAll('.bar');
            if (menuToggle.classList.contains('active')) {
                bars[0].style.transform = 'rotate(-45deg) translate(-5px, 6px)';
                bars[1].style.opacity = '0';
                bars[2].style.transform = 'rotate(45deg) translate(-5px, -6px)';
            } else {
                bars[0].style.transform = 'none';
                bars[1].style.opacity = '1';
                bars[2].style.transform = 'none';
            }
        });
    }

    // ==========================================================================
    // 2. Language Selector Dropdown
    // ==========================================================================
    const langSelectors = document.querySelectorAll('.lang-selector');
    
    langSelectors.forEach(selector => {
        const btn = selector.querySelector('.lang-btn');
        const dropdown = selector.querySelector('.lang-dropdown');
        
        if (btn && dropdown) {
            btn.addEventListener('click', (e) => {
                e.stopPropagation();
                // Close other dropdowns
                document.querySelectorAll('.lang-dropdown.show').forEach(d => {
                    if (d !== dropdown) {
                        d.classList.remove('show');
                        const relatedBtn = d.previousElementSibling;
                        if (relatedBtn) relatedBtn.setAttribute('aria-expanded', 'false');
                    }
                });
                
                dropdown.classList.toggle('show');
                const expanded = btn.getAttribute('aria-expanded') === 'true' || false;
                btn.setAttribute('aria-expanded', !expanded);
            });
            
            // Close dropdown when clicking outside
            document.addEventListener('click', (e) => {
                if (!btn.contains(e.target)) {
                    dropdown.classList.remove('show');
                    btn.setAttribute('aria-expanded', 'false');
                }
            });
        }
    });

    // ==========================================================================
    // 3. TripAdvisor Review Slider (Testimonials)
    // ==========================================================================
    const reviewsTrack = document.getElementById('reviewsTrack');
    const sliderPrev = document.getElementById('sliderPrev');
    const sliderNext = document.getElementById('sliderNext');
    const sliderDotsContainer = document.getElementById('sliderDots');
    
    if (reviewsTrack) {
        const slides = reviewsTrack.querySelectorAll('.review-slide');
        let currentIndex = 0;
        const totalSlides = slides.length;
        
        // Generate dots
        if (sliderDotsContainer && totalSlides > 1) {
            slides.forEach((_, idx) => {
                const dot = document.createElement('div');
                dot.classList.add('slider-dot');
                if (idx === 0) dot.classList.add('active');
                dot.addEventListener('click', () => goToSlide(idx));
                sliderDotsContainer.appendChild(dot);
            });
        }
        
        const dots = sliderDotsContainer ? sliderDotsContainer.querySelectorAll('.slider-dot') : [];
        
        function updateSlider() {
            slides.forEach((slide, idx) => {
                if (idx === currentIndex) {
                    slide.classList.add('active');
                    slide.style.display = 'block';
                } else {
                    slide.classList.remove('active');
                    slide.style.display = 'none';
                }
            });
            
            // Update dots
            dots.forEach((dot, idx) => {
                if (idx === currentIndex) {
                    dot.classList.add('active');
                } else {
                    dot.classList.remove('active');
                }
            });
        }
        
        function goToSlide(index) {
            currentIndex = index;
            updateSlider();
        }
        
        function nextSlide() {
            currentIndex = (currentIndex + 1) % totalSlides;
            updateSlider();
        }
        
        function prevSlide() {
            currentIndex = (currentIndex - 1 + totalSlides) % totalSlides;
            updateSlider();
        }
        
        if (sliderNext) sliderNext.addEventListener('click', nextSlide);
        if (sliderPrev) sliderPrev.addEventListener('click', prevSlide);
        
        // Auto play slider every 6 seconds
        let autoPlayInterval = setInterval(nextSlide, 6000);
        
        // Pause auto play on hover
        const sliderWrapper = document.querySelector('.reviews-slider-container');
        if (sliderWrapper) {
            sliderWrapper.addEventListener('mouseenter', () => clearInterval(autoPlayInterval));
            sliderWrapper.addEventListener('mouseleave', () => {
                clearInterval(autoPlayInterval);
                autoPlayInterval = setInterval(nextSlide, 6000);
            });
        }
        
        // Initial setup
        updateSlider();
    }

    // ==========================================================================
    // 3b. Reviews Read More (Mobile Optimization)
    // ==========================================================================
    const reviewTexts = document.querySelectorAll('.review-text');
    const maxChars = 200; // adjust as needed
        
    // Get the translated "Read More" text from the container, fallback to "Lire plus"
    const sliderContainer = document.querySelector('.reviews-slider-container');
    const readMoreText = sliderContainer && sliderContainer.dataset.readMore ? sliderContainer.dataset.readMore : "Lire plus";

    reviewTexts.forEach(p => {
        const originalText = p.innerHTML.trim();
        if (originalText.length > maxChars) {
            const truncated = originalText.substring(0, maxChars) + '...';
            p.setAttribute('data-full-text', originalText);
            p.setAttribute('data-truncated-text', truncated);
            p.innerHTML = `${truncated} <a href="#" class="read-more-link" style="color:var(--color-secondary); font-weight:bold;">${readMoreText}</a>`;
            
            const link = p.querySelector('.read-more-link');
            link.addEventListener('click', (e) => {
                e.preventDefault();
                p.innerHTML = originalText;
            });
        }
    });

    // ==========================================================================
    // 3c. Room Details Modal (Mobile Optimization)
    // ==========================================================================
    const detailBtns = document.querySelectorAll('.btn-show-details');
    detailBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            const card = e.target.closest('.room-showcase-content');
            if (card) {
                const modal = card.querySelector('.room-details-modal');
                if (modal) {
                    modal.classList.add('show');
                }
            }
        });
    });

    const closeBtns = document.querySelectorAll('.modal-close');
    closeBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            const modal = e.target.closest('.room-details-modal');
            if (modal) {
                modal.classList.remove('show');
            }
        });
    });

    // Close modal on click outside
    const modals = document.querySelectorAll('.room-details-modal');
    modals.forEach(modal => {
        modal.addEventListener('click', (e) => {
            if (e.target === modal) {
                modal.classList.remove('show');
            }
        });
    });


    // 4. Booking Bar Date Initialization & Form Handling
    // ==========================================================================
    const bookingForm = document.getElementById('bookingForm');
    const barCheckIn = document.getElementById('barCheckIn');
    const barCheckOut = document.getElementById('barCheckOut');
    
    if (bookingForm && barCheckIn && barCheckOut) {
        const today = new Date();
        const tomorrow = new Date(today);
        tomorrow.setDate(tomorrow.getDate() + 1);
        
        const dayAfterTomorrow = new Date(tomorrow);
        dayAfterTomorrow.setDate(dayAfterTomorrow.getDate() + 1);
        
        // Format to YYYY-MM-DD
        const formatDate = (date) => {
            const yyyy = date.getFullYear();
            let mm = date.getMonth() + 1;
            let dd = date.getDate();
            if (mm < 10) mm = '0' + mm;
            if (dd < 10) dd = '0' + dd;
            return `${yyyy}-${mm}-${dd}`;
        };
        
        // Set values and min limits
        barCheckIn.min = formatDate(today);
        barCheckIn.value = formatDate(tomorrow);
        barCheckOut.min = formatDate(tomorrow);
        barCheckOut.value = formatDate(dayAfterTomorrow);
        
        // Dynamic dates check out update
        barCheckIn.addEventListener('change', () => {
            const selectedIn = new Date(barCheckIn.value);
            const nextMinOut = new Date(selectedIn);
            nextMinOut.setDate(nextMinOut.getDate() + 1);
            
            barCheckOut.min = formatDate(nextMinOut);
            
            // Auto advance checkout if needed
            const currentOut = new Date(barCheckOut.value);
            if (currentOut <= selectedIn) {
                barCheckOut.value = formatDate(nextMinOut);
            }
        });
        
        // Form submit integration: Intercept and build final URL with query params
        bookingForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const actionUrl = bookingForm.getAttribute('action');
            const inVal = barCheckIn.value;
            const outVal = barCheckOut.value;
            const adultsVal = document.getElementById('barGuests').value;
            
            // Build dynamic url: .../booking/room?start_date=YYYY-MM-DD&end_date=YYYY-MM-DD&adults=X&children=0#RoomSelection-BE
            const finalUrl = `${actionUrl}?start_date=${inVal}&end_date=${outVal}&adults=${adultsVal}&children=0#RoomSelection-BE`;
            window.open(finalUrl, '_blank', 'noopener');
        });
    }

    // ==========================================================================
    // 5. Gallery Filter Logic
    // ==========================================================================
    const filterButtons = document.querySelectorAll('#galleryFilters .filter-btn');
    const galleryItems = document.querySelectorAll('#galleryGrid .gallery-item');
    
    if (filterButtons.length > 0 && galleryItems.length > 0) {
        filterButtons.forEach(btn => {
            btn.addEventListener('click', () => {
                // Active class toggle
                filterButtons.forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                
                const filterValue = btn.getAttribute('data-filter');
                
                galleryItems.forEach(item => {
                    const category = item.getAttribute('data-category');
                    if (filterValue === 'all' || category === filterValue) {
                        item.style.display = 'block';
                    } else {
                        item.style.display = 'none';
                    }
                });
            });
        });
    }

    // ==========================================================================
    // 6. Gallery Lightbox Modal
    // ==========================================================================
    const lightboxModal = document.getElementById('lightboxModal');
    const lightboxImg = document.getElementById('lightboxImg');
    const lightboxClose = document.getElementById('lightboxClose');
    const lightboxPrev = document.getElementById('lightboxPrev');
    const lightboxNext = document.getElementById('lightboxNext');
    
    if (lightboxModal && lightboxImg && galleryItems.length > 0) {
        let activeImages = [];
        let currentImageIdx = 0;
        
        // Collect current active images in the view
        function getActiveImages() {
            return Array.from(galleryItems).filter(item => item.style.display !== 'none');
        }
        
        galleryItems.forEach(item => {
            item.addEventListener('click', () => {
                activeImages = getActiveImages();
                currentImageIdx = activeImages.indexOf(item);
                
                showLightbox();
            });
        });
        
        function showLightbox() {
            const targetImg = activeImages[currentImageIdx].querySelector('.gallery-img');
            lightboxImg.src = targetImg.src;
            lightboxImg.alt = targetImg.alt;
            lightboxModal.classList.add('show');
            document.body.style.overflow = 'hidden'; // Stop page scroll
            lightboxModal.setAttribute('aria-hidden', 'false');
        }
        
        function closeLightbox() {
            lightboxModal.classList.remove('show');
            document.body.style.overflow = 'auto'; // Restore scroll
            lightboxModal.setAttribute('aria-hidden', 'true');
        }
        
        function showNextImage() {
            currentImageIdx = (currentImageIdx + 1) % activeImages.length;
            showLightbox();
        }
        
        function showPrevImage() {
            currentImageIdx = (currentImageIdx - 1 + activeImages.length) % activeImages.length;
            showLightbox();
        }
        
        if (lightboxClose) lightboxClose.addEventListener('click', closeLightbox);
        if (lightboxNext) lightboxNext.addEventListener('click', showNextImage);
        if (lightboxPrev) lightboxPrev.addEventListener('click', showPrevImage);
        
        // Close on backdrop click
        lightboxModal.addEventListener('click', (e) => {
            if (e.target === lightboxModal) {
                closeLightbox();
            }
        });
        
        // Keyboard controls
        document.addEventListener('keydown', (e) => {
            if (!lightboxModal.classList.contains('show')) return;
            
            if (e.key === 'Escape') {
                closeLightbox();
            } else if (e.key === 'ArrowRight') {
                showNextImage();
            } else if (e.key === 'ArrowLeft') {
                showPrevImage();
            }
        });
    }

    // ==========================================================================
    // 7. Contact Form Validations
    // ==========================================================================
    const contactForm = document.getElementById('contactForm');
    const contactSuccess = document.getElementById('contactSuccess');
    const contactError = document.getElementById('contactError');
    
    if (contactForm) {
        // reCAPTCHA key selection based on hostname (Local vs Production)
        const isLocal = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1';
        const siteKey = isLocal ? '6Ld7y2AtAAAAAJBrVvBYBTNzBpDXkuv63a4ZxYnA' : '6LcNy2AtAAAAAOojzTnLrjQm_jwW8pd1z3RXFK68';
        
        // Dynamically load Google reCAPTCHA v3 script
        const recaptchaScript = document.createElement('script');
        recaptchaScript.src = `https://www.google.com/recaptcha/api.js?render=${siteKey}`;
        recaptchaScript.async = true;
        document.head.appendChild(recaptchaScript);
        
        // Google Apps Script Web App URL (Option A: Combined single script URL)
        const APPS_SCRIPT_URL = 'https://script.google.com/macros/s/AKfycbw7HniCOh8mLk68NxUrcrSJ5cDxVdcKB4IYAUp9wroS4Aa5BtPBehIi9TtIQSLUPHmA_A/exec';
        
        contactForm.addEventListener('submit', (e) => {
            e.preventDefault();
            
            const nameInput = document.getElementById('contactName');
            const emailInput = document.getElementById('contactEmail');
            const subjectInput = document.getElementById('contactSubject');
            const messageInput = document.getElementById('contactMessage');
            
            let isValid = true;
            
            // Clean alerts
            if (contactSuccess) contactSuccess.classList.add('d-none');
            if (contactError) contactError.classList.add('d-none');
            
            // Reset validation states
            [nameInput, emailInput, messageInput].forEach(input => {
                if (input) {
                    input.classList.remove('is-invalid');
                    const feedback = input.nextElementSibling;
                    if (feedback && feedback.classList.contains('error-feedback')) {
                        feedback.textContent = '';
                    }
                }
            });
            
            // Name Check
            if (!nameInput.value.trim()) {
                setNameError(nameInput, 'Veuillez saisir votre nom.');
                isValid = false;
            }
            
            // Email Check
            if (!emailInput.value.trim()) {
                setNameError(emailInput, 'Veuillez saisir votre adresse e-mail.');
                isValid = false;
            } else if (!validateEmail(emailInput.value)) {
                setNameError(emailInput, 'Veuillez saisir une adresse e-mail valide.');
                isValid = false;
            }
            
            // Message Check
            if (!messageInput.value.trim()) {
                setNameError(messageInput, 'Veuillez saisir votre message.');
                isValid = false;
            }
            
            if (isValid) {
                const submitBtn = document.getElementById('contactSubmitBtn');
                const origBtnText = submitBtn.textContent;
                
                // Translated sending status
                const lang = document.documentElement.lang || 'fr';
                let loadingText = 'Sending...';
                if (lang === 'fr') loadingText = 'Envoi en cours...';
                else if (lang === 'de') loadingText = 'Wird gesendet...';
                else if (lang === 'it') loadingText = 'Invio in corso...';
                else if (lang === 'es') loadingText = 'Enviando...';
                else if (lang === 'ru') loadingText = 'Отправка...';
                
                submitBtn.disabled = true;
                submitBtn.textContent = loadingText;
                
                // Execute reCAPTCHA to get token
                grecaptcha.ready(() => {
                    grecaptcha.execute(siteKey, {action: 'submit'}).then((token) => {
                        const payload = {
                            name: nameInput.value.trim(),
                            email: emailInput.value.trim(),
                            subject: subjectInput ? subjectInput.value.trim() : '',
                            message: messageInput.value.trim(),
                            recaptchaToken: token,
                            isLocal: isLocal
                        };
                        
                        fetch(APPS_SCRIPT_URL, {
                            method: 'POST',
                            headers: {
                                'Content-Type': 'text/plain;charset=utf-8'
                            },
                            body: JSON.stringify(payload)
                        })
                        .then(() => {
                            submitBtn.disabled = false;
                            submitBtn.textContent = origBtnText;
                            if (contactSuccess) contactSuccess.classList.remove('d-none');
                            contactForm.reset();
                        })
                        .catch((err) => {
                            console.error('Error submitting form:', err);
                            submitBtn.disabled = false;
                            submitBtn.textContent = origBtnText;
                            if (contactError) contactError.classList.remove('d-none');
                        });
                    }).catch((err) => {
                        console.error('reCAPTCHA token error:', err);
                        submitBtn.disabled = false;
                        submitBtn.textContent = origBtnText;
                        if (contactError) contactError.classList.remove('d-none');
                    });
                });
            } else {
                if (contactError) contactError.classList.remove('d-none');
            }
        });
        
        function setNameError(input, message) {
            input.classList.add('is-invalid');
            const feedback = input.nextElementSibling;
            if (feedback && feedback.classList.contains('error-feedback')) {
                feedback.textContent = message;
            }
        }
        
        function validateEmail(email) {
            const re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
            return re.test(String(email).toLowerCase());
        }
    }
});
