document.addEventListener("DOMContentLoaded", () => {

    const form = document.querySelector("form");
    if (!form) {
        return;
    }

    const passwordButtons = document.querySelectorAll(".toggle-password");
    passwordButtons.forEach((button) => {
        button.addEventListener("click", () => {
            const targetId = button.dataset.target;
            const input = document.getElementById(targetId);

            if (!input) {
                return;
            }

            const isPassword = input.type === "password";
            input.type = isPassword ? "text" : "password";
            button.textContent = isPassword ? "🙈" : "👁";

            button.setAttribute(
                "aria-label",
                isPassword
                    ? "Hide password"
                    : "Show password"
            );
        });
    });

    const password1 = document.getElementById("id_password1");
    const password2 = document.getElementById("id_password2");

    if (!password1 || !password2) {
        return;
    }

    const createErrorMessage = () => {
        let error = document.querySelector(".password-match-error");
        if (!error) {
            error = document.createElement("small");
            error.className = "error password-match-error";
            password2.parentElement.appendChild(error);
        }
        return error;
    };

    const removeErrorMessage = () => {
        const error = document.querySelector(".password-match-error");
        if (error) {
            error.remove();
        }
    };

    const validatePasswords = () => {
        const firstPassword = password1.value;
        const secondPassword = password2.value;

        // Nothing to validate yet
        if (!secondPassword) {
            password2.classList.remove("error-input");
            removeErrorMessage();
            return true;
        }

        // Passwords match
        if (firstPassword === secondPassword) {
            password2.classList.remove("error-input");
            removeErrorMessage();
            return true;
        }

        // Passwords don't match
        password2.classList.add("error-input");
        const error = createErrorMessage();
        error.textContent = "Passwords do not match.";
        return false;
    };

    password1.addEventListener(
        "input",
        validatePasswords
    );

    password2.addEventListener(
        "input",
        validatePasswords
    );

    form.addEventListener("submit", (event) => {
        const passwordsMatch = validatePasswords();
        if (!passwordsMatch) {
            event.preventDefault();
            password2.focus();
        }
    });
});