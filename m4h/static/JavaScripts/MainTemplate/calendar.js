document.addEventListener('DOMContentLoaded', function() {
    const calendarEl = document.getElementById('calendar');
    const calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth',
        events: '/get_appointments',
        eventDisplay: 'block',  // Ensure that events are displayed as blocks
        eventTimeFormat: {      // Customize the time format for events
            hour: '2-digit',
            minute: '2-digit',
            meridiem: false
        },
        height: 'auto',         // Adjust the height to fit the container
        headerToolbar: {
            left: 'prev,next today',
            center: 'title',
            right: 'dayGridMonth,timeGridWeek,timeGridDay'
        },
        eventClick: function (info) {
            alert('Appointment: ' + info.event.title + '\nDate: ' + info.event.start);
        },
        eventContent: function (arg) {
            arg.timeText = undefined;
            let italicEl = document.createElement('span');
            italicEl.innerHTML = arg.timeText + ' ' + arg.event.title;

            let arrayOfDomNodes = [italicEl];
            return {domNodes: arrayOfDomNodes};
        }
    });
    calendar.render();
});
