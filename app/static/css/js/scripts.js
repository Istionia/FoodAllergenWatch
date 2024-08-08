document.addEventListener('DOMContentLoaded', (event) => {
    console.log('DOM fully loaded and parsed');

    const form = document.getElementById('allergenForm');
    if (form) {
        form.addEventListener('submit', (e) => {
            e.preventDefault();
            const allergenInput = document.getElementById('allergenInput');
            if (allergenInput.value.trim() === '') {
                alert('Please enter an allergen.');
            } else {
                form.submit();
            }
        });
    }
});
