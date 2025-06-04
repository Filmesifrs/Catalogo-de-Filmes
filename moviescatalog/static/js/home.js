// JavaScript para a tela inicial com Bootstrap

document.addEventListener('DOMContentLoaded', function() {
    // Inicializar o carrossel Bootstrap
    var featuredCarousel = new bootstrap.Carousel(document.getElementById('featuredMoviesCarousel'), {
        interval: 50000000,  // Tempo entre slides em milissegundos
        wrap: true,      // Permite que o carrossel volte ao início após o último slide
        touch: true      // Permite navegação por toque em dispositivos móveis
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
});
