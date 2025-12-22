// Mobile Navigation Toggle
const navToggle = document.querySelector('.nav-toggle');
const navMenu = document.querySelector('.nav-menu');
const navLinks = document.querySelectorAll('.nav-link');

navToggle.addEventListener('click', () => {
    navMenu.classList.toggle('active');
    navToggle.classList.toggle('active');
});

// Close mobile menu when clicking on a link
navLinks.forEach(link => {
    link.addEventListener('click', () => {
        navMenu.classList.remove('active');
        navToggle.classList.remove('active');
    });
});

// Active navigation link highlighting
const sections = document.querySelectorAll('.section, .hero');
const navLinksArray = Array.from(navLinks);

function highlightActiveSection() {
    let current = '';
    const scrollY = window.pageYOffset;

    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.clientHeight;
        const sectionId = section.getAttribute('id');

        if (scrollY >= sectionTop - 200) {
            current = sectionId || 'home';
        }
    });

    navLinksArray.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === `#${current}`) {
            link.classList.add('active');
        }
    });
}

window.addEventListener('scroll', highlightActiveSection);
highlightActiveSection(); // Initial call

// Smooth scroll for navigation links
navLinksArray.forEach(link => {
    link.addEventListener('click', (e) => {
        e.preventDefault();
        const targetId = link.getAttribute('href');
        const targetSection = document.querySelector(targetId);
        
        if (targetSection) {
            const offsetTop = targetSection.offsetTop - 80; // Account for fixed navbar
            window.scrollTo({
                top: offsetTop,
                behavior: 'smooth'
            });
        }
    });
});

// Navbar background on scroll
const navbar = document.querySelector('.navbar');
let lastScroll = 0;

window.addEventListener('scroll', () => {
    const currentScroll = window.pageYOffset;
    
    if (currentScroll > 100) {
        navbar.style.boxShadow = '0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1)';
    } else {
        navbar.style.boxShadow = '0 1px 2px 0 rgb(0 0 0 / 0.05)';
    }
    
    lastScroll = currentScroll;
});

// Intersection Observer for fade-in animations
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

// Observe all sections and cards
const animatedElements = document.querySelectorAll(
    '.timeline-item, .project-card, .publication-item, .certificate-card, .skill-category'
);

animatedElements.forEach((el, index) => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(30px)';
    el.style.transition = `opacity 0.6s ease ${index * 0.1}s, transform 0.6s ease ${index * 0.1}s`;
    observer.observe(el);
});

// Add active class to nav links on scroll
const addActiveClass = () => {
    const scrollPosition = window.scrollY + 100;
    
    navLinksArray.forEach(link => {
        const sectionId = link.getAttribute('href').substring(1);
        const section = document.getElementById(sectionId);
        
        if (section) {
            const sectionTop = section.offsetTop;
            const sectionBottom = sectionTop + section.offsetHeight;
            
            if (scrollPosition >= sectionTop && scrollPosition < sectionBottom) {
                navLinksArray.forEach(l => l.classList.remove('active'));
                link.classList.add('active');
            }
        }
    });
};

window.addEventListener('scroll', addActiveClass);

// Handle external links
document.querySelectorAll('a[href^="http"]').forEach(link => {
    link.setAttribute('target', '_blank');
    link.setAttribute('rel', 'noopener noreferrer');
});

// Add loading animation
window.addEventListener('load', () => {
    document.body.style.opacity = '0';
    setTimeout(() => {
        document.body.style.transition = 'opacity 0.5s ease';
        document.body.style.opacity = '1';
    }, 100);
});

// Carousel Functionality
class Carousel {
    constructor(wrapper) {
        this.wrapper = wrapper;
        this.container = wrapper.querySelector('.carousel-container');
        this.track = wrapper.querySelector('.carousel-track');
        this.slides = Array.from(wrapper.querySelectorAll('.carousel-slide'));
        this.navigation = wrapper.querySelector('.carousel-navigation');
        this.prevBtn = wrapper.querySelector('.carousel-btn-prev');
        this.nextBtn = wrapper.querySelector('.carousel-btn-next');
        this.dotsContainer = wrapper.querySelector('.carousel-dots');
        this.currentIndex = 0;
        this.slidesPerView = this.getSlidesPerView();
        
        if (this.slides.length === 0) return;
        
        this.init();
    }
    
    getSlidesPerView() {
        // For 3D effect, always show 1 slide at a time
        return 1;
    }
    
    init() {
        this.createDots();
        this.updateCarousel();
        this.attachEventListeners();
        window.addEventListener('resize', () => {
            this.slidesPerView = this.getSlidesPerView();
            this.updateCarousel();
        });
    }
    
