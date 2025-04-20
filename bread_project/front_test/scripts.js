
const recipes = [
  { title: 'Белый хлеб', image: 'images/bread2.jpg', description: 'Мука, вода, дрожжи...' },
  { title: 'Чиабатта', image: 'images/bread1.jpg', description: 'Оливковое масло, мука...' },
  { title: 'Бублик', image: 'images/bread3.jpg', description: 'Семечки, соль, сахар...' },
  { title: 'Ржаной хлеб', image: 'images/bread4.jpg', description: 'Ржаная мука и вода...' },
  { title: 'Фокачча', image: 'images/bread5.jpg', description: 'Розмарин, масло...' },
  { title: 'Батон', image: 'images/bread6.jpg', description: 'Мягкий классический хлеб' },
  { title: 'Бриошь', image: 'images/bread7.jpg', description: 'Сладкий и маслянистый' },
  { title: 'Лепёшка', image: 'images/bread8.jpg', description: 'Тонкий и ароматный' }
];

let loadedCount = 0;
const batchSize = 8;

function renderBatch() {
  const container = document.querySelector(".grid");
  const slice = recipes.slice(loadedCount, loadedCount + batchSize);

  slice.forEach(recipe => {
      const card = document.createElement('div');
      card.className = 'card';
      card.setAttribute('data-title', recipe.title.toLowerCase());

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

  document.querySelectorAll('.card').forEach(card => {
    let hoverTimer;
  
    card.addEventListener('mouseenter', () => {
      hoverTimer = setTimeout(() => {
        card.classList.add('flip', 'hovered');
  
        document.querySelectorAll('.card').forEach(otherCard => {
          if (otherCard !== card) {
            otherCard.classList.add('blur');
          }
        });
      }, 2000);
    });
  
    card.addEventListener('mouseleave', () => {
      clearTimeout(hoverTimer);
      card.classList.remove('flip', 'hovered');
  
      document.querySelectorAll('.card').forEach(card => {
        card.classList.remove('blur');
      });
    });
  });  
}

function handleScroll() {
  const nearBottom = window.innerHeight + window.scrollY >= document.body.offsetHeight - 300;
  if (nearBottom && loadedCount < recipes.length) {
      renderBatch();
  }
}

function goToRecipe() {
  window.location.href = "./recipe/recipe.html";
}

function handleSearch(event) {
  const query = event.target.value.toLowerCase();
  document.querySelectorAll('.card').forEach(card => {
      const title = card.getAttribute('data-title');
      card.style.display = title.includes(query) ? '' : 'none';
  });
}

document.addEventListener('DOMContentLoaded', () => {
  renderBatch();
  window.addEventListener('scroll', handleScroll);

  const searchInput = document.querySelector('.search');
  searchInput.addEventListener('input', handleSearch);
});

function toggleFilters() {
  const filter = document.getElementById('filterDropdown');
  filter.style.display = filter.style.display === 'flex' ? 'none' : 'flex';
}

document.addEventListener('click', (e) => {
  const dropdown = document.getElementById('filterDropdown');
  const icon = document.querySelector('.filter-icon');

  if (!dropdown.contains(e.target) && !icon.contains(e.target)) {
      dropdown.style.display = 'none';
  }
});

const grid = document.querySelector('.grid');

grid.addEventListener('mouseleave', () => {
  document.querySelectorAll('.card').forEach(card => {
      card.classList.remove('hovered', 'blur');
  });
});