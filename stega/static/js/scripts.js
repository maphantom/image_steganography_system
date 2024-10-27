
// Function to display success message
function displaySuccessMessage(message) {
    alert("Success: " + message);
}

// Function to display error message
function displayErrorMessage(message) {
    alert("Error: " + message);
}

// Example function to validate form inputs
function validateForm() {
    var coverImage = document.getElementById("cover-image").value;
    var textToEncode = document.getElementById("text-to-encode").value;

    if (!coverImage) {
        displayErrorMessage("Please select a cover image.");
        return false;
    }

    if (!textToEncode) {
        displayErrorMessage("Please enter text to encode.");
        return false;
    }

    // Form validation successful
    return true;
}

// Example function to handle form submission
function handleSubmit() {
    if (validateForm()) {
        // Form validation successful, submit the form
        document.getElementById("main-form").submit();
    }
}