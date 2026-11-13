
// PROJECT FILTERING


const filterButtons = document.querySelectorAll(".filter");
const projectCards = document.querySelectorAll(".project-card");
const searchInput = document.getElementById("projectSearch");

let activeFilter = "all";

function updateProjects() {

    const query = searchInput.value.toLowerCase();

    projectCards.forEach(card => {

        const categories = card.dataset.category.split(" ");
        const content = card.textContent.toLowerCase();

        const matchesFilter =
            activeFilter === "all" ||
            categories.includes(activeFilter);

        const matchesSearch = content.includes(query);

        card.style.display =
            matchesFilter && matchesSearch ? "block" : "none";

    });
}

filterButtons.forEach(button => {

    button.addEventListener("click", () => {

        activeFilter = button.dataset.filter;

        filterButtons.forEach(btn =>
            btn.classList.remove("active")
        );

        button.classList.add("active");

        updateProjects();
    });
});

searchInput.addEventListener("input", updateProjects);



// DARK / LIGHT MODE

const themeButton = document.getElementById("themeToggle");

themeButton.addEventListener("click", () => {

    document.body.classList.toggle("dark");

    const isDark = document.body.classList.contains("dark");

    themeButton.textContent = isDark ? "☀" : "☾";

    localStorage.setItem("portfolio-theme", isDark ? "dark" : "light");

});


// RESTORE THEME

const savedTheme = localStorage.getItem("portfolio-theme");

if (savedTheme === "dark") {
    document.body.classList.add("dark");
    themeButton.textContent = "☀";
}
