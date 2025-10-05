async function analyzeSentiment() {
    const text = document.getElementById("textInput").value;
    const response = await fetch("http://127.0.0.1:5000/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text })
    });
  
    const result = await response.json();
    const resultElement = document.getElementById("result");
  
    // Clear previous classes
    resultElement.classList.remove("positive", "negative");
  
    // Choose emoji based on sentiment
    const emoji = result.label === "POSITIVE" ? "😊" : "😞";
  
    // Set result text with emoji
    resultElement.innerText = `${emoji} Sentiment: ${result.label} (Confidence: ${result.score})`;
  
    // Apply dynamic class
    if (result.label === "POSITIVE") {
      resultElement.classList.add("positive");
    } else {
      resultElement.classList.add("negative");
    }
  }
  