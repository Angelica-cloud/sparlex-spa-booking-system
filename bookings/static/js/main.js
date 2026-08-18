(function ($) {
    "use strict";

    // Spinner
    var spinner = function () {
        setTimeout(function () {
            if ($('#spinner').length > 0) {
                $('#spinner').removeClass('show');
            }
        }, 1);
    };
    spinner(0);
    
    
    // Initiate the wowjs
    new WOW().init();


    // Fixed Navbar
    $(window).scroll(function () {
        if ($(this).scrollTop() > 300) {
            $('.sticky-top').addClass('shadow-sm').css('top', '0px');
        } else {
            $('.sticky-top').removeClass('shadow-sm').css('top', '-200px');
        }
    });
    
    
   // Back to top button
   $(window).scroll(function () {
    if ($(this).scrollTop() > 300) {
        $('.back-to-top').fadeIn('slow');
    } else {
        $('.back-to-top').fadeOut('slow');
    }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
    });


    // Pricing-carousel
    $(".pricing-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 2000,
        center: false,
        dots: true,
        loop: true,
        margin: 25,
        nav : true,
        navText : [
            '<i class="bi bi-arrow-left"></i>',
            '<i class="bi bi-arrow-right"></i>'
        ],
        responsiveClass: true,
        responsive: {
            0:{
                items:1
            },
            576:{
                items:2
            },
            768:{
                items:2
            },
            992:{
                items:3
            },
            1200:{
                items:4
            }
        }
    });

    // Testimonial-carousel
    $(".testimonial-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 2000,
        center: false,
        dots: true,
        loop: true,
        margin: 25,
        nav : true,
        navText : [
            '<i class="bi bi-arrow-left"></i>',
            '<i class="bi bi-arrow-right"></i>'
        ],
        responsiveClass: true,
        responsive: {
            0:{
                items:1
            },
            576:{
                items:1
            },
            768:{
                items:1
            },
            992:{
                items:2
            },
            1200:{
                items:2
            }
        }
    });



    // Modal Video
    $(document).ready(function () {
        var $videoSrc;
        $('.btn-play').click(function () {
            $videoSrc = $(this).data("src");
        });
        console.log($videoSrc);

        $('#videoModal').on('shown.bs.modal', function (e) {
            $("#video").attr('src', $videoSrc + "?autoplay=1&amp;modestbranding=1&amp;showinfo=0");
        })

        $('#videoModal').on('hide.bs.modal', function (e) {
            $("#video").attr('src', $videoSrc);
        })
    });


    // Facts counter
    $('[data-toggle="counter-up"]').counterUp({
        delay: 5,
        time: 2000
    });


})(jQuery);


function togglePassword(id, button){

    const input = document.getElementById(id);
    const icon = button.querySelector("i");

    if(input.type === "password"){

        input.type = "text";

        icon.classList.remove("fa-eye");

        icon.classList.add("fa-eye-slash");

    }else{

        input.type = "password";

        icon.classList.remove("fa-eye-slash");

        icon.classList.add("fa-eye");

    }

}


document.addEventListener("DOMContentLoaded", function () {

    const service = document.getElementById("service");
    const date = document.getElementById("date");
    const time = document.getElementById("time");
    const fullname = document.getElementById("fullname");
    const email = document.getElementById("email");
    const phone = document.getElementById("phone");

    const sumService = document.getElementById("sumService");
    const sumDate = document.getElementById("sumDate");
    const sumTime = document.getElementById("sumTime");
    const sumName = document.getElementById("sumName");
    const sumEmail = document.getElementById("sumEmail");
    const sumPhone = document.getElementById("sumPhone");

function updateSummary() {

    const option = service.options[service.selectedIndex];

    // Service Name
    sumService.textContent =
        option.value ? option.text : "Not Selected";

    // Duration
    document.getElementById("sumDuration").textContent =
        option.dataset.duration || "--";

    // Price
    document.getElementById("sumPrice").textContent =
        option.dataset.price ? "₦" + option.dataset.price : "--";

    // Date
    sumDate.textContent =
        date.value || "--";

    // Time
    sumTime.textContent =
        time.value || "--";

    // Name
    sumName.textContent =
        fullname.value || "--";

    // Email
    sumEmail.textContent =
        email.value || "--";

    // Phone
    sumPhone.textContent =
        phone.value || "--";
}

    service.addEventListener("change", updateSummary);

    date.addEventListener("change", updateSummary);

    time.addEventListener("change", updateSummary);

    fullname.addEventListener("keyup", updateSummary);

    email.addEventListener("keyup", updateSummary);

    phone.addEventListener("keyup", updateSummary);

    updateSummary();

    /* Prevent selecting past dates */

    const today = new Date();

    const yyyy = today.getFullYear();

    const mm = String(today.getMonth()+1).padStart(2,"0");

    const dd = String(today.getDate()).padStart(2,"0");

    document.getElementById("date").min =
        "${yyyy}-${mm}-${dd}";

});

