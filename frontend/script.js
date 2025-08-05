async function checkURL() {
  const url = document.getElementById("urlInput").value;
  const resText = document.getElementById("result");

  resText.innerText = "Checking...";

  try {
    const res = await fetch("/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ url: url })
    });

    if (!res.ok) {
      throw new Error("Server error");
    }

    const data = await res.json();
    resText.innerText = data.phishing
      ? "🚨 This is a phishing URL!"
      : "✅ This is a safe URL.";

  } catch (error) {
    resText.innerText = "❌ Error checking URL.";
    console.error(error);
  }
}
