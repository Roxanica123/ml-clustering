import { Menu } from "./menu/menu.js"
import { TemplateManager } from "./templates/template-manager.js"

export class Page {
    page
    template_manager
    constructor(page) {
        this.page = page
        this.template_manager = new TemplateManager(page);
        this.clear_frames();
        this.add_contents();
    }
    clear_frames() {
        const container = document.querySelector("frames-container");
        container.remove();
    }
    add_contents() {
        const body = document.querySelector("body");
        this.page_container = document.createElement("page-container");
        body.prepend(this.page_container);
        window.menu = new Menu(this);

        const content_container = document.createElement("content-container");
        this.page_container.append(content_container);
        content_container.insertAdjacentHTML('beforeend', this.template_manager.dataset_template);
    }
    async add_model(type) {
        this.get_clean_method_node().insertAdjacentHTML('beforeend', await this.template_manager.em_template(type));
    }
    async add_hierarchial(type) {

        const method = this.get_clean_method_node();
        const content =  await this.template_manager.hierarchial_template(type);
        method.insertAdjacentHTML('afterbegin', content.dendrogram);
        method.appendChild(content.show);
    }
    async add_partitional(type) {
        const method = this.get_clean_method_node();
        const shows = await this.template_manager.partitional_template(type);
        const kmeans = document.createElement("p");
        kmeans.innerText="K-means";
        const kmeans_plus = document.createElement("p");
        kmeans_plus.innerText="K-means++";
        method.appendChild(kmeans);
        method.appendChild(shows.normal);
        method.appendChild(kmeans_plus)
        method.appendChild(shows.plus);
    }
    get_clean_method_node() {
        let method = document.querySelector("method");
        if (method) {
            method.innerHTML = "";
        } else {
            method = document.createElement("method");
            document.querySelector("content-container").appendChild(method);
        }
        return method;
    }

}