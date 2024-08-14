function toggleSidebar() {
    const sidebar = document.getElementById('sidebar');
    sidebar.classList.toggle('active');
    const mainContent = document.querySelector('.main-content');
    if (sidebar.classList.contains('active')) {
        sidebar.style.transform = 'translateX(0)';
        mainContent.style.marginLeft = '270px'; /* Width of the sidebar */
    } else {
        sidebar.style.transform = 'translateX(-100%)';
        mainContent.style.marginLeft = '20px';
    }
}

function fetchPatientData() {
    const patientId = document.getElementById('patient-select').value;
    if (patientId) {
        fetch(`/get_patient_data/${patientId}`)
            .then(response => response.json())
            .then(data => {
                const container = document.getElementById('results-container');
                container.innerHTML = '';

                if (data.blackbox_measurements.length > 0) {
                    const blackboxTable = document.createElement('table');
                    blackboxTable.innerHTML = `
                        <tr>
                            <th>Timestamp</th>
                            <th>EKG</th>
                            <th>Puls</th>
                            <th>SpO2</th>
                            <th>Temperatura Corporala</th>
                            <th>CO2</th>
                            <th>Alcoolemia</th>
                        </tr>
                    `;
                    data.blackbox_measurements.forEach(measurement => {
                        const row = document.createElement('tr');
                        row.innerHTML = `
                            <td>${measurement.timestamp}</td>
                            <td>${measurement.ekg}</td>
                            <td>${measurement.pulse}</td>
                            <td>${measurement.spo2}</td>
                            <td>${measurement.body_temp}</td>
                            <td>${measurement.co2}</td>
                            <td>${measurement.alcohol}</td>
                        `;
                        blackboxTable.appendChild(row);
                    });
                    container.appendChild(blackboxTable);
                }

                if (data.gaitband_measurements.length > 0) {
                    const gaitbandTable = document.createElement('table');
                    gaitbandTable.innerHTML = `
                        <tr>
                            <th>Timestamp</th>
                            <th>Fall Detected</th>
                        </tr>
                    `;
                    data.gaitband_measurements.forEach(measurement => {
                        const row = document.createElement('tr');
                        row.innerHTML = `
                            <td>${measurement.timestamp}</td>
                            <td>${measurement.fall_detected}</td>
                        `;
                        gaitbandTable.appendChild(row);
                    });
                    container.appendChild(gaitbandTable);
                }

                if (data.emg_measurements.length > 0) {
                    const emgTable = document.createElement('table');
                    emgTable.innerHTML = `
                        <tr>
                            <th>Timestamp</th>
                            <th>Muscle Activity</th>
                        </tr>
                    `;
                    data.emg_measurements.forEach(measurement => {
                        const row = document.createElement('tr');
                        row.innerHTML = `
                            <td>${measurement.timestamp}</td>
                            <td>${measurement.muscle_activity}</td>
                        `;
                        emgTable.appendChild(row);
                    });
                    container.appendChild(emgTable);
                }
            })
            .catch(error => console.error('Error fetching patient data:', error));
    }
}
