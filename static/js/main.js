document.addEventListener("DOMContentLoaded", () => {
  const form = document.querySelector(".search");
  const input = form?.querySelector('input[name="q"]');
  if (form && input) form.addEventListener("submit", () => { input.value = input.value.trim(); });
});
