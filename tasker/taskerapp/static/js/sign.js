$(document).ready(function () {
    $("body").css("display", "none");
    $("body").fadeIn(1000);
});
var overlay = document.getElementById("overlay");
window.addEventListener("load", function(){
    overlay.style.display = 'none'
})