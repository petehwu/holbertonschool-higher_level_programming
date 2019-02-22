document.addEventListener('DOMContentLoaded', function () {
  let lang;
  let uri = 'https://fourtonfish.com/hellosalut/?lang=';
  $('INPUT#language_code').keyup(function () {
    lang = $(this).val();
  });
  $(document).keypress(function (e) {
    if (e.which === 13) {
      if ($('INPUT#language_code').is(':focus')) {
        $.get(uri + lang, function (data) {
          $('DIV#hello').text(data.hello);
        });
      }
    }
  });
  $('INPUT#btn_translate').click(function () {
    $.get(uri + lang, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
});
