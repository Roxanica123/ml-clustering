import { Page } from "./page.js";
import { Menu } from "./menu/menu.js"


function changePage(folder) {
    const pageContainer = document.querySelector('page-container');
    pageContainer.innerHTML = ""
    window.page = new Page(folder);
}

window.changePage = changePage;
window.menu = new Menu();
window.page = new Page("./main-page");