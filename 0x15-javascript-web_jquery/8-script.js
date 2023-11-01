$(document).ready(function () {
  $.get('https://swapi.co/api/films/?format=json', function (data) {
    const movies = data.results.map(function (film) {
      return '<li>' + film.title + '</li>';
    });

    $('#list_movies').html('<ul>' + movies.join('') + '</ul');
  });
});
