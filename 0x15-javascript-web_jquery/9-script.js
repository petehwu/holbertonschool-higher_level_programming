let uri = 'https://fourtonfish.com/hellosalut/?lang=';
const lang = $('html').attr('lang');
console.log(lang);
$.get(uri + lang, function (data) {
  $('DIV#hello').text(data.hello);
});
