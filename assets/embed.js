// Modo embebido para el LMS de FUNDES (cápsulas de "Contenido externo").
// Uso: pagina.html?embed=1&solo=<id de la sección>[&pieza=<clase del componente>]
// Deja en la página solo esa pieza, sin encabezado, menú ni pie, para que el
// LMS ponga el texto en lecciones nativas y aquí corra solo lo interactivo.
// Debe cargarse con defer ANTES de interactive.js: mueve la pieza antes de que
// interactive.js inicialice los componentes.
(function () {
  var params = new URLSearchParams(location.search);
  if (params.get('embed') !== '1') return;
  document.documentElement.classList.add('is-embed');

  // solo: id de la sección (opcional). pieza: una o varias clases separadas por
  // coma; se toman todas las coincidencias en orden de aparición.
  var solo = params.get('solo');
  var pieza = params.get('pieza');
  var scope = solo ? document.getElementById(solo) : document;
  if (!scope) return;
  var nodes = pieza
    ? Array.prototype.slice.call(scope.querySelectorAll(pieza.split(',').map(function (c) { return '.' + c.trim(); }).join(',')))
    : [scope];
  if (!nodes.length || nodes[0] === document) return;

  // Una sección de acordeón se muestra abierta y sin su encabezado.
  nodes.forEach(function (node) {
    if (node.tagName === 'DETAILS') {
      node.open = true;
      var summary = node.querySelector(':scope > summary');
      if (summary) summary.hidden = true;
    }
  });

  var main = document.createElement('main');
  main.className = 'embed-pieza';
  main.id = 'contenido-principal';
  var container = document.createElement('div');
  container.className = 'container';
  nodes.forEach(function (node) { container.appendChild(node); });
  main.appendChild(container);
  document.body.replaceChildren(main);

  // Los enlaces que queden abren en otra pestaña para no sacar al aspirante del LMS.
  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a[href]');
    if (a && a.getAttribute('href').charAt(0) !== '#') { a.target = '_blank'; a.rel = 'noopener'; }
  });
})();
