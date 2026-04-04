(function () {
  function addDocsCard() {
    if (document.getElementById('docs-sidebar-card')) return;
    var aside = document.getElementById('aside-content');
    if (!aside) return;

    var card = document.createElement('div');
    card.id = 'docs-sidebar-card';
    card.className = 'card-widget';
    card.innerHTML =
      '<div class="item-headline">' +
        '<i class="fas fa-book" aria-hidden="true"></i>' +
        '<span>Docs</span>' +
      '</div>' +
      '<div style="padding:0 1rem 1rem">' +
        '<ul style="list-style:none;padding:0;margin:0;line-height:2.3">' +
          '<li><a href="/posts/21cfbf15/">&#x1F680; Quick Start</a></li>' +
          '<li><a href="/posts/dc584b87/">&#x1F4D1; Theme Pages</a></li>' +
          '<li><a href="/posts/4aa8abbe/">&#x1F6E0; Theme Config</a></li>' +
          '<li><a href="/posts/ceeb73f/">&#x2694;&#xFE0F; Tag Plugins</a></li>' +
          '<li><a href="/posts/98d20436/">&#x2753; FAQ</a></li>' +
          '<li><a href="/posts/4073eda/">&#x26A1;&#xFE0F; Advanced Tutorial</a></li>' +
          '<li><a href="/posts/198a4240/">&#x2728; Update Log</a></li>' +
        '</ul>' +
      '</div>';

    // Insert after announcement card, or at top of aside
    var announcement = aside.querySelector('.card-announcement');
    if (announcement) {
      announcement.insertAdjacentElement('afterend', card);
    } else {
      aside.insertBefore(card, aside.firstChild);
    }
  }

  // Initial load (script is deferred, DOM is ready)
  addDocsCard();

  // Re-inject after pjax navigation (aside content is replaced)
  document.addEventListener('pjax:success', addDocsCard);
})();
