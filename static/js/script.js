
let sidebar = document.querySelector(".sidebar");
let closeBtn = document.querySelector("#btn");
let sectionArea = document.querySelector(".home-section");

closeBtn.addEventListener("click", () => {
    sidebar.classList.toggle("open");
    menuBtnChange();
});

sectionArea.addEventListener("click", () => {
    sidebar.classList.remove("open");
    menuBtnChange();
});

function menuBtnChange() {
    if (sidebar.classList.contains("open")) {
        closeBtn.classList.replace("bx-menu", "bx-x")
    } else {
        closeBtn.classList.replace("bx-x", "bx-menu")
    }
}

setTimeout(function () {
    if ($('#alert_msg').length > 0) {
        $('#alert_msg').remove();
    }
}, 7000)