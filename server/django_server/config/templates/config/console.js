$(document).ready(function () {

    websocket = 'ws://{{ request.get_host }}:9000/ws/console';
    if (window.WebSocket) {
        ws = new WebSocket(websocket, ['console']);
    }
    else if (window.MozWebSocket) {
        ws = MozWebSocket(websocket);
    }
    else {
        console.log('WebSocket Not Supported');
        return;
    }

    window.onbeforeunload = function (e) {
        $('#console').val($('#console').val() + 'Fermeture de la console... \n');
        ws.close();

        if (!e) e = window.event;
        e.stopPropagation();
        e.preventDefault();
    };
    ws.onmessage = function (evt) {
        if (evt.data == "connected") {
            $('#console').val($('#console').val() + "Connecté !" + '\n');
        }
        else {
            $('#console').val($('#console').val() + evt.data);
            var psconsole = $('#console');
            if (psconsole.length)
                psconsole.scrollTop(psconsole[0].scrollHeight - psconsole.height());
        }
    };
    ws.onopen = function () {
        ws.send("connect");
        $('#console').val($('#console').val() + 'Connexion à la console... \n');
    };
    ws.onclose = function (evt) {
        $('#console').val($('#console').val() + 'Connection closed by server: ' + evt.code + ' \"' + evt.reason + '\"\n');
    };

});