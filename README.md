# ⚡ LEONUKEG — SYSTEM ARCHITECTURE [Reflex Edition]

> **"No construyo páginas. Construyo arquitecturas."**

Welcome to the internal blueprint of the LEONUKEG portfolio. 
This is not a traditional web page. It is a reactive, immersive system built entirely in **Python (Reflex)**, augmented with a custom **Self-Healing DOM** mechanism to bridge React hot-reloads with a high-performance Vanilla JS Web Worker rendering engine.

---

## 🧠 Core Philosophy

1. **Strict Separation of Concerns (SoC):** The UI is dumb; it only renders data. The logic is blind; it doesn't know how it is displayed. Python orchestrates the flow.
2. **Atomic Vibe:** No magic numbers. The visual experience (the "Vibe") is governed by strict CSS design tokens (`leonukeg.css`), ensuring visual consistency regardless of the rendering layer.
3. **Immutability by Default:** State transitions are predictable and isolated to prevent unpredictable side-effects.
4. **Self-Healing DOM:** Vanilla JS canvas loops and HUD event listeners dynamically query DOM elements. This allows the procedural visual engine to survive Reflex/React unmounting and hot-reloading cycles completely gracefully.

---

## 🏗 System Topology

The architecture is built on a solid Python backend that compiles to a dynamic React frontend:

```text
leonukeg_v2/
├── leonukeg_v2.py       # Main system loop & section orchestrator
├── state.py             # Reactive application state (Reflex State)
├── data.py              # Pure data layer (Projects, Labs)
├── components/          # Reusable, stateless UI atoms & molecules
│   ├── hud.py
│   ├── project_card.py
│   └── lab_item.py
└── assets/
    ├── bundle.js           # Self-healing visual engine (DOM bypass)
    ├── lightning.worker.js # Web Worker for concurrent ray calculation
    └── leonukeg.css        # Design tokens and atomic styles
```

---

## 🚀 Engine Boot Sequence

To spin up the local system:

1. **Initialize the Environment:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Engage the System:**
   ```bash
   reflex run
   ```
   *The system will boot the backend (Uvicorn/Granian) and serve the architecture at `http://localhost:3000`.*

---

## 🌌 Visual Engine Specifications

The background isn't a video. It's a procedural **Lightning Engine** running in a concurrent Web Worker, calculating fractal branches in real-time. 
- **Layer 0:** Web Worker calculates vectors, branches, opacities, and lifespans asynchronously at 60+ FPS.
- **Layer 1:** Main thread receives coordinate batches and renders via Canvas 2D to avoid blocking the main UI thread.
- **Layer 2 (Self-Healing):** `bundle.js` monitors the DOM environment. If Reflex hot-reloads and destroys the Canvas node, the engine intercepts the detachment, dynamically re-acquires the newly injected Canvas node, and resumes drawing without dropping a frame.

---

*"El hombre que pone corazón en lo que hace encuentra soluciones donde normalmente los perezosos e indolentes se dan por vencidos."*
**— Freddy León**
