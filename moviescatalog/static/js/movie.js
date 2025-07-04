document.addEventListener("DOMContentLoaded", () => {
  const btnEnviarAvaliacao = document.getElementById("btn-enviar-avaliacao");
  const comentarioTextarea = document.getElementById("comentario-avaliacao");
  const selectNota = document.getElementById("nota-avaliacao");
  const btnToggleWatched = document.getElementById("btn-toggle-watched");
  const listaAvaliacoes = document.getElementById("lista-avaliacoes");

  const resetForm = () => {
    selectNota.value = "0";
    comentarioTextarea.value = "";
  };

  const handleEnviarAvaliacao = () => {
    const selectedRating = parseInt(selectNota.value);

    if (!selectedRating) {
      alert("Por favor, selecione uma nota de 1 a 10.");
      return;
    }

    const comentario = comentarioTextarea.value.trim();

    fetch(`/movie/${movieId}/rate/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]").value
      },
      body: JSON.stringify({
        rating: selectedRating,
        review: comentario
      })
    })
      .then(response => response.json())
      .then(data => {
        if (data.success) {
          updateRatingsList(data.ratings);
          document.querySelector(".nota-media").textContent = data.avg_rating + " / 10";
          resetForm();
          alert("Avaliação enviada com sucesso!");
        } else {
          alert("Erro ao enviar avaliação: " + data.error);
        }
      })
      .catch(error => {
        console.error("Erro:", error);
        alert("Erro ao enviar avaliação. Tente novamente.");
      });
  };

  const updateRatingsList = (ratings) => {
    if (ratings.length === 0) {
      listaAvaliacoes.innerHTML = `
        <p class="sem-avaliacoes">Ainda não há avaliações para este filme. Seja o primeiro a avaliar!</p>
      `;
      return;
    }

    let html = "";
    ratings.forEach(rating => {
      html += `
        <div class="avaliacao-item">
          <div class="avaliacao-header">
            <strong>${rating.username}</strong>
            <div class="rating-display">
              ${generateStars(rating.rating)}
            </div>
            <span class="data-avaliacao">${rating.created_at}</span>
          </div>
          ${rating.review ? `<p class="comentario-avaliacao">${rating.review}</p>` : ""}
        </div>
      `;
    });

    listaAvaliacoes.innerHTML = html;
  };

  const generateStars = (rating10) => {
    const rating5 = rating10 / 2;
    const full = Math.floor(rating5);
    const half = (rating5 - full) >= 0.5 ? 1 : 0;
    const empty = 5 - full - half;

    let stars = "";

    for (let i = 0; i < full; i++) {
      stars += `<i class="bi bi-star-fill"></i>`;
    }
    if (half) {
      stars += `<i class="bi bi-star-half"></i>`;
    }
    for (let i = 0; i < empty; i++) {
      stars += `<i class="bi bi-star"></i>`;
    }

    return stars;
  };

  if (btnToggleWatched) {
    btnToggleWatched.addEventListener("click", () => {
      fetch("/watched/toggle/", {
        method: "POST",
        headers: {
          "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]").value,
          "Content-Type": "application/x-www-form-urlencoded"
        },
        body: new URLSearchParams({ movie_id: movieId })
      })
        .then(response => response.json())
        .then(data => {
          if (data.status === "success") {
            const icon = btnToggleWatched.querySelector("i");
            const label = btnToggleWatched.querySelector("span");

            if (data.watched) {
              icon.className = "bi bi-eye-fill";
              label.textContent = "Assistido";
              btnToggleWatched.dataset.watched = "true";
            } else {
              icon.className = "bi bi-eye";
              label.textContent = "Marcar como assistido";
              btnToggleWatched.dataset.watched = "false";
            }
          } else {
            alert(data.message || "Erro ao marcar como assistido.");
          }
        })
        .catch(error => {
          console.error("Erro:", error);
          alert("Erro de conexão.");
        });
    });
  }

  btnEnviarAvaliacao.addEventListener("click", handleEnviarAvaliacao);
});