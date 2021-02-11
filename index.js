import { MainPageFrame } from "./main-page-frame.js";
import { Page } from "./page.js"

const pics = ["a.jpg", "b.jpg", "c.jpg", "data.jpg"]
window.current_path = "https://roxanica123.github.io/ml-clustering";
window.main_pages = []
window.change_page = function(new_page_location) {
    window.page = new Page(new_page_location)
}

pics.forEach(file => {
    window.main_pages.push(new MainPageFrame("./data/points_with_numbers/" + file))
});