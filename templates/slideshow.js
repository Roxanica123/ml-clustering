export class SlideShow {
    path;
    count;
    frame_number;
    wrapper;
    id;
    constructor(path, id, count, increment) {
        this.increment = increment;
        this.id = id;
        this.path = path;
        increment < 0 ? this.frame_number = count : this.frame_number = 1;
        this.count = count;
        this.create();
        this.create_frames();
        this.change_frame(this.frame_number);
    }
    create() {

        this.wrapper = document.createElement("slideshow-wrapper");
        this.wrapper.setAttribute("id", this.id);
        const buttons_container = document.createElement("buttons-container");
        this.wrapper.appendChild(buttons_container);

        const previous = document.createElement("a");
        previous.innerText = "< Previous";
        const next = document.createElement("a");
        next.innerText = "Next >";

        previous.setAttribute("class", "arrow left");
        previous.onclick = () => { this.change_frame(this.frame_number - this.increment); }
        next.setAttribute("class", "arrow right");
        next.onclick = () => { this.change_frame(this.frame_number + this.increment) }

        buttons_container.appendChild(previous);
        buttons_container.appendChild(next);

    }
    create_frames() {
        for (let i = 1; i <= this.count; i++) {
            const frame_html = `<iframe id="frame${i}" src="${this.path}${i}.html" style="display:none; border:0px;" class="frame" width="1010" height="900"></iframe>`;
            this.wrapper.insertAdjacentHTML("afterbegin", frame_html);
        }
    }
    change_frame(frame_number) {
        if (frame_number <= 0 || frame_number > this.count)
            return;
        this.wrapper.querySelector(`#frame${this.frame_number}`).style.display = "none";
        this.wrapper.querySelector(`#frame${frame_number}`).style.removeProperty("display");
        this.frame_number = frame_number;
    }
}