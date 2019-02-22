const style = document.createElement('style');
style.innerHTML = 'header {color: red;}';
const ref = document.querySelector('script');
ref.parentNode.insertBefore(style, ref);
