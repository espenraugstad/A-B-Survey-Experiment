const form = document.getElementById("surveyForm");
form.addEventListener("submit", async (e) => {
  e.preventDefault();
  const formData = new FormData(form);
  const cola = formData.get("cola");
  if (!cola) {
    alert("Please select a beverage!");
    return;
  }

  let response = await fetch(
    "https://fvor59zibi.execute-api.eu-north-1.amazonaws.com/prod/submission",
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        cola,
        variant: "A",
      }),
    }
  );

  if (response.status === 200) {
    location.href = "../thankyou.html";
  } else {
    console.log(response);
  }
});
