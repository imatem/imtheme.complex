function myFunction() {
  var x = document.getElementById("my-topnav");
  if (x.className === "supermenu") {
    x.className += " responsive";
  } else {
    x.className = "supermenu";
  }
}
