export class Menu {

    constructor() {
        const menuContainer = document.querySelector('menu-container');
        fetch("./menu/menu.html")
            .then(content => content.text())
            .then(
                html_text => {
                    menuContainer.insertAdjacentHTML('beforeend', html_text);
                    this.addStyleLink();
                    this.addEvents();
                }
            )
    }
    addStyleLink() {
        const head = document.querySelector('head');
        const link = document.createElement('link')
        link.setAttribute("rel", "stylesheet");
        link.setAttribute("href", "./menu/menu.css");
        head.appendChild(link);
    }

    addEvents() {
        const menuItems = document.querySelectorAll(".menu-item")
        menuItems.forEach(item => {
            const subItems = item.querySelectorAll("ul li")
            subItems.forEach(subItem => {
                const folder = item.getAttribute("name") + "/" + subItem.getAttribute("name")
                subItem.addEventListener("click", () => { window.changePage(folder) })
            })
        })
    }

}