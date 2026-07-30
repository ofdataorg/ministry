/* Ministry of Data — nav, tracklist filtering and sorting. Progressive: the
   full list is already in the HTML, this only reorders and hides. */
(function () {
  'use strict';

  /* ---- mobile nav ---- */
  var toggle = document.querySelector('.navtoggle');
  var nav = document.getElementById('nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('is-open');
      toggle.setAttribute('aria-expanded', String(open));
    });
    nav.addEventListener('click', function (e) {
      if (e.target.closest('a')) {
        nav.classList.remove('is-open');
        toggle.setAttribute('aria-expanded', 'false');
      }
    });
  }

  /* ---- tracklist controls ---- */
  var panel = document.querySelector('[data-filters]');
  var list = document.querySelector('[data-tracklist]');
  if (!panel || !list) return;

  var items = Array.prototype.slice.call(list.children);
  var counter = panel.querySelector('[data-count]');
  var empty = document.querySelector('[data-empty]');
  var facets = { regions: '', domains: '' };
  var sortKey = 'date';

  function matches(li) {
    return Object.keys(facets).every(function (f) {
      var want = facets[f];
      if (!want) return true;
      var have = (li.dataset[f] || '').split('|');
      return have.indexOf(want) !== -1;
    });
  }

  function compare(a, b) {
    if (sortKey === 'score') return parseFloat(b.dataset.score) - parseFloat(a.dataset.score);
    if (sortKey === 'title') return a.dataset.title.localeCompare(b.dataset.title);
    return b.dataset.date.localeCompare(a.dataset.date);
  }

  function render() {
    var shown = items.filter(matches).sort(compare);
    var frag = document.createDocumentFragment();

    items.forEach(function (li) { li.hidden = true; });
    shown.forEach(function (li, i) {
      li.hidden = false;
      var no = li.querySelector('.track__no');
      if (no) no.textContent = ('0' + (i + 1)).slice(-2);
      frag.appendChild(li);
    });
    list.appendChild(frag);

    if (counter) counter.textContent = shown.length + ' evaluation' + (shown.length === 1 ? '' : 's');
    if (empty) empty.hidden = shown.length !== 0;
  }

  panel.addEventListener('click', function (e) {
    var chip = e.target.closest('[data-facet]');
    if (chip) {
      var facet = chip.dataset.facet;
      facets[facet] = chip.dataset.value;
      panel.querySelectorAll('[data-facet="' + facet + '"]').forEach(function (b) {
        b.classList.toggle('is-on', b === chip);
      });
      render();
      return;
    }

    var seg = e.target.closest('[data-sort]');
    if (seg) {
      sortKey = seg.dataset.sort;
      panel.querySelectorAll('[data-sort]').forEach(function (b) {
        b.classList.toggle('is-on', b === seg);
      });
      render();
    }
  });
})();
