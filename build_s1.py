
s1 = '''
<!-- ═══════════════════════════════════════════ SECTION 1 ═══ -->
<section class="section" id="s1">
  <div class="section-header">
    <div class="section-icon" style="background:var(--blue-bg);">🎯</div>
    <div class="section-meta">
      <span class="section-badge" style="background:var(--blue-bg);color:var(--blue);">Beginner</span>
      <div class="section-title" style="color:var(--blue);">Dart Fundamentals</div>
      <div class="section-subtitle">Variables, types, functions, null safety, OOP, and async programming</div>
    </div>
  </div>

  <!-- 1.1 Variables -->
  <div class="subsection" id="s1-1">
    <h3 style="color:var(--blue);">1.1 Variables &amp; Type System</h3>
    <p>Dart is a <strong>statically typed, type-inferred language</strong>. Every value in Dart is an object — even primitives like <code>int</code> and <code>bool</code> are instances of classes. This means you can call methods on any value, and everything inherits from the root <code>Object</code> class.</p>
    <p><strong>var</strong> lets Dart infer the type at compile time — once assigned, the type locks in. <strong>final</strong> is a runtime constant: set once, never reassigned (but the object itself can be mutable). <strong>const</strong> is a compile-time constant — the value must be known before the program runs and the object is deeply immutable. <strong>dynamic</strong> bypasses type checking entirely and is resolved at runtime — use sparingly.</p>
    <p>Type inference keeps code concise while retaining all type-safety benefits. In real Flutter code, you'll use <code>final</code> most often for widget fields and local variables that don't change after initial assignment.</p>
    <div class="diagram">
      <svg viewBox="0 0 860 260" xmlns="http://www.w3.org/2000/svg">
        <defs><marker id="arr1" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="#8b949e" stroke-width="1.5" stroke-linecap="round"/></marker></defs>
        <!-- Object root -->
        <rect x="330" y="20" width="200" height="48" rx="8" fill="#0d1e3b" stroke="#60a5fa" stroke-width="2"/>
        <text x="430" y="40" font-family="JetBrains Mono" font-size="13" font-weight="700" fill="#60a5fa" text-anchor="middle">Object</text>
        <text x="430" y="58" font-family="JetBrains Mono" font-size="10" fill="#8b949e" text-anchor="middle">Root of all Dart types</text>
        <!-- num -->
        <rect x="200" y="110" width="130" height="44" rx="8" fill="#0d1e3b" stroke="#60a5fa" stroke-width="1.5"/>
        <text x="265" y="128" font-family="JetBrains Mono" font-size="12" font-weight="600" fill="#60a5fa" text-anchor="middle">num</text>
        <text x="265" y="146" font-family="JetBrains Mono" font-size="10" fill="#8b949e" text-anchor="middle">int | double</text>
        <!-- String -->
        <rect x="360" y="110" width="130" height="44" rx="8" fill="#161b22" stroke="#30363d" stroke-width="1.5"/>
        <text x="425" y="128" font-family="JetBrains Mono" font-size="12" font-weight="600" fill="#e6edf3" text-anchor="middle">String</text>
        <text x="425" y="146" font-family="JetBrains Mono" font-size="10" fill="#8b949e" text-anchor="middle">UTF-16 chars</text>
        <!-- bool -->
        <rect x="520" y="110" width="130" height="44" rx="8" fill="#161b22" stroke="#30363d" stroke-width="1.5"/>
        <text x="585" y="128" font-family="JetBrains Mono" font-size="12" font-weight="600" fill="#e6edf3" text-anchor="middle">bool</text>
        <text x="585" y="146" font-family="JetBrains Mono" font-size="10" fill="#8b949e" text-anchor="middle">true | false</text>
        <!-- int -->
        <rect x="90" y="195" width="110" height="40" rx="8" fill="#161b22" stroke="#30363d" stroke-width="1.5"/>
        <text x="145" y="213" font-family="JetBrains Mono" font-size="12" fill="#e6edf3" text-anchor="middle">int</text>
        <text x="145" y="228" font-family="JetBrains Mono" font-size="10" fill="#8b949e" text-anchor="middle">Whole numbers</text>
        <!-- double -->
        <rect x="220" y="195" width="110" height="40" rx="8" fill="#161b22" stroke="#30363d" stroke-width="1.5"/>
        <text x="275" y="213" font-family="JetBrains Mono" font-size="12" fill="#e6edf3" text-anchor="middle">double</text>
        <text x="275" y="228" font-family="JetBrains Mono" font-size="10" fill="#8b949e" text-anchor="middle">64-bit float</text>
        <!-- List -->
        <rect x="650" y="110" width="130" height="44" rx="8" fill="#161b22" stroke="#30363d" stroke-width="1.5"/>
        <text x="715" y="128" font-family="JetBrains Mono" font-size="12" font-weight="600" fill="#e6edf3" text-anchor="middle">List / Map</text>
        <text x="715" y="146" font-family="JetBrains Mono" font-size="10" fill="#8b949e" text-anchor="middle">Collections</text>
        <!-- lines -->
        <line x1="430" y1="68" x2="265" y2="110" stroke="#8b949e" stroke-dasharray="5 3" marker-end="url(#arr1)"/>
        <line x1="430" y1="68" x2="425" y2="110" stroke="#8b949e" stroke-dasharray="5 3" marker-end="url(#arr1)"/>
        <line x1="430" y1="68" x2="585" y2="110" stroke="#8b949e" stroke-dasharray="5 3" marker-end="url(#arr1)"/>
        <line x1="430" y1="68" x2="715" y2="110" stroke="#8b949e" stroke-dasharray="5 3" marker-end="url(#arr1)"/>
        <line x1="265" y1="154" x2="145" y2="195" stroke="#8b949e" stroke-dasharray="5 3" marker-end="url(#arr1)"/>
        <line x1="265" y1="154" x2="275" y2="195" stroke="#8b949e" stroke-dasharray="5 3" marker-end="url(#arr1)"/>
      </svg>
    </div>
    <div class="code-wrap">
      <span class="code-label">Dart</span>
      <button class="copy-btn">Copy</button>
<pre><span class="c">// var — type inferred at compile time, then locked</span>
<span class="k">var</span> <span class="n">name</span> = <span class="s">'Flutter'</span>;          <span class="c">// inferred as String</span>
<span class="k">var</span> <span class="n">version</span> = <span class="num">3.19</span>;             <span class="c">// inferred as double</span>

<span class="c">// final — set once, known at runtime</span>
<span class="k">final</span> <span class="t">String</span> <span class="n">platform</span> = <span class="s">'Mobile'</span>;
<span class="k">final</span> <span class="n">startTime</span> = <span class="t">DateTime</span>.<span class="m">now</span>();  <span class="c">// runtime value</span>

<span class="c">// const — compile-time constant, deeply immutable</span>
<span class="k">const</span> <span class="t">double</span> <span class="n">pi</span> = <span class="num">3.14159</span>;
<span class="k">const</span> <span class="n">maxRetries</span> = <span class="num">3</span>;
<span class="k">const</span> <span class="t">List</span>&lt;<span class="t">String</span>&gt; <span class="n">colors</span> = [<span class="s">'red'</span>, <span class="s">'green'</span>, <span class="s">'blue'</span>];

<span class="c">// dynamic — bypasses type checking (use sparingly)</span>
<span class="k">dynamic</span> <span class="n">anything</span> = <span class="num">42</span>;
<span class="n">anything</span> = <span class="s">'now a string'</span>;   <span class="c">// allowed, no error</span>
<span class="n">anything</span> = <span class="k">true</span>;              <span class="c">// allowed</span>

<span class="c">// Type annotations (explicit)</span>
<span class="t">int</span> <span class="n">count</span> = <span class="num">0</span>;
<span class="t">String</span> <span class="n">message</span> = <span class="s">'Hello'</span>;
<span class="t">bool</span> <span class="n">isLoggedIn</span> = <span class="k">false</span>;
<span class="t">List</span>&lt;<span class="t">int</span>&gt; <span class="n">scores</span> = [<span class="num">95</span>, <span class="num">87</span>, <span class="num">72</span>];
<span class="t">Map</span>&lt;<span class="t">String</span>, <span class="k">dynamic</span>&gt; <span class="n">config</span> = {<span class="s">'theme'</span>: <span class="s">'dark'</span>, <span class="s">'fontSize'</span>: <span class="num">16</span>};</pre>
    </div>
    <div class="info-box info-tip"><strong>💡 Best Practice</strong><p>Prefer <code>final</code> by default. Use <code>const</code> for widget constructors and truly static values. Avoid <code>dynamic</code> unless parsing JSON or interfacing with untyped APIs — it defeats Dart's type safety.</p></div>
    <div class="table-wrap"><table>
      <tr><th>Keyword</th><th>Reassignable</th><th>Mutable Object</th><th>Compile-time</th><th>Best Used When</th></tr>
      <tr><td><code style="background:var(--blue-bg);color:var(--blue);">var</code></td><td>✅ Yes</td><td>✅ Yes</td><td>❌ No</td><td>Local variables with inferred types</td></tr>
      <tr><td><code style="background:var(--teal-bg);color:var(--teal);">final</code></td><td>❌ No</td><td>✅ Yes</td><td>❌ No</td><td>Widget fields, one-time assignments</td></tr>
      <tr><td><code style="background:var(--purple-bg);color:var(--purple);">const</code></td><td>❌ No</td><td>❌ No</td><td>✅ Yes</td><td>Static configs, widget constructors</td></tr>
      <tr><td><code style="background:var(--coral-bg);color:var(--coral);">dynamic</code></td><td>✅ Yes</td><td>✅ Yes</td><td>❌ No</td><td>JSON parsing, plugin interop</td></tr>
    </table></div>
  </div>

  <!-- 1.2 Data Types -->
  <div class="subsection" id="s1-2">
    <h3 style="color:var(--blue);">1.2 Data Types &amp; Collections</h3>
    <p>Dart provides three core collection types: <strong>List</strong> (ordered, duplicates allowed), <strong>Set</strong> (unordered, unique elements only), and <strong>Map</strong> (key-value pairs). All are generic — always specify the type parameter for type safety and better IDE support.</p>
    <p>The <strong>spread operator</strong> (<code>...</code>) merges collections. <strong>Collection if</strong> and <strong>collection for</strong> let you build collections with conditional and iterative logic inline — extremely useful in Flutter widget trees. The <strong>cascade notation</strong> (<code>..</code>) lets you chain multiple operations on the same object without repeating the variable name.</p>
    <div class="diagram">
      <svg viewBox="0 0 860 200" xmlns="http://www.w3.org/2000/svg">
        <defs><marker id="arr2" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="#8b949e" stroke-width="1.5" stroke-linecap="round"/></marker></defs>
        <!-- List -->
        <rect x="40" y="30" width="220" height="140" rx="10" fill="#0d1e3b" stroke="#60a5fa" stroke-width="1.5"/>
        <text x="150" y="55" font-family="JetBrains Mono" font-size="13" font-weight="700" fill="#60a5fa" text-anchor="middle">List&lt;T&gt;</text>
        <text x="150" y="75" font-family="JetBrains Mono" font-size="10" fill="#8b949e" text-anchor="middle">Ordered · Duplicates OK</text>
        <rect x="60" y="88" width="50" height="32" rx="4" fill="#161b22" stroke="#30363d"/>
        <text x="85" y="109" font-family="JetBrains Mono" font-size="11" fill="#e6edf3" text-anchor="middle">[0]</text>
        <rect x="120" y="88" width="50" height="32" rx="4" fill="#161b22" stroke="#30363d"/>
        <text x="145" y="109" font-family="JetBrains Mono" font-size="11" fill="#e6edf3" text-anchor="middle">[1]</text>
        <rect x="180" y="88" width="50" height="32" rx="4" fill="#161b22" stroke="#30363d"/>
        <text x="205" y="109" font-family="JetBrains Mono" font-size="11" fill="#e6edf3" text-anchor="middle">[2]</text>
        <text x="150" y="152" font-family="JetBrains Mono" font-size="10" fill="#8b949e" text-anchor="middle">Indexed access O(1)</text>
        <!-- Set -->
        <rect x="320" y="30" width="220" height="140" rx="10" fill="#1a1433" stroke="#a78bfa" stroke-width="1.5"/>
        <text x="430" y="55" font-family="JetBrains Mono" font-size="13" font-weight="700" fill="#a78bfa" text-anchor="middle">Set&lt;T&gt;</text>
        <text x="430" y="75" font-family="JetBrains Mono" font-size="10" fill="#8b949e" text-anchor="middle">Unordered · Unique only</text>
        <circle cx="370" cy="115" r="22" fill="#161b22" stroke="#30363d"/>
        <text x="370" y="119" font-family="JetBrains Mono" font-size="11" fill="#e6edf3" text-anchor="middle">'a'</text>
        <circle cx="430" cy="105" r="22" fill="#161b22" stroke="#30363d"/>
        <text x="430" y="109" font-family="JetBrains Mono" font-size="11" fill="#e6edf3" text-anchor="middle">'b'</text>
        <circle cx="490" cy="120" r="22" fill="#161b22" stroke="#30363d"/>
        <text x="490" y="124" font-family="JetBrains Mono" font-size="11" fill="#e6edf3" text-anchor="middle">'c'</text>
        <!-- Map -->
        <rect x="600" y="30" width="220" height="140" rx="10" fill="#0d2b22" stroke="#34d399" stroke-width="1.5"/>
        <text x="710" y="55" font-family="JetBrains Mono" font-size="13" font-weight="700" fill="#34d399" text-anchor="middle">Map&lt;K,V&gt;</text>
        <text x="710" y="75" font-family="JetBrains Mono" font-size="10" fill="#8b949e" text-anchor="middle">Key → Value pairs</text>
        <rect x="618" y="88" width="70" height="28" rx="4" fill="#161b22" stroke="#30363d"/>
        <text x="653" y="107" font-family="JetBrains Mono" font-size="11" fill="#60a5fa" text-anchor="middle">'name'</text>
        <text x="698" y="107" font-family="JetBrains Mono" font-size="14" fill="#8b949e">→</text>
        <rect x="718" y="88" width="84" height="28" rx="4" fill="#161b22" stroke="#30363d"/>
        <text x="760" y="107" font-family="JetBrains Mono" font-size="11" fill="#a5d6ff" text-anchor="middle">'Flutter'</text>
        <rect x="618" y="124" width="70" height="28" rx="4" fill="#161b22" stroke="#30363d"/>
        <text x="653" y="143" font-family="JetBrains Mono" font-size="11" fill="#60a5fa" text-anchor="middle">'age'</text>
        <text x="698" y="143" font-family="JetBrains Mono" font-size="14" fill="#8b949e">→</text>
        <rect x="718" y="124" width="54" height="28" rx="4" fill="#161b22" stroke="#30363d"/>
        <text x="745" y="143" font-family="JetBrains Mono" font-size="11" fill="#f2cc60" text-anchor="middle">3</text>
      </svg>
    </div>
    <div class="code-wrap">
      <span class="code-label">Dart</span>
      <button class="copy-btn">Copy</button>
<pre><span class="c">// List — ordered collection</span>
<span class="t">List</span>&lt;<span class="t">String</span>&gt; <span class="n">fruits</span> = [<span class="s">'apple'</span>, <span class="s">'banana'</span>, <span class="s">'mango'</span>];
<span class="n">fruits</span>.<span class="m">add</span>(<span class="s">'grape'</span>);
<span class="n">fruits</span>.<span class="m">removeWhere</span>((<span class="n">f</span>) => <span class="n">f</span>.<span class="m">startsWith</span>(<span class="s">'b'</span>));

<span class="c">// Map — key-value pairs</span>
<span class="t">Map</span>&lt;<span class="t">String</span>, <span class="t">int</span>&gt; <span class="n">scores</span> = {<span class="s">'Alice'</span>: <span class="num">95</span>, <span class="s">'Bob'</span>: <span class="num">87</span>};
<span class="n">scores</span>[<span class="s">'Charlie'</span>] = <span class="num">91</span>;
<span class="k">final</span> <span class="n">top</span> = <span class="n">scores</span>.<span class="m">entries</span>.<span class="m">reduce</span>((<span class="n">a</span>, <span class="n">b</span>) => <span class="n">a</span>.<span class="n">value</span> &gt; <span class="n">b</span>.<span class="n">value</span> ? <span class="n">a</span> : <span class="n">b</span>);

<span class="c">// Set — unique elements</span>
<span class="t">Set</span>&lt;<span class="t">String</span>&gt; <span class="n">unique</span> = {<span class="s">'a'</span>, <span class="s">'b'</span>, <span class="s">'a'</span>}; <span class="c">// only 2 items</span>

<span class="c">// Spread operator</span>
<span class="t">List</span>&lt;<span class="t">String</span>&gt; <span class="n">moreFruits</span> = [<span class="s">'pear'</span>, <span class="s">'plum'</span>];
<span class="t">List</span>&lt;<span class="t">String</span>&gt; <span class="n">allFruits</span> = [...<span class="n">fruits</span>, ...<span class="n">moreFruits</span>];

<span class="c">// Collection if &amp; for — used in Flutter widget trees!</span>
<span class="k">bool</span> <span class="n">isLoggedIn</span> = <span class="k">true</span>;
<span class="t">List</span>&lt;<span class="t">String</span>&gt; <span class="n">menu</span> = [
  <span class="s">'Home'</span>,
  <span class="k">if</span> (<span class="n">isLoggedIn</span>) <span class="s">'Profile'</span>,
  <span class="k">if</span> (<span class="n">isLoggedIn</span>) <span class="s">'Logout'</span> <span class="k">else</span> <span class="s">'Login'</span>,
  <span class="k">for</span> (<span class="k">var</span> <span class="n">item</span> <span class="k">in</span> [<span class="s">'Settings'</span>, <span class="s">'Help'</span>]) <span class="n">item</span>,
];

<span class="c">// Cascade notation (..) — chain operations</span>
<span class="k">final</span> <span class="n">buffer</span> = <span class="t">StringBuffer</span>()
  ..<span class="m">write</span>(<span class="s">'Hello'</span>)
  ..<span class="m">write</span>(<span class="s">' '</span>)
  ..<span class="m">write</span>(<span class="s">'Flutter'</span>);
<span class="m">print</span>(<span class="n">buffer</span>.<span class="m">toString</span>()); <span class="c">// Hello Flutter</span></pre>
    </div>
    <div class="info-box info-key"><strong>🔑 Collection if/for in Flutter</strong><p>Collection if and for are essential in Flutter — they let you conditionally include widgets or build widget lists inline without needing external logic. This keeps your <code>build()</code> method clean and declarative.</p></div>
  </div>

  <!-- 1.3 Functions -->
  <div class="subsection" id="s1-3">
    <h3 style="color:var(--blue);">1.3 Functions &amp; Closures</h3>
    <p>Dart functions are first-class objects — they can be assigned to variables, passed as arguments, and returned from other functions. This enables powerful <strong>higher-order programming patterns</strong> used throughout Flutter (callbacks, builders, listeners).</p>
    <p>Dart supports <strong>positional parameters</strong> (required by position), <strong>optional positional</strong> (<code>[param]</code>), <strong>named parameters</strong> (<code>{param}</code>), and combinations. The <code>required</code> keyword enforces named parameters. <strong>Closures</strong> capture their surrounding scope — a closure remembers variables from the function that created it, enabling patterns like factories and counters.</p>
    <div class="flow-row">
      <div class="flow-box" style="background:var(--blue-bg);border-color:var(--blue);color:var(--blue);">Required Positional</div>
      <span class="flow-arrow">→</span>
      <div class="flow-box" style="background:var(--teal-bg);border-color:var(--teal);color:var(--teal);">Optional Positional [  ]</div>
      <span class="flow-arrow">→</span>
      <div class="flow-box" style="background:var(--purple-bg);border-color:var(--purple);color:var(--purple);">Named Required {req:}</div>
      <span class="flow-arrow">→</span>
      <div class="flow-box" style="background:var(--amber-bg);border-color:var(--amber);color:var(--amber);">Named Optional {opt = default}</div>
    </div>
    <div class="code-wrap">
      <span class="code-label">Dart</span>
      <button class="copy-btn">Copy</button>
<pre><span class="c">// Named parameters with required + defaults</span>
<span class="k">void</span> <span class="m">createUser</span>({
  <span class="k">required</span> <span class="t">String</span> <span class="n">name</span>,
  <span class="k">required</span> <span class="t">String</span> <span class="n">email</span>,
  <span class="t">int</span> <span class="n">age</span> = <span class="num">18</span>,
  <span class="t">String</span> <span class="n">role</span> = <span class="s">'user'</span>,
}) {
  <span class="m">print</span>(<span class="s">'Creating $name &lt;$email&gt; age=$age role=$role'</span>);
}
<span class="m">createUser</span>(<span class="n">name</span>: <span class="s">'Alice'</span>, <span class="n">email</span>: <span class="s">'alice@dev.io'</span>, <span class="n">role</span>: <span class="s">'admin'</span>);

<span class="c">// Arrow functions (single expression)</span>
<span class="t">int</span> <span class="m">square</span>(<span class="t">int</span> <span class="n">n</span>) =&gt; <span class="n">n</span> * <span class="n">n</span>;
<span class="t">bool</span> <span class="m">isEven</span>(<span class="t">int</span> <span class="n">n</span>) =&gt; <span class="n">n</span> % <span class="num">2</span> == <span class="num">0</span>;

<span class="c">// Higher-order function with generics</span>
<span class="t">List</span>&lt;<span class="n">T</span>&gt; <span class="m">filterList</span>&lt;<span class="n">T</span>&gt;(<span class="t">List</span>&lt;<span class="n">T</span>&gt; <span class="n">list</span>, <span class="t">bool</span> <span class="t">Function</span>(<span class="n">T</span>) <span class="n">predicate</span>) =&gt;
    <span class="n">list</span>.<span class="m">where</span>(<span class="n">predicate</span>).<span class="m">toList</span>();

<span class="k">final</span> <span class="n">evens</span> = <span class="m">filterList</span>([<span class="num">1</span>,<span class="num">2</span>,<span class="num">3</span>,<span class="num">4</span>,<span class="num">5</span>], <span class="m">isEven</span>); <span class="c">// [2, 4]</span>

<span class="c">// Closure — captures surrounding scope</span>
<span class="t">Function</span> <span class="m">makeCounter</span>() {
  <span class="t">int</span> <span class="n">count</span> = <span class="num">0</span>;
  <span class="k">return</span> () =&gt; ++<span class="n">count</span>; <span class="c">// captures 'count' variable</span>
}
<span class="k">final</span> <span class="n">counter</span> = <span class="m">makeCounter</span>();
<span class="m">print</span>(<span class="m">counter</span>()); <span class="c">// 1</span>
<span class="m">print</span>(<span class="m">counter</span>()); <span class="c">// 2</span>
<span class="m">print</span>(<span class="m">counter</span>()); <span class="c">// 3</span>

<span class="c">// typedef for reusable function types</span>
<span class="k">typedef</span> <span class="t">Validator</span>&lt;<span class="n">T</span>&gt; = <span class="t">String</span>? <span class="t">Function</span>(<span class="n">T</span> <span class="n">value</span>);
<span class="t">Validator</span>&lt;<span class="t">String</span>&gt; <span class="n">emailValidator</span> = (<span class="n">v</span>) =&gt;
    <span class="n">v</span>.<span class="m">contains</span>(<span class="s">'@'</span>) ? <span class="k">null</span> : <span class="s">'Invalid email'</span>;</pre>
    </div>
    <div class="info-box info-warn"><strong>⚠️ Anonymous Functions in Flutter</strong><p>Avoid creating anonymous functions directly inside <code>build()</code> for performance-sensitive callbacks — they create new function objects each rebuild. Prefer referencing named methods or extracting the logic.</p></div>
  </div>

  <!-- 1.4 Null Safety -->
  <div class="subsection" id="s1-4">
    <h3 style="color:var(--blue);">1.4 Null Safety</h3>
    <p>Dart's <strong>sound null safety</strong> (introduced in Dart 2.12) eliminates null reference exceptions at compile time. By default, no variable can hold <code>null</code> unless explicitly declared nullable with <code>?</code>. The compiler statically analyzes all code paths to guarantee non-nullable variables always have a value.</p>
    <p>The <strong>late</strong> keyword defers initialization — useful for values not available at construction time (e.g., dependency-injected services). The <strong>null assertion operator</strong> (<code>!</code>) overrides the type system — it tells Dart "I know this is non-null" and crashes if wrong. Use it only when you're certain.</p>
    <div class="grid-2">
      <div class="card">
        <div class="card-title" style="color:var(--teal);">Non-Nullable (default)</div>
        <p>Must always have a value. Compiler guarantees it. Zero runtime null checks needed.</p>
        <div class="code-wrap"><button class="copy-btn">Copy</button>
<pre><span class="t">String</span> <span class="n">name</span> = <span class="s">'Flutter'</span>;
<span class="c">// name = null; ← COMPILE ERROR</span></pre>
        </div>
      </div>
      <div class="card">
        <div class="card-title" style="color:var(--coral);">Nullable (with ?)</div>
        <p>Can hold <code>null</code>. Requires null checks before use. Use null-aware operators.</p>
        <div class="code-wrap"><button class="copy-btn">Copy</button>
<pre><span class="t">String</span>? <span class="n">nickname</span> = <span class="k">null</span>;
<span class="c">// safe to assign null</span></pre>
        </div>
      </div>
    </div>
    <div class="code-wrap">
      <span class="code-label">Dart</span>
      <button class="copy-btn">Copy</button>
<pre><span class="t">String</span> <span class="n">name</span> = <span class="s">'Flutter'</span>;      <span class="c">// non-nullable</span>
<span class="t">String</span>? <span class="n">nickname</span> = <span class="k">null</span>;       <span class="c">// nullable — OK</span>

<span class="c">// Null-aware operators</span>
<span class="t">String</span> <span class="n">display</span> = <span class="n">nickname</span> ?? <span class="s">'Anonymous'</span>;  <span class="c">// if null use default</span>
<span class="t">int</span>? <span class="n">length</span> = <span class="n">nickname</span>?.<span class="n">length</span>;            <span class="c">// safe access — null if nickname is null</span>
<span class="n">nickname</span> ??= <span class="s">'Default'</span>;                    <span class="c">// assign only if null</span>

<span class="c">// Null-aware cascade</span>
<span class="n">nickname</span>?..<span class="m">trim</span>()..<span class="m">toLowerCase</span>(); <span class="c">// run cascade only if non-null</span>

<span class="c">// late — must be assigned before first read</span>
<span class="k">late</span> <span class="t">String</span> <span class="n">authToken</span>;
<span class="k">void</span> <span class="m">initAuth</span>() {
  <span class="n">authToken</span> = <span class="m">fetchToken</span>(); <span class="c">// assigned before use</span>
}

<span class="c">// late final — assigned exactly once</span>
<span class="k">late</span> <span class="k">final</span> <span class="t">String</span> <span class="n">userId</span>;
<span class="n">userId</span> = <span class="m">generateId</span>(); <span class="c">// can only be set once</span>

<span class="c">// Null assertion — use carefully!</span>
<span class="t">String</span> <span class="n">forced</span> = <span class="n">nickname</span>!; <span class="c">// throws if nickname is null</span>

<span class="c">// Pattern: check before use</span>
<span class="k">if</span> (<span class="n">nickname</span> != <span class="k">null</span>) {
  <span class="m">print</span>(<span class="n">nickname</span>.<span class="n">length</span>); <span class="c">// promoted to String (non-null)</span>
}</pre>
    </div>
    <div class="info-box info-key"><strong>🔑 Sound Null Safety</strong><p>"Sound" means if the compiler says a variable is non-null, it's guaranteed at runtime — no exceptions. Mixed-mode (unsound) null safety exists in packages that haven't migrated, but your code remains safe.</p></div>
  </div>

  <!-- 1.5 OOP -->
  <div class="subsection" id="s1-5">
    <h3 style="color:var(--blue);">1.5 OOP in Dart</h3>
    <p>Dart is a fully object-oriented language. <strong>Classes</strong> support multiple constructor types: default, named, factory, and const. <strong>Inheritance</strong> (<code>extends</code>) creates is-a relationships with single inheritance. <strong>Mixins</strong> (<code>with</code>) add capabilities without inheritance — perfect for cross-cutting concerns like serialization or logging. <strong>Interfaces</strong> (<code>implements</code>) enforce contracts without inheriting implementation.</p>
    <p><strong>Abstract classes</strong> define contracts with optional partial implementations. <strong>Extension methods</strong> add functionality to existing types without subclassing — one of Dart's most powerful features for writing expressive, clean code.</p>
    <div class="diagram">
      <svg viewBox="0 0 860 280" xmlns="http://www.w3.org/2000/svg">
        <defs><marker id="arr5" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="#8b949e" stroke-width="1.5" stroke-linecap="round"/></marker></defs>
        <!-- abstract Shape -->
        <rect x="310" y="20" width="240" height="52" rx="8" fill="#0d1e3b" stroke="#60a5fa" stroke-width="2"/>
        <text x="430" y="42" font-family="JetBrains Mono" font-size="12" font-weight="700" fill="#60a5fa" text-anchor="middle">abstract Shape</text>
        <text x="430" y="62" font-family="JetBrains Mono" font-size="10" fill="#8b949e" text-anchor="middle">area · perimeter → abstract</text>
        <!-- Circle -->
        <rect x="120" y="130" width="200" height="52" rx="8" fill="#161b22" stroke="#60a5fa" stroke-width="1.5"/>
        <text x="220" y="152" font-family="JetBrains Mono" font-size="12" font-weight="700" fill="#60a5fa" text-anchor="middle">Circle</text>
        <text x="220" y="172" font-family="JetBrains Mono" font-size="10" fill="#8b949e" text-anchor="middle">extends Shape with Serializable</text>
        <!-- Rectangle -->
        <rect x="540" y="130" width="200" height="52" rx="8" fill="#161b22" stroke="#60a5fa" stroke-width="1.5"/>
        <text x="640" y="152" font-family="JetBrains Mono" font-size="12" font-weight="700" fill="#60a5fa" text-anchor="middle">Rectangle</text>
        <text x="640" y="172" font-family="JetBrains Mono" font-size="10" fill="#8b949e" text-anchor="middle">extends Shape with Serializable</text>
        <!-- Mixin -->
        <rect x="350" y="130" width="160" height="52" rx="8" fill="#1a1433" stroke="#a78bfa" stroke-width="1.5" stroke-dasharray="6 3"/>
        <text x="430" y="152" font-family="JetBrains Mono" font-size="12" font-weight="700" fill="#a78bfa" text-anchor="middle">mixin Serializable</text>
        <text x="430" y="172" font-family="JetBrains Mono" font-size="10" fill="#8b949e" text-anchor="middle">toJson() → Map</text>
        <!-- Extension -->
        <rect x="350" y="220" width="160" height="44" rx="8" fill="#0d2b22" stroke="#34d399" stroke-width="1.5"/>
        <text x="430" y="239" font-family="JetBrains Mono" font-size="11" font-weight="700" fill="#34d399" text-anchor="middle">extension StringUtils</text>
        <text x="430" y="256" font-family="JetBrains Mono" font-size="10" fill="#8b949e" text-anchor="middle">on String · capitalized · isEmail</text>
        <!-- lines -->
        <line x1="430" y1="72" x2="220" y2="130" stroke="#60a5fa" stroke-dasharray="5 3" marker-end="url(#arr5)"/>
        <line x1="430" y1="72" x2="640" y2="130" stroke="#60a5fa" stroke-dasharray="5 3" marker-end="url(#arr5)"/>
        <line x1="430" y1="130" x2="220" y2="156" stroke="#a78bfa" stroke-dasharray="4 4" marker-end="url(#arr5)"/>
        <line x1="430" y1="130" x2="640" y2="156" stroke="#a78bfa" stroke-dasharray="4 4" marker-end="url(#arr5)"/>
      </svg>
    </div>
    <div class="code-wrap">
      <span class="code-label">Dart</span>
      <button class="copy-btn">Copy</button>
<pre><span class="k">import</span> <span class="s">'dart:math'</span> <span class="k">show</span> <span class="n">pi</span>;

<span class="k">abstract class</span> <span class="t">Shape</span> {
  <span class="k">double</span> <span class="k">get</span> <span class="n">area</span>;
  <span class="k">double</span> <span class="k">get</span> <span class="n">perimeter</span>;
  <span class="t">String</span> <span class="m">describe</span>() =&gt; <span class="s">'${runtimeType}: area=${area.toStringAsFixed(2)}'</span>;
}

<span class="k">mixin</span> <span class="t">Serializable</span> {
  <span class="t">Map</span>&lt;<span class="t">String</span>, <span class="k">dynamic</span>&gt; <span class="m">toJson</span>();
}

<span class="k">class</span> <span class="t">Circle</span> <span class="k">extends</span> <span class="t">Shape</span> <span class="k">with</span> <span class="t">Serializable</span> {
  <span class="k">final</span> <span class="t">double</span> <span class="n">radius</span>;
  <span class="k">const</span> <span class="t">Circle</span>({<span class="k">required</span> <span class="k">this</span>.<span class="n">radius</span>});
  <span class="t">Circle</span>.<span class="m">unit</span>() : <span class="n">radius</span> = <span class="num">1.0</span>;   <span class="c">// named constructor</span>
  <span class="k">factory</span> <span class="t">Circle</span>.<span class="m">fromJson</span>(<span class="t">Map</span>&lt;<span class="t">String</span>, <span class="k">dynamic</span>&gt; <span class="n">j</span>) =&gt;
      <span class="t">Circle</span>(<span class="n">radius</span>: (<span class="n">j</span>[<span class="s">'radius'</span>] <span class="k">as</span> <span class="t">num</span>).<span class="m">toDouble</span>());

  <span class="ann">@override</span> <span class="t">double</span> <span class="k">get</span> <span class="n">area</span> =&gt; <span class="n">pi</span> * <span class="n">radius</span> * <span class="n">radius</span>;
  <span class="ann">@override</span> <span class="t">double</span> <span class="k">get</span> <span class="n">perimeter</span> =&gt; <span class="num">2</span> * <span class="n">pi</span> * <span class="n">radius</span>;
  <span class="ann">@override</span> <span class="t">Map</span>&lt;<span class="t">String</span>, <span class="k">dynamic</span>&gt; <span class="m">toJson</span>() =&gt;
      {<span class="s">'type'</span>: <span class="s">'circle'</span>, <span class="s">'radius'</span>: <span class="n">radius</span>};
}

<span class="c">// Extension methods — add to existing types</span>
<span class="k">extension</span> <span class="t">StringUtils</span> <span class="k">on</span> <span class="t">String</span> {
  <span class="t">String</span> <span class="k">get</span> <span class="n">capitalized</span> =&gt;
      <span class="m">isEmpty</span> ? <span class="s">''</span> : <span class="k">this</span>[<span class="num">0</span>].<span class="m">toUpperCase</span>() + <span class="m">substring</span>(<span class="num">1</span>);
  <span class="t">bool</span> <span class="k">get</span> <span class="n">isEmail</span> =&gt; <span class="m">contains</span>(<span class="s">'@'</span>) &amp;&amp; <span class="m">contains</span>(<span class="s">'.'</span>);
  <span class="t">String</span> <span class="k">get</span> <span class="n">initials</span> =&gt;
      <span class="m">split</span>(<span class="s">' '</span>).<span class="m">map</span>((<span class="n">w</span>) =&gt; <span class="n">w</span>.<span class="m">isEmpty</span> ? <span class="s">''</span> : <span class="n">w</span>[<span class="num">0</span>]).<span class="m">join</span>(<span class="s">''</span>).<span class="m">toUpperCase</span>();
}

<span class="m">print</span>(<span class="s">'hello world'</span>.<span class="n">capitalized</span>); <span class="c">// Hello world</span>
<span class="m">print</span>(<span class="s">'John Doe'</span>.<span class="n">initials</span>);       <span class="c">// JD</span></pre>
    </div>
    <div class="info-box info-tip"><strong>💡 Mixin vs Interface vs Extends</strong><p>Use <code>extends</code> for a true is-a relationship. Use <code>implements</code> when you only want the contract (must implement all methods). Use <code>with</code> (mixins) for sharing behavior across unrelated classes — like a Serializable capability.</p></div>
  </div>

  <!-- 1.6 Async -->
  <div class="subsection" id="s1-6">
    <h3 style="color:var(--blue);">1.6 Async Programming</h3>
    <p>Dart runs on a <strong>single-threaded event loop</strong>, but async programming allows non-blocking I/O. The event loop processes two queues: the <strong>microtask queue</strong> (higher priority — Future.value, scheduleMicrotask) and the <strong>event queue</strong> (I/O, timers, user events). Microtasks always drain before the next event.</p>
    <p><strong>Future</strong> represents a single async value — uncompleted, completed with data, or completed with error. <strong>async/await</strong> is syntactic sugar over Future chains. <strong>Stream</strong> represents a sequence of async events over time. Single-subscription streams (like HTTP responses) differ from broadcast streams (like user events) which allow multiple listeners.</p>
    <div class="diagram">
      <svg viewBox="0 0 860 200" xmlns="http://www.w3.org/2000/svg">
        <defs><marker id="arr6" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="#8b949e" stroke-width="1.5" stroke-linecap="round"/></marker></defs>
        <!-- Call Stack -->
        <rect x="40" y="30" width="200" height="140" rx="10" fill="#0d1e3b" stroke="#60a5fa" stroke-width="1.5"/>
        <text x="140" y="55" font-family="JetBrains Mono" font-size="12" font-weight="700" fill="#60a5fa" text-anchor="middle">Call Stack</text>
        <rect x="58" y="65" width="164" height="30" rx="4" fill="#161b22" stroke="#30363d"/>
        <text x="140" y="85" font-family="JetBrains Mono" font-size="11" fill="#e6edf3" text-anchor="middle">main()</text>
        <rect x="58" y="100" width="164" height="30" rx="4" fill="#161b22" stroke="#30363d"/>
        <text x="140" y="120" font-family="JetBrains Mono" font-size="11" fill="#e6edf3" text-anchor="middle">fetchData()</text>
        <rect x="58" y="135" width="164" height="28" rx="4" fill="#1a1433" stroke="#a78bfa"/>
        <text x="140" y="154" font-family="JetBrains Mono" font-size="11" fill="#a78bfa" text-anchor="middle">await → suspends</text>
        <!-- Microtask -->
        <rect x="300" y="30" width="200" height="140" rx="10" fill="#1a1433" stroke="#a78bfa" stroke-width="1.5"/>
        <text x="400" y="55" font-family="JetBrains Mono" font-size="12" font-weight="700" fill="#a78bfa" text-anchor="middle">Microtask Queue</text>
        <text x="400" y="78" font-family="JetBrains Mono" font-size="10" fill="#8b949e" text-anchor="middle">HIGH PRIORITY</text>
        <rect x="318" y="88" width="164" height="28" rx="4" fill="#161b22" stroke="#30363d"/>
        <text x="400" y="107" font-family="JetBrains Mono" font-size="11" fill="#e6edf3" text-anchor="middle">Future.value callbacks</text>
        <rect x="318" y="122" width="164" height="28" rx="4" fill="#161b22" stroke="#30363d"/>
        <text x="400" y="141" font-family="JetBrains Mono" font-size="11" fill="#e6edf3" text-anchor="middle">scheduleMicrotask()</text>
        <!-- Event Queue -->
        <rect x="560" y="30" width="260" height="140" rx="10" fill="#0d2b22" stroke="#34d399" stroke-width="1.5"/>
        <text x="690" y="55" font-family="JetBrains Mono" font-size="12" font-weight="700" fill="#34d399" text-anchor="middle">Event Queue</text>
        <text x="690" y="75" font-family="JetBrains Mono" font-size="10" fill="#8b949e" text-anchor="middle">NORMAL PRIORITY</text>
        <rect x="578" y="85" width="224" height="25" rx="4" fill="#161b22" stroke="#30363d"/>
        <text x="690" y="102" font-family="JetBrains Mono" font-size="11" fill="#e6edf3" text-anchor="middle">Timer / Future.delayed</text>
        <rect x="578" y="115" width="224" height="25" rx="4" fill="#161b22" stroke="#30363d"/>
        <text x="690" y="132" font-family="JetBrains Mono" font-size="11" fill="#e6edf3" text-anchor="middle">I/O events (HTTP, File)</text>
        <rect x="578" y="145" width="224" height="22" rx="4" fill="#161b22" stroke="#30363d"/>
        <text x="690" y="160" font-family="JetBrains Mono" font-size="11" fill="#e6edf3" text-anchor="middle">User gestures / streams</text>
        <!-- arrows -->
        <line x1="240" y1="100" x2="300" y2="100" stroke="#a78bfa" stroke-width="1.5" marker-end="url(#arr6)"/>
        <line x1="500" y1="100" x2="560" y2="100" stroke="#34d399" stroke-width="1.5" marker-end="url(#arr6)"/>
      </svg>
    </div>
    <div class="code-wrap">
      <span class="code-label">Dart</span>
      <button class="copy-btn">Copy</button>
<pre><span class="c">// Future — single async value</span>
<span class="t">Future</span>&lt;<span class="t">String</span>&gt; <span class="m">fetchData</span>() <span class="k">async</span> {
  <span class="k">await</span> <span class="t">Future</span>.<span class="m">delayed</span>(<span class="t">Duration</span>(<span class="n">seconds</span>: <span class="num">2</span>));
  <span class="k">return</span> <span class="s">'Hello from server!'</span>;
}

<span class="c">// Error handling in async</span>
<span class="t">Future</span>&lt;<span class="t">User</span>&gt; <span class="m">getUser</span>(<span class="t">int</span> <span class="n">id</span>) <span class="k">async</span> {
  <span class="k">try</span> {
    <span class="k">final</span> <span class="n">response</span> = <span class="k">await</span> <span class="n">http</span>.<span class="m">get</span>(
      <span class="t">Uri</span>.<span class="m">parse</span>(<span class="s">'https://api.example.com/users/$id'</span>),
    );
    <span class="k">if</span> (<span class="n">response</span>.<span class="n">statusCode</span> == <span class="num">200</span>) {
      <span class="k">return</span> <span class="t">User</span>.<span class="m">fromJson</span>(<span class="m">jsonDecode</span>(<span class="n">response</span>.<span class="n">body</span>));
    }
    <span class="k">throw</span> <span class="t">HttpException</span>(<span class="s">'Status: ${response.statusCode}'</span>);
  } <span class="k">on</span> <span class="t">SocketException</span> {
    <span class="k">throw</span> <span class="t">NetworkException</span>(<span class="s">'No internet connection'</span>);
  } <span class="k">catch</span> (<span class="n">e</span>) {
    <span class="k">throw</span> <span class="t">UnexpectedException</span>(<span class="n">e</span>.<span class="m">toString</span>());
  }
}

<span class="c">// Stream — sequence of async values</span>
<span class="t">Stream</span>&lt;<span class="t">int</span>&gt; <span class="m">countdown</span>(<span class="t">int</span> <span class="n">from</span>) <span class="k">async</span>* {
  <span class="k">for</span> (<span class="t">int</span> <span class="n">i</span> = <span class="n">from</span>; <span class="n">i</span> &gt;= <span class="num">0</span>; <span class="n">i</span>--) {
    <span class="k">await</span> <span class="t">Future</span>.<span class="m">delayed</span>(<span class="t">Duration</span>(<span class="n">seconds</span>: <span class="num">1</span>));
    <span class="k">yield</span> <span class="n">i</span>; <span class="c">// emit value to stream</span>
  }
}

<span class="c">// Listen to stream</span>
<span class="m">countdown</span>(<span class="num">5</span>).<span class="m">listen</span>(
  (<span class="n">value</span>) =&gt; <span class="m">print</span>(<span class="s">'Count: $value'</span>),
  <span class="n">onDone</span>: () =&gt; <span class="m">print</span>(<span class="s">'Blast off!'</span>),
  <span class="n">onError</span>: (<span class="n">e</span>) =&gt; <span class="m">print</span>(<span class="s">'Error: $e'</span>),
);</pre>
    </div>
    <div class="info-box info-warn"><strong>⚠️ Async Gap &amp; Context Safety</strong><p>After an <code>await</code>, always check <code>if (mounted)</code> in StatefulWidget before using <code>context</code>. The widget may have been removed from the tree during the async operation, making the context invalid.</p></div>
  </div>
  <!-- 1.7 Memory Management -->
  <div class="subsection" id="s1-7">
    <h3 style="color:var(--blue);">1.7 Memory Management &amp; Garbage Collection</h3>
    <p>Dart uses an advanced, generational Garbage Collector (GC) designed specifically for Flutter's fast UI rendering architecture.</p>
    <div class="grid-2">
      <div class="card" style="background: rgba(96, 165, 250, 0.05); border-color: rgba(96, 165, 250, 0.2);">
        <div class="card-title" style="color:var(--blue);">New Space (Nursery)</div>
        <p>Most objects in Flutter (like local variables and pure UI Widgets that rebuild every frame) die young. The Nursery is small and cleaned out constantly in "scavenge" phases. This phase is extremely fast and specifically optimized to run in the micro-seconds of idle time between flutter frames, preventing any stuttering.</p>
      </div>
      <div class="card" style="background: rgba(167, 139, 250, 0.05); border-color: rgba(167, 139, 250, 0.2);">
        <div class="card-title" style="color:var(--purple);">Old Space</div>
        <p>Objects that survive a scavenge (like long-lived application state, singletons, or heavy cached images) are moved to the Old Space. Cleaning this uses a "Mark-Sweep" algorithm and is executed much less frequently because it is a heavier operation.</p>
      </div>
    </div>
    <div class="table-wrap"><table>
      <tr><th>Pro Tip</th><th>Why it matters for Memory</th></tr>
      <tr><td>Use <code>const</code> constructors</td><td><code>const</code> Widgets are allocated exactly once in a special immutable memory area. They never hit the Nursery and the GC never has to clean them up.</td></tr>
      <tr><td>Call <code>dispose()</code></td><td>Controllers (TextEditingController, AnimationController) wrap native C++ handlers. If you forget to dispose them, Dart's GC won't free the native memory, causing a leak.</td></tr>
      <tr><td>Avoid Global Variables</td><td>Globals stay in Old Space forever until the App dies. Prefer Scoped State.</td></tr>
    </table></div>
  </div>
</section>
'''

with open('flutter_notes.html', 'a') as f:
    f.write(s1)
print('Section 1 appended. Length:', len(s1))
