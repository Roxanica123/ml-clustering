export class Menu {
    page
    constructor(page) {
        this.page = page;
        const menuContainer = this.addMenuContainer();
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
    addMenuContainer() {
        const page_container = document.querySelector("page-container");
        const menu_container = document.createElement("menu-container");
        page_container.appendChild(menu_container);
        return menu_container;
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
                const folder = item.getAttribute("name") + "/" + subItem.getAttribute("name");
                console.log(folder);
                subItem.onclick = () => { this.page["add_" + item.getAttribute("name")](subItem.getAttribute("name")) };
            })
        })
    }

}