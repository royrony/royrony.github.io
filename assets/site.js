// Pause/play control for animated previews. Respects prefers-reduced-motion
// (animations start paused and show a still frame).
(function () {
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  document.querySelectorAll('img[data-gif]').forEach(function (img) {
    var gif = img.getAttribute('data-gif');
    var still = img.getAttribute('data-still');
    var btn = document.createElement('button');
    btn.className = 'pp';
    btn.type = 'button';
    function set(on) {
      img.src = on ? gif : still;
      btn.textContent = on ? 'Pause' : 'Play';
      btn.setAttribute('aria-label', on ? 'Pause animation' : 'Play animation');
    }
    var on = !reduce;
    set(on);
    btn.addEventListener('click', function () { on = !on; set(on); });
    img.parentNode.appendChild(btn);
  });
})();
