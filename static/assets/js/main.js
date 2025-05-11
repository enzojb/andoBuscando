$(window).load(function () { // makes sure the whole site is loaded
    $('#status').fadeOut(); // will first fade out the loading animation
    $('#preloader').delay(350).fadeOut('slow'); // will fade out the white DIV that covers the website.
    $('body').delay(350).css({'overflow': 'visible'});
})
$(document).ready(function () {

    
    $('input').iCheck({
        checkboxClass: 'icheckbox_square-yellow',
        radioClass: 'iradio_square-yellow',
        increaseArea: '20%' // optional
    });


    $('.layout-grid').on('click', function () {
        $('.layout-grid').addClass('active');
        $('.layout-list').removeClass('active');

        $('#list-type').removeClass('proerty-th-list');
        $('#list-type').addClass('proerty-th');

    });

    $('.layout-list').on('click', function () {
        $('.layout-grid').removeClass('active');
        $('.layout-list').addClass('active');

        $('#list-type').addClass('proerty-th-list');
        $('#list-type').removeClass('proerty-th');

    });

});
$(document).ready(function () {
    $("#bg-slider").owlCarousel({
        navigation: false, // Show next and prev buttons
        slideSpeed: 100,
        autoPlay: 5000,
        paginationSpeed: 100,
        singleItem: true,
        mouseDrag: false,
        transitionStyle: "fade"
                // "singleItem:true" is a shortcut for:
                // items : 1, 
                // itemsDesktop : false,
                // itemsDesktopSmall : false,
                // itemsTablet: false,
                // itemsMobile : false 
    });
    $("#prop-smlr-slide_0").owlCarousel({
        navigation: false, // Show next and prev buttons
        slideSpeed: 100,
        pagination: true,
        paginationSpeed: 100,
        items: 3

    });
    $("#testimonial-slider").owlCarousel({
        navigation: false, // Show next and prev buttons
        slideSpeed: 100,
        pagination: true,
        paginationSpeed: 100,
        items: 3
    });

    $('#price-range').slider();
    $('#property-geo').slider();
    $('#min-baths').slider();
    $('#id_ambientes').slider();
    $('#id_metros_cuadrados').slider();
    $('#min-bed').slider();

    var RGBChange = function () {
        $('#RGB').css('background', '#FDC600')
    };

    // Advanced search toggle
    var $SearchToggle = $('.search-form .search-toggle');
    $SearchToggle.hide();

    $('.search-form .toggle-btn').on('click', function (e) {
        e.preventDefault();
        $SearchToggle.slideToggle(300);
    });

 setTimeout(function () {
        // Inicializamos en 0
        $('#contador').text('0');
        $('#contador1').text('0');
        $('#contador2').text('0');
        $('#contador3').text('0');

        // Obtenemos los máximos desde el HTML
        const max0 = parseInt($('#contador').closest('.chart').data('percent'));
        const max1 = parseInt($('#contador1').closest('.chart').data('percent'));
        const max2 = parseInt($('#contador2').closest('.chart').data('percent'));
        const max3 = parseInt($('#contador3').closest('.chart').data('percent'));

        // Creamos una función para iniciar el conteo
        function startCounting() {
            let progreso = 0;
            const maxGlobal = Math.max(max0, max1, max2, max3);

            const intervalo = setInterval(() => {
                progreso++;
                let val0 = parseInt($('#contador').text());
                let val1 = parseInt($('#contador1').text());
                let val2 = parseInt($('#contador2').text());
                let val3 = parseInt($('#contador3').text());

                if (val0 < max0) {
                    $('#contador').text(val0 + 1);
                }
                if (val1 < max1) {
                    $('#contador1').text(val1 + 1);
                }
                if (val2 < max2) {
                    $('#contador2').text(val2 + 1);
                }
                if (val3 < max3) {
                    $('#contador3').text(val3 + 1);
                }

                if (progreso >= maxGlobal) {
                    clearInterval(intervalo);
                }
            }, 50); // Ajustar la velocidad si es necesario
        }

        // Creamos el observador
        const observer = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    // Cuando el elemento es visible en la pantalla, iniciamos el conteo
                    startCounting();
                    observer.unobserve(entry.target); // Deja de observar una vez que ha comenzado
                }
            });
        }, { threshold: 0.5 }); // 0.5 significa que el 50% del elemento debe ser visible para disparar el conteo

        // Observamos cada contador
        observer.observe(document.querySelector('#contador'));
        observer.observe(document.querySelector('#contador1'));
        observer.observe(document.querySelector('#contador2'));
        observer.observe(document.querySelector('#contador3'));
        
    }, 500);


    

})
fetch('/contador/datos/')
    .then(response => response.json())
    .then(data => {
      document.getElementById('total_usuarios').setAttribute('data-percent', data.usuarios);
      document.getElementById('total_propiedades').setAttribute('data-percent', data.propiedades);
      document.getElementById('total_publicaciones').setAttribute('data-percent', data.publicaciones);
    })
    .catch(error => {
      console.error('Error al cargar los datos del contador:', error);
    });
// Initializing WOW.JS

new WOW().init();
