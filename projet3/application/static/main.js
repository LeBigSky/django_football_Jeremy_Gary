window.addEventListener('scroll', function() {
    const navbar = document.querySelector('.navbar'); // Remplace 'navbar' par l'ID réel de ta navbar
    const navLinks = document.querySelector('.navbar-nav')

    // Position du héros par rapport au haut de la page
    const heroHeight = document.getElementById('hero').offsetHeight; // Remplace 'hero' par l'ID réel de ton élément de héros
  
    if (window.pageYOffset > heroHeight) {
      navLinks.style.borderBottom = ""
      navbar.style.backgroundColor = "rgba(0,0,0,0.9)"
      navbar.classList.remove("py-4")
      navLinks.classList.remove("pb-3")
    } else {
      navLinks.style.borderBottom = "3px solid white";
      navbar.style.backgroundColor = "transparent"
      navbar.classList.add("py-4")
      navLinks.classList.add("pb-3")
    }
  });
  