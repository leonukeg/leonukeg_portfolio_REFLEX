/**
 * bundle.js — LEONUKEG Unified Visual Engine (v9.0 - Ultra Resilience)
 */

(function() {
    'use strict';
    console.log("🚀 [LEONUKEG] Booting Engine v9.1 (Self-Healing)...");

    // ── 1. CLOCK MODULE ──────────────────────────────────────────────────
    function initClock() {
        const update = () => {
            const el = document.getElementById('current-time-display');
            if (!el) return;
            const now = new Date();
            const pad = (n) => String(n).padStart(2, '0');
            const timeStr = `${pad(now.getDate())}.${pad(now.getMonth()+1)}.${now.getFullYear()} | ${pad(now.getHours())}:${pad(now.getMinutes())}:${pad(now.getSeconds())}`;
            el.textContent = `──────── ${timeStr} ────────`;
        };
        setInterval(update, 1000);
        update();
    }

    // ── 2. CURSOR & HUD (Direct DOM Bypass) ─────────────────────────────
    function initHudEngine() {
        console.log("🎯 [LEONUKEG] HUD Engine Linked (Dynamic).");

        // Mouse Tracking
        window.addEventListener('mousemove', (e) => {
            const hudBL = document.getElementById('hud-bl');
            const hudBR = document.getElementById('hud-br');
            if (hudBL) hudBL.innerText = `LOC: ${e.clientX} / ${e.clientY}`;
            if (hudBR) {
                const scrollPerc = Math.round((window.scrollY / Math.max(1, document.documentElement.scrollHeight - window.innerHeight)) * 100);
                hudBR.innerText = `LEVEL: ${scrollPerc}%`;
            }
        });

        // Section Tracking
        const updateSections = () => {
            const sections = ['entry', 'system', 'work', 'lab', 'signals'];
            let current = "entry";
            sections.forEach(id => {
                const el = document.getElementById(id);
                if (el && el.getBoundingClientRect().top < window.innerHeight * 0.45) current = id;
            });

            // Update Index
            const idxItems = document.querySelectorAll('.idx');
            const activeIdx = sections.indexOf(current);
            idxItems.forEach((item, i) => item.classList.toggle('active', i === activeIdx));

            // Update HUD Status
            const hudTR = document.getElementById('hud-tr');
            if (hudTR) {
                const STATUS_MAP = {
                    'entry': 'NEURAL NET ACTIVE', 'system': 'SYSTEM LAYER SYNC',
                    'work': 'DATA OVERLOAD DETECTED', 'lab': 'STORM MODE ENABLED',
                    'signals': 'RECEIVING SIGNALS'
                };
                if (STATUS_MAP[current]) hudTR.innerText = STATUS_MAP[current];
            }
        };

        window.addEventListener('scroll', updateSections);
        updateSections();
    }

    // ── 3. LIGHTNING MODULE ─────────────────────────────────────────────
    function initLightning() {
        let canvas = document.getElementById('lightning');
        if (!canvas) {
            setTimeout(initLightning, 100);
            return;
        }
        let ctx = canvas.getContext('2d');
        let segments = [];
        try {
            const worker = new Worker('/lightning.worker.js');
            worker.onmessage = ({ data }) => { segments = data.segments; };
            
            const resize = () => {
                if (canvas && document.body.contains(canvas)) {
                    canvas.width = window.innerWidth * (window.devicePixelRatio || 1);
                    canvas.height = window.innerHeight * (window.devicePixelRatio || 1);
                    ctx.setTransform(window.devicePixelRatio || 1, 0, 0, window.devicePixelRatio || 1, 0, 0);
                }
                worker.postMessage({ type: 'resize', W: window.innerWidth, H: window.innerHeight });
            };
            window.addEventListener('resize', resize);
            resize();
            worker.postMessage({ type: 'init', W: window.innerWidth, H: window.innerHeight });
            
            function render() {
                // SELF-HEALING: If canvas was removed by React/Reflex, re-bind it!
                if (!canvas || !document.body.contains(canvas)) {
                    const newCanvas = document.getElementById('lightning');
                    if (newCanvas) {
                        canvas = newCanvas;
                        ctx = canvas.getContext('2d');
                        resize();
                    }
                }

                if (canvas && ctx && document.body.contains(canvas)) {
                    ctx.fillStyle = 'rgba(5, 8, 22, 0.7)'; 
                    ctx.fillRect(0, 0, window.innerWidth, window.innerHeight);
                    segments.forEach(s => {
                        ctx.beginPath(); ctx.moveTo(s.x1, s.y1); ctx.lineTo(s.x2, s.y2);
                        ctx.strokeStyle = '#1D9E75'; ctx.globalAlpha = (s.life / s.maxLife) * 0.6;
                        ctx.lineWidth = s.width; ctx.stroke();
                    });
                }
                requestAnimationFrame(render);
            }
            render();
        } catch (e) { console.error(e); }
    }

    // ── BOOT ────────────────────────────────────────────────────────────
    initClock();
    initHudEngine();
    initLightning();
    
    // GSAP Fallback
    setTimeout(() => {
        if (typeof gsap !== 'undefined' && typeof ScrollTrigger !== 'undefined') {
            gsap.registerPlugin(ScrollTrigger);
            gsap.from('.hero-name', { opacity: 0, y: 30, duration: 1 });
        }
    }, 1000);
})();
