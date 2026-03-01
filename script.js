/* ============================
   SMOOTH SCROLLING & NAVIGATION
   ============================ */

// Update active nav link on scroll
window.addEventListener('scroll', () => {
    const navLinks = document.querySelectorAll('.nav-link');
    let current = '';

    const sections = document.querySelectorAll('section');
    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        if (pageYOffset >= sectionTop - 60) {
            current = section.getAttribute('id');
        }
    });

    navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href').slice(1) === current) {
            link.classList.add('active');
        }
    });
});

// Scroll to section function
function scrollToSection(sectionId) {
    const section = document.getElementById(sectionId);
    if (section) {
        section.scrollIntoView({ behavior: 'smooth' });
    }
}

// Mobile menu toggle
const hamburger = document.querySelector('.hamburger');
const navMenu = document.querySelector('.nav-menu');

if (hamburger) {
    hamburger.addEventListener('click', () => {
        navMenu.style.display = navMenu.style.display === 'flex' ? 'none' : 'flex';
    });
}

/* ============================
   IMAGE UPLOAD & PREVIEW
   ============================ */

const uploadArea = document.getElementById('uploadArea');
const imageInput = document.getElementById('imageInput');
const previewSection = document.getElementById('previewSection');
const previewImage = document.getElementById('previewImage');

// Drag and drop functionality
uploadArea.addEventListener('dragover', (e) => {
    e.preventDefault();
    uploadArea.style.borderColor = '#FF6B6B';
    uploadArea.style.backgroundColor = 'rgba(255, 107, 107, 0.1)';
});

uploadArea.addEventListener('dragleave', () => {
    uploadArea.style.borderColor = '#4ECDC4';
    uploadArea.style.backgroundColor = 'rgba(78, 205, 196, 0.05)';
});

uploadArea.addEventListener('drop', (e) => {
    e.preventDefault();
    uploadArea.style.borderColor = '#4ECDC4';
    const files = e.dataTransfer.files;
    if (files.length > 0) {
        handleImageUpload(files[0]);
    }
});

// File input change
imageInput.addEventListener('change', (e) => {
    if (e.target.files.length > 0) {
        handleImageUpload(e.target.files[0]);
    }
});

// Handle image upload
function handleImageUpload(file) {
    // Validate file
    if (!file.type.startsWith('image/')) {
        alert('Please upload an image file');
        return;
    }

    if (file.size > 5 * 1024 * 1024) {
        alert('File size must be less than 5MB');
        return;
    }

    // Read file
    const reader = new FileReader();
    reader.onload = (e) => {
        previewImage.src = e.target.result;
        uploadArea.style.display = 'none';
        previewSection.style.display = 'grid';

        // Simulate analysis
        simulateAnalysis();
    };
    reader.readAsDataURL(file);
}

// Simulate damage analysis
function simulateAnalysis() {
    const resultsPlaceholder = document.getElementById('resultsPlaceholder');
    const resultsContent = document.getElementById('resultsContent');

    // Show loading state
    resultsPlaceholder.style.display = 'block';
    resultsContent.style.display = 'none';

    // Simulate processing delay
    setTimeout(() => {
        // Generate random results
        const damageTypes = ['Dent', 'Scratch', 'Paint Damage', 'Collision Damage', 'No Significant Damage'];
        const severities = ['Low', 'Medium', 'High'];
        const areas = ['Front Bumper', 'Door Panel', 'Hood', 'Rear Panel', 'Side Mirror', 'Wheel'];
        
        const randomDamage = damageTypes[Math.floor(Math.random() * damageTypes.length)];
        const randomSeverity = severities[Math.floor(Math.random() * severities.length)];
        const randomConfidence = (80 + Math.random() * 20).toFixed(1);
        const randomArea = areas[Math.floor(Math.random() * areas.length)];

        // Update results
        document.getElementById('damageType').textContent = randomDamage;
        document.getElementById('severity').textContent = randomSeverity;
        document.getElementById('confidence').textContent = randomConfidence + '%';
        document.getElementById('area').textContent = randomArea;

        // Generate recommendations
        const recommendations = getRecommendations(randomSeverity);
        document.getElementById('recommendations').textContent = recommendations;

        // Update severity color
        const severityElement = document.getElementById('severity');
        severityElement.classList.remove('severity-high');
        if (randomSeverity === 'High') {
            severityElement.classList.add('severity-high');
        }

        // Show results
        resultsPlaceholder.style.display = 'none';
        resultsContent.style.display = 'flex';
    }, 2500);
}

// Get recommendations based on severity
function getRecommendations(severity) {
    const recommendations = {
        'Low': 'Minor damage detected. Consider professional inspection for preventive maintenance. Touch-up paint recommended.',
        'Medium': 'Moderate damage detected. Visit a certified repair shop for detailed assessment. Estimated repair time: 2-5 days.',
        'High': 'Severe damage detected. Immediate professional repair recommended. Contact insurance for assessment. Estimated repair time: 1-2 weeks.'
    };

    return recommendations[severity] || 'Please consult with a professional mechanic for detailed assessment.';
}

// Reset detector
function resetDetector() {
    uploadArea.style.display = 'block';
    previewSection.style.display = 'none';
    imageInput.value = '';
}

/* ============================
   CONTACT FORM
   ============================ */

const contactForm = document.querySelector('.contact-form');

if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
        e.preventDefault();
        
        // Get form values
        const name = contactForm.querySelector('input[type="text"]').value;
        const email = contactForm.querySelector('input[type="email"]').value;
        const message = contactForm.querySelector('textarea').value;

        // Validate
        if (!name || !email || !message) {
            alert('Please fill in all fields');
            return;
        }

        // Simulate sending
        const originalText = e.target.textContent;
        const submitBtn = contactForm.querySelector('.submit-btn');
        submitBtn.textContent = 'Sending...';
        submitBtn.disabled = true;

        setTimeout(() => {
            alert(`Thank you for your message, ${name}! We'll get back to you soon.`);
            contactForm.reset();
            submitBtn.textContent = 'Send Message';
            submitBtn.disabled = false;
        }, 1500);
    });
}

/* ============================
   INITIAL PAGE SETUP
   ============================ */

document.addEventListener('DOMContentLoaded', () => {
    // Fade in animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -100px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);

    // Observe feature cards and stat cards
    document.querySelectorAll('.feature-card, .stat-card, .category-item').forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(20px)';
        el.style.transition = 'all 0.5s ease';
        observer.observe(el);
    });
});

/* ============================
   UTILITY FUNCTIONS
   ============================ */

// Format large numbers
function formatNumber(num) {
    return num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',');
}

// Log analytics event (for integration with analytics service)
function trackEvent(eventName, eventData) {
    console.log(`Event: ${eventName}`, eventData);
    // TODO: Integrate with Firebase, Google Analytics, etc.
}
