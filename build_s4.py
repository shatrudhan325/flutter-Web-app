
s4 = '''
<!-- ═══════════════════════════════════════════ SECTION 4 ═══ -->
<section class="section" id="s4">
  <div class="section-header">
    <div class="section-icon" style="background:var(--purple-bg);">🧩</div>
    <div class="section-meta">
      <span class="section-badge" style="background:var(--purple-bg);color:var(--purple);">Intermediate</span>
      <div class="section-title" style="color:var(--purple);">Widgets Deep Dive</div>
      <div class="section-subtitle">Text, forms, buttons, app shell, and custom widget composition</div>
    </div>
  </div>

  <!-- 4.1 Text & RichText -->
  <div class="subsection" id="s4-1">
    <h3 style="color:var(--purple);">4.1 Text &amp; RichText</h3>
    <p>The <strong>Text</strong> widget displays a string with uniform styling via <code>TextStyle</code>. For mixed styles within one block — bold words, colored links, inline icons — use <strong>RichText</strong> with a tree of <code>TextSpan</code> nodes. Each <code>TextSpan</code> inherits style from its parent unless overridden.</p>
    <p><strong>SelectableText</strong> allows users to copy text — important for code snippets and technical content. Set <code>overflow</code> and <code>maxLines</code> to control text clipping. <code>TextScaler</code> in Flutter 3.x replaces <code>textScaleFactor</code> for better accessibility scaling behavior.</p>
    <div class="code-wrap">
      <span class="code-label">Flutter</span>
      <button class="copy-btn">Copy</button>
<pre><span class="c">// RichText with mixed styles</span>
<span class="t">RichText</span>(
  <span class="n">text</span>: <span class="t">TextSpan</span>(
    <span class="n">style</span>: <span class="k">const</span> <span class="t">TextStyle</span>(<span class="n">fontSize</span>: <span class="num">16</span>, <span class="n">color</span>: <span class="t">Colors</span>.<span class="n">black87</span>),
    <span class="n">children</span>: [
      <span class="k">const</span> <span class="t">TextSpan</span>(<span class="n">text</span>: <span class="s">'Welcome to '</span>),
      <span class="t">TextSpan</span>(
        <span class="n">text</span>: <span class="s">'Flutter'</span>,
        <span class="n">style</span>: <span class="k">const</span> <span class="t">TextStyle</span>(
          <span class="n">fontWeight</span>: <span class="t">FontWeight</span>.<span class="n">bold</span>,
          <span class="n">color</span>: <span class="t">Colors</span>.<span class="n">blue</span>,
          <span class="n">decoration</span>: <span class="t">TextDecoration</span>.<span class="n">underline</span>,
        ),
        <span class="n">recognizer</span>: <span class="t">TapGestureRecognizer</span>()
          ..<span class="n">onTap</span> = () =&gt; <span class="m">launchUrl</span>(<span class="t">Uri</span>.<span class="m">parse</span>(<span class="s">'https://flutter.dev'</span>)),
      ),
      <span class="k">const</span> <span class="t">TextSpan</span>(<span class="n">text</span>: <span class="s">' — build beautiful apps!'</span>),
    ],
  ),
)

<span class="c">// Text with overflow handling</span>
<span class="t">Text</span>(
  <span class="n">longTitle</span>,
  <span class="n">maxLines</span>: <span class="num">2</span>,
  <span class="n">overflow</span>: <span class="t">TextOverflow</span>.<span class="n">ellipsis</span>,
  <span class="n">style</span>: <span class="t">Theme</span>.<span class="m">of</span>(<span class="n">context</span>).<span class="n">textTheme</span>.<span class="n">titleLarge</span>?.<span class="m">copyWith</span>(
    <span class="n">fontWeight</span>: <span class="t">FontWeight</span>.<span class="n">w600</span>,
    <span class="n">letterSpacing</span>: <span class="num">0.3</span>,
  ),
)

<span class="c">// SelectableText for copyable content</span>
<span class="k">const</span> <span class="t">SelectableText</span>(
  <span class="s">'flutter pub add provider'</span>,
  <span class="n">style</span>: <span class="t">TextStyle</span>(<span class="n">fontFamily</span>: <span class="s">'monospace'</span>, <span class="n">fontSize</span>: <span class="num">14</span>),
)</pre>
    </div>
    <div class="info-box info-tip"><strong>💡 TextTheme from Material</strong><p>Always use <code>Theme.of(context).textTheme</code> for consistent typography across your app. Material 3 defines: <code>displayLarge/Medium/Small</code>, <code>headlineLarge/..</code>, <code>titleLarge/..</code>, <code>bodyLarge/..</code>, <code>labelLarge/..</code>. Set them in <code>ThemeData.textTheme</code> once, use everywhere.</p></div>
  </div>

  <!-- 4.2 Forms -->
  <div class="subsection" id="s4-2">
    <h3 style="color:var(--purple);">4.2 Forms &amp; Validation</h3>
    <p>The <strong>Form</strong> widget with a <code>GlobalKey&lt;FormState&gt;</code> groups multiple <code>TextFormField</code> validators together. Calling <code>formKey.currentState!.validate()</code> triggers all validators simultaneously and returns true only if all pass. The validator function returns <code>null</code> for valid, or an error string to display.</p>
    <p><strong>TextEditingController</strong> gives programmatic access to the field's text and selection. <strong>FocusNode</strong> manages keyboard focus — moving focus to the next field on submit creates better UX. <strong>Always dispose</strong> both controllers and focus nodes in <code>dispose()</code> to prevent memory leaks.</p>
    <div class="code-wrap">
      <span class="code-label">Flutter</span>
      <button class="copy-btn">Copy</button>
<pre><span class="k">class</span> <span class="t">_LoginFormState</span> <span class="k">extends</span> <span class="t">State</span>&lt;<span class="t">LoginForm</span>&gt; {
  <span class="k">final</span> <span class="n">_formKey</span> = <span class="t">GlobalKey</span>&lt;<span class="t">FormState</span>&gt;();
  <span class="k">final</span> <span class="n">_emailCtrl</span> = <span class="t">TextEditingController</span>();
  <span class="k">final</span> <span class="n">_passCtrl</span> = <span class="t">TextEditingController</span>();
  <span class="k">final</span> <span class="n">_passFocus</span> = <span class="t">FocusNode</span>();
  <span class="t">bool</span> <span class="n">_obscure</span> = <span class="k">true</span>;

  <span class="ann">@override</span>
  <span class="k">void</span> <span class="m">dispose</span>() {
    <span class="n">_emailCtrl</span>.<span class="m">dispose</span>();
    <span class="n">_passCtrl</span>.<span class="m">dispose</span>();
    <span class="n">_passFocus</span>.<span class="m">dispose</span>();
    <span class="k">super</span>.<span class="m">dispose</span>();
  }

  <span class="ann">@override</span>
  <span class="t">Widget</span> <span class="m">build</span>(<span class="t">BuildContext</span> <span class="n">context</span>) {
    <span class="k">return</span> <span class="t">Form</span>(
      <span class="n">key</span>: <span class="n">_formKey</span>,
      <span class="n">autovalidateMode</span>: <span class="t">AutovalidateMode</span>.<span class="n">onUserInteraction</span>,
      <span class="n">child</span>: <span class="t">Column</span>(
        <span class="n">children</span>: [
          <span class="t">TextFormField</span>(
            <span class="n">controller</span>: <span class="n">_emailCtrl</span>,
            <span class="n">keyboardType</span>: <span class="t">TextInputType</span>.<span class="n">emailAddress</span>,
            <span class="n">textInputAction</span>: <span class="t">TextInputAction</span>.<span class="n">next</span>,
            <span class="n">onFieldSubmitted</span>: (<span class="n">_</span>) =&gt; <span class="n">_passFocus</span>.<span class="m">requestFocus</span>(),
            <span class="n">decoration</span>: <span class="k">const</span> <span class="t">InputDecoration</span>(<span class="n">labelText</span>: <span class="s">'Email'</span>),
            <span class="n">validator</span>: (<span class="n">v</span>) {
              <span class="k">if</span> (<span class="n">v</span> == <span class="k">null</span> || <span class="n">v</span>.<span class="m">isEmpty</span>) <span class="k">return</span> <span class="s">'Email required'</span>;
              <span class="k">if</span> (!<span class="n">v</span>.<span class="m">contains</span>(<span class="s">'@'</span>)) <span class="k">return</span> <span class="s">'Invalid email address'</span>;
              <span class="k">return</span> <span class="k">null</span>; <span class="c">// valid</span>
            },
          ),
          <span class="t">TextFormField</span>(
            <span class="n">controller</span>: <span class="n">_passCtrl</span>,
            <span class="n">focusNode</span>: <span class="n">_passFocus</span>,
            <span class="n">obscureText</span>: <span class="n">_obscure</span>,
            <span class="n">decoration</span>: <span class="t">InputDecoration</span>(
              <span class="n">labelText</span>: <span class="s">'Password'</span>,
              <span class="n">suffixIcon</span>: <span class="t">IconButton</span>(
                <span class="n">icon</span>: <span class="t">Icon</span>(<span class="n">_obscure</span> ? <span class="t">Icons</span>.<span class="n">visibility</span> : <span class="t">Icons</span>.<span class="n">visibility_off</span>),
                <span class="n">onPressed</span>: () =&gt; <span class="m">setState</span>(() =&gt; <span class="n">_obscure</span> = !<span class="n">_obscure</span>),
              ),
            ),
            <span class="n">validator</span>: (<span class="n">v</span>) {
              <span class="k">if</span> (<span class="n">v</span> == <span class="k">null</span> || <span class="n">v</span>.<span class="n">length</span> &lt; <span class="num">8</span>) <span class="k">return</span> <span class="s">'Min 8 characters'</span>;
              <span class="k">return</span> <span class="k">null</span>;
            },
          ),
          <span class="t">ElevatedButton</span>(
            <span class="n">onPressed</span>: () {
              <span class="k">if</span> (<span class="n">_formKey</span>.<span class="n">currentState</span>!.<span class="m">validate</span>()) {
                <span class="m">_submitLogin</span>(<span class="n">_emailCtrl</span>.<span class="n">text</span>, <span class="n">_passCtrl</span>.<span class="n">text</span>);
              }
            },
            <span class="n">child</span>: <span class="k">const</span> <span class="t">Text</span>(<span class="s">'Sign In'</span>),
          ),
        ],
      ),
    );
  }
}</pre>
    </div>
    <div class="info-box info-warn"><strong>⚠️ Always Dispose Controllers</strong><p>Every <code>TextEditingController</code> and <code>FocusNode</code> hold resources. Forgetting <code>dispose()</code> causes memory leaks — especially problematic in list items where widgets are created and destroyed frequently.</p></div>
  </div>

  <!-- 4.3 Buttons -->
  <div class="subsection" id="s4-3">
    <h3 style="color:var(--purple);">4.3 Buttons Deep Dive</h3>
    <p>Flutter's Material 3 button hierarchy: <strong>FilledButton</strong> (highest emphasis, primary actions) → <strong>ElevatedButton</strong> → <strong>OutlinedButton</strong> → <strong>TextButton</strong> (lowest emphasis). <strong>IconButton</strong> for icon-only actions. <strong>FloatingActionButton</strong> for the primary screen action.</p>
    <p><strong>InkWell</strong> wraps any widget with Material ripple effects and gesture detection — essential for custom interactive components. Wrap with <strong>Ink</strong> when you need a colored background that shows correct ripple clipping inside a Container.</p>
    <div class="code-wrap">
      <span class="code-label">Flutter</span>
      <button class="copy-btn">Copy</button>
<pre><span class="c">// All button types</span>
<span class="t">FilledButton</span>(<span class="n">onPressed</span>: () {}, <span class="n">child</span>: <span class="k">const</span> <span class="t">Text</span>(<span class="s">'Primary Action'</span>))
<span class="t">ElevatedButton</span>.<span class="m">icon</span>(<span class="n">onPressed</span>: () {}, <span class="n">icon</span>: <span class="k">const</span> <span class="t">Icon</span>(<span class="t">Icons</span>.<span class="n">add</span>), <span class="n">label</span>: <span class="k">const</span> <span class="t">Text</span>(<span class="s">'Add'</span>))
<span class="t">OutlinedButton</span>(<span class="n">onPressed</span>: () {}, <span class="n">child</span>: <span class="k">const</span> <span class="t">Text</span>(<span class="s">'Secondary'</span>))
<span class="t">TextButton</span>(<span class="n">onPressed</span>: () {}, <span class="n">child</span>: <span class="k">const</span> <span class="t">Text</span>(<span class="s">'Learn more'</span>))
<span class="t">IconButton</span>(<span class="n">onPressed</span>: () {}, <span class="n">icon</span>: <span class="k">const</span> <span class="t">Icon</span>(<span class="t">Icons</span>.<span class="n">favorite</span>))

<span class="c">// Custom ButtonStyle with MaterialStateProperty</span>
<span class="t">ElevatedButton</span>(
  <span class="n">style</span>: <span class="t">ButtonStyle</span>(
    <span class="n">backgroundColor</span>: <span class="t">MaterialStateProperty</span>.<span class="m">resolveWith</span>((<span class="n">states</span>) {
      <span class="k">if</span> (<span class="n">states</span>.<span class="m">contains</span>(<span class="t">MaterialState</span>.<span class="n">pressed</span>)) <span class="k">return</span> <span class="t">Colors</span>.<span class="n">purple</span>[<span class="num">800</span>];
      <span class="k">if</span> (<span class="n">states</span>.<span class="m">contains</span>(<span class="t">MaterialState</span>.<span class="n">disabled</span>)) <span class="k">return</span> <span class="t">Colors</span>.<span class="n">grey</span>;
      <span class="k">return</span> <span class="t">Colors</span>.<span class="n">purple</span>;
    }),
    <span class="n">shape</span>: <span class="t">MaterialStateProperty</span>.<span class="m">all</span>(
      <span class="t">RoundedRectangleBorder</span>(<span class="n">borderRadius</span>: <span class="t">BorderRadius</span>.<span class="m">circular</span>(<span class="num">12</span>)),
    ),
  ),
  <span class="n">onPressed</span>: <span class="n">isLoading</span> ? <span class="k">null</span> : <span class="n">_handleSubmit</span>,
  <span class="n">child</span>: <span class="k">const</span> <span class="t">Text</span>(<span class="s">'Submit'</span>),
)

<span class="c">// InkWell — custom clickable card with ripple</span>
<span class="t">Material</span>(
  <span class="n">color</span>: <span class="t">Colors</span>.<span class="n">blue</span>[<span class="num">50</span>],
  <span class="n">borderRadius</span>: <span class="t">BorderRadius</span>.<span class="m">circular</span>(<span class="num">12</span>),
  <span class="n">child</span>: <span class="t">InkWell</span>(
    <span class="n">borderRadius</span>: <span class="t">BorderRadius</span>.<span class="m">circular</span>(<span class="num">12</span>),
    <span class="n">onTap</span>: <span class="n">onCardTap</span>,
    <span class="n">onLongPress</span>: <span class="n">onCardLongPress</span>,
    <span class="n">child</span>: <span class="k">const</span> <span class="t">Padding</span>(
      <span class="n">padding</span>: <span class="t">EdgeInsets</span>.<span class="m">all</span>(<span class="num">16</span>),
      <span class="n">child</span>: <span class="t">Text</span>(<span class="s">'Tap me!'</span>),
    ),
  ),
)</pre>
    </div>
    <div class="table-wrap"><table>
      <tr><th>Button</th><th>Emphasis</th><th>Use When</th><th>Has Background</th></tr>
      <tr><td><code style="background:var(--blue-bg);color:var(--blue);">FilledButton</code></td><td>Highest</td><td>Primary CTA, single key action</td><td>✅ Filled color</td></tr>
      <tr><td><code style="background:var(--purple-bg);color:var(--purple);">ElevatedButton</code></td><td>High</td><td>Important secondary actions</td><td>✅ Elevated</td></tr>
      <tr><td><code style="background:var(--teal-bg);color:var(--teal);">OutlinedButton</code></td><td>Medium</td><td>Secondary/alternative actions</td><td>❌ Outlined</td></tr>
      <tr><td><code style="background:var(--bg3);color:var(--muted);">TextButton</code></td><td>Lowest</td><td>In dialogs, tertiary actions</td><td>❌ Text only</td></tr>
    </table></div>
  </div>

  <!-- 4.4 App Shell -->
  <div class="subsection" id="s4-4">
    <h3 style="color:var(--purple);">4.4 App Shell Widgets</h3>
    <p><strong>Scaffold</strong> provides the visual structure of a screen — AppBar, body, drawer, FAB, bottom bar. <strong>SliverAppBar</strong> collapses as you scroll — useful for immersive headers. <strong>NavigationBar</strong> (Material 3) replaces the older <code>BottomNavigationBar</code> with better theming and adaptive behavior.</p>
    <p><strong>DefaultTabController</strong> with <code>TabBar</code> and <code>TabBarView</code> creates a tabbed UI. For modal bottom sheets, <code>showModalBottomSheet</code> shows a dismissible sheet; <code>showBottomSheet</code> shows a persistent one.</p>
    <div class="diagram">
      <svg viewBox="0 0 860 260" xmlns="http://www.w3.org/2000/svg">
        <rect x="160" y="10" width="540" height="240" rx="12" fill="#161b22" stroke="#30363d" stroke-width="2"/>
        <!-- AppBar -->
        <rect x="160" y="10" width="540" height="48" rx="12" fill="#1a1433" stroke="#a78bfa" stroke-width="1.5"/>
        <text x="340" y="34" font-family="JetBrains Mono" font-size="11" font-weight="700" fill="#a78bfa">AppBar</text>
        <text x="340" y="50" font-family="JetBrains Mono" font-size="9" fill="#8b949e">leading / title / actions</text>
        <rect x="170" y="58" width="28" height="28" rx="4" fill="#0d1117" stroke="#30363d"/>
        <text x="184" y="77" font-family="JetBrains Mono" font-size="9" fill="#8b949e" text-anchor="middle">☰</text>
        <rect x="654" y="58" width="28" height="28" rx="4" fill="#0d1117" stroke="#30363d"/>
        <text x="668" y="77" font-family="JetBrains Mono" font-size="9" fill="#8b949e" text-anchor="middle">⋮</text>
        <!-- Drawer indicator -->
        <rect x="60" y="10" width="90" height="160" rx="8" fill="#0d2b22" stroke="#34d399" stroke-width="1.5" stroke-dasharray="5 3"/>
        <text x="105" y="40" font-family="JetBrains Mono" font-size="10" font-weight="700" fill="#34d399" text-anchor="middle">Drawer</text>
        <text x="105" y="56" font-family="JetBrains Mono" font-size="9" fill="#8b949e" text-anchor="middle">slides from</text>
        <text x="105" y="70" font-family="JetBrains Mono" font-size="9" fill="#8b949e" text-anchor="middle">left edge</text>
        <!-- Body -->
        <rect x="170" y="96" width="520" height="110" rx="6" fill="#0d1117" stroke="#30363d" stroke-width="1"/>
        <text x="430" y="148" font-family="JetBrains Mono" font-size="12" font-weight="700" fill="#8b949e" text-anchor="middle">body</text>
        <text x="430" y="166" font-family="JetBrains Mono" font-size="10" fill="#8b949e" text-anchor="middle">main content area (Scaffold child)</text>
        <!-- FAB -->
        <rect x="620" y="170" width="60" height="36" rx="18" fill="#1a1433" stroke="#a78bfa" stroke-width="1.5"/>
        <text x="650" y="193" font-family="JetBrains Mono" font-size="11" fill="#a78bfa" text-anchor="middle">FAB</text>
        <!-- BottomBar -->
        <rect x="160" y="208" width="540" height="42" rx="8" fill="#2b1d0d" stroke="#fbbf24" stroke-width="1.5"/>
        <text x="340" y="225" font-family="JetBrains Mono" font-size="11" font-weight="700" fill="#fbbf24">NavigationBar</text>
        <text x="340" y="242" font-family="JetBrains Mono" font-size="9" fill="#8b949e">Home · Search · Profile · Settings</text>
      </svg>
    </div>
    <div class="code-wrap">
      <span class="code-label">Flutter</span>
      <button class="copy-btn">Copy</button>
<pre><span class="c">// Modern app shell with NavigationBar (Material 3)</span>
<span class="k">class</span> <span class="t">AppShell</span> <span class="k">extends</span> <span class="t">StatefulWidget</span> {
  <span class="k">const</span> <span class="t">AppShell</span>({<span class="k">super</span>.<span class="n">key</span>});
  <span class="ann">@override</span>
  <span class="t">State</span>&lt;<span class="t">AppShell</span>&gt; <span class="m">createState</span>() =&gt; <span class="t">_AppShellState</span>();
}

<span class="k">class</span> <span class="t">_AppShellState</span> <span class="k">extends</span> <span class="t">State</span>&lt;<span class="t">AppShell</span>&gt; {
  <span class="t">int</span> <span class="n">_selectedIndex</span> = <span class="num">0</span>;
  <span class="k">final</span> <span class="n">_screens</span> = <span class="k">const</span> [<span class="t">FeedScreen</span>(), <span class="t">SearchScreen</span>(), <span class="t">ProfileScreen</span>()];

  <span class="ann">@override</span>
  <span class="t">Widget</span> <span class="m">build</span>(<span class="t">BuildContext</span> <span class="n">context</span>) {
    <span class="k">return</span> <span class="t">Scaffold</span>(
      <span class="n">body</span>: <span class="n">_screens</span>[<span class="n">_selectedIndex</span>],
      <span class="n">bottomNavigationBar</span>: <span class="t">NavigationBar</span>(
        <span class="n">selectedIndex</span>: <span class="n">_selectedIndex</span>,
        <span class="n">onDestinationSelected</span>: (<span class="n">i</span>) =&gt; <span class="m">setState</span>(() =&gt; <span class="n">_selectedIndex</span> = <span class="n">i</span>),
        <span class="n">destinations</span>: <span class="k">const</span> [
          <span class="t">NavigationDestination</span>(<span class="n">icon</span>: <span class="t">Icon</span>(<span class="t">Icons</span>.<span class="n">home</span>), <span class="n">label</span>: <span class="s">'Home'</span>),
          <span class="t">NavigationDestination</span>(<span class="n">icon</span>: <span class="t">Icon</span>(<span class="t">Icons</span>.<span class="n">search</span>), <span class="n">label</span>: <span class="s">'Search'</span>),
          <span class="t">NavigationDestination</span>(<span class="n">icon</span>: <span class="t">Icon</span>(<span class="t">Icons</span>.<span class="n">person</span>), <span class="n">label</span>: <span class="s">'Profile'</span>),
        ],
      ),
    );
  }
}</pre>
    </div>
    <div class="info-box info-key"><strong>🔑 IndexedStack for Persistent State</strong><p>Use <code>IndexedStack</code> instead of <code>_screens[_selectedIndex]</code> to preserve the state of each tab page when switching. <code>IndexedStack</code> builds all children but only shows the one at the current index, keeping their state alive.</p></div>
  </div>

  <!-- 4.5 Custom Widgets -->
  <div class="subsection" id="s4-5">
    <h3 style="color:var(--purple);">4.5 Custom Widgets</h3>
    <p>Composition is the Flutter way. Instead of one monolithic widget, extract smaller purpose-built widgets. Extract when: build() exceeds 60-80 lines, the widget is used in 2+ places, or it has a clearly defined responsibility. <strong>const constructors</strong> are the single biggest performance optimization — mark as <code>const</code> whenever possible to eliminate rebuilds.</p>
    <div class="code-wrap">
      <span class="code-label">Flutter</span>
      <button class="copy-btn">Copy</button>
<pre><span class="c">// Custom ProductCard with slot pattern</span>
<span class="k">class</span> <span class="t">ProductCard</span> <span class="k">extends</span> <span class="t">StatelessWidget</span> {
  <span class="k">final</span> <span class="t">String</span> <span class="n">imageUrl</span>;
  <span class="k">final</span> <span class="t">String</span> <span class="n">name</span>;
  <span class="k">final</span> <span class="t">double</span> <span class="n">price</span>;
  <span class="k">final</span> <span class="t">int</span> <span class="n">rating</span>;
  <span class="k">final</span> <span class="t">VoidCallback</span> <span class="n">onAddToCart</span>;
  <span class="k">final</span> <span class="t">Widget</span>? <span class="n">badge</span>;  <span class="c">// slot for optional badge</span>

  <span class="k">const</span> <span class="t">ProductCard</span>({
    <span class="k">super</span>.<span class="n">key</span>,
    <span class="k">required</span> <span class="k">this</span>.<span class="n">imageUrl</span>,
    <span class="k">required</span> <span class="k">this</span>.<span class="n">name</span>,
    <span class="k">required</span> <span class="k">this</span>.<span class="n">price</span>,
    <span class="k">required</span> <span class="k">this</span>.<span class="n">rating</span>,
    <span class="k">required</span> <span class="k">this</span>.<span class="n">onAddToCart</span>,
    <span class="k">this</span>.<span class="n">badge</span>,  <span class="c">// optional slot</span>
  });

  <span class="ann">@override</span>
  <span class="t">Widget</span> <span class="m">build</span>(<span class="t">BuildContext</span> <span class="n">context</span>) {
    <span class="k">return</span> <span class="t">Card</span>(
      <span class="n">clipBehavior</span>: <span class="t">Clip</span>.<span class="n">antiAlias</span>,
      <span class="n">child</span>: <span class="t">Stack</span>(
        <span class="n">children</span>: [
          <span class="t">Column</span>(
            <span class="n">crossAxisAlignment</span>: <span class="t">CrossAxisAlignment</span>.<span class="n">start</span>,
            <span class="n">children</span>: [
              <span class="t">_ProductImage</span>(<span class="n">url</span>: <span class="n">imageUrl</span>),
              <span class="t">_ProductInfo</span>(<span class="n">name</span>: <span class="n">name</span>, <span class="n">price</span>: <span class="n">price</span>, <span class="n">rating</span>: <span class="n">rating</span>),
              <span class="t">_AddToCartButton</span>(<span class="n">onPressed</span>: <span class="n">onAddToCart</span>),
            ],
          ),
          <span class="k">if</span> (<span class="n">badge</span> != <span class="k">null</span>)
            <span class="t">Positioned</span>(<span class="n">top</span>: <span class="num">8</span>, <span class="n">right</span>: <span class="num">8</span>, <span class="n">child</span>: <span class="n">badge</span>!),
        ],
      ),
    );
  }
}</pre>
    </div>
    <div class="info-box info-tip"><strong>💡 const Widget = Zero Rebuild Cost</strong><p>A <code>const</code> widget is canonicalized — Flutter reuses the same instance across rebuilds. Adding <code>const</code> to a widget that doesn't depend on runtime data is the easiest performance win in Flutter. Enable the <code>prefer_const_constructors</code> lint rule to catch missed opportunities.</p></div>
  </div>
  <!-- 4.4 CustomPaint -->
  <div class="subsection" id="s4-4">
    <h3 style="color:var(--amber);">4.4 CustomPaint &amp; Core Graphics</h3>
    <p>When row, columns, and standard widgets aren't enough (e.g. for drawing charts, complex custom shapes, or painting games), you use <code>CustomPaint</code>. It gives you raw access to a <code>Canvas</code> and a <code>Size</code>, allowing you to draw lines, paths, circles, and gradients directly via Skia/Impeller.</p>
    <div class="code-wrap">
      <div class="mac-header">
        <div class="mac-dots"><div class="mac-dot-r"></div><div class="mac-dot-y"></div><div class="mac-dot-g"></div></div>
        <span class="code-label-mac">Dart</span>
        <button class="copy-btn">Copy</button>
      </div>
<pre><span class="k">class</span> <span class="t">WavePainter</span> <span class="k">extends</span> <span class="t">CustomPainter</span> {
  <span class="ann">@override</span>
  <span class="k">void</span> <span class="m">paint</span>(<span class="t">Canvas</span> <span class="n">canvas</span>, <span class="t">Size</span> <span class="n">size</span>) {
    <span class="k">final</span> <span class="n">paint</span> = <span class="t">Paint</span>()
      ..<span class="n">color</span> = <span class="t">Colors</span>.<span class="n">blueAccent</span>
      ..<span class="n">style</span> = <span class="t">PaintingStyle</span>.<span class="n">fill</span>;

    <span class="k">final</span> <span class="n">path</span> = <span class="t">Path</span>();
    <span class="n">path</span>.<span class="m">moveTo</span>(<span class="num">0</span>, <span class="n">size</span>.<span class="n">height</span> * <span class="num">0.5</span>);
    <span class="c">// Simple bezier curve mimicking a wave</span>
    <span class="n">path</span>.<span class="m">quadraticBezierTo</span>(
      <span class="n">size</span>.<span class="n">width</span> * <span class="num">0.5</span>, <span class="n">size</span>.<span class="n">height</span> * <span class="num">0.2</span>, <span class="c">// Control point</span>
      <span class="n">size</span>.<span class="n">width</span>, <span class="n">size</span>.<span class="n">height</span> * <span class="num">0.5</span>        <span class="c">// End point</span>
    );
    <span class="n">path</span>.<span class="m">lineTo</span>(<span class="n">size</span>.<span class="n">width</span>, <span class="n">size</span>.<span class="n">height</span>);
    <span class="n">path</span>.<span class="m">lineTo</span>(<span class="num">0</span>, <span class="n">size</span>.<span class="n">height</span>);
    <span class="n">path</span>.<span class="m">close</span>();

    <span class="n">canvas</span>.<span class="m">drawPath</span>(<span class="n">path</span>, <span class="n">paint</span>);
  }

  <span class="ann">@override</span>
  <span class="t">bool</span> <span class="m">shouldRepaint</span>(<span class="k">covariant</span> <span class="t">CustomPainter</span> <span class="n">oldDelegate</span>) {
    <span class="k">return</span> <span class="k">false</span>; <span class="c">// Only return true if properties changed</span>
  }
}</pre>
    </div>
  </div>
</section>
'''

with open('flutter_notes.html', 'a') as f:
    f.write(s4)
print('Section 4 appended. Len:', len(s4))
