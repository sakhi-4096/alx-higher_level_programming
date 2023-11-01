document.addEventListener('DOMContentLoaded', function () {
  const headerElements = document.getElementsByTagName('HEADER');
  for (const headerElement of headerElements) {
    headerElement.style.color = '#FF0000';
  }
});
