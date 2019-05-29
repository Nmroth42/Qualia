
new Vue({
    delimiters: ['${', '}$'],
    el: '#app',
    data: {
        isOpen: false,
        message: 'menu',
        isModuleView: false,
        messageView:'view_day'
    },
  methods: {
    toggleHeaderUser() {
            this.isOpen = !this.isOpen
            if ((this.isOpen) == true) {
                this.message = 'close'
            }
            if ((this.isOpen) == false) {
                this.message = 'menu'
            }
        },
    toggleSelectView() {
        this.isModuleView = !this.isModuleView
        console.log(this.isModuleView)
        if ((this.isModuleView) == true) {
            this.messageView = 'apps'
        }
        if ((this.isModuleView) == false) {
            this.messageView = 'view_day'
        }
    }
     
    }
})
$(document).ready(function () {
    
    var $btnTop = $("#btn-top");
    var $header = $("#header");
    $btnTop.fadeOut(0);
    $(window).on("scroll", function () {
        if ($(window).scrollTop() >= 600) {
            $btnTop.fadeIn();
        } else {
            $btnTop.fadeOut();
        }
    });
    $btnTop.on("click", function () {
        $("html,body").animate({
            scrollTop: 0
        }, 450);
    });
    $(window).on("scroll", function () {
        if ($(window).scrollTop() >= 1) {
            $header.addClass("headerShadow");
        } else {
            $header.removeClass("headerShadow");
        }
    });
});





 function myFunction(arg) {
    var id = '#' + arg
    var url = $(id).attr("data-url");
    document.location.href = url;
}
var $overlay = $("#overlay");
var overlay = document.getElementById("overlay");
window.addEventListener("load", function(){
    $overlay.fadeOut(280);
})