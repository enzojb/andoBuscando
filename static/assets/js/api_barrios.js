document.addEventListener('DOMContentLoaded', function () {
    fetch('/propiedad/api/barrios/')
        .then(response => response.json())
        .then(data => {
            const select = document.getElementById('barrio-select');
            const barrios = data.features;

            barrios.forEach(barrio => {
                const nombreBarrio = barrio.properties.BARRIO;
                const option = document.createElement('option');
                option.value = nombreBarrio;
                option.text = nombreBarrio;
                select.appendChild(option);
            });

            if (typeof $ !== 'undefined' && $.fn.selectpicker) {
                $('.selectpicker').selectpicker('refresh');
            }
            const total = barrios.length;
            console.log(total)
            document.getElementById("total_barrios").setAttribute("data-percent", total);

        })
        .catch(error => {
            console.error('Error cargando barrios:', error);
        });
});