document.addEventListener('DOMContentLoaded', function () {
  let lang;
  let uri = 'https://fourtonfish.com/hellosalut/?lang=';
  $('INPUT#language_code').keyup(function () {
    lang = $(this).val();
  });
  $('INPUT#btn_translate').click(function () {
    $.get(uri + lang, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
});
