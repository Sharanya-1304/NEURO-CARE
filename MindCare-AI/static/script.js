/**
 * MindCare AI - Main JavaScript File
 * Handles client-side functionality and interactions
 */

// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Mobile menu toggle (if added later)
const mobileMenuToggle = document.querySelector('.mobile-menu-toggle');
const navLinks = document.querySelector('.nav-links');

if (mobileMenuToggle) {
    mobileMenuToggle.addEventListener('click', function() {
        navLinks.classList.toggle('active');
    });
}

// Health check on page load
window.addEventListener('load', async function() {
    try {
        const response = await fetch('/api/health');
        const data = await response.json();
        console.log('MindCare AI Backend Status:', data.status);
    } catch (error) {
        console.log('Backend connection status:', error.message);
    }
});

// Log page navigation
document.addEventListener('DOMContentLoaded', function() {
    console.log('MindCare AI loaded successfully');
});

// Utility function: Format percentage
function formatPercentage(value) {
    return parseFloat(value).toFixed(2) + '%';
}

// Utility function: Format number
function formatNumber(value) {
    return parseFloat(value).toFixed(2);
}

// Utility function: Get stress level color
function getStressLevelColor(level) {
    switch(level.toLowerCase()) {
        case 'low stress':
            return '#48bb78';
        case 'medium stress':
            return '#f6ad55';
        case 'high stress':
            return '#f56565';
        default:
            return '#667eea';
    }
}

// Utility function: Show notification
function showNotification(message, type = 'success') {
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.textContent = message;
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        padding: 1rem 1.5rem;
        background: ${type === 'success' ? '#48bb78' : '#f56565'};
        color: white;
        border-radius: 5px;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
        z-index: 1000;
        animation: slideIn 0.3s ease;
    `;
    
    document.body.appendChild(notification);
    
    setTimeout(() => {
        notification.style.animation = 'slideOut 0.3s ease';
        setTimeout(() => notification.remove(), 300);
    }, 3000);
}

// Add animation styles
const style = document.createElement('style');
style.textContent = `
    @keyframes slideIn {
        from {
            transform: translateX(400px);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }
    
    @keyframes slideOut {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(400px);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);

// Export functions for use in other scripts
window.MindCareAI = {
    formatPercentage,
    formatNumber,
    getStressLevelColor,
    showNotification
};
