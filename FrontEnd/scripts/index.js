const gotoSurvey = document.getElementById("gotoSurvey");
function getRandomIntInclusive(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min + 1) + min); // The maximum is inclusive and the minimum is inclusive
}

gotoSurvey.addEventListener("click", async () => {
  const variant = getRandomIntInclusive(0, 1);
  if (variant === 0) {
    location.href = "/survey.html";
  } else {
    location.href = "/survey/index.html";
  }
});
