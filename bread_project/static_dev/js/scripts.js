constmozes = [
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
