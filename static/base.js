"use strict";
(() => {
    let menuButton = $('#menuButton')[0];
    let menu = $('#menu')[0];
    menuButton.onclick = function () {
        if (menu.getAttribute('display') === 'block') {
            menu.setAttribute('display', 'none');
        }
        else {
            menu.setAttribute('display', 'block');
        }
    };
})();
