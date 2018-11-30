$(document).ready(function () {
    $("body").css("display", "none");
    $("body").fadeIn(1000);

    /*  $("transition").click(function(event){
          event.preventDefault();
          linkLocation = this.href;
          $("body").fadeOut(100, redirectPage);      
      }); 
           
      function redirectPage() {
          window.location = linkLocation;
      } */
  
});
var overlay = document.getElementById("overlay");
window.addEventListener("load", function () {
    overlay.style.display = 'none'

})