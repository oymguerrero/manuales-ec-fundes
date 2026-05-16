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

  // ---------- Quiz multiple choice ----------
  // Markup esperado:
  // <div class="quiz" data-correct="b">
  //   <p class="quiz__question">...</p>
  //   <div class="quiz__options">
  //     <button class="quiz__option" data-option="a">A</button>
  //     <button class="quiz__option" data-option="b">B</button>
  //   </div>
  //   <div class="quiz__feedback quiz__feedback--correct" hidden>
  //     <strong>✓ Correcto.</strong> ...
  //   </div>
  //   <div class="quiz__feedback quiz__feedback--wrong" hidden>
  //     <strong>✗ Revisa.</strong> ...
  //     <button class="quiz__retry" type="button">Intentar de nuevo</button>
  //   </div>
  // </div>
  function initQuiz(quiz) {
    const correct = quiz.dataset.correct;
    const options = quiz.querySelectorAll('.quiz__option');
    const feedbackCorrect = quiz.querySelector('.quiz__feedback--correct');
    const feedbackWrong = quiz.querySelector('.quiz__feedback--wrong');
    const retryBtn = quiz.querySelector('.quiz__retry');
    if (!correct || !options.length) return;

    function reset() {
      options.forEach(function (o) {
        o.removeAttribute('data-state');
        o.removeAttribute('disabled');
      });
      if (feedbackCorrect) feedbackCorrect.hidden = true;
      if (feedbackWrong) feedbackWrong.hidden = true;
    }

    options.forEach(function (option) {
      option.addEventListener('click', function () {
        const isCorrect = option.dataset.option === correct;
        if (isCorrect) {
          option.setAttribute('data-state', 'correct');
          options.forEach(function (o) {
            if (o !== option) o.setAttribute('disabled', 'disabled');
          });
          if (feedbackCorrect) feedbackCorrect.hidden = false;
          if (feedbackWrong) feedbackWrong.hidden = true;
        } else {
          option.setAttribute('data-state', 'wrong');
          option.setAttribute('disabled', 'disabled');
          if (feedbackWrong) feedbackWrong.hidden = false;
          if (feedbackCorrect) feedbackCorrect.hidden = true;
        }
      });
    });

    if (retryBtn) {
      retryBtn.addEventListener('click', reset);
    }
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

  // ---------- Inicialización ----------
  function init() {
    document.querySelectorAll('.tabs').forEach(initTabs);
    document.querySelectorAll('.checklist').forEach(initChecklist);
    document.querySelectorAll('.flipcard').forEach(initFlipcard);
    document.querySelectorAll('.quiz').forEach(initQuiz);
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
