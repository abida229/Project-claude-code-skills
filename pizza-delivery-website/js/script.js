// Mobile Navigation Toggle
document.addEventListener('DOMContentLoaded', function() {
    const hamburger = document.querySelector('.hamburger');
    const navMenu = document.querySelector('.nav-menu');

    if (hamburger && navMenu) {
        hamburger.addEventListener('click', function() {
            hamburger.classList.toggle('active');
            navMenu.classList.toggle('active');
        });

        // Close mobile menu when clicking on a link
        document.querySelectorAll('.nav-menu a').forEach(link => {
            link.addEventListener('click', () => {
                hamburger.classList.remove('active');
                navMenu.classList.remove('active');
            });
        });
    }

    // Smooth scrolling for navigation links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();

            const targetId = this.getAttribute('href');
            const targetElement = document.querySelector(targetId);

            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop - 70, // Account for fixed header
                    behavior: 'smooth'
                });
            }
        });
    });

    // Form submission handling
    const orderForm = document.getElementById('order-form');
    if (orderForm) {
        orderForm.addEventListener('submit', function(e) {
            e.preventDefault();

            // Get form data
            const formData = new FormData(orderForm);
            const orderData = {};

            for (let [key, value] of formData.entries()) {
                orderData[key] = value;
            }

            // Calculate total price
            let basePrice = 0;
            switch(orderData.pizza) {
                case 'margherita': basePrice = 12.99; break;
                case 'pepperoni': basePrice = 14.99; break;
                case 'vegetarian': basePrice = 13.99; break;
                case 'bbq-chicken': basePrice = 16.99; break;
                case 'supreme': basePrice = 17.99; break;
                case 'hawaiian': basePrice = 15.99; break;
            }

            let sizePrice = 0;
            switch(orderData.size) {
                case 'small': sizePrice = 0; break;
                case 'medium': sizePrice = 2; break;
                case 'large': sizePrice = 4; break;
            }

            const totalPrice = (basePrice + sizePrice) * parseInt(orderData.quantity);

            // Show confirmation
            alert(`Thank you for your order, ${orderData.name}!\n\n` +
                  `Pizza: ${orderData.pizza.replace('-', ' ').replace(/\b\w/g, l => l.toUpperCase())}\n` +
                  `Size: ${orderData.size.charAt(0).toUpperCase() + orderData.size.slice(1)}\n` +
                  `Quantity: ${orderData.quantity}\n` +
                  `Total Price: $${totalPrice.toFixed(2)}\n` +
                  `Delivery Time: ${orderData['delivery-time'] || 'ASAP'}\n` +
                  `Delivery Address: ${orderData.address}`);

            // Here you would normally send the order to a server
            console.log('Order submitted:', orderData);

            // Reset form
            orderForm.reset();
        });
    }

    // Newsletter form submission
    const newsletterForm = document.querySelector('.newsletter-form');
    if (newsletterForm) {
        newsletterForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const emailInput = this.querySelector('input[type="email"]');
            if (emailInput.value) {
                alert(`Thank you for subscribing with ${emailInput.value}! You'll receive our latest offers.`);
                emailInput.value = '';
            }
        });
    }

    // Add current year to footer
    const yearSpan = document.querySelector('.footer-bottom p');
    if (yearSpan) {
        const currentYear = new Date().getFullYear();
        yearSpan.innerHTML = `&copy; ${currentYear} Pizza Delight. All rights reserved.`;
    }

    // Add animation to menu items when they come into view
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = 1;
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);

    const menuItems = document.querySelectorAll('.menu-item');
    menuItems.forEach(item => {
        item.style.opacity = 0;
        item.style.transform = 'translateY(20px)';
        item.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
        observer.observe(item);
    });
});

// Additional utility functions
function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
}

function validatePhone(phone) {
    const re = /^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$/;
    return re.test(phone);
}

// Scroll to top functionality
window.onscroll = function() {
    // Add scroll effect to header
    const navbar = document.querySelector('.navbar');
    if (window.scrollY > 100) {
        navbar.style.background = 'rgba(255, 255, 255, 0.95)';
        navbar.style.backdropFilter = 'blur(10px)';
    } else {
        navbar.style.background = '#fff';
        navbar.style.backdropFilter = 'none';
    }
};