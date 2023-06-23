window.addEventListener('scroll', function() {
    const navbar = document.querySelector('.navbar'); // Remplace 'navbar' par l'ID réel de ta navbar
  
    // Position du héros par rapport au haut de la page
    const heroHeight = document.getElementById('hero').offsetHeight; // Remplace 'hero' par l'ID réel de ton élément de héros
  
    if (window.pageYOffset > heroHeight) {
      navbar.classList.add('bg-dark'); // Ajoute la classe 'bg-dark' à la navbar
    } else {
      navbar.classList.remove('bg-dark'); // Supprime la classe 'bg-dark' de la navbar
    }
  });
  