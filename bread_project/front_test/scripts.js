const recipes = [
  {
    title: "Белый хлеб",
    image: "images/bread2.jpg",
    description: "Мука, вода, дрожжи...",
    rating: 4.3,
    date: "2024-04-10",
  },
  {
    title: "Чиабатта",
    image: "images/bread1.jpg",
    description: "Оливковое масло, мука...",
    rating: 3.8,
    date: "2024-04-15",
  },
  {
    title: "Бублик",
    image: "images/bread3.jpg",
    description: "Семечки, соль, сахар...",
    rating: 4.3,
    date: "2024-04-20",
  },
  {
    title: "Ржаной хлеб",
    image: "images/bread4.jpg",
    description: "Ржаная мука и вода...",
    rating: 3.5,
    date: "2024-04-22",
  },
  {
    title: "Фокачча",
    image: "images/bread5.jpg",
    description: "Розмарин, масло...",
    rating: 4.8,
    date: "2024-04-25",
  },
  {
    title: "Батон",
    image: "images/bread6.jpg",
    description: "Мягкий классический хлеб",
    rating: 3.5,
    date: "2024-04-30",
  },
  {
    title: "Бриошь",
    image: "images/bread7.jpg",
    description: "Сладкий и маслянистый",
    rating: 3.2,
    date: "2024-05-01",
  },
  {
    title: "Лепёшка",
    image: "images/bread8.jpg",
    description: "Тонкий и ароматный",
    rating: 3.8,
    date: "2024-04-15",
  },
];

let loadedCount = 0;
const batchSize = 8;

function renderBatch() {
  const container = document.querySelector(".grid");
  const dateFrom = document.getElementById("date-from")?.value;
  const dateTo = document.getElementById("date-to")?.value;
  const ratingMin = parseFloat(
    document.getElementById("rating-filter")?.value || 0
  );

  const fromDate = dateFrom ? new Date(dateFrom) : null;
  const toDate = dateTo ? new Date(dateTo) : null;

  const filtered = recipes.filter((recipe) => {
    const recipeDate = new Date(recipe.date);
    return (
      (!fromDate || recipeDate >= fromDate) &&
      (!toDate || recipeDate <= toDate) &&
      recipe.rating >= ratingMin
    );
  });

  const slice = filtered.slice(loadedCount, loadedCount + batchSize);

  slice.forEach((recipe) => {
    const card = document.createElement("div");
    card.className = "card";
    card.setAttribute("data-title", recipe.title.toLowerCase());

    card.onclick = () => goToRecipe();

    card.innerHTML = `
          <div class="card-inner">
              <div class="card-front">
                  <img src="${recipe.image}" alt="${recipe.title}" />
                  <p>${recipe.title}</p>
              </div>
              <div class="card-back">
                  <p>${recipe.description}</p>
              </div>
          </div>
      `;

    container.appendChild(card);
  });

  loadedCount += batchSize;

  document.querySelectorAll(".card").forEach((card) => {
    let hoverTimer;

    card.addEventListener("mouseenter", () => {
      hoverTimer = setTimeout(() => {
        card.classList.add("flip", "hovered");

        document.querySelectorAll(".card").forEach((otherCard) => {
          if (otherCard !== card) {
            otherCard.classList.add("blur");
          }
        });
      }, 2000);
    });

    card.addEventListener("mouseleave", () => {
      clearTimeout(hoverTimer);
      card.classList.remove("flip", "hovered");

      document.querySelectorAll(".card").forEach((card) => {
        card.classList.remove("blur");
      });
    });
  });
}

function handleScroll() {
  const nearBottom =
    window.innerHeight + window.scrollY >= document.body.offsetHeight - 300;
  if (nearBottom && loadedCount < recipes.length) {
    renderBatch();
  }
}

function goToRecipe() {
  window.location.href = "/recipe/recipe.html";
}

function handleSearch(event) {
  const query = event.target.value.toLowerCase();
  document.querySelectorAll(".card").forEach((card) => {
    const title = card.getAttribute("data-title");
    card.style.display = title.includes(query) ? "" : "none";
  });
}

document.addEventListener("DOMContentLoaded", () => {
  renderBatch();
  window.addEventListener("scroll", handleScroll);

  const searchInput = document.querySelector(".search");
  searchInput.addEventListener("input", handleSearch);

  ["date-from", "date-to", "rating-filter"].forEach((id) => {
    document.getElementById(id)?.addEventListener("change", () => {
      document.querySelector(".grid").innerHTML = "";
      loadedCount = 0;
      renderBatch();
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
grid.addEventListener("mouseleave", () => {
  document.querySelectorAll(".card").forEach((card) => {
    card.classList.remove("hovered", "blur");
  });
});
