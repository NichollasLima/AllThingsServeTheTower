(function () {
  const version = new Date().getTime(); // Gera timestamp

  // Adiciona CSS com versão
  const css = document.createElement('link');
  css.rel = 'stylesheet';
  css.href = `/AllThingsServeTheTower/style/main.css?v=${version}`;
  document.head.appendChild(css);

})();
