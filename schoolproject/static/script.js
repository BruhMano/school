(function(){
    let btn = document.getElementById('interesting-button-img');
    let burger = document.getElementById('burger');
    let find = false;
    let navbarClasses = document.getElementsByClassName('navbar')[0].classList;
    btn.addEventListener('mouseenter', function(){
        setTimeout(() => {btn.setAttribute('src',"{% static 'button3.png' %}");}, 200);
    });
    btn.addEventListener('mouseleave', function(){
        setTimeout(() => {btn.setAttribute('src',"{% static 'button2.png' %}");}, 200);
    });
    btn.addEventListener('click', function(e){
        e.preventDefault()
        setTimeout(() => {
            console.log('work');
    }, 200);
    });
    burger.addEventListener('click', function(){
        if (navbarClasses[1]){
            navbarClasses.remove('active');
        }
        else{
            navbarClasses.add('active');
        }
    })
})();
