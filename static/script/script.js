// // Wait for the document to be fully loaded
// document.addEventListener('DOMContentLoaded', function () {

//     // Ensure the form is submitted properly
//     const form = document.getElementById('upload-form');
//     const submitButton = document.querySelector('.cta-btn-upload');
    
//     // Add a loader or spinner when the form is being processed
//     form.addEventListener('submit', function (e) {
//         // Prevent default form submission to handle with JavaScript (if needed)
//         e.preventDefault();
        
//         // Show a loading indicator
//         submitButton.innerHTML = "Submitting...";
//         submitButton.disabled = true; // Disable the button to prevent multiple submissions

//         // Simulate form submission (this can be replaced with an actual AJAX call)
//         setTimeout(() => {
//             // Simulate successful submission and restore the button text
//             alert('Form submitted successfully!');
//             submitButton.innerHTML = "Submit Data";
//             submitButton.disabled = false; // Enable the button again
//         }, 2000); // Wait for 2 seconds before simulating submission
//     });

//     // Smooth Scroll for navigation links
//     const scrollLinks = document.querySelectorAll('nav a');
//     scrollLinks.forEach(link => {
//         link.addEventListener('click', function (e) {
//             e.preventDefault();
//             const targetId = this.getAttribute('href').substring(1);
//             const targetElement = document.getElementById(targetId);
            
//             window.scrollTo({
//                 top: targetElement.offsetTop - 50, // Adjust the offset if needed
//                 behavior: 'smooth'
//             });
//         });
//     });

//     // Change background color when the 'Upload Your Data' button is clicked
//     const uploadButton = document.querySelector('.cta-btn');
//     if (uploadButton) {
//         uploadButton.addEventListener('click', function () {
//             document.body.style.backgroundColor = '#e0f7fa'; // Light blue background
//             document.querySelector('#hero').style.backgroundColor = '#00838f'; // Hero section color
//         });
//     }

//     // Dynamic input validation feedback
//     const inputs = document.querySelectorAll('input, select');
//     inputs.forEach(input => {
//         input.addEventListener('blur', function () {
//             if (!this.validity.valid) {
//                 this.style.borderColor = 'red'; // Invalid input feedback
//             } else {
//                 this.style.borderColor = '#ddd'; // Reset valid input styling
//             }
//         });
//     });

// });
