/*---------1. DARK MODE TOGGLE---------*/
const themeToggle = document.querySelector('#theme-toggle');
themeToggle.addEventListener('click', () => {
  document.body.classList.toggle('dark');
const isDark=document.body.classList.contains('dark');
themeToggle.textContent=isDark?'\u2600\uFE0F':'\uD83C\uDF19';//sun and moon emojis
});
/*---------2. BACK-TO-TOP BUTTON---------*/
const ToTop = document.querySelector('#btn-to-top');
window.addEventListener('scroll', () => {
  if (window.scrollY > 300) {
    ToTop.classList.add('show');
  } else {
    ToTop.classList.remove('show');
  }
});
ToTop.addEventListener('click', () => {
  window.scrollTo({ top: 0, behavior: 'smooth' });
});
/*---------3. REVEAL ON SCROLL---------*/
const revealElements = document.querySelectorAll('.reveal');
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
        observer.unobserve(entry.target);
    }
  });
}, { threshold: 0.15 });
revealElements.forEach((item) => observer.observe(item));
