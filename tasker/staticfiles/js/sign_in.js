$(document).ready(function () {
    $("body").css("display", "none");
    $("body").fadeIn(1000);
    var overlay = document.getElementById("overlay");
      $(".transition").click(function(event){
        overlay.style.display = 'block'
        setTimeout(function() {
            overlay.style.display = 'none';

          }, 1000);
           
            
          
       
            
      }); 
           
      function redirectPage() {
          window.location = linkLocation;
      } 
  
});
var overlay = document.getElementById("overlay");
window.addEventListener("load", function () {
    overlay.style.display = 'none';

})