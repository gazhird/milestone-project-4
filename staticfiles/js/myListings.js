


document.getElementById('vehicleEditSelector').addEventListener('change', function() {
    const selectedOption = this.options[this.selectedIndex];

    if (this.value) {
        
        document.getElementById('edit_id').value = this.value;
        document.getElementById('edit_make').value = selectedOption.getAttribute('data-make');
        document.getElementById('edit_model').value = selectedOption.getAttribute('data-model');
        document.getElementById('edit_year').value = selectedOption.getAttribute('data-year');
        document.getElementById('edit_registration').value = selectedOption.getAttribute('data-registration');
        document.getElementById('edit_mileage').value = selectedOption.getAttribute('data-mileage');
        document.getElementById('edit_fuel').value = selectedOption.getAttribute('data-fuel');
        document.getElementById('edit_transmission').value = selectedOption.getAttribute('data-transmission');
        document.getElementById('edit_condition').value = selectedOption.getAttribute('data-condition');
        document.getElementById('edit_colour').value = selectedOption.getAttribute('data-colour');
        document.getElementById('edit_doors').value = selectedOption.getAttribute('data-doors');
        document.getElementById('edit_description').value = selectedOption.getAttribute('data-description');
        document.getElementById('edit_start_price').value = selectedOption.getAttribute('data-start_price');
        document.getElementById('edit_end_date').value = selectedOption.getAttribute('data-end-date');
        document.getElementById('edit_end_time').value = selectedOption.getAttribute('data-end-time');

        for (let i = 1; i <= 4; i++) {
            const imgUrl = selectedOption.getAttribute(`data-image${i}`);
            const previewElement = document.getElementById(`preview_image${i}`);
            const noPreviewElement = document.getElementById(`no_preview_image${i}`);
            
            if (imgUrl) {
                // if there is an image show the image and hide the no image tag
                previewElement.src = imgUrl;
                previewElement.style.display = 'block'; 
                noPreviewElement.style.display = 'none';
            } else {
                previewElement.src = "";
                previewElement.style.display = 'none';
                noPreviewElement.style.display = 'block';
            }
        }
        
    }
});



