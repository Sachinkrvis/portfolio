document.addEventListener("DOMContentLoaded", () => {
    // Select all pop-ups using the new class
    const popups = document.querySelectorAll(".popup-message");

    popups.forEach(popup => {
        // Find the close button for this specific popup
        const closeButton = popup.querySelector(".close-popup");

        // Add a click event listener to the close button
        if (closeButton) {
            closeButton.addEventListener("click", () => {
                popup.style.transition = "opacity 0.5s ease";
                popup.style.opacity = "0";
                setTimeout(() => popup.remove(), 500);
            });
        }
        
        // Auto-hide after 4 seconds
        setTimeout(() => {
            if (popup) { // Check if the popup still exists
                popup.style.transition = "opacity 0.5s ease";
                popup.style.opacity = "0";
                setTimeout(() => popup.remove(), 500);
            }
        }, 4000); 
    });
});
// document.addEventListener("DOMContentLoaded", () => {
//   const popup = document.getElementById("popup-message");
//   if (popup) {
//     setTimeout(() => {
//       popup.style.transition = "opacity 0.5s ease";
//       popup.style.opacity = "0";
//       setTimeout(() => popup.remove(), 500);
//     }, 4000); // auto hide after 4 sec
//   }
// });
