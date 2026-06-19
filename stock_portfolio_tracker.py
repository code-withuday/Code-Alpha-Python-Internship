<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>Stock Portfolio Tracker — Uday Anand</title>
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
body{background:var(--black);color:var(--white);font-family:var(--sans);overflow-x:hidden;min-height:100vh}

.grid{position:fixed;inset:0;pointer-events:none;z-index:0;opacity:.035}
.grid::before{content:'';position:absolute;top:0;left:25%;width:1px;height:100%;background:var(--white)}
.grid::after{content:'';position:absolute;top:0;right:25%;width:1px;height:100%;background:var(--white)}

nav{position:relative;z-index:10;padding:1.8rem 5rem;display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid var(--border)}
.nav-logo{font-family:var(--serif);font-size:1rem;font-weight:300;letter-spacing:.25em;color:var(--white);text-transform:uppercase;text-decoration:none}
.nav-back{font-size:.65rem;letter-spacing:.2em;text-transform:uppercase;color:rgba(255,255,255,.45);text-decoration:none;transition:color .3s;display:flex;align-items:center;gap:.5rem}
.nav-back:hover{color:var(--gold)}

main{position:relative;z-index:1;max-width:1000px;margin:0 auto;padding:5rem 5rem 6rem}

.page-tag{font-family:var(--mono);font-size:.65rem;letter-spacing:.3em;color:var(--gold);text-transform:uppercase;margin-bottom:1.5rem}
.page-title{font-family:var(--serif);font-size:clamp(3rem,7vw,5.5rem);font-weight:300;line-height:.95;letter-spacing:-.02em;margin-bottom:1rem}
.page-title em{font-style:italic;color:var(--gold)}
.page-sub{font-size:.85rem;color:rgba(255,255,255,.4);font-weight:300;max-width:480px;line-height:1.8;margin-bottom:3.5rem}

.tracker-layout{display:grid;grid-template-columns:1fr 1fr;gap:4rem;align-items:start}

.panel-label{font-size:.62rem;letter-spacing:.28em;text-transform:uppercase;color:var(--gold);margin-bottom:1.8rem;display:block}

