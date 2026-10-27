(() => {
  const toggle = document.querySelector('.menu-toggle');
  const nav = document.querySelector('.main-nav');
  const closeMenu = () => {
    if (!toggle || !nav) return;
    toggle.setAttribute('aria-expanded', 'false');
    toggle.innerHTML = `${toggle.dataset.openLabel} <span aria-hidden="true">＋</span>`;
    nav.classList.remove('is-open');
  };
  toggle?.addEventListener('click', () => {
    const expanded = toggle.getAttribute('aria-expanded') === 'true';
    if (expanded) return closeMenu();
    toggle.setAttribute('aria-expanded', 'true');
    toggle.innerHTML = `${toggle.dataset.closeLabel} <span aria-hidden="true">−</span>`;
    nav.classList.add('is-open');
  });
  nav?.addEventListener('click', event => { if (event.target.closest('a')) closeMenu(); });
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && toggle?.getAttribute('aria-expanded') === 'true') {
      closeMenu(); toggle.focus();
    }
  });
  document.addEventListener('click', event => {
    if (!event.target.closest('.header-inner')) closeMenu();
  });
  const toast = document.querySelector('.toast');
  let toastTimer;
  document.querySelectorAll('.copy-email').forEach(button => {
    button.addEventListener('click', async () => {
      let message;
      try {
        await navigator.clipboard.writeText(button.dataset.email);
        message = button.dataset.success;
      } catch {
        message = button.dataset.failure + button.dataset.email;
      }
      toast.textContent = message;
      toast.classList.add('is-visible');
      clearTimeout(toastTimer);
      toastTimer = setTimeout(() => toast.classList.remove('is-visible'), 4500);
    });
  });
})();
