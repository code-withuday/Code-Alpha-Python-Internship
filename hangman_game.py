<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>Hangman — Uday Anand</title>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400&family=Inter:wght@300;400;500&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet"/>
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{
  --black:#050505;
  --white:#f0ede8;
  --gold:#c9a96e;
  --muted:#666;
  --border:#1a1a1a;
  --serif:'Cormorant Garamond',serif;
  --sans:'Inter',sans-serif;
  --mono:'JetBrains Mono',monospace;
}
html{scroll-behavior:smooth}
body{background:var(--black);color:var(--white);font-family:var(--sans);min-height:100vh;display:flex;flex-direction:column;overflow-x:hidden;cursor:none}

/* CURSOR */
.cursor{position:fixed;width:8px;height:8px;background:var(--white);border-radius:50%;pointer-events:none;z-index:9999;transform:translate(-50%,-50%);mix-blend-mode:difference;transition:transform .15s}
.cursor-ring{position:fixed;width:36px;height:36px;border:1px solid rgba(255,255,255,0.25);border-radius:50%;pointer-events:none;z-index:9998;transform:translate(-50%,-50%);transition:all .1s ease}

/* GRID LINES */
.grid{position:fixed;inset:0;pointer-events:none;z-index:0;opacity:.03}
.grid::before{content:'';position:absolute;top:0;left:25%;width:1px;height:100%;background:var(--white)}
.grid::after{content:'';position:absolute;top:0;right:25%;width:1px;height:100%;background:var(--white)}

/* NAV */
nav{position:fixed;top:0;left:0;right:0;z-index:200;padding:1.8rem 4rem;display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid transparent;transition:border-color .3s}
nav.scrolled{border-color:var(--border);background:rgba(5,5,5,0.92);backdrop-filter:blur(12px)}
.nav-logo{font-family:var(--serif);font-size:1rem;font-weight:300;letter-spacing:.25em;color:var(--white);text-transform:uppercase;text-decoration:none}
.nav-tag{font-family:var(--mono);font-size:.6rem;letter-spacing:.2em;color:var(--gold);text-transform:uppercase}

/* MAIN */
main{flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:8rem 2rem 4rem;position:relative;z-index:1}

/* HEADER */
.page-tag{font-family:var(--mono);font-size:.65rem;letter-spacing:.4em;color:var(--gold);text-transform:uppercase;margin-bottom:1.5rem;opacity:0;animation:fadeUp .6s ease .2s forwards}
.page-title{font-family:var(--serif);font-size:clamp(3.5rem,8vw,6.5rem);font-weight:300;line-height:.92;letter-spacing:-.02em;text-align:center;margin-bottom:1rem;opacity:0;animation:fadeUp .8s ease .4s forwards}
.page-title em{font-style:italic;color:var(--gold)}
.page-sub{font-size:.78rem;color:rgba(255,255,255,.35);font-weight:300;letter-spacing:.05em;margin-bottom:3.5rem;text-align:center;opacity:0;animation:fadeUp .6s ease .6s forwards}

/* GAME AREA */
.game-wrap{width:100%;max-width:700px;opacity:0;animation:fadeUp .7s ease .8s forwards}

/* GALLOWS */
.gallows-row{display:flex;justify-content:center;margin-bottom:2.5rem}
.gallows-svg{width:160px;height:180px}

