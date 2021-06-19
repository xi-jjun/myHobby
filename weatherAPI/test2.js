const getJSON= function(url, callback) {
    const xhr = new XMLHttpRequest();
    xhr.open('GET',url,true);
    xhr.responseType = 'json';
    xhr.onload = function() {
        const status = xhr.status;
        if (status === 200) {
            callback(null, xhr.response);
        } else {
            callback(status, xhr.response);
        }
    };
    xhr.send();
}

getJSON('http://api.openweathermap.org/data/2.5/weather?q=Seoul&appid=70632352ff4e5db434db8526275d5c48',
function(err, data) {
    if(err !== null) {
        alert('Error!!!!');
    } else {
        alert('현재 온도는 ${data.main.temp}도 입니다.');
    }
});