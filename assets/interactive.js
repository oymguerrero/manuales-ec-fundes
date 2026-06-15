/* =========================================================
   Mi CompañIA — Componentes interactivos
   Tabs accesibles (ARIA) y checklists con persistencia local
   ========================================================= */

(function () {
  'use strict';

  // ---------- Tabs ----------
  // Markup esperado:
  // <div class="tabs">
  //   <div class="tabs__list" role="tablist" aria-label="...">
  //     <button class="tabs__tab" role="tab" id="tab-x" aria-controls="panel-x" aria-selected="true">...</button>
  //     ...
  //   </div>
  //   <div class="tabs__panel" id="panel-x" role="tabpanel" aria-labelledby="tab-x">...</div>
  //   ...
  // </div>
  function initTabs(container) {
    const tabs = container.querySelectorAll('[role="tab"]');
    const panels = container.querySelectorAll('[role="tabpanel"]');
    if (!tabs.length || !panels.length) return;

    function activate(targetIdx, focusTab) {
      tabs.forEach(function (tab, i) {
        const isActive = i === targetIdx;
        tab.setAttribute('aria-selected', isActive ? 'true' : 'false');
        tab.tabIndex = isActive ? 0 : -1;
      });
      panels.forEach(function (panel, i) {
        panel.hidden = i !== targetIdx;
      });
      if (focusTab) tabs[targetIdx].focus();
    }

    tabs.forEach(function (tab, i) {
      tab.addEventListener('click', function () { activate(i, false); });
      tab.addEventListener('keydown', function (e) {
        let next = null;
        if (e.key === 'ArrowRight') next = (i + 1) % tabs.length;
        else if (e.key === 'ArrowLeft') next = (i - 1 + tabs.length) % tabs.length;
        else if (e.key === 'Home') next = 0;
        else if (e.key === 'End') next = tabs.length - 1;
        if (next !== null) {
          e.preventDefault();
          activate(next, true);
        }
      });
    });

    // Asegurar estado inicial: si ningún tab tiene aria-selected="true", activar el primero
    const initial = Array.prototype.findIndex.call(tabs, function (t) {
      return t.getAttribute('aria-selected') === 'true';
    });
    activate(initial >= 0 ? initial : 0, false);
  }

  // ---------- Checklist con persistencia local ----------
  // Markup esperado:
  // <div class="checklist" data-storage-key="clave-unica">
  //   <ul>
  //     <li><label><input type="checkbox" /><span class="checklist__text">...</span></label></li>
  //     ...
  //   </ul>
  //   <div class="checklist__progress">
  //     <progress class="checklist__bar" max="100" value="0"></progress>
  //     <span class="checklist__count">0 de N</span>
  //   </div>
  // </div>
  function initChecklist(container) {
    const key = 'mi-compania-checklist::' + (container.dataset.storageKey || 'default');
    const items = container.querySelectorAll('input[type="checkbox"]');
    const bar = container.querySelector('.checklist__bar');
    const count = container.querySelector('.checklist__count');
    if (!items.length) return;

    let stored = {};
    try {
      stored = JSON.parse(localStorage.getItem(key) || '{}');
    } catch (e) { stored = {}; }

    items.forEach(function (item, i) {
      if (stored[i]) item.checked = true;
      item.addEventListener('change', function () {
        const state = {};
        items.forEach(function (it, j) { state[j] = it.checked; });
        try {
          localStorage.setItem(key, JSON.stringify(state));
        } catch (e) { /* localStorage lleno o bloqueado: degradación silenciosa */ }
        updateProgress();
      });
    });

    function updateProgress() {
      const total = items.length;
      const done = Array.prototype.filter.call(items, function (i) { return i.checked; }).length;
      const pct = total ? Math.round((done / total) * 100) : 0;
      if (bar) bar.value = pct;
      if (count) count.textContent = done + ' de ' + total + ' (' + pct + '%)';
    }

    updateProgress();
  }

  // ---------- Flip card ----------
  // Markup esperado:
  // <button class="flipcard" aria-pressed="false">
  //   <span class="flipcard__inner">
  //     <span class="flipcard__face flipcard__face--front">...</span>
  //     <span class="flipcard__face flipcard__face--back">...</span>
  //   </span>
  // </button>
  function initFlipcard(card) {
    card.addEventListener('click', function () {
      const pressed = card.getAttribute('aria-pressed') === 'true';
      card.setAttribute('aria-pressed', pressed ? 'false' : 'true');
    });
    card.addEventListener('keydown', function (e) {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        card.click();
      }
    });
  }

  // ---------- Quiz (v2 — multi-tipo) ----------
  // Tipos soportados:
  //   sin data-type o data-type="mc": multiple choice (legacy markup con data-correct).
  //   data-type="vf": verdadero/falso (mismo markup que mc, data-correct="v" o "f").
  //   data-type="order": ordenar pasos. Markup:
  //     <div class="quiz" data-type="order"><ol class="quiz__sortable">
  //       <li class="quiz__item" data-correct-pos="1">Paso A</li>... </ol>
  //       <button class="quiz__check" type="button">Verificar</button></div>
  //   data-type="cloze": completar frase. Markup:
  //     <p class="quiz__cloze">Un <span class="quiz__blank" data-answers="EC,estandar">__</span>...</p>
  function initQuiz(quiz) {
    const type = quiz.dataset.type || 'mc';
    const quizId = quiz.id || quiz.dataset.storageKey || 'quiz-' + Math.random().toString(36).slice(2, 8);

    if (type === 'mc' || type === 'vf') return initQuizChoice(quiz, quizId);
    if (type === 'order') return initQuizOrder(quiz, quizId);
    if (type === 'cloze') return initQuizCloze(quiz, quizId);
  }

  function initQuizChoice(quiz, quizId) {
    const correct = quiz.dataset.correct;
    const options = quiz.querySelectorAll('.quiz__option');
    const feedbackCorrect = quiz.querySelector('.quiz__feedback--correct');
    const feedbackWrong = quiz.querySelector('.quiz__feedback--wrong');
    const retryBtn = quiz.querySelector('.quiz__retry');
    if (!correct || !options.length) return;
    let attempts = 0;

    function reset() {
      options.forEach(function (o) {
        o.removeAttribute('data-state');
        o.removeAttribute('disabled');
      });
      if (feedbackCorrect) feedbackCorrect.hidden = true;
      if (feedbackWrong) feedbackWrong.hidden = true;
      attempts = 0;
    }

    options.forEach(function (option) {
      option.addEventListener('click', function () {
        attempts++;
        const isCorrect = option.dataset.option === correct;
        if (isCorrect) {
          option.setAttribute('data-state', 'correct');
          options.forEach(function (o) { if (o !== option) o.setAttribute('disabled', 'disabled'); });
          if (feedbackCorrect) feedbackCorrect.hidden = false;
          if (feedbackWrong) feedbackWrong.hidden = true;
          recordEvent('quiz', { quizId: quizId, type: quiz.dataset.type || 'mc', correct: true, attempts: attempts });
        } else {
          option.setAttribute('data-state', 'wrong');
          option.setAttribute('disabled', 'disabled');
          if (feedbackWrong) feedbackWrong.hidden = false;
          if (feedbackCorrect) feedbackCorrect.hidden = true;
          recordEvent('quiz', { quizId: quizId, type: quiz.dataset.type || 'mc', correct: false, attempts: attempts });
        }
      });
    });

    if (retryBtn) retryBtn.addEventListener('click', reset);
  }

  function initQuizOrder(quiz, quizId) {
    const list = quiz.querySelector('.quiz__sortable');
    const items = list ? Array.prototype.slice.call(list.querySelectorAll('.quiz__item')) : [];
    const checkBtn = quiz.querySelector('.quiz__check');
    const feedbackCorrect = quiz.querySelector('.quiz__feedback--correct');
    const feedbackWrong = quiz.querySelector('.quiz__feedback--wrong');
    const retryBtn = quiz.querySelector('.quiz__retry');
    if (!list || items.length < 2) return;
    let attempts = 0;

    // Mezclar al inicio (Fisher-Yates) si data-shuffle="true" (default true)
    const shuffle = quiz.dataset.shuffle !== 'false';
    if (shuffle) {
      const shuffled = items.slice();
      for (let i = shuffled.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
      }
      list.innerHTML = '';
      shuffled.forEach(function (it) { list.appendChild(it); });
    }

    // Para cada item: controles ↑ ↓ y rol listitem
    items.forEach(function (item, idx) {
      item.setAttribute('tabindex', '0');
      const controls = document.createElement('span');
      controls.className = 'quiz__item-controls';
      controls.innerHTML = '<button type="button" class="quiz__item-up" aria-label="Mover arriba">▲</button>' +
        '<button type="button" class="quiz__item-down" aria-label="Mover abajo">▼</button>';
      item.appendChild(controls);
    });

    list.addEventListener('click', function (e) {
      const li = e.target.closest('.quiz__item');
      if (!li) return;
      if (e.target.classList.contains('quiz__item-up')) move(li, -1);
      else if (e.target.classList.contains('quiz__item-down')) move(li, 1);
    });

    list.addEventListener('keydown', function (e) {
      const li = e.target.closest('.quiz__item');
      if (!li) return;
      if (e.key === 'ArrowUp' && (e.altKey || e.metaKey)) { e.preventDefault(); move(li, -1); }
      else if (e.key === 'ArrowDown' && (e.altKey || e.metaKey)) { e.preventDefault(); move(li, 1); }
    });

    function move(li, dir) {
      const all = Array.prototype.slice.call(list.querySelectorAll('.quiz__item'));
      const idx = all.indexOf(li);
      const target = idx + dir;
      if (target < 0 || target >= all.length) return;
      if (dir < 0) list.insertBefore(li, all[target]);
      else list.insertBefore(li, all[target].nextSibling);
      li.focus();
    }

    function checkOrder() {
      attempts++;
      const current = Array.prototype.slice.call(list.querySelectorAll('.quiz__item'));
      const ok = current.every(function (it, i) {
        return String(it.dataset.correctPos) === String(i + 1);
      });
      current.forEach(function (it, i) {
        it.setAttribute('data-state', String(it.dataset.correctPos) === String(i + 1) ? 'correct' : 'wrong');
      });
      if (ok) {
        if (feedbackCorrect) feedbackCorrect.hidden = false;
        if (feedbackWrong) feedbackWrong.hidden = true;
        recordEvent('quiz', { quizId: quizId, type: 'order', correct: true, attempts: attempts });
      } else {
        if (feedbackWrong) feedbackWrong.hidden = false;
        if (feedbackCorrect) feedbackCorrect.hidden = true;
        recordEvent('quiz', { quizId: quizId, type: 'order', correct: false, attempts: attempts });
      }
    }

    if (checkBtn) checkBtn.addEventListener('click', checkOrder);
    if (retryBtn) retryBtn.addEventListener('click', function () {
      items.forEach(function (it) { it.removeAttribute('data-state'); });
      if (feedbackCorrect) feedbackCorrect.hidden = true;
      if (feedbackWrong) feedbackWrong.hidden = true;
      attempts = 0;
    });
  }

  function initQuizCloze(quiz, quizId) {
    const blanks = quiz.querySelectorAll('.quiz__blank');
    const checkBtn = quiz.querySelector('.quiz__check');
    const feedbackCorrect = quiz.querySelector('.quiz__feedback--correct');
    const feedbackWrong = quiz.querySelector('.quiz__feedback--wrong');
    const retryBtn = quiz.querySelector('.quiz__retry');
    if (!blanks.length) return;
    let attempts = 0;

    // Convertir cada .quiz__blank en input
    blanks.forEach(function (b) {
      const input = document.createElement('input');
      input.type = 'text';
      input.className = 'quiz__blank-input';
      input.setAttribute('aria-label', 'Completar');
      input.size = Math.max(8, (b.dataset.size || 10) * 1);
      b.innerHTML = '';
      b.appendChild(input);
    });

    function normalize(s) {
      return (s || '').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').trim();
    }

    function checkCloze() {
      attempts++;
      let allOk = true;
      blanks.forEach(function (b) {
        const input = b.querySelector('.quiz__blank-input');
        const value = normalize(input.value);
        const answers = (b.dataset.answers || '').split('|').map(normalize);
        const ok = answers.some(function (a) { return a && a === value; });
        b.setAttribute('data-state', ok ? 'correct' : 'wrong');
        if (!ok) allOk = false;
      });
      if (allOk) {
        if (feedbackCorrect) feedbackCorrect.hidden = false;
        if (feedbackWrong) feedbackWrong.hidden = true;
        recordEvent('quiz', { quizId: quizId, type: 'cloze', correct: true, attempts: attempts });
      } else {
        if (feedbackWrong) feedbackWrong.hidden = false;
        if (feedbackCorrect) feedbackCorrect.hidden = true;
        recordEvent('quiz', { quizId: quizId, type: 'cloze', correct: false, attempts: attempts });
      }
    }

    if (checkBtn) checkBtn.addEventListener('click', checkCloze);
    if (retryBtn) retryBtn.addEventListener('click', function () {
      blanks.forEach(function (b) {
        b.removeAttribute('data-state');
        const i = b.querySelector('.quiz__blank-input');
        if (i) i.value = '';
      });
      if (feedbackCorrect) feedbackCorrect.hidden = true;
      if (feedbackWrong) feedbackWrong.hidden = true;
      attempts = 0;
    });
  }

  // ---------- Audio narración ----------
  // Markup esperado:
  // <div class="audio-narration">
  //   <div class="audio-narration__header">
  //     <button class="audio-narration__toggle" aria-expanded="false" aria-controls="audio-X">
  //       Escuchar esta sección
  //     </button>
  //     <span class="audio-narration__meta">3 min · voz Neural2</span>
  //   </div>
  //   <div class="audio-narration__player" id="audio-X" hidden>
  //     <audio controls preload="none">
  //       <source src="..." type="audio/mpeg" />
  //     </audio>
  //   </div>
  //   <details class="audio-narration__transcript">
  //     <summary>Ver transcripción</summary>
  //     <div class="audio-narration__transcript-body">...</div>
  //   </details>
  // </div>
  function initAudioNarration(container) {
    const toggle = container.querySelector('.audio-narration__toggle');
    const player = container.querySelector('.audio-narration__player');
    const audio = container.querySelector('audio');
    if (!toggle || !player || !audio) return;

    const labelClosed = toggle.dataset.labelClosed || toggle.textContent.trim() || 'Escuchar esta sección';
    const labelOpen = toggle.dataset.labelOpen || 'Ocultar reproductor';

    // El toggle solo controla visibilidad del player. NO pausa el audio.
    // El audio se controla con los botones nativos del <audio> o desde el mini-bar flotante.
    toggle.addEventListener('click', function () {
      const expanded = toggle.getAttribute('aria-expanded') === 'true';
      if (expanded) {
        toggle.setAttribute('aria-expanded', 'false');
        player.hidden = true;
        toggle.textContent = labelClosed;
      } else {
        toggle.setAttribute('aria-expanded', 'true');
        player.hidden = false;
        toggle.textContent = labelOpen;
        if (audio.paused) {
          audio.play().catch(function () { /* el usuario debe pulsar play manualmente */ });
        }
      }
    });

    // Al terminar, restablece el estado inicial
    audio.addEventListener('ended', function () {
      toggle.setAttribute('aria-expanded', 'false');
      player.hidden = true;
      toggle.textContent = labelClosed;
    });

    // ---- Mini-bar flotante ----
    // Toma el título de la sección padre (h2/h3 más cercano)
    const section = container.closest('section') || container.parentElement;
    const titleEl = section && section.querySelector('h1, h2, h3');
    const title = titleEl ? titleEl.textContent.trim() : 'Narración de audio';

    const bar = createFloatingBar(audio, container, title);

    let inView = true;
    let userClosed = false;

    const obs = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { inView = e.isIntersecting; });
      updateBar();
    }, { threshold: 0 });
    obs.observe(container);

    audio.addEventListener('play', function () { userClosed = false; updateBar(); });
    audio.addEventListener('pause', updateBar);
    audio.addEventListener('ended', function () { hideBar(); });

    bar.dataset.audioRef = ''; // marker

    bar.querySelector('.audio-floating__play').addEventListener('click', function () {
      if (audio.paused) audio.play().catch(function () {});
      else audio.pause();
    });
    bar.querySelector('.audio-floating__title').addEventListener('click', function () {
      container.scrollIntoView({ behavior: 'smooth', block: 'center' });
    });
    bar.querySelector('.audio-floating__close').addEventListener('click', function () {
      audio.pause();
      userClosed = true;
      hideBar();
    });

    function updateBar() {
      if (userClosed) { hideBar(); return; }
      // Si el .audio-narration vive dentro de un <details> que NO está abierto
      // (módulo no activo del lesson-tabs), nunca mostramos el mini-bar.
      // Solo aparece cuando el usuario está en el módulo donde vive el audio
      // y ha hecho scroll fuera del reproductor mientras el audio suena.
      const parentDetails = container.closest('details.accordion__item');
      if (parentDetails && !parentDetails.open) {
        hideBar();
        return;
      }
      if (!audio.paused && !inView) {
        showBar(true);
      } else {
        // En todos los demás casos (en vista, pausado, o ambos) ocultamos.
        // El reproductor original ya es visible/accesible; no necesitamos un bar.
        hideBar();
      }
    }

    function showBar(isPlaying) {
      bar.classList.add('audio-floating--visible');
      const btn = bar.querySelector('.audio-floating__play');
      btn.setAttribute('aria-label', isPlaying ? 'Pausar narración' : 'Reanudar narración');
      btn.dataset.state = isPlaying ? 'playing' : 'paused';
    }
    function hideBar() {
      bar.classList.remove('audio-floating--visible');
    }
  }

  function createFloatingBar(audio, container, title) {
    const bar = document.createElement('div');
    bar.className = 'audio-floating';
    bar.setAttribute('role', 'region');
    bar.setAttribute('aria-label', 'Reproductor de audio flotante');
    bar.innerHTML =
      '<button class="audio-floating__play" type="button" data-state="playing" aria-label="Pausar narración">' +
        '<svg class="audio-floating__icon-play" aria-hidden="true" viewBox="0 0 24 24" focusable="false"><path d="M8 5v14l11-7z" fill="currentColor"/></svg>' +
        '<svg class="audio-floating__icon-pause" aria-hidden="true" viewBox="0 0 24 24" focusable="false"><rect x="6" y="5" width="4" height="14" fill="currentColor"/><rect x="14" y="5" width="4" height="14" fill="currentColor"/></svg>' +
      '</button>' +
      '<button class="audio-floating__title" type="button" aria-label="Ir a la sección del audio en la página">' +
        '<svg class="audio-floating__icon-head" aria-hidden="true" viewBox="0 0 24 24" focusable="false"><path fill="currentColor" d="M12 3a8 8 0 0 0-8 8v6a2 2 0 0 0 2 2h2v-7H6v-1a6 6 0 0 1 12 0v1h-2v7h2a2 2 0 0 0 2-2v-6a8 8 0 0 0-8-8z"/></svg>' +
        '<span class="audio-floating__text">' + title + '</span>' +
      '</button>' +
      '<button class="audio-floating__close" type="button" aria-label="Detener narración y cerrar">' +
        '<svg aria-hidden="true" viewBox="0 0 24 24" focusable="false"><path d="M6 6l12 12M18 6L6 18" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"/></svg>' +
      '</button>';
    document.body.appendChild(bar);
    return bar;
  }

  // ---------- Accordion modules: sincronización con TOC + controles globales ----------
  // - Click en anchor (TOC u otro link interno) que apunte a un .accordion__item:
  //   abre el details, hace scroll suave, resalta con animación.
  // - Botón "Expandir todo" / "Colapsar todo": abre o cierra todos los <details>
  //   del grupo .accordion--modules más cercano.
  function initAccordionModules() {
    // Sincronizar clicks de anchors que apuntan a .accordion__item
    document.addEventListener('click', function (e) {
      const link = e.target.closest('a[href^="#"]');
      if (!link) return;
      const targetId = link.getAttribute('href').slice(1);
      if (!targetId) return;
      const target = document.getElementById(targetId);
      if (!target) return;
      // Si el target es un <details> (.accordion__item), abrirlo
      let detailsEl = null;
      if (target.tagName === 'DETAILS') {
        detailsEl = target;
      } else {
        // También buscar si el target está dentro de un <details>
        detailsEl = target.closest('details.accordion__item');
      }
      if (detailsEl) {
        detailsEl.open = true;
        // Pequeño delay para que se aplique el layout abierto antes del scroll
        e.preventDefault();
        requestAnimationFrame(function () {
          detailsEl.scrollIntoView({ behavior: 'smooth', block: 'start' });
          detailsEl.classList.add('is-highlighted');
          setTimeout(function () {
            detailsEl.classList.remove('is-highlighted');
          }, 1300);
        });
      }
    });

    // Controles "Expandir todo" / "Colapsar todo"
    document.querySelectorAll('.accordion-controls').forEach(function (controls) {
      const group = controls.parentElement.querySelector('.accordion--modules')
                 || document.querySelector(controls.dataset.target || '.accordion--modules');
      if (!group) return;
      const expandBtn = controls.querySelector('[data-action="expand"]');
      const collapseBtn = controls.querySelector('[data-action="collapse"]');
      if (expandBtn) {
        expandBtn.addEventListener('click', function () {
          group.querySelectorAll('details.accordion__item').forEach(function (d) {
            d.open = true;
          });
        });
      }
      if (collapseBtn) {
        collapseBtn.addEventListener('click', function () {
          group.querySelectorAll('details.accordion__item').forEach(function (d) {
            d.open = false;
          });
        });
      }
    });

    // Si la URL llega con hash que apunta a un module: abrirlo al cargar
    if (window.location.hash) {
      const id = window.location.hash.slice(1);
      const target = document.getElementById(id);
      if (target) {
        const detailsEl = target.tagName === 'DETAILS' ? target : target.closest('details.accordion__item');
        if (detailsEl) {
          detailsEl.open = true;
          requestAnimationFrame(function () {
            detailsEl.scrollIntoView({ behavior: 'auto', block: 'start' });
            detailsEl.classList.add('is-highlighted');
            setTimeout(function () { detailsEl.classList.remove('is-highlighted'); }, 1300);
          });
        }
      }
    }
  }

  // ---------- Lesson Tabs (LMS-style: sidebar + panel + tracking de avance) ----------
  // Transforma un .accordion.accordion--modules en layout sidebar + panel:
  // - sidebar listado clickeable con check de avance
  // - panel principal con un solo módulo visible
  // - localStorage persiste los módulos marcados como completados
  // - botones "Marcar como leído y continuar →" + "← Anterior"
  // El markup HTML original (details/summary) se mantiene intacto para
  // accesibilidad, Ctrl+F y print. El comportamiento visual es controlado por JS+CSS.
  function initLessonTabs(container) {
    // Solo los <details> que son módulos directos del wrapper .accordion--modules.
    // Sin :scope > selector, los <details> ANIDADOS dentro del contenido (ej. los
    // de las preguntas FAQ del módulo) se tomarían erróneamente como módulos
    // del sidebar y aparecerían como entradas vacías.
    const wrapper = container.querySelector('.accordion.accordion--modules')
                  || container.querySelector('.accordion--modules');
    const items = wrapper
      ? Array.from(wrapper.querySelectorAll(':scope > details.accordion__item'))
      : Array.from(container.querySelectorAll('details.accordion__item'));
    if (!items.length) return;

    // Storage key: data-progress-key o derivado del path
    const storageKey = 'mi-compania-lessons::' +
      (container.dataset.progressKey ||
       (location.pathname.replace(/[^a-z0-9-]/gi, '_') + '::' + (container.getAttribute('aria-label') || 'modules')));

    // Lee estado previo
    let completed = new Set();
    try {
      const raw = JSON.parse(localStorage.getItem(storageKey) || '[]');
      if (Array.isArray(raw)) completed = new Set(raw);
    } catch (e) { /* localStorage bloqueado: degradación silenciosa */ }

    function persist() {
      try {
        localStorage.setItem(storageKey, JSON.stringify(Array.from(completed)));
      } catch (e) { /* nop */ }
    }

    // Construir UI del header (progress) + layout (sidebar + panel)
    // Insertar el header ANTES del container; el layout reemplaza al container interno
    const header = document.createElement('div');
    header.className = 'lesson-tabs__header';
    header.innerHTML =
      '<span class="lesson-tabs__progress-text">' +
        '<strong class="lesson-tabs__count">0</strong> de ' + items.length + ' módulos completados' +
      '</span>' +
      '<div class="lesson-tabs__progress-bar" role="progressbar" aria-label="Avance del capítulo" aria-valuemin="0" aria-valuemax="' + items.length + '" aria-valuenow="0">' +
        '<div class="lesson-tabs__progress-fill"></div>' +
      '</div>' +
      '<button type="button" class="lesson-tabs__reset" aria-label="Reiniciar el avance de este capítulo">Reiniciar</button>';

    const layout = document.createElement('div');
    layout.className = 'lesson-tabs__layout';

    const sidebar = document.createElement('nav');
    sidebar.className = 'lesson-tabs__sidebar';
    sidebar.setAttribute('aria-label', 'Lista de módulos del capítulo');

    const panel = document.createElement('div');
    panel.className = 'lesson-tabs__panel';

    const panelCard = document.createElement('article');
    panelCard.className = 'lesson-tabs__panel-card';

    const panelHeader = document.createElement('div');
    panelHeader.className = 'lesson-tabs__panel-header';
    panelHeader.innerHTML =
      '<span class="lesson-tabs__panel-num"></span>' +
      '<div style="flex:1 1 auto; min-width:0;">' +
        '<h2 class="lesson-tabs__panel-title"></h2>' +
        '<span class="lesson-tabs__panel-meta"></span>' +
      '</div>';

    const panelContent = document.createElement('div');
    panelContent.className = 'lesson-tabs__panel-content';

    const panelFooter = document.createElement('div');
    panelFooter.className = 'lesson-tabs__panel-footer';
    panelFooter.innerHTML =
      '<button type="button" class="lesson-tabs__nav-btn lesson-tabs__nav-btn--prev" data-action="prev">' +
        '<span aria-hidden="true">←</span> Anterior' +
      '</button>' +
      '<button type="button" class="lesson-tabs__nav-btn lesson-tabs__nav-btn--complete" data-action="complete">' +
        '<span aria-hidden="true">✓</span> Marcar como leído y continuar' +
      '</button>';

    panelCard.appendChild(panelHeader);
    panelCard.appendChild(panelContent);
    panelCard.appendChild(panelFooter);
    panel.appendChild(panelCard);

    layout.appendChild(sidebar);
    layout.appendChild(panel);

    // Inyectar header y layout DENTRO del container (.lesson-tabs)
    container.insertBefore(header, container.firstChild);
    container.appendChild(layout);

    // Mover el .accordion accordion--modules wrapper (con todos los <details>) DENTRO del panelContent
    // pero solo para tener los <details> como source de contenido; los items se muestran en el panel.
    const sourceWrapper = container.querySelector('.accordion.accordion--modules')
                       || container.querySelector('.accordion--modules');
    if (sourceWrapper && sourceWrapper.parentElement !== panelContent) {
      panelContent.appendChild(sourceWrapper);
    }

    // Quitar controles "expandir/colapsar" si existieran (no aplican aquí)
    const oldControls = container.querySelector('.accordion-controls');
    if (oldControls) oldControls.remove();

    // Construir items del sidebar: replicar info de cada <summary>
    items.forEach(function (det, index) {
      const id = det.id || ('lesson-' + index);
      if (!det.id) det.id = id;
      const summary = det.querySelector('summary');
      const num = (summary && summary.querySelector('.accordion__num')) ? summary.querySelector('.accordion__num').textContent.trim() : (index + 1);
      const title = (summary && summary.querySelector('.accordion__title-main')) ? summary.querySelector('.accordion__title-main').textContent.trim() : ('Módulo ' + (index + 1));
      const meta = (summary && summary.querySelector('.accordion__meta')) ? summary.querySelector('.accordion__meta').textContent.trim() : '';

      const btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'lesson-tab-item';
      btn.dataset.target = id;
      btn.setAttribute('aria-controls', id);
      btn.innerHTML =
        '<span class="lesson-tab-item__indicator"><span class="lesson-tab-item__num-inside">' + (index + 1) + '</span></span>' +
        '<span class="lesson-tab-item__num">' + num + '</span>' +
        '<span class="lesson-tab-item__title">' + title + '</span>' +
        (meta ? '<span class="lesson-tab-item__meta">' + meta + '</span>' : '');
      sidebar.appendChild(btn);
    });

    function openItem(idx, options) {
      options = options || {};
      if (idx < 0 || idx >= items.length) return;
      // Pausa audios de los módulos que se van a cerrar (audio scoped al módulo activo).
      // Sin esto, un audio iniciado en el módulo 1.1 seguiría sonando al cambiar a 1.3
      // y dispararía el mini-bar flotante de forma molesta (el contenedor original
      // queda oculto vía display:none, IntersectionObserver lo detecta como "fuera").
      items.forEach(function (d, i) {
        if (i !== idx) {
          d.querySelectorAll('audio').forEach(function (a) {
            if (!a.paused) {
              a.pause();
              // Restablece el toggle del .audio-narration si estaba expandido
              const container = a.closest('.audio-narration');
              if (container) {
                const toggle = container.querySelector('.audio-narration__toggle');
                const player = container.querySelector('.audio-narration__player');
                if (toggle && toggle.getAttribute('aria-expanded') === 'true') {
                  toggle.setAttribute('aria-expanded', 'false');
                  if (player) player.hidden = true;
                  toggle.textContent = toggle.dataset.labelClosed || 'Escuchar esta sección';
                }
              }
            }
          });
        }
      });
      // Cerrar todos los demás
      items.forEach(function (d, i) {
        d.open = i === idx;
      });
      // Actualizar visualmente sidebar
      const sidebarBtns = sidebar.querySelectorAll('.lesson-tab-item');
      sidebarBtns.forEach(function (b, i) {
        b.classList.toggle('is-active', i === idx);
      });
      // Actualizar header del panel desde el summary del item activo
      const det = items[idx];
      const summary = det.querySelector('summary');
      const num = (summary && summary.querySelector('.accordion__num')) ? summary.querySelector('.accordion__num').textContent.trim() : (idx + 1);
      const title = (summary && summary.querySelector('.accordion__title-main')) ? summary.querySelector('.accordion__title-main').textContent.trim() : ('Módulo ' + (idx + 1));
      const meta = (summary && summary.querySelector('.accordion__meta')) ? summary.querySelector('.accordion__meta').textContent.trim() : '';
      panelHeader.querySelector('.lesson-tabs__panel-num').textContent = num;
      panelHeader.querySelector('.lesson-tabs__panel-title').textContent = title;
      panelHeader.querySelector('.lesson-tabs__panel-meta').textContent = meta;
      // Actualizar botones de navegación
      const prevBtn = panelFooter.querySelector('[data-action="prev"]');
      const completeBtn = panelFooter.querySelector('[data-action="complete"]');
      prevBtn.disabled = idx === 0;
      const isLast = idx === items.length - 1;
      if (completed.has(items[idx].id)) {
        completeBtn.innerHTML = (isLast
          ? '<span aria-hidden="true">✓</span> Completado · Finalizar capítulo'
          : '<span aria-hidden="true">✓</span> Ya completado · Continuar');
        completeBtn.classList.remove('lesson-tabs__nav-btn--complete');
        completeBtn.classList.add('lesson-tabs__nav-btn--next');
      } else {
        completeBtn.innerHTML = (isLast
          ? '<span aria-hidden="true">✓</span> Marcar como leído y finalizar'
          : '<span aria-hidden="true">✓</span> Marcar como leído y continuar');
        completeBtn.classList.add('lesson-tabs__nav-btn--complete');
        completeBtn.classList.remove('lesson-tabs__nav-btn--next');
      }
      // Scroll al inicio del panel (solo en mobile o si está fuera de vista)
      if (options.scroll !== false) {
        const scrollTarget = layout;
        const rect = scrollTarget.getBoundingClientRect();
        if (rect.top < 0 || rect.top > window.innerHeight * 0.5) {
          scrollTarget.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      }
    }

    function markComplete(idx) {
      if (idx < 0 || idx >= items.length) return;
      completed.add(items[idx].id);
      persist();
      renderProgress();
    }
    function unmarkComplete(idx) {
      if (idx < 0 || idx >= items.length) return;
      completed.delete(items[idx].id);
      persist();
      renderProgress();
    }

    function renderProgress() {
      const total = items.length;
      const done = items.filter(function (d) { return completed.has(d.id); }).length;
      const pct = total ? Math.round((done / total) * 100) : 0;
      header.querySelector('.lesson-tabs__count').textContent = done;
      header.querySelector('.lesson-tabs__progress-fill').style.width = pct + '%';
      const bar = header.querySelector('.lesson-tabs__progress-bar');
      bar.setAttribute('aria-valuenow', String(done));
      // Actualizar visualmente cada sidebar item
      sidebar.querySelectorAll('.lesson-tab-item').forEach(function (b, i) {
        b.classList.toggle('is-done', completed.has(items[i].id));
      });
    }

    // Click en sidebar item → abrir
    sidebar.addEventListener('click', function (e) {
      // Si click en el indicador (✓) de un item completed → desmarcar
      const indicator = e.target.closest('.lesson-tab-item__indicator');
      const btn = e.target.closest('.lesson-tab-item');
      if (!btn) return;
      const idx = Array.from(sidebar.children).indexOf(btn);
      if (idx < 0) return;
      if (indicator && btn.classList.contains('is-done')) {
        // Desmarcar
        unmarkComplete(idx);
        // Re-render botones del panel si este es el active
        if (btn.classList.contains('is-active')) openItem(idx, { scroll: false });
        e.stopPropagation();
        return;
      }
      openItem(idx);
    });

    // Botones del footer
    panelFooter.addEventListener('click', function (e) {
      const action = e.target.closest('[data-action]');
      if (!action) return;
      const currentIdx = items.findIndex(function (d) { return d.open; });
      if (currentIdx < 0) return;
      if (action.dataset.action === 'prev') {
        if (currentIdx > 0) openItem(currentIdx - 1);
      } else if (action.dataset.action === 'complete') {
        markComplete(currentIdx);
        if (currentIdx < items.length - 1) {
          openItem(currentIdx + 1);
        } else {
          openItem(currentIdx, { scroll: false });
        }
      }
    });

    // Reset
    header.querySelector('.lesson-tabs__reset').addEventListener('click', function () {
      if (!window.confirm('¿Reiniciar tu avance en este capítulo? Esto borra los módulos marcados como completados (solo en este navegador).')) return;
      completed = new Set();
      persist();
      renderProgress();
      const activeIdx = items.findIndex(function (d) { return d.open; });
      if (activeIdx >= 0) openItem(activeIdx, { scroll: false });
    });

    // Estado inicial: abrir el primer módulo que tiene [open] o el primero
    let initialIdx = items.findIndex(function (d) { return d.open; });
    if (initialIdx < 0) initialIdx = 0;
    // Si la URL trae hash que coincide con un item, usarlo
    if (window.location.hash) {
      const hashId = window.location.hash.slice(1);
      const hashIdx = items.findIndex(function (d) { return d.id === hashId; });
      if (hashIdx >= 0) initialIdx = hashIdx;
    }
    renderProgress();
    openItem(initialIdx, { scroll: false });
  }

  // ---------- Glosario rico (índice alfabético + filtro en vivo + contador) ----------
  // Auto-construye el toolkit a partir de un <dl class="glossary glossary--rich">.
  // No requiere markup adicional en HTML — el JS genera el toolkit, el data-letter
  // de cada término y el contador. Filtra por nombre y por definición (case insensitive
  // + acentos normalizados).
  function initGlossaryRich(dl) {
    const terms = Array.from(dl.querySelectorAll('.glossary__term'));
    if (!terms.length) return;

    function norm(s) {
      // Normaliza: lowercase + sin diacríticos (acentos, tilde de ñ→n, etc).
      // ̀-ͯ es el rango Unicode de "Combining Diacritical Marks".
      return (s || '').toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '');
    }

    // Asigna data-letter a cada término basado en su nombre
    const lettersInUse = new Set();
    terms.forEach(function (term) {
      const nameEl = term.querySelector('.glossary__name');
      const firstChar = (nameEl ? nameEl.textContent.trim().charAt(0) : '?').toUpperCase();
      const letter = /[A-ZÑ]/.test(firstChar) ? firstChar : '#';
      term.dataset.letter = letter;
      lettersInUse.add(letter);
      // Genera ID si no tiene (para anchoring por letra)
      if (!term.id) {
        const slug = norm(nameEl.textContent.trim()).replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
        term.id = 'glossary-' + slug.slice(0, 60);
      }
    });

    // Construye toolkit
    const toolkit = document.createElement('div');
    toolkit.className = 'glossary-toolkit';
    const allLetters = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'.split('');
    toolkit.innerHTML =
      '<div class="glossary-toolkit__filter-row">' +
        '<input type="search" class="glossary-toolkit__input" ' +
          'placeholder="Buscar término o palabra de la definición…" ' +
          'aria-label="Filtrar términos del glosario" />' +
        '<span class="glossary-toolkit__count"><strong class="js-count">' + terms.length + '</strong> términos</span>' +
      '</div>' +
      '<nav class="glossary-toolkit__index" aria-label="Saltar a letra">' +
        '<span class="glossary-toolkit__index-label">Ir a:</span>' +
        allLetters.map(function (l) {
          const disabled = !lettersInUse.has(l);
          return '<a href="#" class="glossary-toolkit__letter' + (disabled ? '' : '') + '" ' +
                 'data-letter="' + l + '" ' +
                 (disabled ? 'aria-disabled="true" tabindex="-1"' : '') +
                 '>' + l + '</a>';
        }).join('') +
      '</nav>' +
      '<p class="glossary-toolkit__empty">No se encontraron términos con ese filtro. Prueba con otra palabra o limpia el campo.</p>';

    dl.parentNode.insertBefore(toolkit, dl);

    const input = toolkit.querySelector('.glossary-toolkit__input');
    const countEl = toolkit.querySelector('.js-count');
    const emptyEl = toolkit.querySelector('.glossary-toolkit__empty');
    const letterLinks = toolkit.querySelectorAll('.glossary-toolkit__letter');

    function applyFilter(query) {
      const q = norm(query);
      let visible = 0;
      terms.forEach(function (term) {
        const nameEl = term.querySelector('.glossary__name');
        const defEl = term.querySelector('.glossary__def');
        const haystack = norm((nameEl ? nameEl.textContent : '') + ' ' + (defEl ? defEl.textContent : ''));
        const matches = !q || haystack.indexOf(q) >= 0;
        term.hidden = !matches;
        if (matches) visible++;
      });
      countEl.textContent = visible;
      emptyEl.classList.toggle('is-visible', visible === 0);
      // Actualiza estado disabled de letras según términos visibles por letra
      const visibleLetters = new Set();
      terms.forEach(function (t) { if (!t.hidden) visibleLetters.add(t.dataset.letter); });
      letterLinks.forEach(function (link) {
        const l = link.dataset.letter;
        const disable = lettersInUse.has(l) ? !visibleLetters.has(l) : true;
        link.setAttribute('aria-disabled', disable ? 'true' : 'false');
        if (disable) link.setAttribute('tabindex', '-1');
        else link.removeAttribute('tabindex');
      });
    }

    input.addEventListener('input', function () { applyFilter(input.value); });

    letterLinks.forEach(function (link) {
      link.addEventListener('click', function (e) {
        e.preventDefault();
        if (link.getAttribute('aria-disabled') === 'true') return;
        const l = link.dataset.letter;
        // Encuentra el primer término visible con esa letra
        const target = terms.find(function (t) { return t.dataset.letter === l && !t.hidden; });
        if (target) {
          target.scrollIntoView({ behavior: 'smooth', block: 'start' });
          // Highlight efímero
          target.id && (window.location.hash = target.id);
        }
        // Toggle visual: marca como activa
        letterLinks.forEach(function (b) { b.classList.remove('is-active'); });
        link.classList.add('is-active');
      });
    });

    // Estado inicial
    applyFilter('');
  }

  // ---------- Print checklist como PDF ----------
  // Botón [data-action="print-checklist"] → activa modo de impresión que oculta
  // todo el sitio menos el checklist + un encabezado con logo + fecha + footer
  // institucional. El usuario elige "Guardar como PDF" en el diálogo del navegador.
  function initPrintChecklist() {
    document.querySelectorAll('[data-action="print-checklist"]').forEach(function (btn) {
      btn.addEventListener('click', function () {
        // Localiza el checklist destino: el más cercano al botón
        const checklist = btn.closest('.checklist-actions') &&
          btn.closest('.checklist-actions').nextElementSibling &&
          btn.closest('.checklist-actions').nextElementSibling.classList.contains('printable-checklist')
            ? btn.closest('.checklist-actions').nextElementSibling
            : document.querySelector('.printable-checklist');
        if (!checklist) {
          window.print();
          return;
        }

        // Construye el cover dinámicamente con logo + título + fecha
        const today = new Date().toLocaleDateString('es-MX', { year: 'numeric', month: 'long', day: 'numeric' });
        const pageTitle = document.title.split('·')[0].trim() || 'Mi CompañIA';
        // Detecta ruta del logo según profundidad del documento
        const logoPath = (location.pathname.split('/').filter(Boolean).length > 1) ? '../img/logo.png' : 'img/logo.png';

        const cover = document.createElement('div');
        cover.className = 'print-cover';
        cover.innerHTML =
          '<div class="print-cover__header">' +
            '<img src="' + logoPath + '" alt="Mi CompañIA" />' +
            '<div>' +
              '<h1 class="print-cover__title">Lista de verificación · Implementar IA</h1>' +
              '<p class="print-cover__subtitle">' + pageTitle + ' · Manual del Aspirante</p>' +
            '</div>' +
            '<div class="print-cover__date">Generado<br>' + today + '</div>' +
          '</div>' +
          '<p class="print-cover__intro" style="margin-bottom: 18px; color: #4B5563; font-style: italic;">Marca cada elemento conforme lo tengas resuelto. Esta es una vista descargable; el progreso interactivo se sigue guardando en el navegador.</p>';

        // Mueve el checklist al cover temporalmente
        const placeholder = document.createComment('checklist-placeholder');
        checklist.parentNode.replaceChild(placeholder, checklist);
        cover.appendChild(checklist);
        cover.insertAdjacentHTML('beforeend',
          '<div class="print-cover__footer">' +
            'Mi CompañIA · Una iniciativa de FUNDES Latinoamérica con el apoyo de Google.org · ' +
            location.hostname + location.pathname +
          '</div>'
        );
        document.body.appendChild(cover);
        document.body.classList.add('body--printing-checklist');

        function restore() {
          document.body.classList.remove('body--printing-checklist');
          if (placeholder.parentNode) {
            placeholder.parentNode.replaceChild(checklist, placeholder);
          }
          if (cover.parentNode) cover.parentNode.removeChild(cover);
          window.removeEventListener('afterprint', restore);
        }
        window.addEventListener('afterprint', restore);

        // Pequeño delay para que el navegador aplique los estilos
        setTimeout(function () { window.print(); }, 50);
      });
    });
  }

  // ---------- recordEvent: métricas locales (sin backend) ----------
  // Llamar como: recordEvent('quiz', { quizId: 'x', correct: true, attempts: 2 })
  // Guarda los últimos 500 eventos en mi-compania-metrics::v1.
  function recordEvent(type, payload) {
    const KEY = 'mi-compania-metrics::v1';
    try {
      const raw = localStorage.getItem(KEY);
      const arr = raw ? JSON.parse(raw) : [];
      arr.push({ t: type, p: payload, ts: Date.now(), page: location.pathname });
      while (arr.length > 500) arr.shift();
      localStorage.setItem(KEY, JSON.stringify(arr));
    } catch (e) { /* silenciosa: localStorage lleno o privacy mode */ }
  }
  window.miCompaniaRecordEvent = recordEvent;

  function readJSONScript(container, selector) {
    const node = container.querySelector(selector);
    if (!node) return null;
    try { return JSON.parse(node.textContent); }
    catch (e) { console.warn('JSON inválido en', selector, e); return null; }
  }

  function escapeHTML(s) {
    return String(s || '').replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }

  // ---------- Scenario Decision ----------
  // Caso ramificado: contexto + pregunta + opciones (ok/risk/wrong) + feedback + wrap-up.
  // Markup:
  // <div class="scenario-decision" data-storage-key="esc-espiga-01">
  //   <script type="application/json" class="scenario-decision__data">{...}</script>
  //   <noscript>...</noscript>
  // </div>
  function initScenarioDecision(container) {
    const data = readJSONScript(container, '.scenario-decision__data');
    if (!data) return;
    const key = 'mi-compania-scenario::v1::' + (container.dataset.storageKey || 'default');
    let stored = {};
    try { stored = JSON.parse(localStorage.getItem(key) || '{}'); } catch (e) {}

    const optionsHTML = data.options.map(function (opt) {
      return '<button type="button" class="scenario-decision__option" data-option-id="' + escapeHTML(opt.id) +
        '" data-outcome="' + escapeHTML(opt.outcome) + '">' +
        '<span class="scenario-decision__option-id">' + escapeHTML(opt.id.toUpperCase()) + '</span>' +
        '<span class="scenario-decision__option-label">' + escapeHTML(opt.label) + '</span></button>';
    }).join('');

    const headerHTML =
      (data.actor ? '<div class="scenario-decision__actor">' + escapeHTML(data.actor) + '</div>' : '') +
      '<h3 class="scenario-decision__title">' + escapeHTML(data.title) + '</h3>' +
      '<div class="scenario-decision__context">' + escapeHTML(data.context) + '</div>' +
      (data.question ? '<p class="scenario-decision__question">' + escapeHTML(data.question) + '</p>' : '');

    container.innerHTML =
      '<div class="scenario-decision__inner">' +
        headerHTML +
        '<div class="scenario-decision__options" role="group" aria-label="Opciones de decisión">' + optionsHTML + '</div>' +
        '<div class="scenario-decision__feedback" role="status" aria-live="polite" hidden></div>' +
        (data.wrapUp ? '<div class="scenario-decision__wrapup" hidden><strong>Para llevar:</strong> ' + escapeHTML(data.wrapUp) + '</div>' : '') +
        '<button type="button" class="scenario-decision__retry" hidden>Probar otra opción</button>' +
      '</div>';

    const optionBtns = container.querySelectorAll('.scenario-decision__option');
    const feedbackBox = container.querySelector('.scenario-decision__feedback');
    const wrapUpBox = container.querySelector('.scenario-decision__wrapup');
    const retryBtn = container.querySelector('.scenario-decision__retry');

    function showOption(optId) {
      const opt = data.options.find(function (o) { return o.id === optId; });
      if (!opt) return;
      optionBtns.forEach(function (b) {
        const isPicked = b.dataset.optionId === optId;
        b.setAttribute('aria-pressed', isPicked ? 'true' : 'false');
        b.setAttribute('disabled', 'disabled');
        if (isPicked) b.setAttribute('data-state', opt.outcome);
      });
      const badge = opt.outcome === 'ok' ? '✓ Acertaste'
        : opt.outcome === 'risk' ? '⚠ Funciona, pero con riesgos'
        : '✗ Conviene reconsiderarlo';
      feedbackBox.innerHTML =
        '<div class="scenario-decision__badge scenario-decision__badge--' + escapeHTML(opt.outcome) + '">' + badge + '</div>' +
        '<p class="scenario-decision__explain">' + escapeHTML(opt.feedback) + '</p>' +
        (opt.criterio ? '<p class="scenario-decision__criterio"><strong>Criterio relacionado:</strong> ' + escapeHTML(opt.criterio) + '</p>' : '');
      feedbackBox.hidden = false;
      if (wrapUpBox) wrapUpBox.hidden = false;
      if (retryBtn) retryBtn.hidden = false;
      try {
        stored = { picked: optId, outcome: opt.outcome, ts: Date.now() };
        localStorage.setItem(key, JSON.stringify(stored));
      } catch (e) {}
      recordEvent('scenario', { storageKey: container.dataset.storageKey, picked: optId, outcome: opt.outcome });
    }

    optionBtns.forEach(function (btn) {
      btn.addEventListener('click', function () { showOption(btn.dataset.optionId); });
    });
    if (retryBtn) {
      retryBtn.addEventListener('click', function () {
        optionBtns.forEach(function (b) {
          b.removeAttribute('disabled');
          b.removeAttribute('data-state');
          b.setAttribute('aria-pressed', 'false');
        });
        feedbackBox.hidden = true;
        feedbackBox.innerHTML = '';
        if (wrapUpBox) wrapUpBox.hidden = true;
        retryBtn.hidden = true;
      });
    }

    // Restaurar respuesta previa (informa pero permite reintentar)
    if (stored.picked) showOption(stored.picked);
  }

  // ---------- Flashcard Deck (con micro-SRS) ----------
  // Markup:
  // <div class="flashcard-deck" data-storage-key="deck-glosario-conocer">
  //   <script type="application/json" class="flashcard-deck__data">[{front,back,tags},...]</script>
  // </div>
  function initFlashcardDeck(container) {
    const cards = readJSONScript(container, '.flashcard-deck__data');
    if (!cards || !cards.length) return;
    const key = 'mi-compania-deck::v1::' + (container.dataset.storageKey || 'default');
    let scores = {};
    try { scores = JSON.parse(localStorage.getItem(key) || '{}'); } catch (e) {}

    let order = cards.map(function (_, i) { return i; });
    // Priorizar las marcadas como difíciles (score alto = más difícil)
    order.sort(function (a, b) { return (scores[b] || 0) - (scores[a] || 0); });
    let current = 0;
    let flipped = false;

    container.innerHTML =
      '<div class="flashcard-deck__inner">' +
        '<div class="flashcard-deck__meta">' +
          '<span class="flashcard-deck__counter" aria-live="polite">1 / ' + cards.length + '</span>' +
          '<button type="button" class="flashcard-deck__shuffle" aria-label="Mezclar mazo">🔀 Mezclar</button>' +
        '</div>' +
        '<div class="flashcard-deck__card" tabindex="0" role="button" aria-pressed="false" aria-label="Tarjeta, presiona para voltear">' +
          '<div class="flashcard-deck__face flashcard-deck__face--front"></div>' +
          '<div class="flashcard-deck__face flashcard-deck__face--back"></div>' +
        '</div>' +
        '<div class="flashcard-deck__controls" hidden>' +
          '<p class="flashcard-deck__rate">¿Qué tan bien la sabías?</p>' +
          '<button type="button" class="flashcard-deck__rate-btn" data-rate="3">Difícil</button>' +
          '<button type="button" class="flashcard-deck__rate-btn" data-rate="1">Regular</button>' +
          '<button type="button" class="flashcard-deck__rate-btn" data-rate="0">Fácil</button>' +
        '</div>' +
        '<div class="flashcard-deck__nav">' +
          '<button type="button" class="flashcard-deck__prev" aria-label="Anterior">◀ Anterior</button>' +
          '<button type="button" class="flashcard-deck__next" aria-label="Siguiente">Siguiente ▶</button>' +
        '</div>' +
      '</div>';

    const card = container.querySelector('.flashcard-deck__card');
    const frontFace = container.querySelector('.flashcard-deck__face--front');
    const backFace = container.querySelector('.flashcard-deck__face--back');
    const counter = container.querySelector('.flashcard-deck__counter');
    const controls = container.querySelector('.flashcard-deck__controls');
    const shuffleBtn = container.querySelector('.flashcard-deck__shuffle');

    function render() {
      const c = cards[order[current]];
      frontFace.innerHTML = '<span class="flashcard-deck__face-label">Concepto</span><span class="flashcard-deck__face-text">' + escapeHTML(c.front) + '</span>';
      backFace.innerHTML = '<span class="flashcard-deck__face-label">Definición</span><span class="flashcard-deck__face-text">' + escapeHTML(c.back) + '</span>';
      counter.textContent = (current + 1) + ' / ' + cards.length;
      card.setAttribute('aria-pressed', 'false');
      flipped = false;
      controls.hidden = true;
    }

    function flip() {
      flipped = !flipped;
      card.setAttribute('aria-pressed', flipped ? 'true' : 'false');
      if (flipped) controls.hidden = false;
    }

    card.addEventListener('click', flip);
    card.addEventListener('keydown', function (e) {
      if (e.key === ' ' || e.key === 'Enter') { e.preventDefault(); flip(); }
    });

    container.querySelector('.flashcard-deck__prev').addEventListener('click', function () {
      current = (current - 1 + cards.length) % cards.length;
      render();
    });
    container.querySelector('.flashcard-deck__next').addEventListener('click', function () {
      current = (current + 1) % cards.length;
      render();
    });

    container.querySelectorAll('.flashcard-deck__rate-btn').forEach(function (btn) {
      btn.addEventListener('click', function () {
        const rate = parseInt(btn.dataset.rate, 10);
        const cardIdx = order[current];
        scores[cardIdx] = (scores[cardIdx] || 0) + rate;
        try { localStorage.setItem(key, JSON.stringify(scores)); } catch (e) {}
        recordEvent('flashcard', { storageKey: container.dataset.storageKey, cardIdx: cardIdx, rate: rate });
        // Avanzar
        current = (current + 1) % cards.length;
        render();
      });
    });

    shuffleBtn.addEventListener('click', function () {
      for (let i = order.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [order[i], order[j]] = [order[j], order[i]];
      }
      current = 0;
      render();
    });

    render();
  }

  // ---------- Swipe Decide (tarjetas binarias) ----------
  // Markup:
  // <div class="swipe-decide" data-storage-key="..." data-left-label="Taxativo" data-right-label="Recomendación">
  //   <script type="application/json" class="swipe-decide__data">[{text,answer:'left|right',explain},...]</script>
  // </div>
  function initSwipeDecide(container) {
    const items = readJSONScript(container, '.swipe-decide__data');
    if (!items || !items.length) return;
    const leftLabel = container.dataset.leftLabel || 'A';
    const rightLabel = container.dataset.rightLabel || 'B';
    const key = 'mi-compania-swipe::v1::' + (container.dataset.storageKey || 'default');

    let idx = 0, hits = 0, misses = 0;

    container.innerHTML =
      '<div class="swipe-decide__inner">' +
        '<div class="swipe-decide__progress"><span class="swipe-decide__counter">1 / ' + items.length + '</span></div>' +
        '<div class="swipe-decide__stage">' +
          '<div class="swipe-decide__card" tabindex="0" role="article" aria-label="Tarjeta a evaluar"></div>' +
          '<div class="swipe-decide__feedback" role="status" aria-live="polite" hidden></div>' +
        '</div>' +
        '<div class="swipe-decide__actions">' +
          '<button type="button" class="swipe-decide__btn swipe-decide__btn--left" data-answer="left">' +
            '<span class="swipe-decide__btn-hint">A · ←</span>' + escapeHTML(leftLabel) +
          '</button>' +
          '<button type="button" class="swipe-decide__btn swipe-decide__btn--right" data-answer="right">' +
            escapeHTML(rightLabel) + '<span class="swipe-decide__btn-hint">L · →</span>' +
          '</button>' +
        '</div>' +
        '<div class="swipe-decide__end" hidden>' +
          '<p class="swipe-decide__summary"></p>' +
          '<button type="button" class="swipe-decide__restart">Volver a empezar</button>' +
        '</div>' +
      '</div>';

    const cardEl = container.querySelector('.swipe-decide__card');
    const feedbackEl = container.querySelector('.swipe-decide__feedback');
    const counterEl = container.querySelector('.swipe-decide__counter');
    const buttons = container.querySelectorAll('.swipe-decide__btn');
    const endEl = container.querySelector('.swipe-decide__end');
    const summaryEl = container.querySelector('.swipe-decide__summary');
    const restartBtn = container.querySelector('.swipe-decide__restart');

    function render() {
      if (idx >= items.length) return finish();
      cardEl.innerHTML = '<p class="swipe-decide__text">' + escapeHTML(items[idx].text) + '</p>';
      counterEl.textContent = (idx + 1) + ' / ' + items.length;
      feedbackEl.hidden = true;
      feedbackEl.innerHTML = '';
      buttons.forEach(function (b) { b.removeAttribute('disabled'); });
    }

    function pick(answer) {
      const item = items[idx];
      const ok = item.answer === answer;
      if (ok) hits++; else misses++;
      cardEl.setAttribute('data-state', ok ? 'correct' : 'wrong');
      const badge = ok ? '✓ Correcto' : '✗ No exactamente';
      feedbackEl.innerHTML =
        '<div class="swipe-decide__badge swipe-decide__badge--' + (ok ? 'ok' : 'wrong') + '">' + badge + '</div>' +
        (item.explain ? '<p class="swipe-decide__explain">' + escapeHTML(item.explain) + '</p>' : '') +
        '<button type="button" class="swipe-decide__next">Siguiente →</button>';
      feedbackEl.hidden = false;
      buttons.forEach(function (b) { b.setAttribute('disabled', 'disabled'); });
      const nextBtn = feedbackEl.querySelector('.swipe-decide__next');
      nextBtn.addEventListener('click', function () {
        idx++;
        cardEl.removeAttribute('data-state');
        render();
      });
      nextBtn.focus();
      recordEvent('swipe', { storageKey: container.dataset.storageKey, idx: idx, correct: ok });
    }

    function finish() {
      cardEl.parentElement.style.display = 'none';
      container.querySelector('.swipe-decide__actions').style.display = 'none';
      endEl.hidden = false;
      const total = hits + misses;
      const pct = total ? Math.round(hits / total * 100) : 0;
      summaryEl.innerHTML = '<strong>' + hits + ' / ' + total + ' aciertos (' + pct + '%).</strong> ' +
        (pct >= 80 ? 'Excelente criterio.' : pct >= 60 ? 'Buen nivel, revisa las que fallaste.' : 'Vale la pena releer la sección y volver.');
      try { localStorage.setItem(key, JSON.stringify({ hits: hits, misses: misses, ts: Date.now() })); } catch (e) {}
    }

    buttons.forEach(function (b) {
      b.addEventListener('click', function () { pick(b.dataset.answer); });
    });

    // Atajos de teclado A / L y flechas
    container.addEventListener('keydown', function (e) {
      const k = e.key.toLowerCase();
      if (k === 'a' || e.key === 'ArrowLeft') { e.preventDefault(); if (idx < items.length) pick('left'); }
      else if (k === 'l' || e.key === 'ArrowRight') { e.preventDefault(); if (idx < items.length) pick('right'); }
    });

    restartBtn.addEventListener('click', function () {
      idx = 0; hits = 0; misses = 0;
      cardEl.parentElement.style.display = '';
      container.querySelector('.swipe-decide__actions').style.display = '';
      endEl.hidden = true;
      render();
    });

    render();
  }

  // ---------- loadCDN: carga script externo solo cuando se necesita ----------
  // Devuelve una Promise que resuelve cuando el script está disponible.
  // Cachea por URL para no insertar dos veces el mismo CDN.
  const _cdnCache = {};
  function loadCDN(url) {
    if (_cdnCache[url]) return _cdnCache[url];
    _cdnCache[url] = new Promise(function (resolve, reject) {
      const s = document.createElement('script');
      s.src = url;
      s.async = true;
      s.onload = function () { resolve(); };
      s.onerror = function () { reject(new Error('No se pudo cargar: ' + url)); };
      document.head.appendChild(s);
    });
    return _cdnCache[url];
  }

  // ---------- Diagram Mermaid ----------
  // Carga Mermaid (~140 KB) solo si la página tiene .diagram-mermaid.
  // Markup:
  // <figure class="diagram-mermaid">
  //   <pre class="mermaid">flowchart LR; A-->B</pre>
  //   <figcaption>Caption opcional</figcaption>
  // </figure>
  function initDiagramMermaid(container) {
    loadCDN('https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js').then(function () {
      if (!window.mermaid) return;
      // Inicializar UNA VEZ (idempotente)
      if (!window._miCompaniaMermaidInit) {
        window.mermaid.initialize({
          startOnLoad: false,
          securityLevel: 'loose',
          theme: 'base',
          themeVariables: {
            primaryColor: '#28467e',
            primaryTextColor: '#FAFCFF',
            primaryBorderColor: '#1F4E8C',
            lineColor: '#529ed7',
            secondaryColor: '#f7c031',
            tertiaryColor: '#FFF3CC',
            fontFamily: 'Afacad, Inter, sans-serif',
            fontSize: '15px'
          }
        });
        window._miCompaniaMermaidInit = true;
      }
      const pre = container.querySelector('pre.mermaid');
      if (!pre) return;
      try {
        window.mermaid.run({ nodes: [pre] });
      } catch (e) { console.warn('Mermaid render error:', e); }
    }).catch(function (e) { console.warn(e); });
  }

  // ---------- Drag Sort (arrastrar criterios a su zona) ----------
  // Mouse/touch: SortableJS · Teclado: Tab/Space/flechas/Enter
  // Markup:
  // <div class="drag-sort" data-storage-key="ds-criterios-elementos">
  //   <div class="drag-sort__bank">
  //     <div class="drag-sort__item" data-id="f01" data-correct-zone="e1">F01: Reporte inicial</div>...
  //   </div>
  //   <div class="drag-sort__targets">
  //     <div class="drag-sort__zone" data-zone="e1"><h4>Elemento 1</h4><ul></ul></div>
  //     <div class="drag-sort__zone" data-zone="e2">...</div>
  //   </div>
  //   <button class="drag-sort__check" type="button">Verificar</button>
  //   <div class="drag-sort__feedback" role="status" aria-live="polite" hidden></div>
  // </div>
  function initDragSort(container) {
    const key = 'mi-compania-drag::v1::' + (container.dataset.storageKey || 'default');
    const items = Array.prototype.slice.call(container.querySelectorAll('.drag-sort__item'));
    const zones = container.querySelectorAll('.drag-sort__zone');
    const bank = container.querySelector('.drag-sort__bank');
    const checkBtn = container.querySelector('.drag-sort__check');
    const feedback = container.querySelector('.drag-sort__feedback');
    if (!items.length || !zones.length) return;

    // Asegurar que cada zona tenga un <ul> para los drops
    zones.forEach(function (z) {
      if (!z.querySelector('ul')) {
        const ul = document.createElement('ul');
        ul.className = 'drag-sort__zone-list';
        z.appendChild(ul);
      }
    });

    // Anuncio teclado (aria-live)
    let announcer = container.querySelector('.drag-sort__announcer');
    if (!announcer) {
      announcer = document.createElement('div');
      announcer.className = 'drag-sort__announcer visually-hidden';
      announcer.setAttribute('aria-live', 'polite');
      announcer.setAttribute('aria-atomic', 'true');
      container.appendChild(announcer);
    }
    function announce(msg) { announcer.textContent = msg; }

    // Hacer items focables + keyboard
    let grabbed = null;
    items.forEach(function (item) {
      item.setAttribute('tabindex', '0');
      item.setAttribute('role', 'option');
      item.setAttribute('aria-grabbed', 'false');
      item.addEventListener('keydown', function (e) {
        if (e.key === ' ' || e.key === 'Enter') {
          e.preventDefault();
          if (grabbed === item) {
            grabbed.setAttribute('aria-grabbed', 'false');
            announce('Soltado: ' + item.textContent.trim());
            grabbed = null;
          } else {
            if (grabbed) grabbed.setAttribute('aria-grabbed', 'false');
            grabbed = item;
            item.setAttribute('aria-grabbed', 'true');
            announce('Tomado: ' + item.textContent.trim() + '. Usa flechas para moverlo entre zonas, luego Espacio para soltar.');
          }
        } else if (grabbed === item && (e.key === 'ArrowRight' || e.key === 'ArrowLeft' || e.key === 'ArrowUp' || e.key === 'ArrowDown')) {
          e.preventDefault();
          moveGrabbed(e.key);
        } else if (e.key === 'Escape' && grabbed === item) {
          grabbed.setAttribute('aria-grabbed', 'false');
          grabbed = null;
          announce('Movimiento cancelado.');
        }
      });
    });

    function moveGrabbed(direction) {
      // Listas en orden: bank, zone1, zone2, ... (zonas según orden DOM)
      const allLists = [bank];
      zones.forEach(function (z) { allLists.push(z.querySelector('ul') || z); });
      // Encuentra contenedor actual del item
      const currentList = grabbed.parentElement;
      const idx = allLists.indexOf(currentList);
      let nextIdx = idx;
      if (direction === 'ArrowRight' || direction === 'ArrowDown') nextIdx = Math.min(allLists.length - 1, idx + 1);
      else if (direction === 'ArrowLeft' || direction === 'ArrowUp') nextIdx = Math.max(0, idx - 1);
      if (nextIdx === idx) return;
      allLists[nextIdx].appendChild(grabbed);
      const targetLabel = nextIdx === 0 ? 'banco de items' : (allLists[nextIdx].parentElement.querySelector('h4, .drag-sort__zone-title') ? allLists[nextIdx].parentElement.querySelector('h4, .drag-sort__zone-title').textContent.trim() : 'zona ' + nextIdx);
      announce('Movido a: ' + targetLabel);
      grabbed.focus();
    }

    // Cargar SortableJS para mouse/touch
    loadCDN('https://cdn.jsdelivr.net/npm/sortablejs@1.15.2/Sortable.min.js').then(function () {
      if (!window.Sortable) return;
      const groupName = 'drag-sort-' + (container.dataset.storageKey || 'default');
      // IMPORTANTE: pasar opts frescos a cada create. SortableJS muta el objeto
      // (convierte group:'name' en group:{name,pull,put}); si reutilizo el
      // mismo objeto, las zonas creadas después reciben un group mutado que
      // rompe la comunicación bidireccional banco ↔ zona.
      function makeOpts() {
        return {
          group: { name: groupName, pull: true, put: true },
          animation: 150,
          ghostClass: 'drag-sort__ghost',
          chosenClass: 'drag-sort__chosen',
          dragClass: 'drag-sort__dragging',
          emptyInsertThreshold: 20,
          onEnd: function () { persist(); }
        };
      }
      window.Sortable.create(bank, makeOpts());
      zones.forEach(function (z) {
        const ul = z.querySelector('ul') || z;
        window.Sortable.create(ul, makeOpts());
      });
    }).catch(function (e) { console.warn(e); });

    // Restaurar asignación previa
    try {
      const stored = JSON.parse(localStorage.getItem(key) || '{}');
      Object.keys(stored).forEach(function (itemId) {
        const item = items.find(function (it) { return it.dataset.id === itemId; });
        const zone = container.querySelector('.drag-sort__zone[data-zone="' + stored[itemId] + '"]');
        if (item && zone) {
          (zone.querySelector('ul') || zone).appendChild(item);
        }
      });
    } catch (e) {}

    function persist() {
      const state = {};
      zones.forEach(function (z) {
        const zoneId = z.dataset.zone;
        z.querySelectorAll('.drag-sort__item').forEach(function (it) {
          state[it.dataset.id] = zoneId;
        });
      });
      try { localStorage.setItem(key, JSON.stringify(state)); } catch (e) {}
    }

    if (checkBtn) {
      checkBtn.addEventListener('click', function () {
        let total = items.length, correct = 0;
        items.forEach(function (item) {
          const parent = item.parentElement;
          const zoneEl = parent.closest('.drag-sort__zone');
          const inZone = zoneEl ? zoneEl.dataset.zone : null;
          const isCorrect = inZone === item.dataset.correctZone;
          item.setAttribute('data-state', isCorrect ? 'correct' : (inZone ? 'wrong' : 'pending'));
          if (isCorrect) correct++;
        });
        const pct = Math.round(correct / total * 100);
        feedback.innerHTML = '<strong>' + correct + ' de ' + total + ' correctos (' + pct + '%).</strong> ' +
          (pct === 100 ? 'Asignación perfecta.' : 'Revisa los marcados en rojo y reintenta.');
        feedback.hidden = false;
        persist();
        recordEvent('drag-sort', { storageKey: container.dataset.storageKey, correct: correct, total: total });
      });
    }
  }

  // ---------- Case Lab (laboratorio del caso La Espiga) ----------
  // Estructura: tabs internos (productos/plantillas) + columnas "lo que pide F21"
  // vs "cómo se llenó para La Espiga"
  // Markup:
  // <div class="case-lab" data-storage-key="case-lab-e1">
  //   <h3 class="case-lab__title">Plantillas del Elemento 1 · llenadas para La Espiga</h3>
  //   <div class="case-lab__tabs" role="tablist"></div>
  //   <div class="case-lab__panels"></div>
  //   <script type="application/json" class="case-lab__data">{...}</script>
  // </div>
  function initCaseLab(container) {
    const data = readJSONScript(container, '.case-lab__data');
    if (!data || !data.products) return;

    const tabsEl = container.querySelector('.case-lab__tabs');
    const panelsEl = container.querySelector('.case-lab__panels');
    if (!tabsEl || !panelsEl) return;

    tabsEl.setAttribute('role', 'tablist');

    data.products.forEach(function (prod, i) {
      const tabId = 'caselab-tab-' + Math.random().toString(36).slice(2, 8);
      const panelId = 'caselab-panel-' + Math.random().toString(36).slice(2, 8);
      const isFirst = i === 0;
      const tab = document.createElement('button');
      tab.type = 'button';
      tab.className = 'case-lab__tab';
      tab.id = tabId;
      tab.setAttribute('role', 'tab');
      tab.setAttribute('aria-controls', panelId);
      tab.setAttribute('aria-selected', isFirst ? 'true' : 'false');
      tab.tabIndex = isFirst ? 0 : -1;
      tab.innerHTML = '<span class="case-lab__tab-num">' + escapeHTML(prod.num) + '</span> ' + escapeHTML(prod.title);
      tabsEl.appendChild(tab);

      const panel = document.createElement('div');
      panel.className = 'case-lab__panel';
      panel.id = panelId;
      panel.setAttribute('role', 'tabpanel');
      panel.setAttribute('aria-labelledby', tabId);
      panel.hidden = !isFirst;

      const rowsHTML = (prod.rows || []).map(function (r) {
        return '<div class="case-lab__row">' +
          '<div class="case-lab__cell case-lab__cell--f21"><span class="case-lab__cell-label">El estándar solicita </span>' + escapeHTML(r.f21) + '</div>' +
          '<div class="case-lab__cell case-lab__cell--espiga"><span class="case-lab__cell-label">Carlos lo cumplió así</span>' + escapeHTML(r.espiga) + '</div>' +
        '</div>';
      }).join('');

      panel.innerHTML =
        (prod.intro ? '<p class="case-lab__intro">' + escapeHTML(prod.intro) + '</p>' : '') +
        '<div class="case-lab__rows">' + rowsHTML + '</div>' +
        (prod.note ? '<aside class="case-lab__note"><strong>Nota del consultor:</strong> ' + escapeHTML(prod.note) + '</aside>' : '');
      panelsEl.appendChild(panel);
    });

    // Navegación teclado tipo tabs
    const tabs = container.querySelectorAll('.case-lab__tab');
    const panels = container.querySelectorAll('.case-lab__panel');
    function activate(idx, focus) {
      tabs.forEach(function (t, j) {
        const active = j === idx;
        t.setAttribute('aria-selected', active ? 'true' : 'false');
        t.tabIndex = active ? 0 : -1;
      });
      panels.forEach(function (p, j) { p.hidden = j !== idx; });
      if (focus) tabs[idx].focus();
    }
    tabs.forEach(function (t, idx) {
      t.addEventListener('click', function () { activate(idx, false); });
      t.addEventListener('keydown', function (e) {
        let next = null;
        if (e.key === 'ArrowRight') next = (idx + 1) % tabs.length;
        else if (e.key === 'ArrowLeft') next = (idx - 1 + tabs.length) % tabs.length;
        else if (e.key === 'Home') next = 0;
        else if (e.key === 'End') next = tabs.length - 1;
        if (next !== null) { e.preventDefault(); activate(next, true); }
      });
    });
  }

  // ---------- Timeline Interactive ----------
  // Markup:
  // <div class="timeline-interactive" data-storage-key="proceso-pasos">
  //   <script type="application/json" class="timeline-interactive__data">[{title, date, body},...]</script>
  // </div>
  function initTimelineInteractive(container) {
    const steps = readJSONScript(container, '.timeline-interactive__data');
    if (!steps || !steps.length) return;

    const stepsHTML = steps.map(function (s, i) {
      const id = 'timeline-step-' + Math.random().toString(36).slice(2, 6);
      return '<button type="button" class="timeline-interactive__step" data-idx="' + i + '" aria-expanded="' + (i === 0 ? 'true' : 'false') + '" aria-controls="' + id + '-panel">' +
        '<span class="timeline-interactive__dot">' + (i + 1) + '</span>' +
        '<span class="timeline-interactive__step-title">' + escapeHTML(s.title) + '</span>' +
        (s.date ? '<span class="timeline-interactive__date">' + escapeHTML(s.date) + '</span>' : '') +
        '</button>';
    }).join('');

    const panelsHTML = steps.map(function (s, i) {
      const id = 'timeline-step-' + Math.random().toString(36).slice(2, 6);
      return '<div class="timeline-interactive__panel" id="' + id + '-panel" data-idx="' + i + '" ' + (i === 0 ? '' : 'hidden') + '>' +
        '<h4>' + escapeHTML(s.title) + '</h4>' +
        '<div class="timeline-interactive__body">' + (s.body || '') + '</div>' +
        '</div>';
    }).join('');

    container.innerHTML =
      '<ol class="timeline-interactive__track">' + stepsHTML + '</ol>' +
      '<div class="timeline-interactive__detail">' + panelsHTML + '</div>';

    const buttons = container.querySelectorAll('.timeline-interactive__step');
    const panels = container.querySelectorAll('.timeline-interactive__panel');

    function show(idx) {
      buttons.forEach(function (b) {
        const active = parseInt(b.dataset.idx, 10) === idx;
        b.setAttribute('aria-expanded', active ? 'true' : 'false');
        b.classList.toggle('timeline-interactive__step--active', active);
      });
      panels.forEach(function (p) {
        p.hidden = parseInt(p.dataset.idx, 10) !== idx;
      });
    }

    buttons.forEach(function (b) {
      b.addEventListener('click', function () { show(parseInt(b.dataset.idx, 10)); });
    });
    show(0);
  }

  // ---------- Progress Skill (Dashboard de progreso) ----------
  // Lee todas las claves mi-compania-* de localStorage y muestra al
  // usuario un panel con su propio recorrido.
  // Markup:
  // <div class="progress-skill" data-storage-key="dashboard-global">
  //   <h3>Tu progreso</h3>
  //   <!-- el JS rellena el resto -->
  // </div>
  function initProgressSkill(container) {
    const data = collectProgress();

    container.innerHTML =
      '<div class="progress-skill__inner">' +
        '<h3 class="progress-skill__title">Tu recorrido por Mi CompañIA</h3>' +
        '<p class="progress-skill__subtitle">Lo que ya completaste en este navegador (solo tú lo ves — no hay backend).</p>' +
        '<div class="progress-skill__metrics">' +
          '<div class="progress-skill__metric"><span class="progress-skill__metric-value">' + data.modulesCompleted + '</span><span class="progress-skill__metric-label">módulos completados</span></div>' +
          '<div class="progress-skill__metric"><span class="progress-skill__metric-value">' + data.quizzesAnswered + '</span><span class="progress-skill__metric-label">quizzes respondidos</span></div>' +
          '<div class="progress-skill__metric"><span class="progress-skill__metric-value">' + data.firstTryPct + '%</span><span class="progress-skill__metric-label">aciertos al primer intento</span></div>' +
          '<div class="progress-skill__metric"><span class="progress-skill__metric-value">' + data.scenariosResolved + '</span><span class="progress-skill__metric-label">escenarios resueltos</span></div>' +
        '</div>' +
        '<div class="progress-skill__chapters">' +
          '<h4>Capítulos visitados</h4>' +
          (data.chapters.length ? '<ul class="progress-skill__chapter-list">' + data.chapters.map(function (c) {
            const pct = c.total ? Math.round(c.done / c.total * 100) : 0;
            return '<li class="progress-skill__chapter">' +
              '<span class="progress-skill__chapter-name">' + escapeHTML(c.label) + '</span>' +
              '<div class="progress-skill__chapter-bar"><div class="progress-skill__chapter-fill" style="width:' + pct + '%"></div></div>' +
              '<span class="progress-skill__chapter-pct">' + pct + '%</span>' +
            '</li>';
          }).join('') + '</ul>' : '<p class="progress-skill__empty">Aún no visitaste ningún capítulo. Empieza por <a href="' + (location.pathname.indexOf('maestro') >= 0 ? 'que-es.html' : 'maestro/index.html') + '">la bienvenida</a>.</p>') +
        '</div>' +
        '<div class="progress-skill__actions">' +
          '<button type="button" class="progress-skill__export">Exportar mi progreso (JSON)</button>' +
          '<button type="button" class="progress-skill__reset">Borrar mi progreso</button>' +
        '</div>' +
      '</div>';

    container.querySelector('.progress-skill__export').addEventListener('click', function () {
      const all = collectAllStorage();
      const blob = new Blob([JSON.stringify(all, null, 2)], { type: 'application/json' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = 'mi-compania-progreso-' + new Date().toISOString().slice(0, 10) + '.json';
      a.click();
      URL.revokeObjectURL(url);
    });
    container.querySelector('.progress-skill__reset').addEventListener('click', function () {
      if (!confirm('Esto borra TODO tu progreso guardado en este navegador (checklists, quizzes, escenarios, decks). ¿Continuar?')) return;
      const keys = [];
      for (let i = 0; i < localStorage.length; i++) {
        const k = localStorage.key(i);
        if (k && k.indexOf('mi-compania') === 0) keys.push(k);
      }
      keys.forEach(function (k) { localStorage.removeItem(k); });
      location.reload();
    });
  }

  function collectProgress() {
    const result = {
      modulesCompleted: 0,
      quizzesAnswered: 0,
      quizzesCorrectFirstTry: 0,
      firstTryPct: 0,
      scenariosResolved: 0,
      chapters: []
    };
    // chapters (lesson-tabs progress)
    const chapterMap = {
      'maestro-cap1-bienvenida': 'Maestro · Bienvenida',
      'maestro-cap2-que-es': 'Maestro · Qué es la certificación',
      'maestro-cap3-como-se-evalua': 'Maestro · Cómo se evalúa',
      'maestro-cap4-proceso': 'Maestro · Proceso paso a paso',
      'maestro-cap5-es-para-ti': 'Maestro · ¿Es para ti?',
      'maestro-cap6-recursos': 'Maestro · Recursos',
      'estandar-a-bienvenida': 'Implementar IA · Bienvenida',
      'estandar-a-elemento-1': 'Implementar IA · Elemento 1',
      'estandar-a-elemento-2': 'Implementar IA · Elemento 2',
      'estandar-a-elemento-3': 'Implementar IA · Elemento 3',
      'estandar-a-instrumento': 'Implementar IA · Instrumento',
      'estandar-a-ruta': 'Implementar IA · Ruta de preparación',
      'estandar-a-recursos': 'Implementar IA · Recursos'
    };
    try {
      for (let i = 0; i < localStorage.length; i++) {
        const k = localStorage.key(i);
        if (!k) continue;
        if (k.indexOf('mi-compania-lessons::') === 0) {
          try {
            const v = JSON.parse(localStorage.getItem(k) || '{}');
            const key = k.replace('mi-compania-lessons::', '');
            const label = chapterMap[key] || key;
            const done = Object.keys(v).filter(function (id) { return v[id]; }).length;
            const total = Object.keys(v).length;
            if (total > 0) {
              result.chapters.push({ label: label, done: done, total: total });
              if (done === total) result.modulesCompleted += total;
              else result.modulesCompleted += done;
            }
          } catch (e) {}
        }
      }
      // metrics events
      const metrics = JSON.parse(localStorage.getItem('mi-compania-metrics::v1') || '[]');
      const quizEvents = metrics.filter(function (e) { return e.t === 'quiz'; });
      result.quizzesAnswered = quizEvents.length;
      result.quizzesCorrectFirstTry = quizEvents.filter(function (e) { return e.p && e.p.correct && e.p.attempts === 1; }).length;
      if (quizEvents.length > 0) {
        result.firstTryPct = Math.round(result.quizzesCorrectFirstTry / quizEvents.length * 100);
      }
      result.scenariosResolved = metrics.filter(function (e) { return e.t === 'scenario'; }).length;
    } catch (e) {}
    return result;
  }

  function collectAllStorage() {
    const all = {};
    try {
      for (let i = 0; i < localStorage.length; i++) {
        const k = localStorage.key(i);
        if (!k || k.indexOf('mi-compania') !== 0) continue;
        try { all[k] = JSON.parse(localStorage.getItem(k)); }
        catch (e) { all[k] = localStorage.getItem(k); }
      }
    } catch (e) {}
    return {
      exported: new Date().toISOString(),
      origin: location.origin,
      entries: all
    };
  }

  // ---------- Chart Block (wrapper Chart.js) ----------
  // Markup:
  // <div class="chart-block" data-storage-key="pesos-iec">
  //   <h3 class="chart-block__title">Distribución de pesos en el IEC</h3>
  //   <div class="chart-block__canvas-wrap"><canvas></canvas></div>
  //   <script type="application/json" class="chart-block__data">
  //     { "type": "doughnut", "data": { "labels": [...], "datasets": [{...}] }, "options": {...} }
  //   </script>
  // </div>
  function initChartBlock(container) {
    const config = readJSONScript(container, '.chart-block__data');
    if (!config) return;
    const canvas = container.querySelector('canvas');
    if (!canvas) return;

    loadCDN('https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js').then(function () {
      if (!window.Chart) return;
      // Defaults de marca
      window.Chart.defaults.font.family = 'Afacad, Inter, sans-serif';
      window.Chart.defaults.color = '#28467e';
      // Paleta default
      const brandPalette = ['#28467e', '#f7c031', '#529ed7', '#3FA35B', '#1F4E8C', '#f29100'];
      if (config.data && config.data.datasets) {
        config.data.datasets.forEach(function (ds) {
          if (!ds.backgroundColor) ds.backgroundColor = brandPalette;
          if (!ds.borderColor && config.type !== 'doughnut' && config.type !== 'pie') ds.borderColor = '#28467e';
          if (ds.borderWidth === undefined) ds.borderWidth = 2;
        });
      }
      try {
        new window.Chart(canvas.getContext('2d'), config);
      } catch (e) { console.warn('Chart.js render error:', e); }
    }).catch(function (e) { console.warn(e); });
  }

  // ---------- Diagnostic Multi (cuestionario con scoring multi-categoría) ----------
  // Útil para canalizar al usuario hacia una opción entre varias.
  // Markup:
  // <div class="diagnostic-multi" data-storage-key="que-estandar">
  //   <script type="application/json" class="diagnostic-multi__data">
  //     {
  //       "categories": [
  //         {"id":"A", "label":"Implementar IA", "href":"...", "available":true,
  //          "summary":"...", "match_label":"alta compatibilidad"},
  //         {"id":"B", "label":"...", "available":false, ...}
  //       ],
  //       "questions": [
  //         {"text":"¿...?", "options":[
  //           {"label":"opción a", "scores":{"A":2,"B":0,"C":0,"D":0}, "block": false},
  //           {"label":"opción b", "scores":{}, "block": true, "block_reason": "..."}
  //         ]}
  //       ],
  //       "wrap_up": "..."
  //     }
  //   </script>
  // </div>
  function initDiagnosticMulti(container) {
    const data = readJSONScript(container, '.diagnostic-multi__data');
    if (!data || !data.questions || !data.categories) return;
    const key = 'mi-compania-diagnostic::v1::' + (container.dataset.storageKey || 'default');

    const state = { answers: {}, blocked: false, blockReason: '' };
    try {
      const stored = JSON.parse(localStorage.getItem(key) || 'null');
      if (stored && stored.answers) Object.assign(state, stored);
    } catch (e) {}

    function render() {
      const total = data.questions.length;
      const answered = Object.keys(state.answers).length;
      const completed = answered === total && !state.blocked;
      let html = '<div class="diagnostic-multi__inner">';
      html += '<div class="diagnostic-multi__progress">';
      html += '<span class="diagnostic-multi__progress-label">Diagnóstico · pregunta ' + Math.min(answered + 1, total) + ' de ' + total + '</span>';
      html += '<div class="diagnostic-multi__progress-bar"><div class="diagnostic-multi__progress-fill" style="width:' + Math.round((answered / total) * 100) + '%"></div></div>';
      html += '</div>';

      data.questions.forEach(function (q, qi) {
        const answered = state.answers[qi] !== undefined;
        const hidden = qi > Object.keys(state.answers).length;
        html += '<fieldset class="diagnostic-multi__question"' + (hidden ? ' hidden' : '') + ' data-qi="' + qi + '">';
        html += '<legend><span class="diagnostic-multi__q-num">' + (qi + 1) + '</span> ' + escapeHTML(q.text) + '</legend>';
        q.options.forEach(function (opt, oi) {
          const isSelected = state.answers[qi] === oi;
          html += '<label class="diagnostic-multi__option' + (isSelected ? ' diagnostic-multi__option--selected' : '') + '">';
          html += '<input type="radio" name="dq-' + qi + '" value="' + oi + '"' + (isSelected ? ' checked' : '') + '>';
          html += '<span>' + escapeHTML(opt.label) + '</span>';
          html += '</label>';
        });
        html += '</fieldset>';
      });

      if (state.blocked) {
        html += '<div class="diagnostic-multi__result diagnostic-multi__result--blocked">';
        html += '<h3>Este programa de certificación NO es para tu caso</h3>';
        html += '<p>' + escapeHTML(state.blockReason) + '</p>';
        html += '<button type="button" class="diagnostic-multi__reset">Volver a empezar</button>';
        html += '</div>';
      } else if (completed) {
        // calcular scores
        const scores = {};
        data.categories.forEach(function (c) { scores[c.id] = 0; });
        Object.keys(state.answers).forEach(function (qi) {
          const opt = data.questions[qi].options[state.answers[qi]];
          if (opt.scores) {
            Object.keys(opt.scores).forEach(function (cid) {
              if (scores[cid] !== undefined) scores[cid] += opt.scores[cid];
            });
          }
        });
        // ordenar categorías por score
        const ranked = data.categories.slice().sort(function (a, b) { return (scores[b.id] || 0) - (scores[a.id] || 0); });
        const maxScore = ranked[0] ? scores[ranked[0].id] : 0;

        html += '<div class="diagnostic-multi__result">';
        html += '<h3>Tu perfil encaja con</h3>';
        ranked.forEach(function (cat, idx) {
          const score = scores[cat.id] || 0;
          const pct = maxScore > 0 ? Math.round((score / maxScore) * 100) : 0;
          const isTop = idx === 0;
          const isStrong = pct >= 60;
          html += '<div class="diagnostic-multi__match' + (isTop ? ' diagnostic-multi__match--top' : '') + (isStrong ? '' : ' diagnostic-multi__match--weak') + '">';
          html += '<div class="diagnostic-multi__match-header">';
          html += '<span class="diagnostic-multi__match-label">' + escapeHTML(cat.label) + '</span>';
          if (isTop && isStrong) html += '<span class="diagnostic-multi__match-badge">Recomendado</span>';
          else if (!cat.available) html += '<span class="diagnostic-multi__match-badge diagnostic-multi__match-badge--coming">En construcción</span>';
          html += '<span class="diagnostic-multi__match-pct">' + pct + '%</span>';
          html += '</div>';
          html += '<div class="diagnostic-multi__match-bar"><div class="diagnostic-multi__match-fill" style="width:' + pct + '%"></div></div>';
          if (cat.summary) html += '<p class="diagnostic-multi__match-summary">' + escapeHTML(cat.summary) + '</p>';
          if (cat.href && cat.available) {
            html += '<a class="diagnostic-multi__match-cta" href="' + escapeHTML(cat.href) + '">Ir al curso de ' + escapeHTML(cat.label) + ' →</a>';
          } else if (!cat.available) {
            html += '<p class="diagnostic-multi__match-coming">Este curso está en construcción. Mientras tanto, conoce el marco general en el <a href="../index.html">listado de manuales</a>.</p>';
          }
          html += '</div>';
        });
        if (data.wrap_up) {
          html += '<aside class="diagnostic-multi__wrapup"><strong>Para llevar:</strong> ' + escapeHTML(data.wrap_up) + '</aside>';
        }
        html += '<button type="button" class="diagnostic-multi__reset">Volver a hacer el diagnóstico</button>';
        html += '</div>';
      }

      html += '</div>';
      container.innerHTML = html;

      // bind handlers
      container.querySelectorAll('input[type="radio"]').forEach(function (radio) {
        radio.addEventListener('change', function () {
          const qi = parseInt(radio.name.replace('dq-', ''), 10);
          const oi = parseInt(radio.value, 10);
          const opt = data.questions[qi].options[oi];
          state.answers[qi] = oi;
          if (opt.block) {
            state.blocked = true;
            state.blockReason = opt.block_reason || 'Tu respuesta indica que este conjunto de estándares no aplica a tu caso.';
          }
          try { localStorage.setItem(key, JSON.stringify(state)); } catch (e) {}
          recordEvent('diagnostic', { storageKey: container.dataset.storageKey, qi: qi, oi: oi });
          render();
          // Scroll a la siguiente pregunta
          setTimeout(function () {
            const next = container.querySelector('.diagnostic-multi__question[data-qi="' + (qi + 1) + '"]');
            if (next && !next.hidden) next.scrollIntoView({ behavior: 'smooth', block: 'center' });
            else if (state.blocked || Object.keys(state.answers).length === data.questions.length) {
              const result = container.querySelector('.diagnostic-multi__result');
              if (result) result.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
          }, 100);
        });
      });
      const resetBtn = container.querySelector('.diagnostic-multi__reset');
      if (resetBtn) {
        resetBtn.addEventListener('click', function () {
          state.answers = {};
          state.blocked = false;
          state.blockReason = '';
          try { localStorage.removeItem(key); } catch (e) {}
          render();
          container.scrollIntoView({ behavior: 'smooth', block: 'start' });
        });
      }
    }

    render();
  }

  // ---------- Inicialización ----------
  function init() {
    document.querySelectorAll('.tabs').forEach(initTabs);
    document.querySelectorAll('.checklist').forEach(initChecklist);
    document.querySelectorAll('.flipcard').forEach(initFlipcard);
    document.querySelectorAll('.quiz').forEach(initQuiz);
    document.querySelectorAll('.scenario-decision').forEach(initScenarioDecision);
    document.querySelectorAll('.flashcard-deck').forEach(initFlashcardDeck);
    document.querySelectorAll('.swipe-decide').forEach(initSwipeDecide);
    document.querySelectorAll('.drag-sort').forEach(initDragSort);
    document.querySelectorAll('.case-lab').forEach(initCaseLab);
    document.querySelectorAll('.timeline-interactive').forEach(initTimelineInteractive);
    document.querySelectorAll('.diagram-mermaid').forEach(initDiagramMermaid);
    document.querySelectorAll('.progress-skill').forEach(initProgressSkill);
    document.querySelectorAll('.chart-block').forEach(initChartBlock);
    document.querySelectorAll('.diagnostic-multi').forEach(initDiagnosticMulti);
    document.querySelectorAll('.audio-narration').forEach(initAudioNarration);
    document.querySelectorAll('.lesson-tabs').forEach(initLessonTabs);
    document.querySelectorAll('.glossary--rich').forEach(initGlossaryRich);
    initPrintChecklist();
    // Solo aplicar el handler genérico de accordion modules si NO está dentro de lesson-tabs
    initAccordionModules();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
