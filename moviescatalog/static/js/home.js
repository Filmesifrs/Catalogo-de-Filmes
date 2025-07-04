// JavaScript para a tela inicial com Bootstrap

document.addEventListener('DOMContentLoaded', function() {
  // Carrossel de Filmes destaque (intervalo de 5 segundos)
  new bootstrap.Carousel(document.getElementById('featuredMoviesCarousel'), {
    interval: 5000,
    wrap: true,
    touch: true
  });

  // Carrossel de atores (intervalo de 40 segundos)
  new bootstrap.Carousel(document.getElementById('actorsCarousel'), {
    interval: 40000,
    wrap: true,
    touch: true
  });

  // Carrossel de categorias (intervalo de 60 segundos)
  new bootstrap.Carousel(document.getElementById('categoriesCarousel'), {
    interval: 60000,
    wrap: true,
    touch: true
  });

  // Funcionalidade do botão de busca
  const searchButton = document.querySelector('.search-button');
  const searchInput = document.querySelector('.search-input');

  if (searchButton && searchInput) {
    // Função para realizar a busca
    function performSearch() {
      const searchTerm = searchInput.value.trim();
      if (searchTerm) {
        // Redirecionar para a página de resultados da busca
        window.location.href = `/search/?query=${encodeURIComponent(searchTerm)}`;
      } else {
        // Se o campo estiver vazio, mostrar um alerta
        alert('Por favor, digite algo para buscar.');
      }
    }

    // Buscar ao clicar no botão
    searchButton.addEventListener('click', function(e) {
      e.preventDefault();
      performSearch();
    });

    // Permitir busca ao pressionar Enter
    searchInput.addEventListener('keypress', function(e) {
      if (e.key === 'Enter') {
        e.preventDefault();
        performSearch();
      }
    });
  }

  const movieCards = document.querySelectorAll('.movie-card, .top-movie-card');
  movieCards.forEach(card => {
    card.addEventListener('click', function() {
      // Aqui podemos implementar a navegação para a página de detalhes do filme
      console.log('Card de filme clicado');
      // Exemplo: window.location.href = `/movie/${movieId}/`;
    });
  });

  document.querySelectorAll('.genre-item').forEach(item => {
    item.addEventListener('click', function () {
      const genreName = this.getAttribute('data-name');
      if (genreName) {
        window.location.href = `/search/?genre=${encodeURIComponent(genreName)}`;
      }
    });
  });

  document.querySelectorAll('.actor-item').forEach(item => {
    item.addEventListener('click', function () {
      const actorName = this.getAttribute('data-name');
      if (actorName) {
        window.location.href = `/search/?actor=${encodeURIComponent(actorName)}`;
      }
    });
  });
});
