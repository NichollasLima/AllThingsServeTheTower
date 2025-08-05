(function () {
  const version = new Date().getTime(); // Timestamp para bustar cache

  // ✅ Injetar CSS com versão
  const css = document.createElement('link');
  css.rel = 'stylesheet';
  css.href = `/AllThingsServeTheTower/style/main.css?v=${version}`;
  document.head.appendChild(css);

  // ✅ Injetar outros JS com versão (se necessário)
  const extraScripts = [
    '/AllThingsServeTheTower/static/js/menu.js',
    '/AllThingsServeTheTower/static/js/analytics.js'
  ];

  extraScripts.forEach(src => {
    const script = document.createElement('script');
    script.src = `${src}?v=${version}`;
    document.body.appendChild(script);
  });

  // ✅ Atualizar favicon com timestamp (opcional, só se estiver trocando de tempos em tempos)
  const favicon = document.querySelector("link[rel='icon']");
  if (favicon) {
    favicon.href = `https://i.imgur.com/R3raers.png?v=${version}`;
  }

  // ✅ Exemplo: atualizar imagem dinamicamente (opcional)
  // const logo = document.getElementById("logo");
  // if (logo) {
  //   logo.src = `/AllThingsServeTheTower/img/logo.png?v=${version}`;
  // }

})();
