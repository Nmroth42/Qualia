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
    $("#id_username").change(function () {
        console.log($(this).val());
    });
    $("#id_username").change(function () {
        var username = $(this).val();

        $.ajax({
            url: '/ajax/validate_username/',
            data: {
                'username': username
            },
            dataType: 'json',
            success: function (data) {
                if (data.is_taken) {
                    alert("A user with this username already exists.");
                    $("#id_username").val("");
                }
            }
        });

    });
});
var overlay = document.getElementById("overlay");
window.addEventListener("load", function () {
    overlay.style.display = 'none'

})