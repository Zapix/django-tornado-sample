(function(){
    var socket = new WebSocket('ws://' + djangoConstants.currentSite + ':' + djangoConstants.wsPort + '/ws/')
    socket.onmessage = function(recvData){
        recvData = JSON.parse(recvData.data);
        if(recvData.message){
            var $li = $("<li>").text(recvData.message);
            $(".income-list").prepend($li);
        }
    }
})();