
s15 = '''
<!-- ═══════════════════════════════════════════ SECTION 14 ═══ -->
<section class="section" id="s14">
  <div class="section-header">
    <div class="section-icon" style="background:var(--coral-bg);">🔀</div>
    <div class="section-meta">
      <span class="section-badge" style="background:var(--coral-bg);color:var(--coral);">Dart Core</span>
      <div class="section-title" style="color:var(--coral);">Conditions, Loops &amp; Operators</div>
      <div class="section-subtitle">Control flow mastery — if/else, switch, loops, break, assert, and all operators</div>
    </div>
  </div>

  <!-- 14.1 Conditions -->
  <div class="subsection" id="s14-1">
    <h3 style="color:var(--coral);">14.1 Conditions &amp; Branching</h3>
    <p>Dart supports the standard <strong>if / else if / else</strong> ladder, plus the powerful <strong>switch</strong> statement and Dart 3's new <strong>pattern matching switch expressions</strong>. Use <code>assert()</code> during development to catch invalid states early — assertions are stripped in production builds.</p>
    <div class="table-wrap"><table>
      <tr><th>Statement</th><th>Use Case</th><th>Dart 3 Upgrade</th></tr>
      <tr><td><code style="background:var(--coral-bg);color:var(--coral);">if / else</code></td><td>Any boolean condition</td><td>Same syntax</td></tr>
      <tr><td><code style="background:var(--blue-bg);color:var(--blue);">switch</code></td><td>Multiple values of same variable</td><td>Switch expressions + patterns</td></tr>
      <tr><td><code style="background:var(--amber-bg);color:var(--amber);">ternary ? :</code></td><td>Inline single condition</td><td>Same syntax</td></tr>
      <tr><td><code style="background:var(--purple-bg);color:var(--purple);">assert()</code></td><td>Dev-time invariant checking</td><td>Same — removed in release builds</td></tr>
    </table></div>
    <div class="code-wrap">
      <div class="mac-header">
        <div class="mac-dots"><div class="mac-dot-r"></div><div class="mac-dot-y"></div><div class="mac-dot-g"></div></div>
        <span class="code-label-mac">Dart</span>
        <button class="copy-btn">Copy</button>
      </div>
<pre><span class="c">// Classic if / else if / else</span>
<span class="t">int</span> <span class="n">score</span> = <span class="num">82</span>;
<span class="k">if</span> (<span class="n">score</span> >= <span class="num">90</span>) {
  <span class="m">print</span>(<span class="s">'Grade: A'</span>);
} <span class="k">else if</span> (<span class="n">score</span> >= <span class="num">75</span>) {
  <span class="m">print</span>(<span class="s">'Grade: B'</span>);
} <span class="k">else</span> {
  <span class="m">print</span>(<span class="s">'Grade: C'</span>);
}

<span class="c">// Ternary operator</span>
<span class="t">String</span> <span class="n">result</span> = <span class="n">score</span> >= <span class="num">50</span> ? <span class="s">'Pass'</span> : <span class="s">'Fail'</span>;

<span class="c">// Classic switch (Dart 2)</span>
<span class="t">String</span> <span class="n">day</span> = <span class="s">'Monday'</span>;
<span class="k">switch</span> (<span class="n">day</span>) {
  <span class="k">case</span> <span class="s">'Saturday'</span>:
  <span class="k">case</span> <span class="s">'Sunday'</span>:
    <span class="m">print</span>(<span class="s">'Weekend!'</span>);
    <span class="k">break</span>;
  <span class="k">default</span>:
    <span class="m">print</span>(<span class="s">'Weekday'</span>);
}

<span class="c">// Dart 3 — Switch Expression (returns a value)</span>
<span class="t">String</span> <span class="n">dayType</span> = <span class="k">switch</span> (<span class="n">day</span>) {
  <span class="s">'Saturday'</span> || <span class="s">'Sunday'</span> => <span class="s">'Weekend'</span>,
  _ => <span class="s">'Weekday'</span>,
};

<span class="c">// assert — throws AssertionError in debug mode only</span>
<span class="t">int</span> <span class="n">age</span> = <span class="num">25</span>;
<span class="m">assert</span>(<span class="n">age</span> >= <span class="num">0</span>, <span class="s">'Age cannot be negative!'</span>);</pre>
    </div>
    <div class="info-box info-tip"><strong>💡 Dart 3 Patterns</strong><p>Switch expressions in Dart 3 support destructuring — you can match on object shapes: <code>switch (shape) { Circle(radius: var r) => pi * r * r, Rectangle(width: var w, height: var h) => w * h }</code>. This eliminates verbose if/instanceof chains from Java-style code.</p></div>
  </div>

  <!-- 14.2 Loops -->
  <div class="subsection" id="s14-2">
    <h3 style="color:var(--coral);">14.2 Loops — for, while, forEach &amp; break/continue</h3>
    <p>Dart has four loop types. <strong>for</strong> (classic C-style), <strong>for-in</strong> (iterate iterables), <strong>while</strong> (condition-first), and <strong>do-while</strong> (body-first, always executes at least once). <code>break</code> exits the loop. <code>continue</code> skips to the next iteration.</p>
    <div class="flow-row">
      <div class="flow-box" style="background:var(--blue-bg);border-color:var(--blue);color:var(--blue);">for (init; cond; step)</div>
      <span class="flow-arrow">→</span>
      <div class="flow-box" style="background:var(--teal-bg);border-color:var(--teal);color:var(--teal);">for (item in list)</div>
      <span class="flow-arrow">→</span>
      <div class="flow-box" style="background:var(--purple-bg);border-color:var(--purple);color:var(--purple);">while (condition)</div>
      <span class="flow-arrow">→</span>
      <div class="flow-box" style="background:var(--amber-bg);border-color:var(--amber);color:var(--amber);">do { } while (cond)</div>
    </div>
    <div class="code-wrap">
      <div class="mac-header">
        <div class="mac-dots"><div class="mac-dot-r"></div><div class="mac-dot-y"></div><div class="mac-dot-g"></div></div>
        <span class="code-label-mac">Dart</span>
        <button class="copy-btn">Copy</button>
      </div>
<pre><span class="c">// Classic for loop</span>
<span class="k">for</span> (<span class="t">int</span> <span class="n">i</span> = <span class="num">0</span>; <span class="n">i</span> &lt; <span class="num">5</span>; <span class="n">i</span>++) {
  <span class="m">print</span>(<span class="s">'Index: $i'</span>);
}

<span class="c">// For-in (iterates any Iterable)</span>
<span class="t">List</span>&lt;<span class="t">String</span>&gt; <span class="n">colors</span> = [<span class="s">'red'</span>, <span class="s">'green'</span>, <span class="s">'blue'</span>];
<span class="k">for</span> (<span class="k">var</span> <span class="n">color</span> <span class="k">in</span> <span class="n">colors</span>) {
  <span class="m">print</span>(<span class="n">color</span>);
}

<span class="c">// forEach (functional, no break support)</span>
<span class="n">colors</span>.<span class="m">forEach</span>((<span class="n">c</span>) => <span class="m">print</span>(<span class="n">c</span>.<span class="m">toUpperCase</span>()));

<span class="c">// While loop</span>
<span class="t">int</span> <span class="n">count</span> = <span class="num">0</span>;
<span class="k">while</span> (<span class="n">count</span> &lt; <span class="num">3</span>) {
  <span class="m">print</span>(<span class="s">'count: $count'</span>);
  <span class="n">count</span>++;
}

<span class="c">// Do-while (guaranteed at least 1 execution)</span>
<span class="k">do</span> {
  <span class="m">print</span>(<span class="s">'Runs once even if false'</span>);
} <span class="k">while</span> (<span class="k">false</span>);

<span class="c">// break — exit early</span>
<span class="k">for</span> (<span class="t">int</span> <span class="n">i</span> = <span class="num">0</span>; <span class="n">i</span> &lt; <span class="num">10</span>; <span class="n">i</span>++) {
  <span class="k">if</span> (<span class="n">i</span> == <span class="num">5</span>) <span class="k">break</span>;  <span class="c">// stops at 5</span>
  <span class="m">print</span>(<span class="n">i</span>);
}

<span class="c">// continue — skip current iteration</span>
<span class="k">for</span> (<span class="t">int</span> <span class="n">i</span> = <span class="num">0</span>; <span class="n">i</span> &lt; <span class="num">6</span>; <span class="n">i</span>++) {
  <span class="k">if</span> (<span class="n">i</span> % <span class="num">2</span> == <span class="num">0</span>) <span class="k">continue</span>;  <span class="c">// skip even numbers</span>
  <span class="m">print</span>(<span class="n">i</span>);  <span class="c">// prints 1, 3, 5</span>
}</pre>
    </div>
    <div class="info-box info-warn"><strong>⚠️ forEach vs for-in in Flutter</strong><p>Prefer <code>for-in</code> over <code>.forEach()</code> in Flutter. The <code>forEach</code> callback cannot use <code>await</code>, <code>break</code>, or <code>continue</code>. Use <code>for-in</code> with <code>await</code> inside async functions when processing lists of futures sequentially.</p></div>
  </div>

  <!-- 14.3 Operators -->
  <div class="subsection" id="s14-3">
    <h3 style="color:var(--coral);">14.3 Dart Operators Deep Dive</h3>
    <p>Dart has all standard operators plus several unique ones. The <strong>cascade (..)</strong>, <strong>null-aware (??)</strong>, <strong>null-aware cascade (?..) </strong>, <strong>type test (is, is!, as)</strong>, and <strong>conditional access (?.)</strong> operators are especially important in real apps.</p>
    <div class="table-wrap"><table>
      <tr><th>Operator</th><th>Symbol</th><th>Example</th><th>Description</th></tr>
      <tr><td>Arithmetic</td><td><code>+  -  *  /  ~/  %</code></td><td><code>10 ~/ 3</code> → <code>3</code></td><td><code>~/</code> is integer division</td></tr>
      <tr><td>Comparison</td><td><code>==  !=  &lt;  &gt;  &lt;=  &gt;=</code></td><td><code>5 != 3</code> → <code>true</code></td><td>Returns bool</td></tr>
      <tr><td>Logical</td><td><code>&amp;&amp;  ||  !</code></td><td><code>a &amp;&amp; b</code></td><td>Short-circuit evaluation</td></tr>
      <tr><td>Null-aware</td><td><code>??  ??=  ?.</code></td><td><code>name ?? 'Guest'</code></td><td>Handle nulls safely</td></tr>
      <tr><td>Type test</td><td><code>is  is!  as</code></td><td><code>x is String</code></td><td>Runtime type checking</td></tr>
      <tr><td>Cascade</td><td><code>..  ?..</code></td><td><code>list..add(1)..add(2)</code></td><td>Chain calls on same object</td></tr>
      <tr><td>Spread</td><td><code>...  ...?</code></td><td><code>[...list1, ...list2]</code></td><td>Merge collections</td></tr>
    </table></div>
    <div class="code-wrap">
      <div class="mac-header">
        <div class="mac-dots"><div class="mac-dot-r"></div><div class="mac-dot-y"></div><div class="mac-dot-g"></div></div>
        <span class="code-label-mac">Dart</span>
        <button class="copy-btn">Copy</button>
      </div>
<pre><span class="c">// Integer division vs regular division</span>
<span class="m">print</span>(<span class="num">10</span> / <span class="num">3</span>);   <span class="c">// 3.333... (double)</span>
<span class="m">print</span>(<span class="num">10</span> ~/ <span class="num">3</span>);  <span class="c">// 3 (int, truncates)</span>
<span class="m">print</span>(<span class="num">10</span> % <span class="num">3</span>);   <span class="c">// 1 (modulus/remainder)</span>

<span class="c">// Type operators</span>
<span class="k">dynamic</span> <span class="n">val</span> = <span class="s">'Hello'</span>;
<span class="k">if</span> (<span class="n">val</span> <span class="k">is</span> <span class="t">String</span>) {           <span class="c">// Runtime type check — also promotes type</span>
  <span class="m">print</span>(<span class="n">val</span>.<span class="m">toUpperCase</span>());    <span class="c">// val is promoted to String here</span>
}
<span class="t">String</span> <span class="n">forced</span> = <span class="n">val</span> <span class="k">as</span> <span class="t">String</span>; <span class="c">// Cast — throws if wrong type</span>

<span class="c">// Null-aware assignment</span>
<span class="t">String</span>? <span class="n">username</span>;
<span class="n">username</span> ??= <span class="s">'Guest'</span>;  <span class="c">// Assigns only if null</span>
<span class="m">print</span>(<span class="n">username</span>);       <span class="c">// Guest</span>

<span class="c">// Cascade for building objects fluently</span>
<span class="k">final</span> <span class="n">paint</span> = <span class="t">Paint</span>()
  ..<span class="n">color</span> = <span class="t">Colors</span>.<span class="n">blue</span>
  ..<span class="n">strokeWidth</span> = <span class="num">2.0</span>
  ..<span class="n">style</span> = <span class="t">PaintingStyle</span>.<span class="n">fill</span>;

<span class="c">// Null-aware cascade (?..)</span>
<span class="t">Paint</span>? <span class="n">maybePaint</span>;
<span class="n">maybePaint</span>?..<span class="n">color</span> = <span class="t">Colors</span>.<span class="n">red</span>; <span class="c">// Safe — does nothing if null</span></pre>
    </div>
  </div>
</section>

<!-- ═══════════════════════════════════════════ SECTION 15 ═══ -->
<section class="section" id="s15">
  <div class="section-header">
    <div class="section-icon" style="background:var(--amber-bg);">📅</div>
    <div class="section-meta">
      <span class="section-badge" style="background:var(--amber-bg);color:var(--amber);">Dart Core</span>
      <div class="section-title" style="color:var(--amber);">Strings, DateTime &amp; Enums</div>
      <div class="section-subtitle">String manipulation, date/time formatting, and enhanced Dart 3 enums</div>
    </div>
  </div>

  <!-- 15.1 Strings -->
  <div class="subsection" id="s15-1">
    <h3 style="color:var(--amber);">15.1 String Methods &amp; Manipulation</h3>
    <p>Dart's <code>String</code> is an immutable sequence of UTF-16 code units. It has a rich set of built-in methods. String interpolation with <code>&#36;variable</code> and <code>&#36;{expression}</code> is the idiomatic way to build strings — never use concatenation (+) in loops as it creates new objects each time.</p>
    <div class="code-wrap">
      <div class="mac-header">
        <div class="mac-dots"><div class="mac-dot-r"></div><div class="mac-dot-y"></div><div class="mac-dot-g"></div></div>
        <span class="code-label-mac">Dart</span>
        <button class="copy-btn">Copy</button>
      </div>
<pre><span class="t">String</span> <span class="n">text</span> = <span class="s">'  Hello, Flutter World!  '</span>;

<span class="c">// Case &amp; whitespace</span>
<span class="m">print</span>(<span class="n">text</span>.<span class="m">trim</span>());           <span class="c">// 'Hello, Flutter World!'</span>
<span class="m">print</span>(<span class="n">text</span>.<span class="m">toUpperCase</span>());    <span class="c">// '  HELLO, FLUTTER WORLD!  '</span>
<span class="m">print</span>(<span class="n">text</span>.<span class="m">toLowerCase</span>());    <span class="c">// '  hello, flutter world!  '</span>

<span class="c">// Searching &amp; checking</span>
<span class="m">print</span>(<span class="n">text</span>.<span class="m">contains</span>(<span class="s">'Flutter'</span>));        <span class="c">// true</span>
<span class="m">print</span>(<span class="n">text</span>.<span class="m">startsWith</span>(<span class="s">'  Hello'</span>));      <span class="c">// true</span>
<span class="m">print</span>(<span class="n">text</span>.<span class="m">endsWith</span>(<span class="s">'!'</span>));             <span class="c">// false (trailing spaces)</span>
<span class="m">print</span>(<span class="n">text</span>.<span class="m">indexOf</span>(<span class="s">'Flutter'</span>));        <span class="c">// 9 (char position)</span>

<span class="c">// Slicing &amp; replacing</span>
<span class="m">print</span>(<span class="n">text</span>.<span class="m">substring</span>(<span class="num">2</span>, <span class="num">7</span>));           <span class="c">// 'Hello'</span>
<span class="m">print</span>(<span class="n">text</span>.<span class="m">replaceAll</span>(<span class="s">'Flutter'</span>, <span class="s">'Dart'</span>)); <span class="c">// replaces all occurrences</span>
<span class="m">print</span>(<span class="n">text</span>.<span class="m">split</span>(<span class="s">','</span>));               <span class="c">// ['  Hello', ' Flutter World!  ']</span>

<span class="c">// Interpolation — preferred over concatenation</span>
<span class="t">String</span> <span class="n">name</span> = <span class="s">'Shatrudhan'</span>;
<span class="t">int</span> <span class="n">version</span> = <span class="num">3</span>;
<span class="m">print</span>(<span class="s">'Hello $name, welcome to Flutter $version!'</span>);
<span class="m">print</span>(<span class="s">'Name has ${name.length} characters'</span>);  <span class="c">// Expression in braces</span>

<span class="c">// Multi-line strings</span>
<span class="t">String</span> <span class="n">multiLine</span> = <span class="s">'''
  Line 1
  Line 2
  Line 3
