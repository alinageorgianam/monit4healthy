document.addEventListener('DOMContentLoaded', function() {
    const ctx = document.getElementById('uricAcidChart').getContext('2d');

    let fetchUrl = '/get_latest_medical_data';

    fetch(fetchUrl)
        .then(response => response.text())
        .then(text => {
            console.log('Raw response:', text);  // Adăugăm un log pentru răspunsul brut
            const data = JSON.parse(text);
            if (data.length > 0) {
                const labels = data.map(entry => entry.measurement_date);
                const uricAcidLevels = data.map(entry => entry.uric_acid_level);

                const chartConfig = {
                    type: 'line',
                    data: {
                        labels: labels,
                        datasets: [{
                            label: 'Nivel Uric Acid',
                            data: uricAcidLevels,
                            borderColor: '#FFFFFF',
                            borderWidth: 1,
                            backgroundColor: '#FFFFFF',  // Adăugăm un fundal pentru linii
                            fill: true
                        }]
                    },
                    options: {
                        responsive: true,
                        scales: {
                            x: {
                                display: true,
                                title: {
                                    display: true,
                                    text: 'Data',
                                    color: '#FFFFFF',
                                    font: {
                                        size: 14
                                    }
                                },
                                ticks: {
                                    color: '#FFFFFF',
                                    font: {
                                        size: 12
                                    }
                                },
                                grid: {
                                    color: '#757a79'
                                }
                            },
                            y: {
                                display: true,
                                title: {
                                    display: true,
                                    text: 'Nivel Uric Acid (mg/dL)',
                                    color: '#FFFFFF',
                                    font: {
                                        size: 14
                                    }
                                },
                                ticks: {
                                    color: '#FFFFFF',
                                    font: {
                                        size: 12
                                    }
                                },
                                grid: {
                                    color: '#757a79'
                                }
                            }
                        },
                        plugins: {
                            legend: {
                                labels: {
                                    color: '#FFFFFF',
                                    font: {
                                        size: 14
                                    }
                                }
                            },
                            tooltip: {
                                backgroundColor: 'rgba(0, 0, 0, 0.7)',
                                titleFont: {
                                    size: 14
                                },
                                bodyFont: {
                                    size: 12
                                },
                                footerFont: {
                                    size: 12
                                }
                            }
                        }
                    }
                };

                const chart = new Chart(ctx, chartConfig);

                document.getElementById('uricAcidChart').addEventListener('click', function() {
                    const modal = document.getElementById('chartModal');
                    const modalChartCtx = document.getElementById('modalUricAcidChart').getContext('2d');
                    modal.style.display = 'block';
                    new Chart(modalChartCtx, chartConfig);
                });

                document.getElementById('closeModal').addEventListener('click', function() {
                    const modal = document.getElementById('chartModal');
                    modal.style.display = 'none';
                });

                window.onclick = function(event) {
                    const modal = document.getElementById('chartModal');
                    if (event.target == modal) {
                        modal.style.display = 'none';
                    }
                }
            }
        })
        .catch(error => console.error('Error fetching data:', error));
});
