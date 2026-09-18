/* jshint esversion: 11 */

document.addEventListener("DOMContentLoaded", function () {
    const addButton = document.getElementById("add-ingredient");
    const formList = document.getElementById("ingredient-form-list");
    const emptyForm = document.getElementById("empty-ingredient-form");
    const totalForms = document.getElementById(
        "id_recipe_ingredients-TOTAL_FORMS"
    );

    if (!addButton || !formList || !emptyForm || !totalForms) {
        return;
    }

    addButton.addEventListener("click", function () {
        const formNumber = Number(totalForms.value);

        const newFormHtml = emptyForm.innerHTML.replaceAll(
            "__prefix__",
            formNumber
        );

        formList.insertAdjacentHTML(
            "beforeend",
            newFormHtml
        );

        totalForms.value = formNumber + 1;
    });
});