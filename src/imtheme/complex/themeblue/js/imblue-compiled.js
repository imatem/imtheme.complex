/*For gigant  activities slider*/

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
  if (slideIndex > slides.length) {
    slideIndex = 1;
  }
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


/* For the tobleron */
$('#sb-slider').slicebox();
$(function() {
  var Page = (function() {
    var $navArrows = $( '#nav-arrows' ).hide(),
      $shadow = $( '#shadow' ).hide(),
      slicebox = $( '#sb-slider' ).slicebox( {
        onReady : function() {
          $navArrows.show();
          $shadow.show();
        },
        orientation : 'v',
        cuboidsRandom : false,
        cuboidsCount: 1,
        autoplay : true,
        speed : 600,
        interval: 5000,
        colorHiddenSides : '#222',
        //fallbackFadeSpeed : 300,
        //easing : 'ease',
      } ),

      init = function() {
        initEvents();

      },
      initEvents = function() {
        // add navigation events
        $navArrows.children( ':first' ).on( 'click', function() {
          slicebox.next();
          return false;
        } );
        $navArrows.children( ':last' ).on( 'click', function() {

          slicebox.previous();
          return false;
        } );
      };
      return { init : init };
  })();
  Page.init();
});


/*For rotated news */
$(function(){
function run() {
  var prev = $("#rotated li:first-child");
  $.unique(prev).each(function(i) {
    $(this).delay(i*600).slideUp(function() {
      $(this).appendTo(this.parentNode).slideDown();
    });
  });
}

window.setInterval(run,10000);
});
