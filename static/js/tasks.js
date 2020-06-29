const delBtn = document.querySelector(".delete-button");
const modal = document.querySelector(".modal");
const cancelBtn = document.querySelector(".button-cancel");
const cnfrmBtn = document.querySelector(".button-confirm");

delBtn.addEventListener("click", () => {
    overlay.style.display = "flex";
    modal.style.display = "flex";
    cancelBtn.addEventListener("click", hideElements);
    const buttons = delBtn.parentNode;
    const parentDiv = buttons.parentNode;
    const nodes = parentDiv.childNodes;
    const text = nodes[0].textContent;
    console.log(text);
});

overlay.addEventListener("click", hideElements);

function hideElements() {
    overlay.style.display = "none";
    modal.style.display = "none";
}