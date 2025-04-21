function showNotification(message) {
  const note = document.getElementById("notification");
  if (!note) return;

  note.textContent = message;
  note.classList.add("visible");

  setTimeout(() => {
    note.classList.remove("visible");
  }, 3000);
}

document.addEventListener("DOMContentLoaded", () => {
  const isLoggedIn = localStorage.getItem("isLoggedIn") === "true";
  const profileContent = document.querySelector(".profile-container");
  const authSection = document.getElementById("auth-section");

  const nicknameBox = document.querySelector(".nickname-box");
  const nicknameInput = document.getElementById("nickname-input");
  const avatarInput = document.getElementById("avatar-input");
  const avatarImg = document.getElementById("profile-avatar");

  const editBtn = document.getElementById("edit-profile-btn");
  const nameField = document.getElementById("name");
  const surnameField = document.getElementById("surname");
  const emailField = document.getElementById("email");
  const newPasswordInput = document.getElementById("new-password");
  const passwordField = document.querySelector(".password-field");

  let editing = false;

  if (!isLoggedIn) {
    authSection?.classList.remove("hidden");
    profileContent?.classList.add("hidden");
  } else {
    authSection?.classList.add("hidden");
    profileContent?.classList.remove("hidden");

    const nickname = localStorage.getItem("nickname") || "";
    const name = localStorage.getItem("name") || "";
    const surname = localStorage.getItem("surname") || "";
    const email = localStorage.getItem("email") || "";
    const createdAt = localStorage.getItem("createdAt") || "-";
    const updatedAt = localStorage.getItem("updatedAt") || "-";

    if (nicknameBox) nicknameBox.textContent = nickname;
    if (nicknameInput) nicknameInput.value = nickname;

    if (nameField) nameField.value = name;
    if (surnameField) surnameField.value = surname;
    if (emailField) emailField.value = email;

    const createdBox = document.querySelector(".profile-dates");
    if (createdBox) {
      createdBox.innerHTML = `Дата создания профиля<br>${createdAt}<br>Последнее изменение<br>${updatedAt}`;
    }

    const storedAvatar = localStorage.getItem("avatar");
    if (storedAvatar && avatarImg) {
      avatarImg.src = storedAvatar;
    }

    if (nicknameInput) nicknameInput.style.display = "none";
    if (avatarInput) avatarInput.style.display = "none";
  }

  editBtn?.addEventListener("click", () => {
    editing = !editing;

    if (editing) {
      if (passwordField) passwordField.classList.remove("hidden");
      editBtn.textContent = "Сохранить";
    } else {
      editBtn.textContent = "Редактировать профиль";

      const nickname = nicknameInput.value.trim();
      const name = nameField.value;
      const surname = surnameField.value;
      const email = emailField.value;

      if (!nickname || !name || !surname || !email) {
        showNotification("Пожалуйста, заполните все поля профиля");
        editing = true;
        editBtn.textContent = "Сохранить";
        if (passwordField) passwordField.classList.remove("hidden");
        return;
      }

      localStorage.setItem("nickname", nickname);
      localStorage.setItem("name", name);
      localStorage.setItem("surname", surname);
      localStorage.setItem("email", email);
      localStorage.setItem("updatedAt", new Date().toLocaleString());

      if (nicknameBox) nicknameBox.textContent = nickname;

      location.reload();
    }

    [nameField, surnameField, emailField].forEach((field) => {
      if (field) field.readOnly = !editing;
    });

    if (nicknameInput) nicknameInput.style.display = editing ? "block" : "none";
    if (avatarInput) avatarInput.style.display = editing ? "block" : "none";
  });

  avatarInput?.addEventListener("change", (e) => {
    const file = e.target.files[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = () => {
      const dataUrl = reader.result;
      avatarImg.src = dataUrl;
      localStorage.setItem("avatar", dataUrl);
    };
    reader.readAsDataURL(file);
  });

  document.getElementById("show-login")?.addEventListener("click", () => {
    document.getElementById("login-form")?.classList.remove("hidden");
    document.getElementById("register-form")?.classList.add("hidden");
  });

  document.getElementById("show-register")?.addEventListener("click", () => {
    document.getElementById("register-form")?.classList.remove("hidden");
    document.getElementById("login-form")?.classList.add("hidden");
  });

  document.getElementById("register-submit")?.addEventListener("click", () => {
    const name = document.getElementById("reg-name").value.trim();
    const surname = document.getElementById("reg-surname").value.trim();
    const email = document.getElementById("reg-email").value.trim();
    const password = document.getElementById("reg-password").value.trim();
    const nickname = document.getElementById("reg-nickname").value.trim();

    if (!name || !surname || !email || !password || !nickname) {
      showNotification("Заполните все поля");
      return;
    }

    localStorage.setItem("isLoggedIn", "true");
    localStorage.setItem("name", name);
    localStorage.setItem("surname", surname);
    localStorage.setItem("email", email);
    localStorage.setItem("password", password);
    localStorage.setItem("nickname", nickname);
    localStorage.setItem("createdAt", new Date().toLocaleString());
    localStorage.setItem("updatedAt", new Date().toLocaleString());

    location.reload();
  });

  document.getElementById("login-submit")?.addEventListener("click", () => {
    const email = document.getElementById("login-email").value.trim();
    const password = document.getElementById("login-password").value.trim();

    if (!email || !password) {
      showNotification("Заполните все поля");
      return;
    }

    if (
      localStorage.getItem("email") === email &&
      localStorage.getItem("password") === password
    ) {
      localStorage.setItem("isLoggedIn", "true");
      location.reload();
    } else {
      showNotification("Неверный email или пароль.");
    }
  });

  document.getElementById("logout-btn")?.addEventListener("click", () => {
    localStorage.clear();
    location.reload();
  });
});
