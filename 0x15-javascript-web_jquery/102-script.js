$(document).ready(function () {
  $('#btn_translate').click(function () {
    $('#hello').empty();
    const len = $('#language_code').val();
    $.get('https://fourtonfish.com/hellosalut/?lang=' + len, function (data) {
      $('#hello').append(data.hello);
    });
  });
});
