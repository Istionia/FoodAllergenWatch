document.addEventListener('DOMContentLoaded', () => {
    console.log('DOM fully loaded and parsed');

    const form = document.getElementById('allergenForm');
    if (form) {
        form.addEventListener('submit', handleFormSubmit);
    }
});

/**
 * Handles the form submission event.
 * @param {Event} e - The event object.
 */
function handleFormSubmit(e) {
    e.preventDefault();
    const allergenInput = document.getElementById('allergenInput');
    
    if (!allergenInput) {
        console.error('Allergen input element not found.');
        return;
    }

    if (allergenInput.value.trim() === '') {
        alert('Please enter an allergen.');
    } else {
        form.submit();
    }
}