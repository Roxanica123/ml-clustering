export class Page {
    constructor(folderPath) {
        const pageContainer = document.querySelector('page-container');
        fetch(folderPath + "/page.html")
            .then(content => content.text())
            .then(
                html_text => {
                    pageContainer.insertAdjacentHTML('beforeend', html_text);
                    this.addStyleLink(folderPath);
                }
            )
    }
    addStyleLink(folderPath) {
        const head = document.querySelector('head');
        const link = document.createElement('link')
        link.setAttribute("rel", "stylesheet");
        link.setAttribute("href", folderPath + "/page.css");
        head.appendChild(link);
    }
}