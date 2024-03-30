// script.js
document.addEventListener('DOMContentLoaded', function() {
    const uploadForm = document.querySelector('#upload-form');
    const fileInput = document.querySelector('#file-input');
    const successMessage = document.querySelector('#success-message');

    uploadForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const formData = new FormData(uploadForm);

        try {
            const response = await fetch('/upload', {
                method: 'POST',
                body: formData,
            });

            if (response.ok) {
                successMessage.textContent = 'File uploaded successfully!';
            } else {
                successMessage.textContent = 'Error uploading file. Please try again.';
            }
        } catch (error) {
            console.error('Error:', error);
            successMessage.textContent = 'An unexpected error occurred. Please try again later.';
        }
    });
});