'''</span>;

<span class="c">// StringBuffer for efficient building</span>
<span class="k">final</span> <span class="n">sb</span> = <span class="t">StringBuffer</span>();
<span class="k">for</span> (<span class="t">int</span> <span class="n">i</span> = <span class="num">1</span>; <span class="n">i</span> &lt;= <span class="num">5</span>; <span class="n">i</span>++) {
  <span class="n">sb</span>.<span class="m">write</span>(<span class="s">'Item $i, '</span>);
}
<span class="m">print</span>(<span class="n">sb</span>.<span class="m">toString</span>()); <span class="c">// 'Item 1, Item 2, Item 3, Item 4, Item 5, '</span></pre>
    </div>
    <div class="info-box info-key"><strong>🔑 String Immutability</strong><p>Every <code>String</code> method returns a <strong>new</strong> String — the original is unchanged. Never concatenate inside loops (<code>str = str + item</code> creates N objects). Use <code>StringBuffer</code> or <code>list.join()</code> for loop-based string building.</p></div>
  </div>

  <!-- 15.2 DateTime -->
  <div class="subsection" id="s15-2">
    <h3 style="color:var(--amber);">15.2 DateTime &amp; Duration</h3>
    <p>Dart's <code>DateTime</code> class handles date and time. Use <code>DateTime.now()</code> for the current time, <code>DateTime.utc()</code> for UTC, and <code>DateTime.parse()</code> to parse ISO 8601 strings. <code>Duration</code> represents a span of time and is used for arithmetic on <code>DateTime</code> objects.</p>
    <div class="code-wrap">
      <div class="mac-header">
        <div class="mac-dots"><div class="mac-dot-r"></div><div class="mac-dot-y"></div><div class="mac-dot-g"></div></div>
        <span class="code-label-mac">Dart</span>
        <button class="copy-btn">Copy</button>
      </div>
<pre><span class="c">// Creating DateTime objects</span>
<span class="k">final</span> <span class="n">now</span> = <span class="t">DateTime</span>.<span class="m">now</span>();
<span class="k">final</span> <span class="n">specific</span> = <span class="t">DateTime</span>(<span class="num">2024</span>, <span class="num">4</span>, <span class="num">6</span>, <span class="num">10</span>, <span class="num">30</span>); <span class="c">// April 6, 2024 at 10:30</span>
<span class="k">final</span> <span class="n">fromString</span> = <span class="t">DateTime</span>.<span class="m">parse</span>(<span class="s">'2024-04-06T10:30:00Z'</span>);
<span class="k">final</span> <span class="n">utcNow</span> = <span class="t">DateTime</span>.<span class="m">now</span>().<span class="m">toUtc</span>(); <span class="c">// Convert to UTC</span>

<span class="c">// Accessing parts</span>
<span class="m">print</span>(<span class="n">now</span>.<span class="n">year</span>);        <span class="c">// 2024</span>
<span class="m">print</span>(<span class="n">now</span>.<span class="n">month</span>);       <span class="c">// 4 (April)</span>
<span class="m">print</span>(<span class="n">now</span>.<span class="n">day</span>);         <span class="c">// current day</span>
<span class="m">print</span>(<span class="n">now</span>.<span class="n">weekday</span>);     <span class="c">// 1=Mon, 7=Sun</span>
<span class="m">print</span>(<span class="n">now</span>.<span class="n">hour</span>);        <span class="c">// 0-23</span>
<span class="m">print</span>(<span class="n">now</span>.<span class="n">millisecondsSinceEpoch</span>);<span class="c">// Unix timestamp in ms</span>

<span class="c">// Duration arithmetic</span>
<span class="k">final</span> <span class="n">tomorrow</span> = <span class="n">now</span>.<span class="m">add</span>(<span class="t">Duration</span>(<span class="n">days</span>: <span class="num">1</span>));
<span class="k">final</span> <span class="n">lastWeek</span> = <span class="n">now</span>.<span class="m">subtract</span>(<span class="t">Duration</span>(<span class="n">days</span>: <span class="num">7</span>));
<span class="k">final</span> <span class="n">inFiveHours</span> = <span class="n">now</span>.<span class="m">add</span>(<span class="t">Duration</span>(<span class="n">hours</span>: <span class="num">5</span>, <span class="n">minutes</span>: <span class="num">30</span>));

<span class="c">// Comparing dates</span>
<span class="m">print</span>(<span class="n">tomorrow</span>.<span class="m">isAfter</span>(<span class="n">now</span>));    <span class="c">// true</span>
<span class="m">print</span>(<span class="n">lastWeek</span>.<span class="m">isBefore</span>(<span class="n">now</span>));   <span class="c">// true</span>

<span class="c">// Difference between two dates</span>
<span class="k">final</span> <span class="n">diff</span> = <span class="n">tomorrow</span>.<span class="m">difference</span>(<span class="n">now</span>);
<span class="m">print</span>(<span class="n">diff</span>.<span class="n">inHours</span>);    <span class="c">// 24</span>
<span class="m">print</span>(<span class="n">diff</span>.<span class="n">inMinutes</span>);  <span class="c">// 1440</span>

<span class="c">// Formatting (use the 'intl' package for locale-aware formatting)</span>
<span class="c">// import 'package:intl/intl.dart';</span>
<span class="c">// final formatted = DateFormat('dd MMM yyyy').format(now); // '06 Apr 2024'</span>
<span class="c">// Basic ISO format without package:</span>
<span class="m">print</span>(<span class="n">now</span>.<span class="m">toIso8601String</span>()); <span class="c">// '2024-04-06T10:30:00.000'</span></pre>
    </div>
  </div>

  <!-- 15.3 Enums (Dart 3) -->
  <div class="subsection" id="s15-3">
    <h3 style="color:var(--amber);">15.3 Enhanced Enums (Dart 2.17+)</h3>
    <p>Dart's enhanced enums are far more powerful than those in most other languages. They can have <strong>fields, constructors, methods, and implement interfaces/mixins</strong>. This lets you attach data and behavior directly to enum values — eliminating helper maps and switch statements.</p>
    <div class="code-wrap">
      <div class="mac-header">
        <div class="mac-dots"><div class="mac-dot-r"></div><div class="mac-dot-y"></div><div class="mac-dot-g"></div></div>
        <span class="code-label-mac">Dart</span>
        <button class="copy-btn">Copy</button>
      </div>
<pre><span class="c">// Basic enum</span>
<span class="k">enum</span> <span class="t">Status</span> { <span class="n">loading</span>, <span class="n">success</span>, <span class="n">error</span> }

<span class="c">// Enhanced enum with fields + methods (Dart 2.17+)</span>
<span class="k">enum</span> <span class="t">Planet</span> {
  mercury(<span class="n">mass</span>: <span class="num">3.303e+23</span>, <span class="n">radius</span>: <span class="num">2.4397e6</span>),
  venus(<span class="n">mass</span>: <span class="num">4.869e+24</span>, <span class="n">radius</span>: <span class="num">6.0518e6</span>),
  earth(<span class="n">mass</span>: <span class="num">5.976e+24</span>, <span class="n">radius</span>: <span class="num">6.37814e6</span>);

  <span class="k">const</span> <span class="t">Planet</span>({<span class="k">required</span> <span class="k">this</span>.<span class="n">mass</span>, <span class="k">required</span> <span class="k">this</span>.<span class="n">radius</span>});

  <span class="k">final</span> <span class="t">double</span> <span class="n">mass</span>;
  <span class="k">final</span> <span class="t">double</span> <span class="n">radius</span>;

  <span class="c">// Computed property</span>
  <span class="t">double</span> <span class="k">get</span> <span class="n">surfaceGravity</span> {
    <span class="k">const</span> <span class="n">G</span> = <span class="num">6.67430e-11</span>;
    <span class="k">return</span> <span class="n">G</span> * <span class="n">mass</span> / (<span class="n">radius</span> * <span class="n">radius</span>);
  }

  <span class="c">// Method</span>
  <span class="t">double</span> <span class="m">surfaceWeight</span>(<span class="t">double</span> <span class="n">otherMass</span>) => <span class="n">otherMass</span> * <span class="n">surfaceGravity</span>;
}

<span class="k">void</span> <span class="m">main</span>() {
  <span class="k">const</span> <span class="t">double</span> <span class="n">weight</span> = <span class="num">75.0</span>; <span class="c">// kg</span>
  <span class="m">print</span>(<span class="t">Planet</span>.<span class="n">earth</span>.<span class="m">surfaceWeight</span>(<span class="n">weight</span>)); <span class="c">// ~735 Newtons</span>

  <span class="c">// Enum in switch expression (exhaustive — no default needed)</span>
  <span class="t">Status</span> <span class="n">status</span> = <span class="t">Status</span>.<span class="n">loading</span>;
  <span class="t">String</span> <span class="n">label</span> = <span class="k">switch</span> (<span class="n">status</span>) {
    <span class="t">Status</span>.<span class="n">loading</span> => <span class="s">'Loading...'</span>,
    <span class="t">Status</span>.<span class="n">success</span> => <span class="s">'Done!'</span>,
    <span class="t">Status</span>.<span class="n">error</span>   => <span class="s">'Error!'</span>,
  };

  <span class="c">// Enum utilities</span>
  <span class="m">print</span>(<span class="t">Status</span>.<span class="n">loading</span>.<span class="n">name</span>);    <span class="c">// 'loading'</span>
  <span class="m">print</span>(<span class="t">Status</span>.<span class="n">values</span>);          <span class="c">// [Status.loading, Status.success, Status.error]</span>
  <span class="m">print</span>(<span class="t">Status</span>.<span class="n">values</span>.<span class="m">byName</span>(<span class="s">'error'</span>)); <span class="c">// Status.error</span>
}</pre>
    </div>
    <div class="info-box info-tip"><strong>💡 Enums in Flutter State Management</strong><p>Use enums to model widget/screen states (instead of booleans like <code>isLoading</code>, <code>hasError</code>). A single <code>Status</code> enum with <code>idle | loading | success | failure</code> makes your state exhaustive, explicit, and impossible to be in two states at once. Riverpod's <code>AsyncValue</code> is built on this exact pattern.</p></div>
  </div>
</section>

<!-- ═══════════════════════════════════════════ SECTION 16 ═══ -->
<section class="section" id="s16">
  <div class="section-header">
    <div class="section-icon" style="background:var(--purple-bg);">🎨</div>
    <div class="section-meta">
      <span class="section-badge" style="background:var(--purple-bg);color:var(--purple);">Flutter UI</span>
      <div class="section-title" style="color:var(--purple);">Animations &amp; Adaptive Design</div>
      <div class="section-subtitle">Implicit animations, explicit controllers, Hero, and responsive/adaptive layouts</div>
    </div>
  </div>

  <!-- 16.1 Animation Types -->
  <div class="subsection" id="s16-1">
    <h3 style="color:var(--purple);">16.1 Animation System Overview</h3>
    <p>Flutter has two levels of animations. <strong>Implicit animations</strong> (AnimatedContainer, AnimatedOpacity, TweenAnimationBuilder) manage their own <code>AnimationController</code> — just set the new value and they animate. <strong>Explicit animations</strong> (AnimationController + AnimatedBuilder) give you full control — you drive the timeline manually.</p>
    <div class="table-wrap"><table>
      <tr><th>Type</th><th>Widget</th><th>When to Use</th></tr>
      <tr><td><strong>Implicit</strong></td><td><code>AnimatedContainer</code>, <code>AnimatedOpacity</code>, <code>AnimatedPadding</code>, <code>AnimatedAlign</code></td><td>Simple property changes triggered by setState</td></tr>
      <tr><td><strong>Tween Builder</strong></td><td><code>TweenAnimationBuilder</code></td><td>Custom tween on any widget without a controller</td></tr>
      <tr><td><strong>Explicit</strong></td><td><code>AnimationController</code> + <code>AnimatedBuilder</code></td><td>Repeating, sequenced, or manually triggered anims</td></tr>
      <tr><td><strong>Hero</strong></td><td><code>Hero</code></td><td>Shared element transition between screens</td></tr>
      <tr><td><strong>Page Route</strong></td><td><code>PageRouteBuilder</code></td><td>Custom screen transition animations</td></tr>
    </table></div>
    <div class="code-wrap">
      <div class="mac-header">
        <div class="mac-dots"><div class="mac-dot-r"></div><div class="mac-dot-y"></div><div class="mac-dot-g"></div></div>
        <span class="code-label-mac">Dart — Implicit vs Explicit</span>
        <button class="copy-btn">Copy</button>
      </div>
<pre><span class="c">// IMPLICIT — AnimatedContainer (easiest)</span>
<span class="k">class</span> <span class="t">PulsingBox</span> <span class="k">extends</span> <span class="t">StatefulWidget</span> {
  <span class="k">const</span> <span class="t">PulsingBox</span>({<span class="k">super</span>.<span class="n">key</span>});
  <span class="ann">@override</span>
  <span class="t">State</span>&lt;<span class="t">PulsingBox</span>&gt; <span class="m">createState</span>() => _PulsingBoxState();
}

<span class="k">class</span> <span class="t">_PulsingBoxState</span> <span class="k">extends</span> <span class="t">State</span>&lt;<span class="t">PulsingBox</span>&gt; {
  <span class="t">bool</span> <span class="n">_big</span> = <span class="k">false</span>;

  <span class="ann">@override</span>
  <span class="t">Widget</span> <span class="m">build</span>(<span class="t">BuildContext</span> <span class="n">context</span>) {
    <span class="k">return</span> <span class="t">GestureDetector</span>(
      <span class="n">onTap</span>: () => <span class="m">setState</span>(() => <span class="n">_big</span> = !<span class="n">_big</span>),
      <span class="n">child</span>: <span class="t">AnimatedContainer</span>(   <span class="c">// Auto-animates on property change</span>
        <span class="n">duration</span>: <span class="k">const</span> <span class="t">Duration</span>(<span class="n">milliseconds</span>: <span class="num">300</span>),
        <span class="n">curve</span>: <span class="t">Curves</span>.<span class="n">easeInOut</span>,
        <span class="n">width</span>: <span class="n">_big</span> ? <span class="num">200</span> : <span class="num">100</span>,
        <span class="n">height</span>: <span class="n">_big</span> ? <span class="num">200</span> : <span class="num">100</span>,
        <span class="n">color</span>: <span class="n">_big</span> ? <span class="t">Colors</span>.<span class="n">purple</span> : <span class="t">Colors</span>.<span class="n">blue</span>,
      ),
    );
  }
}

<span class="c">// EXPLICIT — AnimationController (full control)</span>
<span class="k">class</span> <span class="t">SpinningIcon</span> <span class="k">extends</span> <span class="t">StatefulWidget</span> {
  <span class="k">const</span> <span class="t">SpinningIcon</span>({<span class="k">super</span>.<span class="n">key</span>});
  <span class="ann">@override</span>
  <span class="t">State</span>&lt;<span class="t">SpinningIcon</span>&gt; <span class="m">createState</span>() => _SpinningIconState();
}

<span class="k">class</span> <span class="t">_SpinningIconState</span> <span class="k">extends</span> <span class="t">State</span>&lt;<span class="t">SpinningIcon</span>&gt;
    <span class="k">with</span> <span class="t">SingleTickerProviderStateMixin</span> {
  <span class="k">late</span> <span class="t">AnimationController</span> <span class="n">_ctrl</span>;

  <span class="ann">@override</span>
  <span class="k">void</span> <span class="m">initState</span>() {
    <span class="k">super</span>.<span class="m">initState</span>();
    <span class="n">_ctrl</span> = <span class="t">AnimationController</span>(
      <span class="n">vsync</span>: <span class="k">this</span>,
      <span class="n">duration</span>: <span class="k">const</span> <span class="t">Duration</span>(<span class="n">seconds</span>: <span class="num">2</span>),
    )..<span class="m">repeat</span>();  <span class="c">// Spin forever</span>
  }

  <span class="ann">@override</span>
  <span class="k">void</span> <span class="m">dispose</span>() {
    <span class="n">_ctrl</span>.<span class="m">dispose</span>(); <span class="c">// MUST dispose!</span>
    <span class="k">super</span>.<span class="m">dispose</span>();
  }

  <span class="ann">@override</span>
  <span class="t">Widget</span> <span class="m">build</span>(<span class="t">BuildContext</span> <span class="n">context</span>) {
    <span class="k">return</span> <span class="t">AnimatedBuilder</span>(
      <span class="n">animation</span>: <span class="n">_ctrl</span>,
      <span class="n">builder</span>: (<span class="n">context</span>, <span class="n">child</span>) {
        <span class="k">return</span> <span class="t">Transform</span>.<span class="m">rotate</span>(
          <span class="n">angle</span>: <span class="n">_ctrl</span>.<span class="n">value</span> * <span class="num">6.28</span>, <span class="c">// 2*pi radians</span>
          <span class="n">child</span>: <span class="n">child</span>,
        );
      },
      <span class="n">child</span>: <span class="k">const</span> <span class="t">Icon</span>(<span class="t">Icons</span>.<span class="n">settings</span>, <span class="n">size</span>: <span class="num">48</span>),
    );
  }
}</pre>
    </div>
  </div>

  <!-- 16.2 Adaptive & Responsive -->
  <div class="subsection" id="s16-2">
    <h3 style="color:var(--purple);">16.2 Adaptive &amp; Responsive Design</h3>
    <p><strong>Responsive</strong> means the layout adapts to different screen <em>sizes</em>. <strong>Adaptive</strong> means the UI adapts to different <em>platforms</em> (iOS vs Android — using Cupertino vs Material widgets). Use <code>MediaQuery</code> and <code>LayoutBuilder</code> for responsive, and <code>Platform.isIOS</code> or <code>defaultTargetPlatform</code> for adaptive.</p>
    <div class="grid-2">
      <div class="card glass glow-hover" style="border-top: 3px solid var(--blue);">
        <div class="card-title" style="color:var(--blue);">MediaQuery</div>
        <p>Provides screen dimensions and pixel density. Available anywhere in the widget tree via context.</p>
<pre style="background:transparent;border:none;margin-top:10px;"><code style="color:var(--muted);"><span class="k">final</span> <span class="n">size</span> = <span class="t">MediaQuery</span>
  .<span class="m">of</span>(<span class="n">context</span>).<span class="n">size</span>;
<span class="k">final</span> <span class="n">w</span> = <span class="n">size</span>.<span class="n">width</span>;   <span class="c">// screen width</span>
<span class="k">final</span> <span class="n">h</span> = <span class="n">size</span>.<span class="n">height</span>;  <span class="c">// screen height</span></code></pre>
      </div>
      <div class="card glass glow-hover" style="border-top: 3px solid var(--purple);">
        <div class="card-title" style="color:var(--purple);">LayoutBuilder</div>
        <p>Provides parent constraints — use for widgets that need to know their own available space.</p>
<pre style="background:transparent;border:none;margin-top:10px;"><code style="color:var(--muted);"><span class="t">LayoutBuilder</span>(
  <span class="n">builder</span>: (<span class="n">ctx</span>, <span class="n">constraints</span>) {
    <span class="k">if</span> (<span class="n">constraints</span>.<span class="n">maxWidth</span> &gt; <span class="num">600</span>) {
      <span class="k">return</span> <span class="t">WideLayout</span>();
    }
    <span class="k">return</span> <span class="t">NarrowLayout</span>();
  },
)</code></pre>
      </div>
    </div>
    <div class="code-wrap">
      <div class="mac-header">
        <div class="mac-dots"><div class="mac-dot-r"></div><div class="mac-dot-y"></div><div class="mac-dot-g"></div></div>
        <span class="code-label-mac">Dart — Responsive Navigation + Adaptive Widget</span>
        <button class="copy-btn">Copy</button>
      </div>
<pre><span class="c">// Responsive: Switch navigation type based on screen width</span>
<span class="t">Widget</span> <span class="m">build</span>(<span class="t">BuildContext</span> <span class="n">context</span>) {
  <span class="k">final</span> <span class="n">width</span> = <span class="t">MediaQuery</span>.<span class="m">sizeOf</span>(<span class="n">context</span>).<span class="n">width</span>; <span class="c">// sizeOf is more efficient</span>

  <span class="k">return</span> width &gt; <span class="num">800</span>
    ? <span class="t">Row</span>(<span class="n">children</span>: [<span class="t">SideNavigationRail</span>(), <span class="t">Expanded</span>(<span class="n">child</span>: <span class="t">Content</span>())])
    : <span class="t">Scaffold</span>(<span class="n">bottomNavigationBar</span>: <span class="t">BottomNav</span>(), <span class="n">body</span>: <span class="t">Content</span>());
}

<span class="c">// Adaptive: Render platform-specific widget</span>
<span class="k">import</span> <span class="s">'dart:io'</span>;

<span class="t">Widget</span> <span class="m">buildButton</span>(<span class="t">String</span> <span class="n">label</span>, <span class="t">VoidCallback</span> <span class="n">onPressed</span>) {
  <span class="k">if</span> (<span class="t">Platform</span>.<span class="n">isIOS</span>) {
    <span class="k">return</span> <span class="t">CupertinoButton</span>(<span class="n">onPressed</span>: <span class="n">onPressed</span>, <span class="n">child</span>: <span class="t">Text</span>(<span class="n">label</span>));
  } <span class="k">else</span> {
    <span class="k">return</span> <span class="t">ElevatedButton</span>(<span class="n">onPressed</span>: <span class="n">onPressed</span>, <span class="n">child</span>: <span class="t">Text</span>(<span class="n">label</span>));
  }
}

<span class="c">// SafeArea — respects notches, system bars</span>
<span class="t">Scaffold</span>(
  <span class="n">body</span>: <span class="t">SafeArea</span>(   <span class="c">// Pads away from notch and status bar</span>
    <span class="n">child</span>: <span class="t">MyContent</span>(),
  ),
);</pre>
    </div>
    <div class="info-box info-key"><strong>🔑 MediaQuery.sizeOf vs .of</strong><p>Use <code>MediaQuery.sizeOf(context)</code> instead of <code>MediaQuery.of(context).size</code> in Flutter 3.7+. The <code>sizeOf</code> method only rebuilds the widget when the size changes — not for every MediaQuery property change — dramatically reducing unnecessary rebuilds.</p></div>
  </div>
</section>
'''

