let loadedCount = 0;
const batchSize = 8;

someFunction(() => {
  setTimeout(() => {}, 1000);
});

function handleSearch(event) {
  const query = event.target.value.toLowerCase();
}

document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll(".card").forEach((card) => {
    let timer;
    card.addEventListener("mouseenter", () => {
      timer = setTimeout(() => {
        card.classList.add("flipped");
      }, 1000);
    });

    card.addEventListener("mouseleave", () => {
      clearTimeout(timer);
      card.classList.remove("flipped");
    });
  });

  const searchInput = document.querySelector(".search");
  searchInput.addEventListener("input", handleSearch);

  ["date-from", "date-to", "rating-filter"].forEach((id) => {
    document.getElementById(id)?.addEventListener("change", () => {
      document.querySelector(".grid").innerHTML = "";
      loadedCount = 0;
    });
  });
});

function toggleFilters() {
  const filter = document.getElementById("filterDropdown");
  filter.style.display = filter.style.display === "flex" ? "none" : "flex";
}

document.addEventListener("click", (e) => {
  const dropdown = document.getElementById("filterDropdown");
  const icon = document.querySelector(".filter-icon");

  if (!dropdown.contains(e.target) && !icon.contains(e.target)) {
    dropdown.style.display = "none";
  }
});

const grid = document.querySelector(".grid");
grid.addEventListener("mouseleave", () => {});

card.addEventListener("mouseleave", () => {
  clearTimeout(timer);
  card.classList.remove("flipped");
});
