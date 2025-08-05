document.addEventListener("DOMContentLoaded", () => {
  const input = document.getElementById("globalSearch");
  const resultsList = document.getElementById("searchResults");

  let pages = [];

  // Carrega o JSON gerado pelo Python
  fetch("/AllThingsServeTheTower/data/pages_data.json")
    .then(res => res.json())
    .then(data => pages = data)
    .catch(() => {
      resultsList.innerHTML = "<li>Erro ao carregar dados de busca.</li>";
    });

  input.addEventListener("input", () => {
    const query = input.value.trim().toLowerCase();
    resultsList.innerHTML = "";

    if (query.length < 2) {
      // Não pesquisa com menos de 2 letras
      return;
    }

    const filtered = pages.filter(page => {
      return (
        page.title.toLowerCase().includes(query) ||
        page.description.toLowerCase().includes(query)
      );
    });

    if (filtered.length === 0) {
      resultsList.innerHTML = "<li>Nenhum resultado encontrado.</li>";
      return;
    }

    filtered.forEach(page => {
      const li = document.createElement("li");
      const a = document.createElement("a");
      a.href = page.url;
      a.textContent = page.title;
      a.title = page.description; // mostra descrição no tooltip
      li.appendChild(a);
      resultsList.appendChild(li);
    });
  });
});
