document.addEventListener('DOMContentLoaded', (event) => {
    const detailsElements = document.querySelectorAll('details[name="hobbies"]');
    const hobbyImage = document.querySelector(".hobby-image");
    console.log(hobbyImage)

    detailsElements.forEach((details) => {
        details.addEventListener('toggle', function(){
            if(details.open){
                hobbyImage.style.backgroundImage = `url(${details.getAttribute('data-image-url')})`;
                // hobbyImage.style.transition = 'all 0.3s ease-in-out';
            }
        })
    })
})