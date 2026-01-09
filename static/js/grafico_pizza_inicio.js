document.addEventListener('DOMContentLoaded', function () {
    const ctx = document.getElementById('grafico_pizza');

    if (!ctx) return;

    new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: GRAFICO_PIZZA_LABELS,
            datasets: [{
                label: 'Chamados',
                data: GRAFICO_PIZZA_VALORES,
                borderWidth: 1,
                backgroundColor: [
                    '#e27b91ff',
                    '#04436F',
                    '#71E397'
                ]
            }]
        },
        options: {
            responsive: true
        }
    });
});