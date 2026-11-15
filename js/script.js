// Project filtering and text search
const filterButtons = document.querySelectorAll(".filter");
const projectCards = document.querySelectorAll(".project-card");
const searchInput = document.getElementById("projectSearch");
const noResults = document.getElementById("noResults");
const menuToggle = document.getElementById("menuToggle");
const mainNav = document.getElementById("mainNav");

let activeFilter = "all";

function filterProjects() {
  const query = (searchInput?.value || "").trim().toLowerCase();
  let visibleCount = 0;

  projectCards.forEach((card) => {
    const categories = (card.dataset.category || "").split(/\s+/);
    const searchableText = `${card.dataset.search || ""} ${card.textContent}`.toLowerCase();
    const matchesFilter = activeFilter === "all" || categories.includes(activeFilter);
    const matchesSearch = searchableText.includes(query);
    const isVisible = matchesFilter && matchesSearch;

    card.hidden = !isVisible;
    if (isVisible) visibleCount += 1;
  });

  if (noResults) noResults.hidden = visibleCount !== 0;
}

filterButtons.forEach((button) => {
  button.addEventListener("click", () => {
    activeFilter = button.dataset.filter || "all";
    filterButtons.forEach((item) => {
      const isActive = item === button;
      item.classList.toggle("active", isActive);
      item.setAttribute("aria-pressed", String(isActive));
    });
    filterProjects();
  });
});

searchInput?.addEventListener("input", filterProjects);

// Mobile navigation
menuToggle?.addEventListener("click", () => {
  const isOpen = mainNav.classList.toggle("open");
  menuToggle.setAttribute("aria-expanded", String(isOpen));
  menuToggle.setAttribute("aria-label", isOpen ? "Close navigation" : "Open navigation");
});

mainNav?.querySelectorAll("a").forEach((link) => {
  link.addEventListener("click", () => {
    mainNav.classList.remove("open");
    menuToggle?.setAttribute("aria-expanded", "false");
    menuToggle?.setAttribute("aria-label", "Open navigation");
  });
});
