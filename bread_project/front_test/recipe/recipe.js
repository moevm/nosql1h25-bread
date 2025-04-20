function showNotification(message) {
  const note = document.getElementById("notification");
  if (!note) return;

  note.textContent = message;
  note.classList.remove("hidden");

  setTimeout(() => {
    note.classList.add("hidden");
  }, 3000);
}

document.addEventListener("DOMContentLoaded", () => {
  const tabReviews = document.getElementById("tab-reviews");
  const tabRate = document.getElementById("tab-rate");
  const sectionReviews = document.getElementById("reviews-section");
  const sectionRate = document.getElementById("rate-section");

  tabReviews.addEventListener("click", () => {
    tabReviews.classList.add("active");
    tabRate.classList.remove("active");
    sectionReviews.classList.remove("hidden");
    sectionRate.classList.add("hidden");
  });

  tabRate.addEventListener("click", () => {
    tabRate.classList.add("active");
    tabReviews.classList.remove("active");
    sectionRate.classList.remove("hidden");
    sectionReviews.classList.add("hidden");
  });

  const stars = document.querySelectorAll("#star-rating span");
  stars.forEach(star => {
    star.addEventListener("click", () => {
      const value = parseInt(star.getAttribute("data-value"));
      document.getElementById("star-rating").setAttribute("data-score", value);
      stars.forEach((s, i) => {
        s.classList.toggle("selected", i < value);
      });
    });
  });
});

function addReview() {
  const text = document.getElementById("review-text").value.trim();
  const score = parseInt(document.getElementById("star-rating").getAttribute("data-score")) || 0;

  if (!text || score === 0) {
    showNotification("Введите текст и выберите оценку!");
    return;
  }

  const now = new Date();
  const formatted = now.toLocaleDateString() + ", " + now.toLocaleTimeString();
  const starsDisplay = "★".repeat(score) + "☆".repeat(5 - score);

  const reviewBlock = document.createElement("div");
  reviewBlock.className = "review";
  reviewBlock.innerHTML = `
    <div class="review-header">Аноним, ${formatted} <span class="stars">${starsDisplay}</span></div>
    <div class="review-text">${text}</div>
  `;

  document.getElementById("reviews-section").appendChild(reviewBlock);
  document.getElementById("review-text").value = "";
  document.querySelectorAll("#star-rating span").forEach(s => s.classList.remove("selected"));
  document.getElementById("star-rating").setAttribute("data-score", "0");

  showNotification("Отзыв добавлен!");
}