# Append to the HTML file before the closing </main> tag
with open('flutter_notes.html', 'r') as f:
    content = f.read()

# Also update the TOC to include sections 11-16
old_toc = '''        <a class="toc-item" href="#s10"><span class="toc-num">10</span><span class="toc-label">Clean Architecture</span></a>'''
new_toc = '''        <a class="toc-item" href="#s10"><span class="toc-num">10</span><span class="toc-label">Clean Architecture</span></a>
        <a class="toc-item" href="#s11"><span class="toc-num">11</span><span class="toc-label">Collections Deep Dive</span></a>
        <a class="toc-item" href="#s12"><span class="toc-num">12</span><span class="toc-label">OOP Details &amp; File I/O</span></a>
        <a class="toc-item" href="#s13"><span class="toc-num">13</span><span class="toc-label">Async Deep Dive</span></a>
        <a class="toc-item" href="#s14"><span class="toc-num">14</span><span class="toc-label">Conditions &amp; Operators</span></a>
        <a class="toc-item" href="#s15"><span class="toc-num">15</span><span class="toc-label">Strings, DateTime &amp; Enums</span></a>
        <a class="toc-item" href="#s16"><span class="toc-num">16</span><span class="toc-label">Animations &amp; Adaptive UI</span></a>'''

content = content.replace(old_toc, new_toc)

# Insert new section before </main>
content = content.replace('  </main>', s15 + '\n  </main>')

with open('flutter_notes.html', 'w') as f:
    f.write(content)

print('Sections 14, 15, 16 added + TOC updated. New length:', len(content))
