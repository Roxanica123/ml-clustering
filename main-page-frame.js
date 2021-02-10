export class MainPageFrame{
    page
    attributes = {width: "auto",  height: "auto"}
    constructor(frame_path){
        this.page = this.get_page(frame_path);
        this.attributes["src"] = frame_path;
        this.insert_frame();
    }
    insert_frame(){
        const container = document.querySelector('frames-container');
        const iframe = document.createElement("img");
        Object.keys(this.attributes).forEach(attribute => {
            iframe.setAttribute(attribute, this.attributes[attribute]);
        });
        iframe.onclick = () => {window.change_page(this.page)}
        container.appendChild(iframe)
    }
    get_page(frame_path){
        const file_name = frame_path.split("/").pop();
        const page_name = file_name.replace(".jpg", "");
        return page_name
    }
}