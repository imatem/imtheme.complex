function myFunction() {
  var x = document.getElementById("portal-globalnav");
  if (x.className === "supermenu") {
    x.className += " responsive";
  } else {
    x.className = "supermenu";
  }
}
