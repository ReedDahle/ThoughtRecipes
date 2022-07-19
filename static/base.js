function onMenuButtonClick() {
    let menu = document.getElementById('menu');
    
    if (menu.style.display === 'block') {
        menu.style.display = 'none'
    }
    else if (menu.style.display === 'none') {
        menu.style.display = 'block'
    }
}