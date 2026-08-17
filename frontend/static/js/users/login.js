const toggleBtn = document.querySelector('.toggle-password-btn');
const passwordInput = document.querySelector('#password');

toggleBtn.addEventListener('click', () => {
    const isPassword = passwordInput.getAttribute('type') === 'password';
    passwordInput.setAttribute('type', isPassword ? 'text' : 'password');

    toggleBtn.style.opacity = isPassword ? '0.5' : '1';
});