.field{margin-bottom:1.8rem}
.field-label{font-size:.7rem;letter-spacing:.15em;text-transform:uppercase;color:rgba(255,255,255,.4);margin-bottom:.8rem;display:block}
select, input{
  width:100%;
  background:transparent;
  border:none;
  border-bottom:1px solid var(--border);
  color:var(--white);
  font-family:var(--serif);
  font-size:1.4rem;
  font-weight:300;
  padding:.6rem 0;
  outline:none;
  transition:border-color .3s;
  appearance:none;
}
select:focus, input:focus{border-color:var(--gold)}
select option{background:#0a0a0a;color:var(--white)}

.btn-calc{
  width:100%;
  background:transparent;
  border:1px solid var(--gold);
  color:var(--gold);
  font-family:var(--mono);
  font-size:.72rem;
  letter-spacing:.25em;
  text-transform:uppercase;
  padding:1.1rem 0;
  cursor:pointer;
  transition:all .35s;
  margin-top:1rem;
}
.btn-calc:hover{background:var(--gold);color:var(--black)}

.result-panel{
  border:1px solid var(--border);
  padding:3rem 2.5rem;
  min-height:280px;
  display:flex;
  flex-direction:column;
  justify-content:center;
  transition:border-color .4s;
}
.result-panel.active{border-color:var(--gold)}
.result-empty{font-size:.8rem;color:rgba(255,255,255,.25);font-weight:300;text-align:center;line-height:1.8}

.result-row{display:flex;justify-content:space-between;padding:.9rem 0;border-bottom:1px solid var(--border)}
.result-row:last-child{border-bottom:none}
.result-label{font-size:.7rem;letter-spacing:.15em;text-transform:uppercase;color:rgba(255,255,255,.4)}
.result-value{font-size:.9rem;color:var(--white);font-weight:300}

.result-total-wrap{margin-top:1.5rem;padding-top:1.5rem;border-top:1px solid var(--border)}
.result-total-label{font-size:.62rem;letter-spacing:.28em;text-transform:uppercase;color:var(--gold);margin-bottom:.8rem;display:block}
.result-total{font-family:var(--serif);font-size:3rem;font-weight:300;line-height:1;color:var(--white)}

.error-text{font-size:.85rem;color:#d4574e;font-weight:300;text-align:center}

.code-ref{margin-top:5rem;padding-top:3rem;border-top:1px solid var(--border)}
.code-box{background:#080808;border:1px solid #1c1c1c;border-left:1px solid var(--gold);padding:2rem 1.8rem;font-family:var(--mono);font-size:.73rem;line-height:2.1;color:rgba(255,255,255,.5);overflow-x:auto}
.cm{color:#3a3a3a}.ck{color:var(--gold)}.cs{color:#7eb8f7}.cf{color:#c8a6e8}

footer{position:relative;z-index:1;padding:2.5rem 5rem;border-top:1px solid var(--border);display:flex;justify-content:space-between;align-items:center}
footer p{font-family:var(--mono);font-size:.6rem;color:var(--muted);letter-spacing:.08em}

@media(max-width:768px){
  nav{padding:1.5rem 1.8rem}
  main{padding:3.5rem 1.8rem 4rem}
  .tracker-layout{grid-template-columns:1fr;gap:2.5rem}
  footer{padding:2rem 1.8rem;flex-direction:column;gap:.6rem;text-align:center}
}
</style>
</head>
<body>
<div class="grid"></div>

<nav>
  <a class="nav-logo" href="index.html">Uday Anand</a>
  <a class="nav-back" href="index.html">← Back to portfolio</a>
</nav>

<main>
  <p class="page-tag">Project demo</p>
  <h1 class="page-title">Stock Portfolio<br><em>Tracker.</em></h1>
  <p class="page-sub">A Python project that calculates total investment value from a dictionary of real-world stocks. This is a live browser version of the original script — same logic, interactive interface.</p>

  <div class="tracker-layout">

    <div>
      <span class="panel-label">01 — Enter details</span>

      <div class="field">
        <label class="field-label">Stock name</label>
        <select id="stockSelect">
          <option value="tata">Tata — ₹380</option>
          <option value="bmw">BMW — ₹7,488</option>
          <option value="mercedes_benz">Mercedes Benz — ₹5,176</option>
          <option value="cooper">Cooper — ₹6,480</option>
          <option value="volkswagen">Volkswagen — ₹9,581</option>
          <option value="rolls royce">Rolls Royce — ₹1,237</option>
          <option value="tesla">Tesla — ₹396</option>
          <option value="toyota">Toyota — ₹2,814</option>
          <option value="maruti_suzuki">Maruti Suzuki — ₹13,072</option>
          <option value="ford">Ford — ₹1,428</option>
        </select>
      </div>

      <div class="field">
        <label class="field-label">Quantity</label>
        <input id="qtyInput" type="number" min="1" value="1"/>
      </div>

      <button class="btn-calc" id="calcBtn">Calculate investment</button>
    </div>

    <div>
      <span class="panel-label">02 — Result</span>
      <div class="result-panel" id="resultPanel">
        <p class="result-empty">Select a stock and quantity,<br>then calculate to see your<br>total investment value.</p>
      </div>
    </div>

  </div>


</main>

<footer>
  <p>© 2026 Uday Anand</p>
  <p>Python Developer &amp; Graphic Designer · Delhi, India</p>
</footer>

<script>
const stocks = {
  "tata": 380, "bmw": 7488, "mercedes_benz": 5176, "cooper": 6480,
  "volkswagen": 9581, "rolls royce": 1237, "tesla": 396,
  "toyota": 2814, "maruti_suzuki": 13072, "ford": 1428
};

document.getElementById('calcBtn').addEventListener('click', () => {
  const select = document.getElementById('stockSelect');
  const stockName = select.value;
  const stockLabel = select.options[select.selectedIndex].text.split(' — ')[0];
  const qty = parseInt(document.getElementById('qtyInput').value) || 0;
  const panel = document.getElementById('resultPanel');

  if (stockName in stocks && qty > 0) {
    const price = stocks[stockName];
    const total = price * qty;
    panel.classList.add('active');
    panel.innerHTML = `
      <div class="result-row"><span class="result-label">Stock</span><span class="result-value">${stockLabel}</span></div>
      <div class="result-row"><span class="result-label">Price / unit</span><span class="result-value">₹${price.toLocaleString('en-IN')}</span></div>
      <div class="result-row"><span class="result-label">Quantity</span><span class="result-value">${qty}</span></div>
      <div class="result-total-wrap">
        <span class="result-total-label">Total investment</span>
        <div class="result-total">₹${total.toLocaleString('en-IN')}</div>
      </div>
    `;
  } else {
    panel.classList.remove('active');
    panel.innerHTML = `<p class="error-text">Stock not found.<br>Please select a valid stock.</p>`;
  }
});
</script>
</body>
</html>
