

// function showCategory() {
//     // Hide all
//     document.querySelectorAll('.category-display').forEach(function(box) {
//     box.style.display = 'none';
//     });

//     // Show selected
//     const selectedValue = document.getElementById('select-category').value;
//     document.getElementById(selectedValue).style.display = 'block';
//     }

//     // Show first on page load
//     showCategory();

//     // change when different category selected
//     document.getElementById('select-category').addEventListener('change', showCategory);
    
    






// screen size displayer (Viewport) temp 
function showWidth() {
    document.body.setAttribute('data-width', window.innerWidth + 'px');
}
window.addEventListener('resize', showWidth);
showWidth();



// vehicle detail page, click image carousel 
function nextImg(x) {

    document.getElementById('image1').style.display = "none";
    document.getElementById('image2').style.display = "none";
    document.getElementById('image3').style.display = "none";
    document.getElementById('image4').style.display = "none";
    document.getElementById('image' + x ).style.display = "block";
    document.getElementById('imgNum').innerHTML = "<h4>" + x + "/4</h4>";
                
}

nextImg(1);