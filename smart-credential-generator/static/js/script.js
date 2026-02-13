// ================= THEME HANDLING =================
function applyTheme() {
  const theme = localStorage.getItem("theme");
  if (theme === "dark") document.body.classList.add("dark");
}

function toggleTheme() {
  document.body.classList.toggle("dark");
  localStorage.setItem(
    "theme",
    document.body.classList.contains("dark") ? "dark" : "light"
  );
}

applyTheme();

// ================= EMAIL CHECK =================
function checkEmail() {
  const email = emailInput.value;
  let missing = [];

  if (!email.includes("@")) missing.push("Missing @ symbol");
  if (!email.includes(".")) missing.push("Missing domain (.com)");
  if (!/\d/.test(email)) missing.push("Add at least one number");
  if (email.length < 8) missing.push("Increase length (min 8 chars)");

  emailResult.innerHTML =
    missing.length === 0
      ? "<span class='good'>✅ Email ID looks strong</span>"
      : "<span class='bad'>❌ Weak Email</span><ul>" +
        missing.map(m => `<li>${m}</li>`).join("") +
        "</ul>";
}

// ================= EMAIL GENERATOR =================
function generateEmail() {
  const key = emailKeyword.value || "user";
  const mode = document.querySelector("input[name='emailMode']:checked").value;
  const prefix = ["real", "its", "smart", "official"];
  const suffix = ["123", "dev", "2026", "mail"];

  emailList.innerHTML = "";

  for (let i = 0; i < 5; i++) {
    let email = key;

    if (mode === "prefix") email = prefix[i] + key;
    if (mode === "suffix") email = key + suffix[i];
    if (mode === "both") email = prefix[i] + key + suffix[i];
    if (mode === "auto") email = prefix[i] + key + Math.floor(Math.random() * 1000);

    emailList.innerHTML += `<li>${email}@gmail.com</li>`;
  }
}

// ================= PASSWORD GENERATOR =================
function generatePassword() {
  const len = parseInt(passLen.value);
  const level = document.querySelector("input[name='level']:checked").value;

  let chars = "abcdefghijklmnopqrstuvwxyz";
  if (level !== "easy") chars += "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
  if (level === "hard") chars += "!@#$%^&*";

  let pass = "";
  for (let i = 0; i < len; i++)
    pass += chars[Math.floor(Math.random() * chars.length)];

  passResult.innerText = pass;
}

// ================= PASSWORD CHECK =================
function checkPassword() {
  const p = checkPass.value;
  let miss = [];

  if (p.length < 8) miss.push("Minimum 8 characters");
  if (!/[A-Z]/.test(p)) miss.push("Uppercase letter");
  if (!/[a-z]/.test(p)) miss.push("Lowercase letter");
  if (!/\d/.test(p)) miss.push("Number");
  if (!/[!@#$%^&*]/.test(p)) miss.push("Special character");

  passCheckResult.innerHTML =
    miss.length === 0
      ? "<span class='good'>✅ Strong & Secure Password</span>"
      : "<span class='bad'>❌ Missing Requirements</span><ul>" +
        miss.map(m => `<li>${m}</li>`).join("") +
        "</ul>";
}

// ================= EMAIL TEMPLATES =================
function loadTemplate(type) {
  const t = {
    professional:
      "Subject: Meeting Request\n\nDear Sir/Madam,\nI hope you are doing well...",
    friends:
      "Hey 😊\nJust wanted to check in and see how things are going!",
    internship:
      "Subject: Internship Application\n\nRespected Sir/Madam,\nI am writing to apply...",
    apology:
      "Subject: Apology\n\nI sincerely apologize for the inconvenience caused...",
    thanks:
      "Subject: Thank You\n\nThank you very much for your guidance and support.",
    leave:
      "Subject: Leave Request\n\nI request leave from ___ to ___ due to..."
  };
  templateArea.value = t[type] || "";
}

function copyTemplate() {
  templateArea.select();
  document.execCommand("copy");
  alert("Template copied to clipboard!");
}