/* WORD DISPLAY */
.word-row{display:flex;justify-content:center;gap:10px;flex-wrap:wrap;margin-bottom:2.5rem}
.letter-slot{display:flex;flex-direction:column;align-items:center;gap:.5rem}
.letter-char{font-family:var(--serif);font-size:2.2rem;font-weight:300;color:var(--gold);min-height:2.4rem;display:flex;align-items:center;opacity:0;transform:translateY(8px);transition:opacity .3s,transform .3s}
.letter-char.show{opacity:1;transform:translateY(0)}
.letter-line{width:28px;height:1px;background:#333}
.letter-line.active{background:var(--gold)}

/* STATS ROW */
.stats-row{display:grid;grid-template-columns:repeat(3,1fr);gap:1px;background:var(--border);margin-bottom:2.5rem}
.stat-box{background:var(--black);padding:1.4rem 1rem;text-align:center}
.stat-label{font-family:var(--mono);font-size:.55rem;letter-spacing:.22em;text-transform:uppercase;color:var(--muted);margin-bottom:.5rem}
.stat-val{font-family:var(--serif);font-size:2rem;font-weight:300;color:var(--white)}
.stat-val.danger{color:#e07070}
.stat-val.gold{color:var(--gold)}

/* WRONG LETTERS */
.wrong-row{margin-bottom:2.5rem;border-top:1px solid var(--border);padding-top:1.5rem}
.wrong-label{font-family:var(--mono);font-size:.58rem;letter-spacing:.25em;text-transform:uppercase;color:var(--muted);margin-bottom:.9rem}
.wrong-chips{display:flex;flex-wrap:wrap;gap:.45rem;min-height:26px}
.wrong-chip{font-family:var(--mono);font-size:.65rem;letter-spacing:.08em;color:#e07070;border:1px solid rgba(224,112,112,.2);padding:.2rem .65rem}

/* KEYBOARD */
.keyboard{margin-bottom:2rem}
.kb-row{display:flex;justify-content:center;gap:6px;margin-bottom:6px}
.kb-btn{font-family:var(--mono);font-size:.7rem;letter-spacing:.1em;width:44px;height:44px;border:1px solid #2a2a2a;background:transparent;color:rgba(255,255,255,.6);cursor:pointer;transition:all .2s;-webkit-tap-highlight-color:rgba(201,169,110,0.2);position:relative;z-index:10}
.kb-btn:hover:not(:disabled){border-color:var(--gold);color:var(--white)}
.kb-btn.correct{border-color:var(--gold);color:var(--gold);background:rgba(201,169,110,.08)}
.kb-btn.wrong{border-color:#333;color:#333;cursor:not-allowed}
.kb-btn:disabled{cursor:not-allowed}

/* STATUS */
.status-msg{text-align:center;padding:1.5rem;border:1px solid var(--border);margin-bottom:2rem;display:none}
.status-msg.win{display:block;border-color:rgba(201,169,110,.3);background:rgba(201,169,110,.04)}
.status-msg.lose{display:block;border-color:rgba(224,112,112,.2);background:rgba(224,112,112,.04)}
.status-title{font-family:var(--serif);font-size:2rem;font-weight:300;margin-bottom:.5rem}
.status-title.win{color:var(--gold)}
.status-title.lose{color:#e07070;font-style:italic}
.status-word{font-family:var(--mono);font-size:.7rem;letter-spacing:.2em;color:var(--muted);text-transform:uppercase}
.status-word span{color:var(--white)}

/* NEW GAME BTN */
.new-btn{width:100%;padding:1.1rem;border:1px solid #2a2a2a;background:transparent;color:rgba(255,255,255,.55);font-family:var(--mono);font-size:.7rem;letter-spacing:.2em;text-transform:uppercase;cursor:pointer;transition:all .3s}
.new-btn:hover{border-color:var(--gold);color:var(--gold)}

/* FOOTER */
footer{padding:2rem 4rem;border-top:1px solid var(--border);display:flex;justify-content:space-between;align-items:center;position:relative;z-index:1}
footer p{font-family:var(--mono);font-size:.58rem;color:var(--muted);letter-spacing:.08em}
footer a{color:var(--gold);text-decoration:none}

@keyframes fadeUp{from{opacity:0;transform:translateY(24px)}to{opacity:1;transform:translateY(0)}}

@media(max-width:600px){
  nav{padding:1.4rem 1.6rem}
  body{cursor:auto}
  .cursor,.cursor-ring{display:none}
  .kb-btn{width:36px;height:36px;font-size:.62rem}
  main{padding:7rem 1.2rem 3rem}
  footer{flex-direction:column;gap:.6rem;text-align:center;padding:1.5rem}
}
</style>
</head>
<body>

<div class="cursor" id="cur"></div>
<div class="cursor-ring" id="ring"></div>
<div class="grid"></div>

<nav id="nav">
  <a class="nav-logo" href="https://code-withuday.github.io/portfolio">Uday Anand</a>
  <span class="nav-tag">Hangman Game</span>
</nav>

<main>
  <p class="page-tag">Python Project — Word Game</p>
  <h1 class="page-title">Hang<em>man.</em></h1>
  <p class="page-sub">Guess the hidden word before the man is hanged — 6 chances only.</p>

  <div class="game-wrap">

    <!-- STATUS -->
    <div class="status-msg" id="statusMsg">
      <div class="status-title" id="statusTitle"></div>
      <div class="status-word">The word was — <span id="statusWord"></span></div>
    </div>

    <!-- GALLOWS -->
    <div class="gallows-row">
      <svg class="gallows-svg" viewBox="0 0 160 180" fill="none" xmlns="http://www.w3.org/2000/svg">
        <!-- Structure -->
        <line x1="20" y1="170" x2="140" y2="170" stroke="#2a2a2a" stroke-width="2"/>
        <line x1="50" y1="170" x2="50" y2="15" stroke="#2a2a2a" stroke-width="2"/>
        <line x1="50" y1="15" x2="105" y2="15" stroke="#2a2a2a" stroke-width="2"/>
        <line x1="105" y1="15" x2="105" y2="38" stroke="#2a2a2a" stroke-width="2"/>
        <!-- Body parts -->
        <circle id="p-head" cx="105" cy="50" r="12" stroke="#c9a96e" stroke-width="1.5" fill="none" opacity="0" style="transition:opacity .4s"/>
        <line id="p-body" x1="105" y1="62" x2="105" y2="100" stroke="#c9a96e" stroke-width="1.5" opacity="0" style="transition:opacity .4s"/>
        <line id="p-la" x1="105" y1="72" x2="85" y2="90" stroke="#c9a96e" stroke-width="1.5" opacity="0" style="transition:opacity .4s"/>
        <line id="p-ra" x1="105" y1="72" x2="125" y2="90" stroke="#c9a96e" stroke-width="1.5" opacity="0" style="transition:opacity .4s"/>
        <line id="p-ll" x1="105" y1="100" x2="88" y2="122" stroke="#c9a96e" stroke-width="1.5" opacity="0" style="transition:opacity .4s"/>
        <line id="p-rl" x1="105" y1="100" x2="122" y2="122" stroke="#c9a96e" stroke-width="1.5" opacity="0" style="transition:opacity .4s"/>
      </svg>
    </div>

    <!-- WORD -->
    <div class="word-row" id="wordRow"></div>

    <!-- STATS -->
    <div class="stats-row">
      <div class="stat-box">
        <div class="stat-label">Lives Left</div>
        <div class="stat-val" id="livesVal">6</div>
      </div>
      <div class="stat-box">
        <div class="stat-label">Wrong</div>
        <div class="stat-val" id="wrongVal">0</div>
      </div>
      <div class="stat-box">
        <div class="stat-label">Category</div>
        <div class="stat-val gold" id="catVal" style="font-size:1.1rem;padding-top:.4rem">—</div>
      </div>
    </div>

    <!-- WRONG LETTERS -->
    <div class="wrong-row">
      <div class="wrong-label">Wrong guesses</div>
      <div class="wrong-chips" id="wrongChips"></div>
    </div>

    <!-- KEYBOARD -->
    <div class="keyboard" id="keyboard"></div>

    <!-- NEW GAME -->
    <button class="new-btn" onclick="newGame()">New Game →</button>

  </div>
</main>

<footer>
  <p>Built by <a href="https://code-withuday.github.io/portfolio">Uday Anand</a> · Python Developer</p>
  <p>Hangman — Python Logic Project</p>
</footer>

<script>
// CURSOR
const cur=document.getElementById('cur'),ring=document.getElementById('ring');
let mx=0,my=0,rx=0,ry=0;
document.addEventListener('mousemove',e=>{mx=e.clientX;my=e.clientY;cur.style.left=mx+'px';cur.style.top=my+'px'});
(function follow(){rx+=(mx-rx)*.12;ry+=(my-ry)*.12;ring.style.left=rx+'px';ring.style.top=ry+'px';requestAnimationFrame(follow)})();
document.querySelectorAll('button,a').forEach(el=>{
  el.addEventListener('mouseenter',()=>{ring.style.transform='translate(-50%,-50%) scale(2.2)';ring.style.borderColor='rgba(201,169,110,0.45)'});
  el.addEventListener('mouseleave',()=>{ring.style.transform='translate(-50%,-50%) scale(1)';ring.style.borderColor='rgba(255,255,255,0.25)'});
});

// NAV SCROLL
window.addEventListener('scroll',()=>{
  document.getElementById('nav').classList.toggle('scrolled',window.scrollY>20)
});

const words = [
  {w:"apple",c:"Fruits"},{w:"banana",c:"Fruits"},{w:"grapes",c:"Fruits"},
  {w:"kiwi",c:"Fruits"},{w:"watermelon",c:"Fruits"},{w:"dragonfruit",c:"Fruits"},
  {w:"mango",c:"Fruits"},{w:"strawberry",c:"Fruits"},{w:"pineapple",c:"Fruits"},
  {w:"python",c:"Tech"},{w:"github",c:"Tech"},{w:"developer",c:"Tech"},
  {w:"keyboard",c:"Tech"},{w:"javascript",c:"Tech"},{w:"algorithm",c:"Tech"},
  {w:"delhi",c:"Cities"},{w:"mumbai",c:"Cities"},{w:"london",c:"Cities"},
  {w:"paris",c:"Cities"},{w:"tokyo",c:"Cities"}
];

const parts = ['p-head','p-body','p-la','p-ra','p-ll','p-rl'];
const kbRows = ['qwertyuiop','asdfghjkl','zxcvbnm'];

let secret, category, guessed, wrong, gameOver;

function newGame(){
  const pick = words[Math.floor(Math.random()*words.length)];
  secret = pick.w; category = pick.c;
  guessed = new Set(); wrong = []; gameOver = false;

  document.getElementById('statusMsg').className = 'status-msg';
  document.getElementById('wrongChips').innerHTML = '';
  document.getElementById('livesVal').textContent = '6';
  document.getElementById('livesVal').className = 'stat-val';
  document.getElementById('wrongVal').textContent = '0';
  document.getElementById('catVal').textContent = category;
  parts.forEach(id => document.getElementById(id).style.opacity = '0');

  renderWord();
  buildKeyboard();
}

function renderWord(){
  const row = document.getElementById('wordRow');
  row.innerHTML = secret.split('').map(l => `
    <div class="letter-slot">
      <div class="letter-char ${guessed.has(l)?'show':''}" id="lc-${l}-${secret.indexOf(l)}">${l.toUpperCase()}</div>
      <div class="letter-line ${guessed.has(l)?'active':''}"></div>
    </div>
  `).join('');
  // Show all instances
  secret.split('').forEach((l,i) => {
    if(guessed.has(l)){
      const slots = row.querySelectorAll('.letter-slot');
      const ch = slots[i].querySelector('.letter-char');
      const ln = slots[i].querySelector('.letter-line');
      if(ch) ch.classList.add('show');
      if(ln) ln.classList.add('active');
    }
  });
}

function buildKeyboard(){
  const kb = document.getElementById('keyboard');
  kb.innerHTML = kbRows.map(row =>
    `<div class="kb-row">${row.split('').map(l =>
      `<button class="kb-btn" id="kb-${l}" onclick="guess('${l}')">${l.toUpperCase()}</button>`
    ).join('')}</div>`
  ).join('');
}

function guess(letter){
  if(gameOver) return;
  const btn = document.getElementById('kb-'+letter);
  if(!btn || btn.disabled) return;
  btn.disabled = true;

  if(secret.includes(letter)){
    guessed.add(letter);
    btn.classList.add('correct');
    renderWord();
    if(secret.split('').every(l => guessed.has(l))){
      gameOver = true;
      showStatus('win');
    }
  } else {
    wrong.push(letter);
    btn.classList.add('wrong');
    document.getElementById('wrongChips').innerHTML +=
      `<span class="wrong-chip">${letter.toUpperCase()}</span>`;
    const lives = 6 - wrong.length;
    document.getElementById('livesVal').textContent = lives;
    document.getElementById('wrongVal').textContent = wrong.length;
    if(lives <= 2) document.getElementById('livesVal').className = 'stat-val danger';
    if(wrong.length <= 6) document.getElementById(parts[wrong.length-1]).style.opacity = '1';
    if(wrong.length >= 6){
      gameOver = true;
      guessed = new Set(secret.split(''));
      renderWord();
      showStatus('lose');
    }
  }
}

function showStatus(type){
  const msg = document.getElementById('statusMsg');
  const title = document.getElementById('statusTitle');
  const word = document.getElementById('statusWord');
  msg.className = 'status-msg ' + type;
  title.className = 'status-title ' + type;
  title.textContent = type === 'win' ? 'Well Played.' : 'Game Over.';
  word.textContent = secret.toUpperCase();
  msg.scrollIntoView({behavior:'smooth',block:'center'});
}

// Keyboard input
document.addEventListener('keydown', e => {
  if(e.key.match(/^[a-zA-Z]$/) && !e.ctrlKey && !e.metaKey)
    guess(e.key.toLowerCase());
});

newGame();
</script>
</body>
</html>
