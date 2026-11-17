const form = document.getElementById("loginForm");
const username = document.getElementById("username");
const password = document.getElementById("password");
const message = document.getElementById("message");

form.addEventListener("submit", (event) => {
  event.preventDefault();
  const user = username.value.trim();
  const pass = password.value;
  let valid = true;

  document.getElementById("usernameError").textContent = "";
  document.getElementById("passwordError").textContent = "";
  message.textContent = "";
  message.style.color = "#15803d";

  if (!user) {
    document.getElementById("usernameError").textContent = "Username is required.";
    valid = false;
  } else if (!/^[A-Za-z0-9_]{3,20}$/.test(user)) {
    document.getElementById("usernameError").textContent = "Use 3–20 letters, numbers, or underscores.";
    valid = false;
  }
  if (!pass) {
    document.getElementById("passwordError").textContent = "Password is required.";
    valid = false;
  } else if (pass.length < 8) {
    document.getElementById("passwordError").textContent = "Password must contain at least 8 characters.";
    valid = false;
  }

  if (!valid) return;
  if (user === "student" && pass === "Student@123") {
    message.textContent = "Login successful!";
  } else {
    message.style.color = "#dc2626";
    message.textContent = "Invalid username or password.";
  }
});
