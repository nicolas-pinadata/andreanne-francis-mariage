document.addEventListener("DOMContentLoaded", function () {
  const button = document.querySelector("[data-menu-button]");
  const menu = document.querySelector("[data-mobile-menu]");

  if (!button || !menu) return;

  button.addEventListener("click", function () {
    menu.classList.toggle("hidden");
  });
});