/**
 * app.js — LEONUKEG System Orchestrator
 * Brutal persistence for GSAP and Lightning in React environments.
 */

function initAll() {
    console.log("🚀 [LEONUKEG] System initialization triggered.");

    // 1. Inicializar Rayos (si el canvas existe)
    if (window.initLightning) {
        window.initLightning();
    }

    // 2. Inicializar Animaciones GSAP
    if (typeof gsap !== 'undefined' && typeof ScrollTrigger !== 'undefined') {
        gsap.registerPlugin(ScrollTrigger);
        
        // Limpiar estados previos
        ScrollTrigger.getAll().forEach(t => t.kill());
        gsap.set('.entry-label, .hero-name, .hero-sub, .hero-tagline, .scroll-hint', { opacity: 0, y: 20 });

        console.log("⚡ [LEONUKEG] Running entrance animations...");

        const introTL = gsap.timeline({ delay: 0.8 });
        introTL
          .to('.entry-label', { opacity: 1, y: 0, duration: 0.7, ease: 'power2.out' })
          .to('.hero-name',   { opacity: 1, y: 0, duration: 0.9, ease: 'power2.out' }, '-=0.35')
          .to('.hero-sub',    { opacity: 1, y: 0, duration: 0.7, ease: 'power2.out' }, '-=0.45')
          .to('.hero-tagline',{ opacity: 1, y: 0, duration: 0.8, ease: 'power2.out' }, '-=0.35')
          .to('.scroll-hint', { opacity: 1, duration: 0.6 });

        // Scroll Animations
        const sysEls = ['.system-h1','.system-body','.stack-label','.stack-line','.system-quote'];
        sysEls.forEach((sel, i) => {
          gsap.fromTo(sel,
            { opacity: 0, y: 40 },
            { opacity: 1, y: 0, duration: 0.9, ease: 'power3.out',
              scrollTrigger: { trigger: sel, start: 'top 90%' }, delay: i * 0.1 }
          );
        });

        document.querySelectorAll('.project').forEach((el, i) => {
          gsap.fromTo(el,
            { opacity: 0, y: 60, scale: 0.95 },
            { opacity: 1, y: 0, scale: 1, duration: 1.0, ease: 'power4.out',
              scrollTrigger: { trigger: el, start: 'top 92%' }, delay: i * 0.12 }
          );
        });
        
        // Refresh ScrollTrigger to ensure positions are correct
        ScrollTrigger.refresh();
    }
}

// EL OBSERVADOR: Vigila cuando el DOM de React termina de cargar los elementos clave
const observer = new MutationObserver((mutations, obs) => {
    const hero = document.querySelector('.hero-name');
    const canvas = document.getElementById('lightning');
    
    if (hero && canvas) {
        console.log("✅ [LEONUKEG] DOM Elements detected. Booting system...");
        initAll();
        // Una vez que arrancamos, dejamos de observar para ahorrar recursos
        obs.disconnect();
    }
});

// Iniciamos la observación del body
observer.observe(document.body, {
    childList: true,
    subtree: true
});

// También intentamos arrancar en carga normal por si acaso
window.addEventListener('load', initAll);
window.addEventListener('DOMContentLoaded', initAll);
