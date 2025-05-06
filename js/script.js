function switchView(view) {
  document.getElementById('login').classList.remove('active');
  document.getElementById('cadastro').classList.remove('active');
  document.getElementById('novaSenha').classList.remove('active');
  document.getElementById(view).classList.add('active');
  document.getElementById('modal').classList.remove('active');
}

function showModal() {
  document.getElementById('modal').classList.add('active');
}
