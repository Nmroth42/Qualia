new Vue({
    delimiters: ['${', '}$'],
    el: '#app',
    data: {
        isOpen: true,
        message: 'menu'
    },
  methods: {
    toggleHeaderUser() {
            this.isOpen = !this.isOpen
            if ((this.isOpen) == true) {
                this.message = 'menu'
            }
            if ((this.isOpen) == false) {
                this.message = 'close'
            }
        }
     
    }
})
$(document).ready(function () {
    var $btnTop = $("#btn-top");
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
});



 function myFunction(arg) {
    var id = '#' + arg
    var url = $(id).attr("data-url");
    document.location.href = url;
}