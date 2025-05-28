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
      searchButton.addEventListener('click', function() {
        const searchTerm = searchInput.value.trim();
        if (searchTerm) {
          // Aqui podemos implementar a busca
          console.log('Buscando por:', searchTerm);
          // Exemplo de redirecionamento para uma página de resultados
          // window.location.href = `/search/?q=${encodeURIComponent(searchTerm)}`;
        }
      });

      // Permitir busca ao pressionar Enter
      searchInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
          const searchTerm = searchInput.value.trim();
          if (searchTerm) {
            console.log('Buscando por:', searchTerm);
            // Exemplo de redirecionamento para uma página de resultados
            // window.location.href = `/search/?q=${encodeURIComponent(searchTerm)}`;
          }
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
