import { SlideShow } from "./slideshow.js";

export class TemplateManager {
    page;
    dataset_template;
    constructor(page) {
        this.page = page;
        this.build_dataset_template();
    }
    build_dataset_template() {
        this.dataset_template =
            `<dataset_container>
                <iframe src="./data/points_with_numbers/${this.page}.html" width="1010" height="900" style="border:0px;"></iframe>
                <p>If you want to test it out, the coordinates of these points can be found <a href="../data/coordinates/${this.spage}.txt">here</a></p>
            </dataset_container>`;
    }
    async em_template(type) {
        const embed_text = await
        import (`../data/model/${type}/${this.page}/embed.js`);
        return `<em_container>${embed_text.embed}</em_container>`;
    }
    async partitional_template(type) {
        const path_kmeans = `../data/partitional/${type}/${this.page}/kmeans/`;
        const path_plus = `../data/partitional/${type}/${this.page}/kmeans++/`;
        const slideshow_kmeans = new SlideShow(path_kmeans, "kmeans", (await
            import (path_kmeans + "count.js")).count, 1);
        const slideshow_plus = new SlideShow(path_plus, "plus", (await
            import (path_plus + "count.js")).count, 1);
        return { normal: slideshow_kmeans.wrapper, plus: slideshow_plus.wrapper };
    }
    async hierarchial_template(type) {
        const path = `../data/hierarchial/${type}/${this.page}/`;
        const slideshow = new SlideShow(path, "show", (await
            import (path + "count.js")).count, -1);
        const dendrogram_template =
            `<dendrogram_container>
                <iframe src="${path}/dendrogram.html" width="1010" height="900" style="border:0px;"></iframe>
            </dendrogram_container>`;
        return { dendrogram: dendrogram_template, show: slideshow.wrapper }
    }
}