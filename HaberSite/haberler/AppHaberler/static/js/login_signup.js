 const loginToggle = document.getElementById('login-toggle');
const signupToggle = document.getElementById('signup-toggle');
const slider = document.getElementById('slider');
const loginForm = document.getElementById('login-form');
const signupForm = document.getElementById('signup-form');

loginToggle.addEventListener('click', () => {
  loginToggle.classList.add('active');
  signupToggle.classList.remove('active');
  slider.style.left = '0%';
  loginForm.classList.add('active');
  signupForm.classList.remove('active');
});

signupToggle.addEventListener('click', () => {
  signupToggle.classList.add('active');
  loginToggle.classList.remove('active');
  slider.style.left = '50%';
  signupForm.classList.add('active');
  loginForm.classList.remove('active');
});

