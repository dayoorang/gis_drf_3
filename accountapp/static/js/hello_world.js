
function send_input() {
    axios.post('/accounts/hello_world/', {
    input_data: document.getElementById('input_data').value
  })
  .then(function (response) {
    console.log(response);

    document.getElementById('text').innerHTML = response.data['text'];
    document.getElementById('new_model_created_at').innerHTML = response.data['created_at'];

  })
  .catch(function (error) {
    console.log(error);
  });
}



<!-- 서버 호출 -->
axios.get('/accounts/hello_world/')
  .then(function (response) {
    // handle success
    console.log(response);

    for (let i = 0; i < response.data.length; i++){
    document.getElementById('new_model_list').innerHTML += '<h5>'+response.data[i]['text']+'</h5>';
    document.getElementById('new_model_list').innerHTML += '<p>'+response.data[i]['created_at']+'</p>';

    }

  })
  .catch(function (error) {
    // handle error
    console.log(error);
  })
  .then(function () {
    // always executed
  });

