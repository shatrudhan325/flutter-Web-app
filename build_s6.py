
s6 = '''
<!-- ═══════════════════════════════════════════ SECTION 6 ═══ -->
<section class="section" id="s6">
  <div class="section-header">
    <div class="section-icon" style="background:var(--amber-bg);">⚡</div>
    <div class="section-meta">
      <span class="section-badge" style="background:var(--amber-bg);color:var(--amber);">Intermediate → Advanced</span>
      <div class="section-title" style="color:var(--amber);">State Management</div>
      <div class="section-subtitle">setState, Provider, Riverpod, BLoC — patterns from simple to enterprise</div>
    </div>
  </div>

  <!-- 6.1 setState -->
  <div class="subsection" id="s6-1">
    <h3 style="color:var(--amber);">6.1 setState — Local State</h3>
    <p><strong>setState</strong> is Flutter's built-in mechanism for triggering a widget rebuild. It's perfect for <strong>local UI state</strong> — toggles, form input, counters, tab selections — that doesn't need to be shared with other widgets. The rule: if only one widget needs the state, keep it local.</p>
    <p>Call <code>setState()</code> with the minimal change needed. Never put expensive operations inside <code>setState()</code>'s callback — only state mutations go there. To optimize, extract child widgets as <code>const</code> or separate <code>StatelessWidget</code>s so they don't rebuild when the parent calls <code>setState()</code>.</p>
    <div class="code-wrap">
      <span class="code-label">Flutter</span>
      <button class="copy-btn">Copy</button>
<pre><span class="c">// Optimized counter — extracted child doesn't rebuild</span>
<span class="k">class</span> <span class="t">CounterPage</span> <span class="k">extends</span> <span class="t">StatefulWidget</span> {
  <span class="k">const</span> <span class="t">CounterPage</span>({<span class="k">super</span>.<span class="n">key</span>});
  <span class="ann">@override</span>
  <span class="t">State</span>&lt;<span class="t">CounterPage</span>&gt; <span class="m">createState</span>() =&gt; <span class="t">_CounterPageState</span>();
}

<span class="k">class</span> <span class="t">_CounterPageState</span> <span class="k">extends</span> <span class="t">State</span>&lt;<span class="t">CounterPage</span>&gt; {
  <span class="t">int</span> <span class="n">_count</span> = <span class="num">0</span>;

  <span class="k">void</span> <span class="m">_increment</span>() =&gt; <span class="m">setState</span>(() =&gt; <span class="n">_count</span>++);
  <span class="k">void</span> <span class="m">_decrement</span>() =&gt; <span class="m">setState</span>(() =&gt; <span class="n">_count</span>--);
  <span class="k">void</span> <span class="m">_reset</span>()     =&gt; <span class="m">setState</span>(() =&gt; <span class="n">_count</span> = <span class="num">0</span>);

  <span class="ann">@override</span>
  <span class="t">Widget</span> <span class="m">build</span>(<span class="t">BuildContext</span> <span class="n">context</span>) {
    <span class="k">return</span> <span class="t">Scaffold</span>(
      <span class="n">body</span>: <span class="t">Column</span>(
        <span class="n">mainAxisAlignment</span>: <span class="t">MainAxisAlignment</span>.<span class="n">center</span>,
        <span class="n">children</span>: [
          <span class="k">const</span> <span class="t">AppLogo</span>(),  <span class="c">// const — never rebuilds</span>
          <span class="t">CounterDisplay</span>(<span class="n">count</span>: <span class="n">_count</span>),  <span class="c">// rebuilds on count change</span>
          <span class="t">Row</span>(
            <span class="n">mainAxisAlignment</span>: <span class="t">MainAxisAlignment</span>.<span class="n">center</span>,
            <span class="n">children</span>: [
              <span class="t">IconButton</span>(<span class="n">onPressed</span>: <span class="n">_decrement</span>, <span class="n">icon</span>: <span class="k">const</span> <span class="t">Icon</span>(<span class="t">Icons</span>.<span class="n">remove</span>)),
              <span class="t">TextButton</span>(<span class="n">onPressed</span>: <span class="n">_reset</span>, <span class="n">child</span>: <span class="k">const</span> <span class="t">Text</span>(<span class="s">'Reset'</span>)),
              <span class="t">IconButton</span>(<span class="n">onPressed</span>: <span class="n">_increment</span>, <span class="n">icon</span>: <span class="k">const</span> <span class="t">Icon</span>(<span class="t">Icons</span>.<span class="n">add</span>)),
            ],
          ),
        ],
      ),
    );
  }
}</pre>
    </div>
    <div class="info-box info-tip"><strong>💡 When setState is Enough</strong><p>Use setState for: form field visibility toggles, loading spinners, local tab selections, animation triggers, expansion states. Reach for Provider/Riverpod only when state needs to be <em>shared</em> across widget subtrees or persisted beyond the widget's lifecycle.</p></div>
  </div>

  <!-- 6.2 Provider -->
  <div class="subsection" id="s6-2">
    <h3 style="color:var(--amber);">6.2 Provider</h3>
    <p><strong>Provider</strong> is built on InheritedWidget. A <code>ChangeNotifier</code> class holds state and calls <code>notifyListeners()</code> to trigger rebuilds. <code>context.watch&lt;T&gt;()</code> subscribes to changes and rebuilds on every notification. <code>context.read&lt;T&gt;()</code> reads the value once without subscribing — use it in callbacks and event handlers. <code>context.select&lt;T,S&gt;()</code> subscribes only to a specific piece of the model.</p>
    <div class="diagram">
      <svg viewBox="0 0 860 200" xmlns="http://www.w3.org/2000/svg">
        <defs><marker id="arr62" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="#8b949e" stroke-width="1.5" stroke-linecap="round"/></marker></defs>
        <rect x="30" y="20" width="800" height="160" rx="10" fill="#161b22" stroke="#30363d"/>
        <text x="430" y="42" font-family="JetBrains Mono" font-size="11" fill="#8b949e" text-anchor="middle">ChangeNotifierProvider scope</text>
        <rect x="60" y="55" width="200" height="60" rx="8" fill="#2b1d0d" stroke="#fbbf24" stroke-width="1.5"/>
        <text x="160" y="80" font-family="JetBrains Mono" font-size="11" font-weight="700" fill="#fbbf24" text-anchor="middle">CartProvider</text>
        <text x="160" y="98" font-family="JetBrains Mono" font-size="10" fill="#8b949e" text-anchor="middle">notifyListeners()</text>
        <rect x="320" y="55" width="160" height="60" rx="8" fill="#0d1e3b" stroke="#60a5fa" stroke-width="1.5"/>
        <text x="400" y="80" font-family="JetBrains Mono" font-size="11" font-weight="700" fill="#60a5fa" text-anchor="middle">CartBadge</text>
        <text x="400" y="98" font-family="JetBrains Mono" font-size="10" fill="#8b949e" text-anchor="middle">context.watch ✓</text>
        <rect x="540" y="55" width="160" height="60" rx="8" fill="#161b22" stroke="#30363d" stroke-width="1.5"/>
        <text x="620" y="80" font-family="JetBrains Mono" font-size="11" font-weight="700" fill="#8b949e" text-anchor="middle">AppBar</text>
        <text x="620" y="98" font-family="JetBrains Mono" font-size="10" fill="#8b949e" text-anchor="middle">no watch — no rebuild</text>
        <rect x="320" y="135" width="160" height="36" rx="8" fill="#0d2b22" stroke="#34d399" stroke-width="1.5"/>
        <text x="400" y="158" font-family="JetBrains Mono" font-size="11" fill="#34d399" text-anchor="middle">AddButton (read)</text>
        <line x1="260" y1="85" x2="320" y2="85" stroke="#fbbf24" stroke-width="1.5" marker-end="url(#arr62)"/>
        <line x1="400" y1="115" x2="400" y2="135" stroke="#34d399" stroke-dasharray="4 3" marker-end="url(#arr62)"/>
      </svg>
    </div>
    <div class="code-wrap">
      <span class="code-label">Flutter</span>
      <button class="copy-btn">Copy</button>
<pre><span class="c">// ChangeNotifier model</span>
<span class="k">class</span> <span class="t">CartProvider</span> <span class="k">extends</span> <span class="t">ChangeNotifier</span> {
  <span class="k">final</span> <span class="t">List</span>&lt;<span class="t">CartItem</span>&gt; <span class="n">_items</span> = [];

  <span class="t">List</span>&lt;<span class="t">CartItem</span>&gt; <span class="k">get</span> <span class="n">items</span> =&gt; <span class="t">List</span>.<span class="m">unmodifiable</span>(<span class="n">_items</span>);
  <span class="t">int</span> <span class="k">get</span> <span class="n">itemCount</span> =&gt; <span class="n">_items</span>.<span class="n">length</span>;
  <span class="t">double</span> <span class="k">get</span> <span class="n">total</span> =&gt; <span class="n">_items</span>.<span class="m">fold</span>(<span class="num">0</span>, (<span class="n">sum</span>, <span class="n">i</span>) =&gt; <span class="n">sum</span> + <span class="n">i</span>.<span class="n">price</span> * <span class="n">i</span>.<span class="n">qty</span>);

  <span class="k">void</span> <span class="m">addItem</span>(<span class="t">Product</span> <span class="n">product</span>) {
    <span class="k">final</span> <span class="n">idx</span> = <span class="n">_items</span>.<span class="m">indexWhere</span>((<span class="n">i</span>) =&gt; <span class="n">i</span>.<span class="n">id</span> == <span class="n">product</span>.<span class="n">id</span>);
    <span class="k">if</span> (<span class="n">idx</span> &gt;= <span class="num">0</span>) { <span class="n">_items</span>[<span class="n">idx</span>].<span class="n">qty</span>++; }
    <span class="k">else</span> { <span class="n">_items</span>.<span class="m">add</span>(<span class="t">CartItem</span>.<span class="m">fromProduct</span>(<span class="n">product</span>)); }
    <span class="m">notifyListeners</span>();  <span class="c">// triggers all watchers</span>
  }

  <span class="k">void</span> <span class="m">removeItem</span>(<span class="t">String</span> <span class="n">id</span>) {
    <span class="n">_items</span>.<span class="m">removeWhere</span>((<span class="n">i</span>) =&gt; <span class="n">i</span>.<span class="n">id</span> == <span class="n">id</span>);
    <span class="m">notifyListeners</span>();
  }
}

<span class="c">// Provide at root</span>
<span class="t">ChangeNotifierProvider</span>(<span class="n">create</span>: (<span class="n">_</span>) =&gt; <span class="t">CartProvider</span>(), <span class="n">child</span>: <span class="k">const</span> <span class="t">MyApp</span>())

<span class="c">// In widgets:</span>
<span class="k">final</span> <span class="n">total</span> = <span class="n">context</span>.<span class="m">watch</span>&lt;<span class="t">CartProvider</span>&gt;().<span class="n">total</span>;   <span class="c">// rebuilds on change</span>
<span class="n">context</span>.<span class="m">read</span>&lt;<span class="t">CartProvider</span>&gt;().<span class="m">addItem</span>(<span class="n">product</span>);        <span class="c">// no rebuild</span>

<span class="c">// Selector — only rebuilds when itemCount changes</span>
<span class="t">Selector</span>&lt;<span class="t">CartProvider</span>, <span class="t">int</span>&gt;(
  <span class="n">selector</span>: (<span class="n">_</span>, <span class="n">cart</span>) =&gt; <span class="n">cart</span>.<span class="n">itemCount</span>,
  <span class="n">builder</span>: (<span class="n">_</span>, <span class="n">count</span>, <span class="n">__</span>) =&gt; <span class="t">CartBadge</span>(<span class="n">count</span>: <span class="n">count</span>),
)</pre>
    </div>
    <div class="info-box info-warn"><strong>⚠️ context.watch in Callbacks</strong><p>Never use <code>context.watch</code> inside button <code>onPressed</code> or other callbacks — calling it outside <code>build()</code> will throw. Use <code>context.read</code> for event handlers. The rule: <code>watch</code> = inside build, <code>read</code> = inside callbacks.</p></div>
  </div>

  <!-- 6.3 Riverpod -->
  <div class="subsection" id="s6-3">
    <h3 style="color:var(--amber);">6.3 Riverpod — Modern Approach</h3>
    <p><strong>Riverpod</strong> fixes Provider's key limitations: no <code>BuildContext</code> required, providers are globally accessible and testable, no <code>ProviderNotFoundException</code>, and <code>autoDispose</code> cleans up providers when no longer needed. Providers are defined at top-level — they are <strong>not</strong> part of the widget tree.</p>
    <p>Provider types form a hierarchy: <code>Provider</code> (read-only computed value) → <code>StateProvider</code> (simple mutable state) → <code>NotifierProvider</code> (complex state with methods) → <code>FutureProvider</code> (async data) → <code>StreamProvider</code> (live data stream). <code>.family</code> makes a provider take a parameter. <code>.autoDispose</code> disposes when last listener unsubscribes.</p>
    <div class="diagram">
      <svg viewBox="0 0 860 180" xmlns="http://www.w3.org/2000/svg">
        <defs><marker id="arr63" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="#8b949e" stroke-width="1.5" stroke-linecap="round"/></marker></defs>
        <rect x="20" y="60" width="130" height="52" rx="8" fill="#2b1d0d" stroke="#fbbf24" stroke-width="1.5"/>
        <text x="85" y="82" font-family="JetBrains Mono" font-size="11" font-weight="700" fill="#fbbf24" text-anchor="middle">Provider</text>
        <text x="85" y="100" font-family="JetBrains Mono" font-size="9" fill="#8b949e" text-anchor="middle">read-only value</text>
        <rect x="180" y="60" width="140" height="52" rx="8" fill="#2b1d0d" stroke="#fbbf24" stroke-width="1.5"/>
        <text x="250" y="82" font-family="JetBrains Mono" font-size="11" font-weight="700" fill="#fbbf24" text-anchor="middle">StateProvider</text>
        <text x="250" y="100" font-family="JetBrains Mono" font-size="9" fill="#8b949e" text-anchor="middle">simple state</text>
        <rect x="350" y="60" width="160" height="52" rx="8" fill="#2b1d0d" stroke="#fbbf24" stroke-width="2"/>
        <text x="430" y="82" font-family="JetBrains Mono" font-size="11" font-weight="700" fill="#fbbf24" text-anchor="middle">NotifierProvider</text>
        <text x="430" y="100" font-family="JetBrains Mono" font-size="9" fill="#8b949e" text-anchor="middle">complex logic + state</text>
        <rect x="540" y="60" width="140" height="52" rx="8" fill="#0d2b22" stroke="#34d399" stroke-width="1.5"/>
        <text x="610" y="82" font-family="JetBrains Mono" font-size="11" font-weight="700" fill="#34d399" text-anchor="middle">FutureProvider</text>
        <text x="610" y="100" font-family="JetBrains Mono" font-size="9" fill="#8b949e" text-anchor="middle">async data</text>
        <rect x="710" y="60" width="140" height="52" rx="8" fill="#0d1e3b" stroke="#60a5fa" stroke-width="1.5"/>
        <text x="780" y="82" font-family="JetBrains Mono" font-size="11" font-weight="700" fill="#60a5fa" text-anchor="middle">StreamProvider</text>
        <text x="780" y="100" font-family="JetBrains Mono" font-size="9" fill="#8b949e" text-anchor="middle">live stream</text>
        <line x1="150" y1="86" x2="180" y2="86" stroke="#8b949e" marker-end="url(#arr63)"/>
        <line x1="320" y1="86" x2="350" y2="86" stroke="#8b949e" marker-end="url(#arr63)"/>
        <line x1="510" y1="86" x2="540" y2="86" stroke="#8b949e" marker-end="url(#arr63)"/>
        <line x1="680" y1="86" x2="710" y2="86" stroke="#8b949e" marker-end="url(#arr63)"/>
        <text x="430" y="155" font-family="JetBrains Mono" font-size="10" fill="#8b949e" text-anchor="middle">All support .family (parameterized) and .autoDispose modifiers</text>
      </svg>
    </div>
    <div class="code-wrap">
      <span class="code-label">Flutter</span>
      <button class="copy-btn">Copy</button>
<pre><span class="c">// Simple state — theme toggle</span>
<span class="k">final</span> <span class="n">themeProvider</span> = <span class="t">StateProvider</span>&lt;<span class="t">ThemeMode</span>&gt;(
  (<span class="n">ref</span>) =&gt; <span class="t">ThemeMode</span>.<span class="n">system</span>);

<span class="c">// Complex state with logic</span>
<span class="k">class</span> <span class="t">AuthNotifier</span> <span class="k">extends</span> <span class="t">Notifier</span>&lt;<span class="t">AuthState</span>&gt; {
  <span class="ann">@override</span>
  <span class="t">AuthState</span> <span class="m">build</span>() =&gt; <span class="k">const</span> <span class="t">AuthState</span>.<span class="m">initial</span>();

  <span class="k">Future</span>&lt;<span class="k">void</span>&gt; <span class="m">login</span>(<span class="t">String</span> <span class="n">email</span>, <span class="t">String</span> <span class="n">pass</span>) <span class="k">async</span> {
    <span class="n">state</span> = <span class="k">const</span> <span class="t">AuthState</span>.<span class="m">loading</span>();
    <span class="k">try</span> {
      <span class="k">final</span> <span class="n">user</span> = <span class="k">await</span> <span class="n">ref</span>.<span class="m">read</span>(<span class="n">authRepoProvider</span>).<span class="m">login</span>(<span class="n">email</span>, <span class="n">pass</span>);
      <span class="n">state</span> = <span class="t">AuthState</span>.<span class="m">authenticated</span>(<span class="n">user</span>);
    } <span class="k">catch</span> (<span class="n">e</span>) {
      <span class="n">state</span> = <span class="t">AuthState</span>.<span class="m">error</span>(<span class="n">e</span>.<span class="m">toString</span>());
    }
  }
  <span class="k">void</span> <span class="m">logout</span>() {
    <span class="n">ref</span>.<span class="m">read</span>(<span class="n">authRepoProvider</span>).<span class="m">logout</span>();
    <span class="n">state</span> = <span class="k">const</span> <span class="t">AuthState</span>.<span class="m">initial</span>();
  }
}
<span class="k">final</span> <span class="n">authProvider</span> = <span class="t">NotifierProvider</span>&lt;<span class="t">AuthNotifier</span>, <span class="t">AuthState</span>&gt;(<span class="t">AuthNotifier</span>.<span class="k">new</span>);

<span class="c">// FutureProvider with autoDispose + family</span>
<span class="k">final</span> <span class="n">userProvider</span> = <span class="t">FutureProvider</span>.<span class="n">autoDispose</span>
    .<span class="m">family</span>&lt;<span class="t">User</span>, <span class="t">int</span>&gt;((<span class="n">ref</span>, <span class="n">userId</span>) <span class="k">async</span> {
  <span class="k">return</span> <span class="n">ref</span>.<span class="m">read</span>(<span class="n">userRepoProvider</span>).<span class="m">getUser</span>(<span class="n">userId</span>);
});

<span class="c">// In ConsumerWidget — no BuildContext needed for providers</span>
<span class="k">class</span> <span class="t">ProfilePage</span> <span class="k">extends</span> <span class="t">ConsumerWidget</span> {
  <span class="k">final</span> <span class="t">int</span> <span class="n">userId</span>;
  <span class="k">const</span> <span class="t">ProfilePage</span>({<span class="k">super</span>.<span class="n">key</span>, <span class="k">required</span> <span class="k">this</span>.<span class="n">userId</span>});
  <span class="ann">@override</span>
  <span class="t">Widget</span> <span class="m">build</span>(<span class="t">BuildContext</span> <span class="n">context</span>, <span class="t">WidgetRef</span> <span class="n">ref</span>) {
    <span class="k">final</span> <span class="n">userAsync</span> = <span class="n">ref</span>.<span class="m">watch</span>(<span class="n">userProvider</span>(<span class="n">userId</span>));
    <span class="k">return</span> <span class="n">userAsync</span>.<span class="m">when</span>(
      <span class="n">data</span>: (<span class="n">user</span>) =&gt; <span class="t">UserCard</span>(<span class="n">user</span>: <span class="n">user</span>),
      <span class="n">loading</span>: () =&gt; <span class="k">const</span> <span class="t">CircularProgressIndicator</span>(),
      <span class="n">error</span>: (<span class="n">e</span>, <span class="n">_</span>) =&gt; <span class="t">ErrorWidget</span>(<span class="n">e</span>),
    );
  }
}</pre>
    </div>
    <div class="info-box info-key"><strong>🔑 ref.watch vs ref.read vs ref.listen</strong><p><code>ref.watch</code> subscribes and rebuilds on change (use in <code>build</code>). <code>ref.read</code> reads once without subscribing (use in callbacks). <code>ref.listen</code> triggers a side effect callback on change without rebuilding (use for navigation, snackbars).</p></div>
  </div>

  <!-- 6.4 BLoC -->
  <div class="subsection" id="s6-4">
    <h3 style="color:var(--amber);">6.4 BLoC Pattern</h3>
    <p>The <strong>Business Logic Component</strong> pattern strictly separates UI from business logic. <strong>Events</strong> are inputs (user actions, lifecycle events). <strong>States</strong> are outputs (what the UI renders). The Bloc processes events and emits states asynchronously. This makes business logic fully testable without Flutter — just Dart classes.</p>
    <p><strong>Cubit</strong> is a simplified BLoC without events — it exposes methods that emit states directly. Use Cubit when you don't need event history or complex transformations. Use BLoC when you need event debouncing, event transformation, or event logging middleware (EventTransformer).</p>
    <div class="diagram">
      <svg viewBox="0 0 860 180" xmlns="http://www.w3.org/2000/svg">
        <defs><marker id="arr64" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="#8b949e" stroke-width="1.5" stroke-linecap="round"/></marker></defs>
        <rect x="20" y="60" width="160" height="60" rx="8" fill="#0d1e3b" stroke="#60a5fa" stroke-width="1.5"/>
        <text x="100" y="85" font-family="JetBrains Mono" font-size="11" font-weight="700" fill="#60a5fa" text-anchor="middle">UI Widget</text>
        <text x="100" y="103" font-family="JetBrains Mono" font-size="10" fill="#8b949e" text-anchor="middle">BlocBuilder</text>
        <rect x="350" y="40" width="200" height="100" rx="8" fill="#2b1d0d" stroke="#fbbf24" stroke-width="2"/>
        <text x="450" y="70" font-family="JetBrains Mono" font-size="12" font-weight="700" fill="#fbbf24" text-anchor="middle">BLoC</text>
        <text x="450" y="90" font-family="JetBrains Mono" font-size="10" fill="#8b949e" text-anchor="middle">on&lt;Event&gt;(handler)</text>
        <text x="450" y="108" font-family="JetBrains Mono" font-size="10" fill="#8b949e" text-anchor="middle">emit(state)</text>
        <rect x="680" y="60" width="160" height="60" rx="8" fill="#0d2b22" stroke="#34d399" stroke-width="1.5"/>
        <text x="760" y="85" font-family="JetBrains Mono" font-size="11" font-weight="700" fill="#34d399" text-anchor="middle">Repository</text>
        <text x="760" y="103" font-family="JetBrains Mono" font-size="10" fill="#8b949e" text-anchor="middle">API / DB</text>
        <line x1="180" y1="78" x2="350" y2="78" stroke="#fbbf24" stroke-width="1.5" marker-end="url(#arr64)"/>
        <text x="265" y="70" font-family="JetBrains Mono" font-size="9" fill="#fbbf24" text-anchor="middle">add(Event)</text>
        <line x1="350" y1="102" x2="180" y2="102" stroke="#60a5fa" stroke-width="1.5" marker-end="url(#arr64)"/>
        <text x="265" y="118" font-family="JetBrains Mono" font-size="9" fill="#60a5fa" text-anchor="middle">emit(State)</text>
        <line x1="550" y1="90" x2="680" y2="90" stroke="#34d399" stroke-width="1.5" marker-end="url(#arr64)"/>
        <text x="615" y="82" font-family="JetBrains Mono" font-size="9" fill="#34d399" text-anchor="middle">fetch data</text>
      </svg>
    </div>
    <div class="code-wrap">
      <span class="code-label">Flutter</span>
      <button class="copy-btn">Copy</button>
<pre><span class="c">// Events</span>
<span class="k">abstract class</span> <span class="t">AuthEvent</span> {}
<span class="k">class</span> <span class="t">LoginRequested</span> <span class="k">extends</span> <span class="t">AuthEvent</span> {
  <span class="k">final</span> <span class="t">String</span> <span class="n">email</span>, <span class="n">password</span>;
  <span class="t">LoginRequested</span>({<span class="k">required</span> <span class="k">this</span>.<span class="n">email</span>, <span class="k">required</span> <span class="k">this</span>.<span class="n">password</span>});
}
<span class="k">class</span> <span class="t">LogoutRequested</span> <span class="k">extends</span> <span class="t">AuthEvent</span> {}

<span class="c">// States (sealed class in Dart 3+)</span>
<span class="k">sealed class</span> <span class="t">AuthState</span> {}
<span class="k">class</span> <span class="t">AuthInitial</span> <span class="k">extends</span> <span class="t">AuthState</span> {}
<span class="k">class</span> <span class="t">AuthLoading</span> <span class="k">extends</span> <span class="t">AuthState</span> {}
<span class="k">class</span> <span class="t">AuthAuthenticated</span> <span class="k">extends</span> <span class="t">AuthState</span> { <span class="k">final</span> <span class="t">User</span> <span class="n">user</span>; <span class="t">AuthAuthenticated</span>(<span class="k">this</span>.<span class="n">user</span>); }
<span class="k">class</span> <span class="t">AuthError</span> <span class="k">extends</span> <span class="t">AuthState</span> { <span class="k">final</span> <span class="t">String</span> <span class="n">message</span>; <span class="t">AuthError</span>(<span class="k">this</span>.<span class="n">message</span>); }

<span class="c">// BLoC</span>
<span class="k">class</span> <span class="t">AuthBloc</span> <span class="k">extends</span> <span class="t">Bloc</span>&lt;<span class="t">AuthEvent</span>, <span class="t">AuthState</span>&gt; {
  <span class="k">final</span> <span class="t">AuthRepository</span> <span class="n">_repo</span>;
  <span class="t">AuthBloc</span>(<span class="k">this</span>.<span class="n">_repo</span>) : <span class="k">super</span>(<span class="t">AuthInitial</span>()) {
    <span class="m">on</span>&lt;<span class="t">LoginRequested</span>&gt;(<span class="n">_onLogin</span>);
    <span class="m">on</span>&lt;<span class="t">LogoutRequested</span>&gt;(<span class="n">_onLogout</span>);
  }

  <span class="k">Future</span>&lt;<span class="k">void</span>&gt; <span class="m">_onLogin</span>(<span class="t">LoginRequested</span> <span class="n">event</span>, <span class="t">Emitter</span>&lt;<span class="t">AuthState</span>&gt; <span class="n">emit</span>) <span class="k">async</span> {
    <span class="m">emit</span>(<span class="t">AuthLoading</span>());
    <span class="k">try</span> {
      <span class="k">final</span> <span class="n">user</span> = <span class="k">await</span> <span class="n">_repo</span>.<span class="m">login</span>(<span class="n">event</span>.<span class="n">email</span>, <span class="n">event</span>.<span class="n">password</span>);
      <span class="m">emit</span>(<span class="t">AuthAuthenticated</span>(<span class="n">user</span>));
    } <span class="k">catch</span> (<span class="n">e</span>) { <span class="m">emit</span>(<span class="t">AuthError</span>(<span class="n">e</span>.<span class="m">toString</span>())); }
  }
  <span class="k">void</span> <span class="m">_onLogout</span>(<span class="n">_</span>, <span class="n">__</span>) { <span class="n">_repo</span>.<span class="m">logout</span>(); <span class="m">emit</span>(<span class="t">AuthInitial</span>()); }
}

<span class="c">// In widget — BlocConsumer combines Builder + Listener</span>
<span class="t">BlocConsumer</span>&lt;<span class="t">AuthBloc</span>, <span class="t">AuthState</span>&gt;(
  <span class="n">listener</span>: (<span class="n">ctx</span>, <span class="n">state</span>) {
    <span class="k">if</span> (<span class="n">state</span> <span class="k">is</span> <span class="t">AuthAuthenticated</span>) <span class="n">ctx</span>.<span class="m">go</span>(<span class="s">'/home'</span>);
    <span class="k">if</span> (<span class="n">state</span> <span class="k">is</span> <span class="t">AuthError</span>) <span class="t">ScaffoldMessenger</span>.<span class="m">of</span>(<span class="n">ctx</span>).<span class="m">showSnackBar</span>(<span class="t">SnackBar</span>(<span class="n">content</span>: <span class="t">Text</span>(<span class="n">state</span>.<span class="n">message</span>)));
  },
  <span class="n">builder</span>: (<span class="n">ctx</span>, <span class="n">state</span>) =&gt; <span class="k">switch</span> (<span class="n">state</span>) {
    <span class="t">AuthLoading</span>() =&gt; <span class="k">const</span> <span class="t">CircularProgressIndicator</span>(),
    <span class="n">_</span> =&gt; <span class="t">LoginForm</span>(),
  },
)</pre>
    </div>
    <div class="info-box info-tip"><strong>💡 Cubit vs BLoC</strong><p>Use <code>Cubit</code> for simple state machines (loading/loaded/error). Use <code>Bloc</code> when you need event debouncing (search-as-you-type), event transformation, or need to log/replay events for analytics.</p></div>
  </div>

  <!-- 6.5 Comparison -->
  <div class="subsection" id="s6-5">
    <h3 style="color:var(--amber);">6.5 State Management Comparison</h3>
    <div class="table-wrap"><table>
      <tr><th>Solution</th><th>Boilerplate</th><th>Learning Curve</th><th>Scalability</th><th>Testability</th><th>Best For</th></tr>
      <tr><td><code style="background:var(--blue-bg);color:var(--blue);">setState</code></td><td>Minimal</td><td>⭐</td><td>Single widget</td><td>Easy</td><td>Local UI state</td></tr>
      <tr><td><code style="background:var(--teal-bg);color:var(--teal);">Provider</code></td><td>Low</td><td>⭐⭐</td><td>Medium apps</td><td>Good</td><td>Teams new to state mgmt</td></tr>
      <tr><td><code style="background:var(--amber-bg);color:var(--amber);">Riverpod</code></td><td>Medium</td><td>⭐⭐⭐</td><td>Large apps</td><td>Excellent</td><td>Modern Flutter apps</td></tr>
      <tr><td><code style="background:var(--purple-bg);color:var(--purple);">BLoC</code></td><td>High</td><td>⭐⭐⭐⭐</td><td>Enterprise</td><td>Excellent</td><td>Large teams, complex flows</td></tr>
      <tr><td><code style="background:var(--coral-bg);color:var(--coral);">GetX</code></td><td>Very Low</td><td>⭐</td><td>Small/medium</td><td>Poor</td><td>Rapid prototyping</td></tr>
    </table></div>
    <div class="info-box info-key"><strong>🔑 The Community Consensus (2024)</strong><p><strong>Riverpod</strong> has become the community favorite for new projects — it solves Provider's pain points while remaining approachable. <strong>BLoC</strong> dominates enterprise/large-team codebases where strict architecture and testability matter most. Avoid GetX in production for its poor separation of concerns.</p></div>
  </div>
  <!-- 6.4 Riverpod vs Bloc -->
  <div class="subsection" id="s6-4">
    <h3 style="color:var(--amber);">6.4 Architectural Comparison: Riverpod vs BLoC</h3>
    <p>Choosing between the two most popular state management solutions dictates your app's architecture.</p>
    <div class="grid-2">
      <div class="card glass glow-hover" style="border-top: 3px solid var(--blue);">
        <div class="card-title">Riverpod (Functional)</div>
        <p>Created by the author of Provider. It solves Provider's biggest flaw: <code>ProviderNotFoundException</code> at runtime. Riverpod is completely compile-time safe. It relies on global constant declarations that act as "keys" to state. It heavily promotes functional programming paradigms and immutable state.</p>
        <ul style="margin-top: 10px;">
          <li>✅ No BuildContext needed to read state</li>
          <li>✅ Safe merging/combining of states</li>
          <li>❌ Can be chaotic if globalProviders aren't structured well</li>
        </ul>
      </div>
      <div class="card glass glow-hover" style="border-top: 3px solid var(--purple);">
        <div class="card-title">BLoC (Event-Driven)</div>
        <p>Created by Felix Angelov (formerly at Google). It enforces a strict unidirectional data flow: <strong>UI dispatches Events ➡️ BLoC processes Events ➡️ BLoC emits State</strong>. It heavily relies on the Widget tree (InheritedWidget) for scoping.</p>
        <ul style="margin-top: 10px;">
          <li>✅ Extremely predictable and traceable</li>
          <li>✅ Standardized architecture across massive teams</li>
          <li>❌ High boilerplate (Events, States, Blocs files required)</li>
        </ul>
      </div>
    </div>
  </div>
</section>
'''

with open('flutter_notes.html', 'a') as f:
    f.write(s6)
print('Section 6 appended. Len:', len(s6))
