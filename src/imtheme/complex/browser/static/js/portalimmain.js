/*For gigant  activities slider*/
$(document).ready(function() {


var slideIndex = 0;
    showSlides();

    function plusSlides(n) {
      showSlides2(slideIndex += n);
    }

    function currentSlide(n) {
      showSlides2(slideIndex = n);
    }

    function showSlides() {
      var i;
      var slides = document.getElementsByClassName("mySlides");
      var dots = document.getElementsByClassName("dot");
      for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
      }
      slideIndex++;
      if (slideIndex > slides.length) {slideIndex = 1}
      for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");
      }
      slides[slideIndex-1].style.display = "block";
      dots[slideIndex-1].className += " active";
      setTimeout(showSlides, 6000); // Change image every x seconds
    }


    function showSlides2(n) {
      var i;
      var slides = document.getElementsByClassName("mySlides");
      var dots = document.getElementsByClassName("dot");
      if (n > slides.length) {slideIndex = 1}
      if (n < 1) {slideIndex = slides.length}
      for (i = 0; i < slides.length; i++) {
          slides[i].style.display = "none";
      }
      for (i = 0; i < dots.length; i++) {
          dots[i].className = dots[i].className.replace(" active", "");
      }
      slides[slideIndex-1].style.display = "block";
      dots[slideIndex-1].className += " active";
    }
// End activities slider

  // $("#lupis").click(function() {
  //   var element = document.getElementById("searchbar");

  //   if (element.classList) {
  //     element.classList.toggle("searchbar");
  //   } else {
  //     var classes = element.className.split(" ");
  //     var i = classes.indexOf("searchbar");

  //     if (i >= 0)
  //       classes.splice(i, 1);
  //     else
  //       classes.push("searchbar");
  //       element.className = classes.join(" ");
  //   }
  // });

  $("#lupis").click(function() {
    var x = document.getElementById("searchbar");
    x.classList.toggle("searchbar");
  });

});
