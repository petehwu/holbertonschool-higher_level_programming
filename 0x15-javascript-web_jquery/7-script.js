const uri = 'https://swapi.co/api/people/5/?format=json';
$.get(uri, function (data) {
  $('DIV#character').html(data.name);
});
