// Cosmetic offset so this site's Busuanzi PV/UV counters look continuous
// with the original blog (luketsengtw.github.io) after the site was duplicated.
// Baseline captured 2026-08-07: UV 952 / PV 4570.
(function () {
  var OFFSET = { uv: 952, pv: 4570 };

  function applyOffset(id, offset) {
    var el = document.getElementById(id);
    if (!el || el.dataset.offsetApplied) return;

    var current = parseInt(el.textContent.replace(/[,\s]/g, ''), 10);
    if (isNaN(current)) return;

    el.dataset.offsetApplied = 'true';
    el.textContent = (current + offset).toLocaleString();
  }

  function patch() {
    applyOffset('busuanzi_value_site_uv', OFFSET.uv);
    applyOffset('busuanzi_value_site_pv', OFFSET.pv);
  }

  function watch() {
    ['busuanzi_value_site_uv', 'busuanzi_value_site_pv'].forEach(function (id) {
      var el = document.getElementById(id);
      if (!el) return;
      var observer = new MutationObserver(function () {
        patch();
      });
      observer.observe(el, { childList: true, characterData: true, subtree: true });
    });
  }

  watch();
  document.addEventListener('pjax:complete', function () {
    document.querySelectorAll('#busuanzi_value_site_uv, #busuanzi_value_site_pv').forEach(function (el) {
      delete el.dataset.offsetApplied;
    });
    watch();
  });
})();
