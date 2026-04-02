s11 = '''
<!-- ═══════════════════════════════════════════ SECTION 11 ═══ -->
<section class="section" id="s11">
  <div class="section-header">
    <div class="section-icon" style="background:var(--teal-bg);">📦</div>
    <div class="section-meta">
      <span class="section-badge" style="background:var(--teal-bg);color:var(--teal);">Advanced Dart</span>
      <div class="section-title" style="color:var(--teal);">Collections &amp; Iterables</div>
      <div class="section-subtitle">Deep dive into Lists, Sets, Maps, and higher-order functions</div>
    </div>
  </div>

  <!-- 11.1 Iterables & Higher-Order Functions -->
  <div class="subsection" id="s11-1">
    <h3 style="color:var(--teal);">11.1 Iterables &amp; Higher-Order Functions</h3>
    <p>In Dart, an <strong>Iterable</strong> is a collection of elements that can be accessed sequentially. Both <code>List</code> and <code>Set</code> implement <code>Iterable</code>. Maps don't directly implement it, but their <code>keys</code> and <code>values</code> properties are Iterables.</p>
    <p>Dart provides powerful higher-order functions that transform, filter, and aggregate iterables natively, replacing traditional `for` loops with concise, declarative operations.</p>
    
    <div class="table-wrap"><table>
      <tr><th>Method</th><th>Description</th><th>Equivalent to</th></tr>
      <tr><td><code style="background:var(--blue-bg);color:var(--blue);">map((e) => ...)</code></td><td>Transforms each element into a new element. Returns an Iterable.</td><td>JavaScript <code>map</code>, Python <code>map()</code></td></tr>
      <tr><td><code style="background:var(--teal-bg);color:var(--teal);">where((e) => condition)</code></td><td>Filters elements based on a true/false condition.</td><td>JavaScript <code>filter</code>, Python <code>filter()</code></td></tr>
      <tr><td><code style="background:var(--amber-bg);color:var(--amber);">reduce((a, b) => ...)</code></td><td>Combines all elements into a single value iteratively. Throws if empty.</td><td>JavaScript <code>reduce</code></td></tr>
      <tr><td><code style="background:var(--purple-bg);color:var(--purple);">fold(init, (a, b) => ...)</code></td><td>Like `reduce`, but with an initial value. Handles empty iterables safely.</td><td>Swift <code>reduce</code></td></tr>
      <tr><td><code style="background:var(--coral-bg);color:var(--coral);">any / every((e) => bool)</code></td><td>Checks if some (`any`) or all (`every`) elements match a condition.</td><td>JavaScript <code>some / every</code></td></tr>
    </table></div>

    <div class="code-wrap">
      <span class="code-label">Dart</span>
      <button class="copy-btn">Copy</button>
<pre><span class="k">final</span> <span class="t">List</span>&lt;<span class="t">int</span>&gt; <span class="n">numbers</span> = [<span class="num">1</span>, <span class="num">2</span>, <span class="num">3</span>, <span class="num">4</span>, <span class="num">5</span>, <span class="num">6</span>];

<span class="c">// map - Multiply every number by 2</span>
<span class="k">final</span> <span class="n">doubled</span> = <span class="n">numbers</span>.<span class="m">map</span>((<span class="n">n</span>) =&gt; <span class="n">n</span> * <span class="num">2</span>).<span class="m">toList</span>(); <span class="c">// [2, 4, 6, 8, 10, 12]</span>

<span class="c">// where - Filter only even numbers</span>
<span class="k">final</span> <span class="n">evens</span> = <span class="n">numbers</span>.<span class="m">where</span>((<span class="n">n</span>) =&gt; <span class="n">n</span> % <span class="num">2</span> == <span class="num">0</span>).<span class="m">toList</span>(); <span class="c">// [2, 4, 6]</span>

<span class="c">// reduce - Sum all numbers (no initial value)</span>
<span class="k">final</span> <span class="n">sum</span> = <span class="n">numbers</span>.<span class="m">reduce</span>((<span class="n">total</span>, <span class="n">element</span>) =&gt; <span class="n">total</span> + <span class="n">element</span>); <span class="c">// 21</span>

<span class="c">// fold - Sum with an initial value of 100</span>
<span class="k">final</span> <span class="n">totalSum</span> = <span class="n">numbers</span>.<span class="m">fold</span>(<span class="num">100</span>, (<span class="n">prev</span>, <span class="n">element</span>) =&gt; <span class="n">prev</span> + <span class="n">element</span>); <span class="c">// 121</span>

<span class="c">// Chaining iterable methods</span>
<span class="k">final</span> <span class="n">complex</span> = <span class="n">numbers</span>
    .<span class="m">where</span>((<span class="n">n</span>) =&gt; <span class="n">n</span> &gt; <span class="num">2</span>)             <span class="c">// [3, 4, 5, 6]</span>
    .<span class="m">map</span>((<span class="n">n</span>) =&gt; <span class="s">'Item $n'</span>)           <span class="c">// ['Item 3', 'Item 4', 'Item 5', 'Item 6']</span>
    .<span class="m">toList</span>();</pre>
    </div>
  </div>

  <!-- 11.2 Collection Control Flow -->
  <div class="subsection" id="s11-2">
    <h3 style="color:var(--teal);">11.2 Deep Dive: Collection `if`, `for`, and Spreads</h3>
    <p>Dart makes building collections incredibly fluid using control flow operators inside the collection literals themselves. They are heavily utilized in Flutter to dynamically generate lists of widgets without boilerplate mapping functions.</p>

    <div class="info-box info-tip"><strong>💡 Spread Operator (...)</strong><p>The spread operator unwraps an iterable and inserts its elements into the surrounding collection. The null-aware spread (<code>...?</code>) only spreads the iterable if it is not null.</p></div>

    <div class="code-wrap">
      <span class="code-label">Dart</span>
      <button class="copy-btn">Copy</button>
<pre><span class="c">// Spread Operator</span>
<span class="k">final</span> <span class="t">List</span>&lt;<span class="t">String</span>&gt; <span class="n">basics</span> = [<span class="s">'Dart'</span>, <span class="s">'Flutter'</span>];
<span class="t">List</span>&lt;<span class="t">String</span>&gt;? <span class="n">extensions</span> = <span class="k">null</span>;
<span class="k">final</span> <span class="n">allSkills</span> = [
  <span class="s">'HTML'</span>,
  ...<span class="n">basics</span>,               <span class="c">// Spreads: 'Dart', 'Flutter'</span>
  ...?<span class="n">extensions</span>,             <span class="c">// Null-aware spread, does nothing if null</span>
];

<span class="c">// Collection If &amp; For (Flutter Widget Scenario)</span>
<span class="k">final</span> <span class="t">bool</span> <span class="n">isAdmin</span> = <span class="k">true</span>;
<span class="k">final</span> <span class="t">List</span>&lt;<span class="t">User</span>&gt; <span class="n">users</span> = [<span class="t">User</span>(<span class="s">'Alice'</span>), <span class="t">User</span>(<span class="s">'Bob'</span>)];

<span class="k">final</span> <span class="n">widgetTree</span> = [
  <span class="t">HeaderWidget</span>(),
  
  <span class="c">// 1. Collection If</span>
  <span class="k">if</span> (<span class="n">isAdmin</span>)
    <span class="t">AdminPanelWidget</span>()
  <span class="k">else</span>
    <span class="t">UserPanelWidget</span>(),
    
  <span class="c">// 2. Collection For</span>
  <span class="k">for</span> (<span class="k">var</span> <span class="n">user</span> <span class="k">in</span> <span class="n">users</span>)
    <span class="t">UserTileWidget</span>(<span class="n">user</span>),
    
  <span class="t">FooterWidget</span>(),
];</pre>
    </div>
  </div>

  <!-- 11.3 Map Deep Dive -->
  <div class="subsection" id="s11-3">
    <h3 style="color:var(--teal);">11.3 Map Iteration &amp; Modification</h3>
    <p>Maps store Key-Value pairs. While you can iterate over `.keys` or `.values`, the `.entries` property is the most robust way to iterate over Maps, providing access to both key and value simultaneously via <code>MapEntry</code>.</p>
    
    <div class="code-wrap">
      <span class="code-label">Dart</span>
      <button class="copy-btn">Copy</button>
<pre><span class="k">final</span> <span class="t">Map</span>&lt;<span class="t">String</span>, <span class="t">int</span>&gt; <span class="n">inventory</span> = {
  <span class="s">'Apples'</span>: <span class="num">50</span>,
  <span class="s">'Oranges'</span>: <span class="num">20</span>,
  <span class="s">'Bananas'</span>: <span class="num">5</span>,
};

<span class="c">// Iterating through entries</span>
<span class="k">for</span> (<span class="k">var</span> <span class="n">entry</span> <span class="k">in</span> <span class="n">inventory</span>.<span class="m">entries</span>) {
  <span class="m">print</span>(<span class="s">'${entry.key} count: ${entry.value}'</span>);
}

<span class="c">// Safely put an item if it doesn't exist</span>
<span class="n">inventory</span>.<span class="m">putIfAbsent</span>(<span class="s">'Grapes'</span>, () =&gt; <span class="num">100</span>);

<span class="c">// Updating a value</span>
<span class="n">inventory</span>.<span class="m">update</span>(<span class="s">'Bananas'</span>, (<span class="n">value</span>) =&gt; <span class="n">value</span> + <span class="num">10</span>);

<span class="c">// Map from Iterable</span>
<span class="k">final</span> <span class="t">List</span>&lt;<span class="t">String</span>&gt; <span class="n">keys</span> = [<span class="s">'x'</span>, <span class="s">'y'</span>, <span class="s">'z'</span>];
<span class="k">final</span> <span class="n">coords</span> = <span class="t">Map</span>.<span class="m">fromIterable</span>(
  <span class="n">keys</span>,
  <span class="n">key</span>: (<span class="n">k</span>) =&gt; <span class="n">k</span>,
  <span class="n">value</span>: (<span class="n">k</span>) =&gt; <span class="num">0</span>,
); <span class="c">// {'x': 0, 'y': 0, 'z': 0}</span></pre>
    </div>
  </div>
</section>
'''

with open('flutter_notes.html', 'a') as f:
    f.write(s11)
print('Section 11 (Collections) appended. Len:', len(s11))
