var overlay = document.getElementById("overlay");
window.addEventListener("load", function(){
    overlay.style.display = 'none'
})
$(document).ready(function () {
    $("body").css("display", "none");
    $("body").fadeIn(850);
    
    $("a.transition").click(function(event){
        event.preventDefault();
        linkLocation = this.href;
        $("body").fadeOut(0, redirectPage);      
    });
         
    function redirectPage() {
        window.location = linkLocation;
    }
});
