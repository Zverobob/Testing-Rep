let page = document.querySelector('.page');
let themeLamp = document.querySelector('.lamp');
themeLamp.onclick = function () {
    page.classList.toggle('dark-theme');
}