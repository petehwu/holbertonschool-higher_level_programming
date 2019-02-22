const uri = 'https://swapi.co/api/films/?format=json';
$.get(uri, function (data) {
  $.each(data.results, function (index, val) {
    $('UL#list_movies').append('<li>' + val.title + '</li>');
  });
});
