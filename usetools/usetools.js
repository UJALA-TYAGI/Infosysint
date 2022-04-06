function reveal() {
  var reveals = document.querySelectorAll(".reveal");
  for (var i = 0; i < reveals.length; i++) {
    var windowHeight = window.innerHeight;
    var elementTop = reveals[i].getBoundingClientRect().top;
    var elementVisible = 150;
    if (elementTop < windowHeight - elementVisible) {
      reveals[i].classList.add("active");
    } else {
      reveals[i].classList.remove("active");
    }
  }
}

window.addEventListener("scroll", reveal);

const targetDiv = document.getElementById("output");
const btn = document.getElementById("submit-button");
btn.onclick = function () {
  if (targetDiv.style.display == "none") {
    targetDiv.style.display = "block";
  } else {
    targetDiv.style.display = "block";
  }
};
