const ctx = document.getElementById('chart').getContext('2d');
    const chart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: [], // Adaugă datele de pe axa X (de ex., date)
            datasets: [{
                label: 'Valori Blackbox Medical',
                data: [], // Adaugă datele de pe axa Y (de ex., valori)
                borderColor: 'rgb(75, 192, 192)',
                tension: 0.1
            }]
        },
        options: {
            responsive: true,
            plugins: {
                zoom: {
                    pan: {
                        enabled: true,
                        mode: 'xy'
                    },
                    zoom: {
                        wheel: {
                            enabled: true
                        },
                        pinch: {
                            enabled: true
                        },
                        mode: 'xy'
                    }
                },
                tooltip: {
                    enabled: true,
                    callbacks: {
                        label: function(tooltipItem) {
                            return `Data: ${tooltipItem.label}, Valoare: ${tooltipItem.raw}`;
                        }
                    }
                }
            }
        }
    });

    // Funcție pentru comutare între grafic și tabel
    function showChart(id) {
        document.getElementById('chart-container').style.display = 'block';
        document.getElementById('table-container').style.display = 'none';
        // Încarcă datele pentru grafic în funcție de `id`
        chart.data.labels = ["2023-01-01", "2023-01-02"]; // Exemplu de date X
        chart.data.datasets[0].data = [10, 15]; // Exemplu de date Y
        chart.update();
    }

    function showTable(id) {
        document.getElementById('chart-container').style.display = 'none';
        document.getElementById('table-container').style.display = 'block';
        // Încarcă datele în tabel în funcție de `id`
        $('#data-table').DataTable({
            destroy: true,
            data: [
                ["2023-01-01", 10],
                ["2023-01-02", 15]
            ],
            columns: [
                { title: "Data" },
                { title: "Valoare" }
            ]
        });
    }

    // Inițializare tabel cu DataTables
    $(document).ready(function() {
        $('#data-table').DataTable();
    });