    createDots() {
        if (!this.dotsContainer) return;
        
        const totalDots = this.slides.length;
        this.dotsContainer.innerHTML = '';
        
        for (let i = 0; i < totalDots; i++) {
            const dot = document.createElement('button');
            dot.classList.add('carousel-dot');
            if (i === 0) dot.classList.add('active');
            dot.setAttribute('aria-label', `Go to slide ${i + 1}`);
            dot.addEventListener('click', () => this.goToSlide(i));
            this.dotsContainer.appendChild(dot);
        }
    }
    
    updateCarousel() {
        const slideWidth = 100;
        const translateX = -this.currentIndex * slideWidth;
        this.track.style.transform = `translateX(${translateX}%)`;
        
        // Update 3D transforms for each slide - only show current slide, hide others
        this.slides.forEach((slide, index) => {
            const relativeIndex = index - this.currentIndex;
            let transform = '';
            let zIndex = 0;
            let opacity = 1;
            
            if (relativeIndex === 0) {
                // Center slide - fully visible
                transform = 'translateZ(0) rotateY(0deg) scale(1)';
                zIndex = 3;
                opacity = 1;
            } else {
                // Hide all other slides
                transform = 'translateZ(-200px) rotateY(0deg) scale(0.95)';
                zIndex = 0;
                opacity = 0;
            }
            
            slide.style.transform = transform;
            slide.style.zIndex = zIndex;
            slide.style.opacity = opacity;
        });
        
        // Update dots
        if (this.dotsContainer) {
            const dots = this.dotsContainer.querySelectorAll('.carousel-dot');
            dots.forEach((dot, index) => {
                dot.classList.toggle('active', index === this.currentIndex);
            });
        }
        
        // Update button states
        const maxIndex = this.slides.length - 1;
        if (this.prevBtn) {
            this.prevBtn.style.opacity = this.currentIndex === 0 ? '0.5' : '1';
            this.prevBtn.style.pointerEvents = this.currentIndex === 0 ? 'none' : 'auto';
        }
        if (this.nextBtn) {
            this.nextBtn.style.opacity = this.currentIndex >= maxIndex ? '0.5' : '1';
            this.nextBtn.style.pointerEvents = this.currentIndex >= maxIndex ? 'none' : 'auto';
        }
    }
    
    goToSlide(index) {
        const maxIndex = this.slides.length - 1;
        this.currentIndex = Math.max(0, Math.min(index, maxIndex));
        this.updateCarousel();
    }
    
    next() {
        const maxIndex = this.slides.length - 1;
        if (this.currentIndex < maxIndex) {
            this.currentIndex += 1;
            this.updateCarousel();
        }
    }
    
    prev() {
        if (this.currentIndex > 0) {
            this.currentIndex -= 1;
            this.updateCarousel();
        }
    }
    
    attachEventListeners() {
        if (this.prevBtn) {
            this.prevBtn.addEventListener('click', () => this.prev());
        }
        if (this.nextBtn) {
            this.nextBtn.addEventListener('click', () => this.next());
        }
        
        // Touch/swipe support
        let startX = 0;
        let currentX = 0;
        let isDragging = false;
        
        this.track.addEventListener('mousedown', (e) => {
            isDragging = true;
            startX = e.clientX;
            this.track.style.cursor = 'grabbing';
        });
        
        this.track.addEventListener('mousemove', (e) => {
            if (!isDragging) return;
            currentX = e.clientX;
        });
        
        this.track.addEventListener('mouseup', () => {
            if (!isDragging) return;
            isDragging = false;
            this.track.style.cursor = 'grab';
            
            const diff = startX - currentX;
            if (Math.abs(diff) > 50) {
                if (diff > 0) {
                    this.next();
                } else {
                    this.prev();
                }
            }
        });
        
        this.track.addEventListener('mouseleave', () => {
            isDragging = false;
            this.track.style.cursor = 'grab';
        });
        
        // Touch events
        this.track.addEventListener('touchstart', (e) => {
            startX = e.touches[0].clientX;
        });
        
        this.track.addEventListener('touchmove', (e) => {
            currentX = e.touches[0].clientX;
        });
        
        this.track.addEventListener('touchend', () => {
            const diff = startX - currentX;
            if (Math.abs(diff) > 50) {
                if (diff > 0) {
                    this.next();
                } else {
                    this.prev();
                }
            }
        });
    }
}

// Initialize all carousels
document.addEventListener('DOMContentLoaded', () => {
    const carouselWrappers = document.querySelectorAll('.carousel-wrapper');
    carouselWrappers.forEach(wrapper => {
        new Carousel(wrapper);
    });
});

