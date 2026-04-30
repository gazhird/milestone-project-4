

function showCategory() {
    // Hide all
    document.querySelectorAll('.category-display').forEach(function(box) {
    box.style.display = 'none';
    });

    // Show selected
    const selectedValue = document.getElementById('select-category').value;
    document.getElementById(selectedValue).style.display = 'block';
    }

    // Show first on page load
    showCategory();

    // change when different category selected
    document.getElementById('select-category').addEventListener('change', showCategory);
    
        