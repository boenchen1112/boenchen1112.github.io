---
title: yt-dlp Command Builder
date: 2026-08-11 00:00:00
---

Build a ready-to-run [yt-dlp](https://github.com/yt-dlp/yt-dlp) command without memorizing flags. Everything runs in your browser — no video, URL, or file ever touches this server. `yt-dlp` itself runs on **your** machine.

## 1. Install yt-dlp (one-time)

<div class="ytdlp-install">
  <div class="ytdlp-install-tab">
    <strong>Windows (winget)</strong>
    <pre><code>winget install yt-dlp.yt-dlp</code></pre>
  </div>
  <div class="ytdlp-install-tab">
    <strong>macOS (Homebrew)</strong>
    <pre><code>brew install yt-dlp</code></pre>
  </div>
  <div class="ytdlp-install-tab">
    <strong>Any OS (pip)</strong>
    <pre><code>pip install -U yt-dlp</code></pre>
  </div>
</div>

You'll also need [ffmpeg](https://ffmpeg.org/download.html) installed for audio extraction and merging video+audio.

## 2. Build your command

<div id="ytdlp-builder" class="ytdlp-builder">
  <label for="ytdlp-url">Video URL</label>
  <input type="url" id="ytdlp-url" placeholder="https://…" />

  <label for="ytdlp-format">Format</label>
  <select id="ytdlp-format">
    <option value="best">Best (video + audio, mp4)</option>
    <option value="audio">Audio only (mp3)</option>
    <option value="video_only">Video only, best quality</option>
  </select>

  <label for="ytdlp-output">Output filename template</label>
  <input type="text" id="ytdlp-output" value="%(title)s.%(ext)s" />

  <div class="ytdlp-checkboxes">
    <label><input type="checkbox" id="ytdlp-playlist" /> Download full playlist (if URL is a playlist)</label>
    <label><input type="checkbox" id="ytdlp-subs" /> Embed subtitles (English)</label>
  </div>

  <p class="ytdlp-command-label">Command:</p>
  <pre class="ytdlp-command"><code id="ytdlp-output-command">yt-dlp</code></pre>
  <button type="button" id="ytdlp-copy">Copy command</button>
  <span id="ytdlp-copy-status" class="ytdlp-copy-status"></span>
</div>

Paste the URL, pick your options, then copy the command into a terminal where `yt-dlp` is installed and hit enter.

<style>
.ytdlp-install { display: flex; flex-wrap: wrap; gap: 1rem; margin: 1rem 0; }
.ytdlp-install-tab { flex: 1 1 200px; }
.ytdlp-install-tab pre { margin-top: 0.4rem; }
.ytdlp-builder { display: flex; flex-direction: column; gap: 0.5rem; max-width: 560px; }
.ytdlp-builder label { font-weight: 600; margin-top: 0.5rem; }
.ytdlp-builder input[type="url"],
.ytdlp-builder input[type="text"],
.ytdlp-builder select {
  width: 100%;
  padding: 0.5rem 0.6rem;
  border: 1px solid var(--btn-border-color, #ccc);
  border-radius: 6px;
  font-size: 0.95rem;
  box-sizing: border-box;
}
.ytdlp-checkboxes { display: flex; flex-direction: column; gap: 0.3rem; margin-top: 0.5rem; }
.ytdlp-checkboxes label { font-weight: normal; display: flex; align-items: center; gap: 0.4rem; }
.ytdlp-command-label { margin-top: 1rem; margin-bottom: 0.2rem; font-weight: 600; }
.ytdlp-command { overflow-x: auto; }
#ytdlp-copy {
  align-self: flex-start;
  padding: 0.5rem 1rem;
  border-radius: 6px;
  border: none;
  background: var(--btn-bg, #4a4a4a);
  color: #fff;
  cursor: pointer;
}
#ytdlp-copy:hover { opacity: 0.85; }
.ytdlp-copy-status { font-size: 0.85rem; opacity: 0.8; }
</style>

<script>
(function () {
  var FORMAT_ARGS = {
    best: ['-f', 'bv*+ba/b', '--merge-output-format', 'mp4'],
    audio: ['-x', '--audio-format', 'mp3'],
    video_only: ['-f', 'bv*'],
  };

  function shellQuote(str) {
    if (str === '') return '""';
    return '"' + String(str).replace(/(["$`\\])/g, '\\$1') + '"';
  }

  function build() {
    var url = document.getElementById('ytdlp-url').value.trim();
    var format = document.getElementById('ytdlp-format').value;
    var output = document.getElementById('ytdlp-output').value.trim() || '%(title)s.%(ext)s';
    var playlist = document.getElementById('ytdlp-playlist').checked;
    var subs = document.getElementById('ytdlp-subs').checked;

    var args = ['yt-dlp'].concat(FORMAT_ARGS[format] || FORMAT_ARGS.best);
    if (!playlist) args.push('--no-playlist');
    if (subs) args.push('--embed-subs', '--sub-langs', 'en');
    args.push('-o', shellQuote(output));
    args.push(url ? shellQuote(url) : shellQuote('<video URL>'));

    document.getElementById('ytdlp-output-command').textContent = args.join(' ');
  }

  ['ytdlp-url', 'ytdlp-format', 'ytdlp-output', 'ytdlp-playlist', 'ytdlp-subs'].forEach(function (id) {
    var el = document.getElementById(id);
    if (el) el.addEventListener('input', build);
  });

  var copyBtn = document.getElementById('ytdlp-copy');
  if (copyBtn) {
    copyBtn.addEventListener('click', function () {
      var text = document.getElementById('ytdlp-output-command').textContent;
      var status = document.getElementById('ytdlp-copy-status');
      navigator.clipboard.writeText(text).then(function () {
        status.textContent = 'Copied!';
        setTimeout(function () { status.textContent = ''; }, 1500);
      }, function () {
        status.textContent = 'Copy failed — select and copy manually.';
      });
    });
  }

  build();

  document.addEventListener('pjax:complete', function () {
    if (document.getElementById('ytdlp-builder')) build();
  });
})();
</script>
