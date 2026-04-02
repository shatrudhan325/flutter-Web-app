
s2 = '''
<!-- ═══════════════════════════════════════════ SECTION 2 ═══ -->
<section class="section" id="s2">
  <div class="section-header">
    <div class="section-icon" style="background:var(--purple-bg);">🟣</div>
    <div class="section-meta">
      <span class="section-badge" style="background:var(--purple-bg);color:var(--purple);">Beginner</span>
      <div class="section-title" style="color:var(--purple);">Flutter Fundamentals</div>
      <div class="section-subtitle">Architecture, widget tree, stateless vs stateful, and BuildContext</div>
    </div>
  </div>

  <!-- 2.1 How Flutter Works -->
  <div class="subsection" id="s2-1">
    <h3 style="color:var(--purple);">2.1 How Flutter Works</h3>
    <p>Flutter is a <strong>multi-platform UI toolkit</strong> that does not rely on native UI components. Instead it uses its own high-performance rendering engine (<strong>Skia</strong> or the newer <strong>Impeller</strong>) to paint every pixel directly onto a canvas. This means Flutter widgets look and behave identically on every platform — Android, iOS, Web, Windows, macOS, and Linux.</p>
    <p>The framework is organized into four conceptual layers. Your Dart code sits at the top. The <strong>Flutter Framework</strong> provides Material, Cupertino, and the base widget library. The <strong>Flutter Engine</strong> handles rendering, text layout, and the Dart runtime. The <strong>Platform Embedder</strong> integrates with each native OS to provide the canvas, input events, and plugin channels.</p>
    <p>In <strong>debug mode</strong>, Dart uses JIT (Just-In-Time) compilation for hot reload. In <strong>release mode</strong>, Dart AOT (Ahead-Of-Time) compiles to native machine code — producing fast, small binaries with no interpreter overhead.</p>
    <div class="diagram">
      <svg viewBox="0 0 860 300" xmlns="http://www.w3.org/2000/svg">
        <defs><marker id="arr21" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="#8b949e" stroke-width="1.5" stroke-linecap="round"/></marker></defs>
        <rect x="40" y="20" width="780" height="50" rx="8" fill="#1a1433" stroke="#a78bfa" stroke-width="2"/>
        <text x="430" y="42" font-family="JetBrains Mono" font-size="13" font-weight="700" fill="#a78bfa" text-anchor="middle">Your Dart Code</text>
        <text x="430" y="60" font-family="JetBrains Mono" font-size="10" fill="#8b949e" text-anchor="middle">Widgets · State · Business Logic · Routes</text>
        <rect x="40" y="84" width="780" height="50" rx="8" fill="#0d1e3b" stroke="#60a5fa" stroke-width="1.5"/>
        <text x="430" y="106" font-family="JetBrains Mono" font-size="13" font-weight="700" fill="#60a5fa" text-anchor="middle">Flutter Framework</text>
        <text x="430" y="124" font-family="JetBrains Mono" font-size="10" fill="#8b949e" text-anchor="middle">Material · Cupertino · Widgets · Animation · Gestures · Rendering</text>
        <rect x="40" y="148" width="780" height="50" rx="8" fill="#0d2b22" stroke="#34d399" stroke-width="1.5"/>
        <text x="430" y="170" font-family="JetBrains Mono" font-size="13" font-weight="700" fill="#34d399" text-anchor="middle">Flutter Engine</text>
        <text x="430" y="188" font-family="JetBrains Mono" font-size="10" fill="#8b949e" text-anchor="middle">Skia / Impeller · Dart Runtime · Text · Plugin APIs · Compositor</text>
        <rect x="40" y="212" width="780" height="50" rx="8" fill="#2b1d0d" stroke="#fbbf24" stroke-width="1.5"/>
        <text x="430" y="234" font-family="JetBrains Mono" font-size="13" font-weight="700" fill="#fbbf24" text-anchor="middle">Platform Embedder</text>
        <text x="430" y="252" font-family="JetBrains Mono" font-size="10" fill="#8b949e" text-anchor="middle">Android (Java/Kotlin) · iOS (ObjC/Swift) · Web · Windows · macOS · Linux</text>
        <rect x="40" y="276" width="780" height="18" rx="6" fill="#161b22" stroke="#30363d"/>
        <text x="430" y="289" font-family="JetBrains Mono" font-size="10" fill="#8b949e" text-anchor="middle">Native OS Canvas / GPU</text>
        <line x1="430" y1="70" x2="430" y2="84" stroke="#8b949e" stroke-width="1.5" marker-end="url(#arr21)"/>
        <line x1="430" y1="134" x2="430" y2="148" stroke="#8b949e" stroke-width="1.5" marker-end="url(#arr21)"/>
        <line x1="430" y1="198" x2="430" y2="212" stroke="#8b949e" stroke-width="1.5" marker-end="url(#arr21)"/>
        <line x1="430" y1="262" x2="430" y2="276" stroke="#8b949e" stroke-width="1.5" marker-end="url(#arr21)"/>
      </svg>
    </div>
    <div class="info-box info-tip"><strong>💡 Impeller — The Future Renderer</strong><p>Impeller replaces Skia as Flutter's default renderer on iOS (stable) and Android (beta). It pre-compiles shaders at build time to eliminate shader compilation jank — a common complaint with Skia's on-demand shader compilation.</p></div>
    <div class="flow-row">
      <div class="flow-box" style="background:var(--purple-bg);border-color:var(--purple);color:var(--purple);">Debug: JIT + Hot Reload</div>
      <span class="flow-arrow">|</span>
      <div class="flow-box" style="background:var(--teal-bg);border-color:var(--teal);color:var(--teal);">Profile: AOT + DevTools</div>
      <span class="flow-arrow">|</span>
      <div class="flow-box" style="background:var(--amber-bg);border-color:var(--amber);color:var(--amber);">Release: AOT + Obfuscated</div>
    </div>
  </div>

  <!-- 2.2 Widget Tree -->
  <div class="subsection" id="s2-2">
    <h3 style="color:var(--purple);">2.2 Widget Tree &amp; Three Trees</h3>
    <p>Flutter has three distinct trees that work in concert. The <strong>Widget tree</strong> is immutable — widgets are lightweight configuration objects. When <code>setState()</code> is called, Flutter rebuilds the widget tree from that point down. The <strong>Element tree</strong> is the live instance tree — Elements persist across rebuilds and reconcile the old widget tree with the new one. <strong>RenderObjects</strong> do the actual layout and painting.</p>
    <p>This architecture means: rebuilding widgets is cheap (they're just Dart objects), but relayout and repaint are expensive. Flutter only repaints when the render object truly needs to change. <strong>BuildContext</strong> is actually the Element — it represents the widget's position in the tree.</p>
    <div class="diagram">
      <svg viewBox="0 0 860 280" xmlns="http://www.w3.org/2000/svg">
        <defs><marker id="arr22" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="#8b949e" stroke-width="1.5" stroke-linecap="round"/></marker></defs>
        <!-- MaterialApp -->
        <rect x="310" y="10" width="240" height="44" rx="8" fill="#2b1d0d" stroke="#fbbf24" stroke-width="2"/>
        <text x="430" y="29" font-family="JetBrains Mono" font-size="12" font-weight="700" fill="#fbbf24" text-anchor="middle">MaterialApp</text>
        <text x="430" y="46" font-family="JetBrains Mono" font-size="10" fill="#8b949e" text-anchor="middle">scaffold: amber</text>
        <!-- Scaffold -->
        <rect x="310" y="74" width="240" height="40" rx="8" fill="#2b1d0d" stroke="#fbbf24" stroke-width="1.5"/>
        <text x="430" y="90" font-family="JetBrains Mono" font-size="12" font-weight="700" fill="#fbbf24" text-anchor="middle">Scaffold</text>
        <text x="430" y="106" font-family="JetBrains Mono" font-size="10" fill="#8b949e" text-anchor="middle">appBar · body · FAB</text>
        <!-- AppBar -->
        <rect x="100" y="144" width="200" height="40" rx="8" fill="#0d2b22" stroke="#34d399" stroke-width="1.5"/>
        <text x="200" y="160" font-family="JetBrains Mono" font-size="12" font-weight="700" fill="#34d399" text-anchor="middle">AppBar</text>
        <text x="200" y="176" font-family="JetBrains Mono" font-size="10" fill="#8b949e" text-anchor="middle">display: teal</text>
        <!-- Column -->
        <rect x="560" y="144" width="200" height="40" rx="8" fill="#0d2b22" stroke="#34d399" stroke-width="1.5"/>
        <text x="660" y="160" font-family="JetBrains Mono" font-size="12" font-weight="700" fill="#34d399" text-anchor="middle">Column</text>
        <text x="660" y="176" font-family="JetBrains Mono" font-size="10" fill="#8b949e" text-anchor="middle">layout: teal</text>
        <!-- Text AppBar -->
        <rect x="40" y="218" width="160" height="36" rx="8" fill="#161b22" stroke="#30363d" stroke-width="1.5"/>
        <text x="120" y="236" font-family="JetBrains Mono" font-size="11" fill="#60a5fa" text-anchor="middle">Text</text>
        <text x="120" y="250" font-family="JetBrains Mono" font-size="10" fill="#8b949e" text-anchor="middle">"Flutter Notes"</text>
        <!-- Text Col -->
        <rect x="470" y="218" width="140" height="36" rx="8" fill="#161b22" stroke="#30363d" stroke-width="1.5"/>
        <text x="540" y="236" font-family="JetBrains Mono" font-size="11" fill="#60a5fa" text-anchor="middle">Text</text>
        <text x="540" y="250" font-family="JetBrains Mono" font-size="10" fill="#8b949e" text-anchor="middle">"Welcome"</text>
        <!-- ElevatedButton -->
        <rect x="630" y="218" width="190" height="36" rx="8" fill="#1a1433" stroke="#a78bfa" stroke-width="1.5"/>
        <text x="725" y="236" font-family="JetBrains Mono" font-size="11" fill="#a78bfa" text-anchor="middle">ElevatedButton</text>
        <text x="725" y="250" font-family="JetBrains Mono" font-size="10" fill="#8b949e" text-anchor="middle">interactive: purple</text>
        <!-- lines -->
        <line x1="430" y1="54" x2="430" y2="74" stroke="#8b949e" stroke-dasharray="5 3" marker-end="url(#arr22)"/>
        <line x1="430" y1="114" x2="200" y2="144" stroke="#8b949e" stroke-dasharray="5 3" marker-end="url(#arr22)"/>
        <line x1="430" y1="114" x2="660" y2="144" stroke="#8b949e" stroke-dasharray="5 3" marker-end="url(#arr22)"/>
        <line x1="200" y1="184" x2="120" y2="218" stroke="#8b949e" stroke-dasharray="5 3" marker-end="url(#arr22)"/>
        <line x1="660" y1="184" x2="540" y2="218" stroke="#8b949e" stroke-dasharray="5 3" marker-end="url(#arr22)"/>
        <line x1="660" y1="184" x2="725" y2="218" stroke="#8b949e" stroke-dasharray="5 3" marker-end="url(#arr22)"/>
      </svg>
    </div>
    <div class="info-box info-key"><strong>🔑 Widget = Config, Element = Instance</strong><p>Never confuse widgets and elements. <code>Widget</code> describes what to build — it's disposable. <code>Element</code> manages lifecycle and holds state. When you call <code>setState()</code>, Flutter only reconstructs the Widget tree; the Element tree is reconciled, and only changed RenderObjects repaint.</p></div>
  </div>

  <!-- 2.3 Stateless vs Stateful -->
  <div class="subsection" id="s2-3">
    <h3 style="color:var(--purple);">2.3 Stateless vs Stateful Widgets</h3>
    <p>A <strong>StatelessWidget</strong> is a pure function of its configuration — given the same inputs, it always produces the same UI. It has no internal mutable state. This makes it predictable, easy to test, and highly performant. Use it for static content, display-only components, and layouts that don't change.</p>
    <p>A <strong>StatefulWidget</strong> creates a separate <code>State</code> object that persists across rebuilds. The <code>State</code> holds mutable data and can trigger rebuilds via <code>setState()</code>. The lifecycle is critical to understand: <code>initState()</code> for one-time setup, <code>build()</code> for rendering, <code>didUpdateWidget()</code> when parent changes configs, and <code>dispose()</code> for cleanup.</p>
    <div class="diagram">
      <svg viewBox="0 0 860 200" xmlns="http://www.w3.org/2000/svg">
        <defs><marker id="arr23" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="#8b949e" stroke-width="1.5" stroke-linecap="round"/></marker></defs>
        <!-- steps -->
        <rect x="20" y="80" width="110" height="40" rx="8" fill="#0d2b22" stroke="#34d399" stroke-width="1.5"/>
        <text x="75" y="96" font-family="JetBrains Mono" font-size="10" font-weight="700" fill="#34d399" text-anchor="middle">createState()</text>
        <text x="75" y="112" font-family="JetBrains Mono" font-size="9" fill="#8b949e" text-anchor="middle">green: init</text>
        <rect x="150" y="80" width="110" height="40" rx="8" fill="#0d2b22" stroke="#34d399" stroke-width="1.5"/>
        <text x="205" y="96" font-family="JetBrains Mono" font-size="10" font-weight="700" fill="#34d399" text-anchor="middle">initState()</text>
        <text x="205" y="112" font-family="JetBrains Mono" font-size="9" fill="#8b949e" text-anchor="middle">once only</text>
        <rect x="280" y="80" width="130" height="40" rx="8" fill="#0d2b22" stroke="#34d399" stroke-width="1.5"/>
        <text x="345" y="96" font-family="JetBrains Mono" font-size="10" font-weight="700" fill="#34d399" text-anchor="middle">didChangeDeps()</text>
        <text x="345" y="112" font-family="JetBrains Mono" font-size="9" fill="#8b949e" text-anchor="middle">if dep changes</text>
        <rect x="430" y="80" width="90" height="40" rx="8" fill="#0d1e3b" stroke="#60a5fa" stroke-width="2"/>
        <text x="475" y="96" font-family="JetBrains Mono" font-size="10" font-weight="700" fill="#60a5fa" text-anchor="middle">build()</text>
        <text x="475" y="112" font-family="JetBrains Mono" font-size="9" fill="#8b949e" text-anchor="middle">active</text>
        <rect x="540" y="50" width="100" height="36" rx="8" fill="#1a1433" stroke="#a78bfa" stroke-width="1.5"/>
        <text x="590" y="68" font-family="JetBrains Mono" font-size="10" font-weight="700" fill="#a78bfa" text-anchor="middle">setState()</text>
        <text x="590" y="80" font-family="JetBrains Mono" font-size="9" fill="#8b949e" text-anchor="middle">→ rebuild</text>
        <rect x="650" y="80" width="110" height="40" rx="8" fill="#0d1e3b" stroke="#60a5fa" stroke-width="1.5"/>
        <text x="705" y="96" font-family="JetBrains Mono" font-size="10" font-weight="700" fill="#60a5fa" text-anchor="middle">didUpdateWidget</text>
        <text x="705" y="112" font-family="JetBrains Mono" font-size="9" fill="#8b949e" text-anchor="middle">parent rebuild</text>
        <rect x="650" y="145" width="110" height="40" rx="8" fill="#2b0f14" stroke="#fb7185" stroke-width="1.5"/>
        <text x="705" y="162" font-family="JetBrains Mono" font-size="10" font-weight="700" fill="#fb7185" text-anchor="middle">dispose()</text>
        <text x="705" y="178" font-family="JetBrains Mono" font-size="9" fill="#8b949e" text-anchor="middle">cleanup</text>
        <!-- lines -->
        <line x1="130" y1="100" x2="150" y2="100" stroke="#34d399" marker-end="url(#arr23)"/>
        <line x1="260" y1="100" x2="280" y2="100" stroke="#34d399" marker-end="url(#arr23)"/>
        <line x1="410" y1="100" x2="430" y2="100" stroke="#60a5fa" marker-end="url(#arr23)"/>
        <line x1="520" y1="100" x2="540" y2="68" stroke="#a78bfa" marker-end="url(#arr23)"/>
        <line x1="590" y1="86" x2="475" y2="80" stroke="#a78bfa" stroke-dasharray="4 3" marker-end="url(#arr23)"/>
        <line x1="640" y1="100" x2="650" y2="100" stroke="#60a5fa" marker-end="url(#arr23)"/>
        <line x1="705" y1="120" x2="705" y2="145" stroke="#fb7185" marker-end="url(#arr23)"/>
      </svg>
    </div>
    <div class="code-wrap">
      <span class="code-label">Flutter</span>
      <button class="copy-btn">Copy</button>
<pre><span class="c">// StatelessWidget — pure function of config</span>
<span class="k">class</span> <span class="t">WelcomeCard</span> <span class="k">extends</span> <span class="t">StatelessWidget</span> {
  <span class="k">final</span> <span class="t">String</span> <span class="n">username</span>;
  <span class="k">const</span> <span class="t">WelcomeCard</span>({<span class="k">super</span>.<span class="n">key</span>, <span class="k">required</span> <span class="k">this</span>.<span class="n">username</span>});

  <span class="ann">@override</span>
  <span class="t">Widget</span> <span class="m">build</span>(<span class="t">BuildContext</span> <span class="n">context</span>) {
    <span class="k">return</span> <span class="t">Card</span>(
      <span class="n">child</span>: <span class="t">Padding</span>(
        <span class="n">padding</span>: <span class="k">const</span> <span class="t">EdgeInsets</span>.<span class="m">all</span>(<span class="num">16</span>),
        <span class="n">child</span>: <span class="t">Text</span>(<span class="s">'Welcome, $username!'</span>,
          <span class="n">style</span>: <span class="t">Theme</span>.<span class="m">of</span>(<span class="n">context</span>).<span class="n">textTheme</span>.<span class="n">headlineSmall</span>),
      ),
    );
  }
}

<span class="c">// StatefulWidget — mutable state</span>
<span class="k">class</span> <span class="t">ToggleButton</span> <span class="k">extends</span> <span class="t">StatefulWidget</span> {
  <span class="k">const</span> <span class="t">ToggleButton</span>({<span class="k">super</span>.<span class="n">key</span>});
  <span class="ann">@override</span>
  <span class="t">State</span>&lt;<span class="t">ToggleButton</span>&gt; <span class="m">createState</span>() =&gt; <span class="t">_ToggleButtonState</span>();
}

<span class="k">class</span> <span class="t">_ToggleButtonState</span> <span class="k">extends</span> <span class="t">State</span>&lt;<span class="t">ToggleButton</span>&gt; {
  <span class="t">bool</span> <span class="n">_isOn</span> = <span class="k">false</span>;

  <span class="ann">@override</span>
  <span class="k">void</span> <span class="m">initState</span>() {
    <span class="k">super</span>.<span class="m">initState</span>(); <span class="c">// always call super first</span>
    <span class="c">// one-time setup: controllers, listeners, etc.</span>
  }

  <span class="ann">@override</span>
  <span class="t">Widget</span> <span class="m">build</span>(<span class="t">BuildContext</span> <span class="n">context</span>) {
    <span class="k">return</span> <span class="t">ElevatedButton</span>(
      <span class="n">onPressed</span>: () =&gt; <span class="m">setState</span>(() =&gt; <span class="n">_isOn</span> = !<span class="n">_isOn</span>),
      <span class="n">style</span>: <span class="t">ElevatedButton</span>.<span class="m">styleFrom</span>(
        <span class="n">backgroundColor</span>: <span class="n">_isOn</span> ? <span class="t">Colors</span>.<span class="n">green</span> : <span class="t">Colors</span>.<span class="n">grey</span>,
      ),
      <span class="n">child</span>: <span class="t">Text</span>(<span class="n">_isOn</span> ? <span class="s">'ON'</span> : <span class="s">'OFF'</span>),
    );
  }

  <span class="ann">@override</span>
  <span class="k">void</span> <span class="m">dispose</span>() {
    <span class="c">// dispose controllers, cancel subscriptions</span>
    <span class="k">super</span>.<span class="m">dispose</span>(); <span class="c">// always call super last</span>
  }
}</pre>
    </div>
    <div class="table-wrap"><table>
      <tr><th>Feature</th><th>StatelessWidget</th><th>StatefulWidget</th></tr>
      <tr><td>Has mutable state</td><td>❌</td><td>✅ via State object</td></tr>
      <tr><td>Rebuilds on</td><td>Parent rebuild only</td><td>setState() + parent</td></tr>
      <tr><td>Use when</td><td>Static/display content</td><td>User input, animations</td></tr>
      <tr><td>Performance</td><td>⚡ Fastest</td><td>Slightly more overhead</td></tr>
    </table></div>
  </div>

  <!-- 2.4 BuildContext -->
  <div class="subsection" id="s2-4">
    <h3 style="color:var(--purple);">2.4 BuildContext In Depth</h3>
    <p><strong>BuildContext</strong> is literally the Element — your widget's position in the tree. It enables widgets to communicate upward through the tree to find ancestors. <code>Theme.of(context)</code>, <code>MediaQuery.of(context)</code>, <code>Navigator.of(context)</code> all traverse up the Element tree to find the nearest matching ancestor.</p>
    <p>Contexts are only valid within their build scope. After an <code>await</code>, the widget may have been disposed — always check <code>mounted</code> before using context post-async. Never store context in a field of a State object for async use without checking mounted.</p>
    <div class="code-wrap">
      <span class="code-label">Flutter</span>
      <button class="copy-btn">Copy</button>
<pre><span class="c">// Safe context usage after async</span>
<span class="k">class</span> <span class="t">_LoginPageState</span> <span class="k">extends</span> <span class="t">State</span>&lt;<span class="t">LoginPage</span>&gt; {
  <span class="t">bool</span> <span class="n">_loading</span> = <span class="k">false</span>;

  <span class="k">Future</span>&lt;<span class="k">void</span>&gt; <span class="m">_handleLogin</span>() <span class="k">async</span> {
    <span class="m">setState</span>(() =&gt; <span class="n">_loading</span> = <span class="k">true</span>);
    <span class="k">try</span> {
      <span class="k">await</span> <span class="n">authService</span>.<span class="m">login</span>(<span class="n">email</span>, <span class="n">password</span>);
      <span class="c">// ✅ Check mounted after await!</span>
      <span class="k">if</span> (!<span class="n">mounted</span>) <span class="k">return</span>;
      <span class="t">Navigator</span>.<span class="m">of</span>(<span class="n">context</span>).<span class="m">pushReplacement</span>(
        <span class="t">MaterialPageRoute</span>(<span class="n">builder</span>: (<span class="n">_</span>) =&gt; <span class="k">const</span> <span class="t">HomeScreen</span>()),
      );
    } <span class="k">catch</span> (<span class="n">e</span>) {
      <span class="k">if</span> (!<span class="n">mounted</span>) <span class="k">return</span>;
      <span class="t">ScaffoldMessenger</span>.<span class="m">of</span>(<span class="n">context</span>).<span class="m">showSnackBar</span>(
        <span class="t">SnackBar</span>(<span class="n">content</span>: <span class="t">Text</span>(<span class="n">e</span>.<span class="m">toString</span>())),
      );
    } <span class="k">finally</span> {
      <span class="k">if</span> (<span class="n">mounted</span>) <span class="m">setState</span>(() =&gt; <span class="n">_loading</span> = <span class="k">false</span>);
    }
  }

  <span class="ann">@override</span>
  <span class="t">Widget</span> <span class="m">build</span>(<span class="t">BuildContext</span> <span class="n">context</span>) {
    <span class="c">// Access theme, size, navigator from context</span>
    <span class="k">final</span> <span class="n">theme</span> = <span class="t">Theme</span>.<span class="m">of</span>(<span class="n">context</span>);
    <span class="k">final</span> <span class="n">size</span> = <span class="t">MediaQuery</span>.<span class="m">sizeOf</span>(<span class="n">context</span>);
    <span class="m">print</span>(<span class="s">'Screen: ${size.width}x${size.height}'</span>);
    <span class="k">return</span> <span class="t">Scaffold</span>(
      <span class="n">backgroundColor</span>: <span class="n">theme</span>.<span class="n">colorScheme</span>.<span class="n">surface</span>,
      <span class="n">body</span>: <span class="t">Center</span>(<span class="n">child</span>: <span class="t">Text</span>(<span class="s">'Login'</span>)),
    );
  }
}</pre>
    </div>
    <div class="info-box info-warn"><strong>⚠️ Context Scope</strong><p>Avoid calling <code>Navigator.of(context)</code> or <code>ScaffoldMessenger.of(context)</code> inside <code>initState()</code> — the widget isn't in the tree yet. Use <code>WidgetsBinding.instance.addPostFrameCallback()</code> or move to <code>didChangeDependencies()</code>.</p></div>
  </div>
  <!-- 2.5 Three Trees -->
  <div class="subsection" id="s2-5">
    <h3 style="color:var(--purple);">2.5 Element vs RenderObject (The Three Trees)</h3>
    <p>We touched on this in 2.2, but tracking the lifecycle reveals why Flutter is so fast:</p>
    <div class="grid-2">
      <div class="card glass glow-hover" style="border-top: 3px solid var(--blue);">
        <div class="card-title">1. Widget Tree (Config)</div>
        <p>You write this. It represents the <strong>immutable configurations</strong>. These are destroyed and recreated constantly (e.g. 60 times a second during an animation). It costs essentially nothing to create Dart classes.</p>
      </div>
      <div class="card glass glow-hover" style="border-top: 3px solid var(--purple);">
        <div class="card-title">2. Element Tree (Lifecycle)</div>
        <p>Flutter builds this automatically. This is the <strong>mutable instantiation</strong> of a widget at a specific location in the UI. If you rebuild a Widget, Flutter compares it to the corresponding Element. If the type and Key are the same, the Element is kept and just updated.</p>
      </div>
      <div class="card glass glow-hover" style="border-top: 3px solid var(--teal);">
        <div class="card-title">3. RenderObject Tree (Pixels)</div>
        <p>The Element instantiates a RenderObject. This handles measuring constraints (layout) and drawing pixels (paint). Relayouting and repainting are the <strong>expensive operations</strong> that cause jank.</p>
      </div>
    </div>
    
  </div>
</section>
'''

with open('flutter_notes.html', 'a') as f:
    f.write(s2)
print('Section 2 appended. Len:', len(s2))
