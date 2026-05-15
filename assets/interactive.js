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
    if (!toggle || !player) return;

    toggle.addEventListener('click', function () {
      const expanded = toggle.getAttribute('aria-expanded') === 'true';
      if (expanded) {
        // Pausar y ocultar
        if (audio && !audio.paused) audio.pause();
        toggle.setAttribute('aria-expanded', 'false');
        player.hidden = true;
        toggle.firstChild && (toggle.lastChild.textContent = toggle.dataset.labelClosed || 'Escuchar esta sección');
      } else {
        toggle.setAttribute('aria-expanded', 'true');
        player.hidden = false;
        if (audio) {
          audio.play().catch(function () { /* el usuario debe pulsar play en el control */ });
        }
        if (toggle.dataset.labelOpen) {
          toggle.lastChild.textContent = toggle.dataset.labelOpen;
        }
      }
    });
  }

  // ---------- Inicialización ----------
  function init() {
    document.querySelectorAll('.tabs').forEach(initTabs);
    document.querySelectorAll('.checklist').forEach(initChecklist);
    document.querySelectorAll('.flipcard').forEach(initFlipcard);
    document.querySelectorAll('.quiz').forEach(initQuiz);
    document.querySelectorAll('.audio-narration').forEach(initAudioNarration);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
