
s5 = '''
<!-- ═══════════════════════════════════════════ SECTION 5 ═══ -->
<section class="section" id="s5">
  <div class="section-header">
    <div class="section-icon" style="background:var(--blue-bg);">🧭</div>
    <div class="section-meta">
      <span class="section-badge" style="background:var(--blue-bg);color:var(--blue);">Intermediate</span>
      <div class="section-title" style="color:var(--blue);">Navigation</div>
      <div class="section-subtitle">Navigator 1.0 imperative stack, GoRouter declarative URL routing</div>
    </div>
  </div>

  <!-- 5.1 Navigator 1.0 -->
  <div class="subsection" id="s5-1">
    <h3 style="color:var(--blue);">5.1 Navigator 1.0 — Imperative</h3>
    <p>Navigator maintains a <strong>stack of Route objects</strong>. <code>push()</code> adds a route on top (new screen forward). <code>pop()</code> removes the top route (goes back). <code>pushReplacement</code> replaces the current route — use it after login to prevent the user going "back" to the login screen. <code>pushAndRemoveUntil</code> clears the stack — useful for logout flows.</p>
    <p>Routes can <strong>return data</strong> — <code>push()</code> returns a Future that resolves when the pushed route is popped. Pass data via constructor arguments. <code>WillPopScope</code> intercepts the back button to show confirmation dialogs or prevent accidental exits.</p>
    <div class="diagram">
      <svg viewBox="0 0 860 200" xmlns="http://www.w3.org/2000/svg">
        <defs><marker id="arr51" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="#8b949e" stroke-width="1.5" stroke-linecap="round"/></marker></defs>
        <text x="20" y="20" font-family="JetBrains Mono" font-size="11" fill="#8b949e">Navigator Stack — push adds on top, pop removes top</text>
        <!-- Stack state 1 -->
        <rect x="20" y="35" width="180" height="140" rx="8" fill="#161b22" stroke="#30363d"/>
        <text x="110" y="55" font-family="JetBrains Mono" font-size="10" fill="#8b949e" text-anchor="middle">Before</text>
        <rect x="30" y="60" width="160" height="40" rx="6" fill="#0d1e3b" stroke="#60a5fa" stroke-width="1.5"/>
        <text x="110" y="85" font-family="JetBrains Mono" font-size="11" fill="#60a5fa" text-anchor="middle">HomeScreen</text>
        <rect x="30" y="105" width="160" height="40" rx="6" fill="#161b22" stroke="#30363d"/>
        <text x="110" y="130" font-family="JetBrains Mono" font-size="11" fill="#8b949e" text-anchor="middle">(empty below)</text>
        <!-- push arrow -->
        <line x1="200" y1="110" x2="280" y2="80" stroke="#34d399" stroke-width="2" marker-end="url(#arr51)"/>
        <text x="230" y="75" font-family="JetBrains Mono" font-size="10" fill="#34d399">push()</text>
        <!-- Stack state 2 -->
        <rect x="280" y="35" width="180" height="140" rx="8" fill="#161b22" stroke="#30363d"/>
        <text x="370" y="55" font-family="JetBrains Mono" font-size="10" fill="#8b949e" text-anchor="middle">After push</text>
        <rect x="290" y="60" width="160" height="40" rx="6" fill="#1a1433" stroke="#a78bfa" stroke-width="2"/>
        <text x="370" y="85" font-family="JetBrains Mono" font-size="11" fill="#a78bfa" text-anchor="middle">DetailScreen ← TOP</text>
        <rect x="290" y="105" width="160" height="40" rx="6" fill="#0d1e3b" stroke="#60a5fa" stroke-width="1.5"/>
        <text x="370" y="130" font-family="JetBrains Mono" font-size="11" fill="#60a5fa" text-anchor="middle">HomeScreen</text>
        <!-- pop arrow -->
        <line x1="460" y1="80" x2="540" y2="110" stroke="#fb7185" stroke-width="2" marker-end="url(#arr51)"/>
        <text x="480" y="75" font-family="JetBrains Mono" font-size="10" fill="#fb7185">pop()</text>
        <!-- Stack state 3 -->
        <rect x="540" y="35" width="180" height="140" rx="8" fill="#161b22" stroke="#30363d"/>
        <text x="630" y="55" font-family="JetBrains Mono" font-size="10" fill="#8b949e" text-anchor="middle">After pop</text>
        <rect x="550" y="60" width="160" height="40" rx="6" fill="#0d1e3b" stroke="#60a5fa" stroke-width="1.5"/>
        <text x="630" y="85" font-family="JetBrains Mono" font-size="11" fill="#60a5fa" text-anchor="middle">HomeScreen ← TOP</text>
        <text x="630" y="130" font-family="JetBrains Mono" font-size="10" fill="#8b949e" text-anchor="middle">DetailScreen removed</text>
        <!-- pushReplacement -->
        <rect x="740" y="35" width="100" height="140" rx="8" fill="#0d2b22" stroke="#34d399"/>
        <text x="790" y="55" font-family="JetBrains Mono" font-size="9" fill="#34d399" text-anchor="middle">pushReplace</text>
        <rect x="750" y="65" width="80" height="35" rx="4" fill="#161b22" stroke="#34d399" stroke-width="1"/>
        <text x="790" y="87" font-family="JetBrains Mono" font-size="9" fill="#34d399" text-anchor="middle">HomeScreen</text>
        <text x="790" y="125" font-family="JetBrains Mono" font-size="9" fill="#8b949e" text-anchor="middle">LoginScreen</text>
        <text x="790" y="140" font-family="JetBrains Mono" font-size="9" fill="#fb7185" text-anchor="middle">removed</text>
      </svg>
    </div>
    <div class="code-wrap">
      <span class="code-label">Flutter</span>
      <button class="copy-btn">Copy</button>
<pre><span class="c">// Basic push</span>
<span class="t">Navigator</span>.<span class="m">of</span>(<span class="n">context</span>).<span class="m">push</span>(
  <span class="t">MaterialPageRoute</span>(<span class="n">builder</span>: (<span class="n">_</span>) =&gt; <span class="t">DetailScreen</span>(<span class="n">itemId</span>: <span class="n">item</span>.<span class="n">id</span>)),
);

<span class="c">// Push and await result (returns data on pop)</span>
<span class="k">final</span> <span class="t">String</span>? <span class="n">selectedColor</span> = <span class="k">await</span> <span class="t">Navigator</span>.<span class="m">of</span>(<span class="n">context</span>).<span class="m">push</span>&lt;<span class="t">String</span>&gt;(
  <span class="t">MaterialPageRoute</span>(<span class="n">builder</span>: (<span class="n">_</span>) =&gt; <span class="k">const</span> <span class="t">ColorPickerScreen</span>()),
);
<span class="k">if</span> (<span class="n">selectedColor</span> != <span class="k">null</span> &amp;&amp; <span class="n">mounted</span>) {
  <span class="m">_applyColor</span>(<span class="n">selectedColor</span>);
}

<span class="c">// Pop with result</span>
<span class="t">Navigator</span>.<span class="m">of</span>(<span class="n">context</span>).<span class="m">pop</span>(<span class="s">'red'</span>); <span class="c">// returns 'red' to awaiting push</span>

<span class="c">// After login — clear all back stack</span>
<span class="t">Navigator</span>.<span class="m">of</span>(<span class="n">context</span>).<span class="m">pushAndRemoveUntil</span>(
  <span class="t">MaterialPageRoute</span>(<span class="n">builder</span>: (<span class="n">_</span>) =&gt; <span class="k">const</span> <span class="t">HomeScreen</span>()),
  (<span class="n">route</span>) =&gt; <span class="k">false</span>, <span class="c">// remove all routes below</span>
);

<span class="c">// Custom page transition</span>
<span class="t">Navigator</span>.<span class="m">of</span>(<span class="n">context</span>).<span class="m">push</span>(<span class="t">PageRouteBuilder</span>(
  <span class="n">pageBuilder</span>: (<span class="n">_</span>, <span class="n">anim</span>, <span class="n">__</span>) =&gt; <span class="k">const</span> <span class="t">SettingsScreen</span>(),
  <span class="n">transitionsBuilder</span>: (<span class="n">_</span>, <span class="n">anim</span>, <span class="n">__</span>, <span class="n">child</span>) =&gt;
    <span class="t">SlideTransition</span>(
      <span class="n">position</span>: <span class="t">Tween</span>(<span class="n">begin</span>: <span class="k">const</span> <span class="t">Offset</span>(<span class="num">1</span>, <span class="num">0</span>), <span class="n">end</span>: <span class="t">Offset</span>.<span class="n">zero</span>)
        .<span class="m">animate</span>(<span class="t">CurvedAnimation</span>(<span class="n">parent</span>: <span class="n">anim</span>, <span class="n">curve</span>: <span class="t">Curves</span>.<span class="n">easeInOut</span>)),
      <span class="n">child</span>: <span class="n">child</span>,
    ),
  <span class="n">transitionDuration</span>: <span class="k">const</span> <span class="t">Duration</span>(<span class="n">milliseconds</span>: <span class="num">300</span>),
));</pre>
    </div>
    <div class="info-box info-tip"><strong>💡 Named Routes vs Direct Push</strong><p>Named routes (<code>pushNamed('/detail')</code>) reduce coupling but can't pass typed objects — you must use <code>arguments</code> and cast. Direct push with constructor arguments is type-safe and preferred. GoRouter solves this properly with path parameters.</p></div>
  </div>

  <!-- 5.2 GoRouter -->
  <div class="subsection" id="s5-2">
    <h3 style="color:var(--blue);">5.2 GoRouter — Recommended</h3>
    <p><strong>GoRouter</strong> is the Flutter team's recommended routing package. It's declarative and URL-based — every screen has a URL path, enabling deep linking on mobile and proper URL navigation on web. <strong>ShellRoute</strong> wraps routes in a persistent shell (like a bottom navigation bar) that survives navigation. <strong>redirect</strong> enables auth guards declaratively.</p>
    <p>Type-safe path and query parameters via <code>state.pathParameters</code> and <code>state.uri.queryParameters</code>. The <code>.family</code> pattern with GoRouter + Riverpod enables powerful nested route state management. GoRouter integrates with Flutter's <code>Navigator 2.0</code> under the hood, providing full deep link and back button support on all platforms.</p>
    <div class="diagram">
      <svg viewBox="0 0 860 240" xmlns="http://www.w3.org/2000/svg">
        <defs><marker id="arr52" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="#8b949e" stroke-width="1.5" stroke-linecap="round"/></marker></defs>
        <!-- Root -->
        <rect x="340" y="10" width="180" height="44" rx="8" fill="#0d1e3b" stroke="#60a5fa" stroke-width="2"/>
        <text x="430" y="29" font-family="JetBrains Mono" font-size="12" font-weight="700" fill="#60a5fa" text-anchor="middle">/ (root)</text>
        <text x="430" y="47" font-family="JetBrains Mono" font-size="10" fill="#8b949e" text-anchor="middle">GoRouter initialLocation</text>
        <!-- ShellRoute -->
        <rect x="200" y="90" width="240" height="44" rx="8" fill="#0d2b22" stroke="#34d399" stroke-width="1.5"/>
        <text x="320" y="108" font-family="JetBrains Mono" font-size="11" font-weight="700" fill="#34d399" text-anchor="middle">ShellRoute</text>
        <text x="320" y="126" font-family="JetBrains Mono" font-size="10" fill="#8b949e" text-anchor="middle">AppShell (BottomNav)</text>
        <!-- /home/feed -->
        <rect x="100" y="170" width="140" height="40" rx="6" fill="#161b22" stroke="#34d399"/>
        <text x="170" y="188" font-family="JetBrains Mono" font-size="10" fill="#34d399" text-anchor="middle">/home/feed</text>
        <text x="170" y="203" font-family="JetBrains Mono" font-size="9" fill="#8b949e" text-anchor="middle">FeedScreen</text>
        <!-- /home/search -->
        <rect x="260" y="170" width="140" height="40" rx="6" fill="#161b22" stroke="#34d399"/>
        <text x="330" y="188" font-family="JetBrains Mono" font-size="10" fill="#34d399" text-anchor="middle">/home/search</text>
        <text x="330" y="203" font-family="JetBrains Mono" font-size="9" fill="#8b949e" text-anchor="middle">SearchScreen</text>
        <!-- /profile/:userId -->
        <rect x="450" y="90" width="180" height="44" rx="8" fill="#161b22" stroke="#60a5fa"/>
        <text x="540" y="108" font-family="JetBrains Mono" font-size="10" fill="#60a5fa" text-anchor="middle">/profile/:userId</text>
        <text x="540" y="124" font-family="JetBrains Mono" font-size="9" fill="#8b949e" text-anchor="middle">ProfileScreen(userId)</text>
        <!-- /auth/login -->
        <rect x="660" y="90" width="160" height="44" rx="8" fill="#2b0f14" stroke="#fb7185"/>
        <text x="740" y="108" font-family="JetBrains Mono" font-size="10" fill="#fb7185" text-anchor="middle">/auth/login</text>
        <text x="740" y="124" font-family="JetBrains Mono" font-size="9" fill="#8b949e" text-anchor="middle">LoginScreen (redirect)</text>
        <!-- lines -->
        <line x1="430" y1="54" x2="320" y2="90" stroke="#8b949e" stroke-dasharray="5 3" marker-end="url(#arr52)"/>
        <line x1="430" y1="54" x2="540" y2="90" stroke="#8b949e" stroke-dasharray="5 3" marker-end="url(#arr52)"/>
        <line x1="430" y1="54" x2="740" y2="90" stroke="#fb7185" stroke-dasharray="5 3" marker-end="url(#arr52)"/>
        <line x1="320" y1="134" x2="170" y2="170" stroke="#34d399" stroke-dasharray="4 3" marker-end="url(#arr52)"/>
        <line x1="320" y1="134" x2="330" y2="170" stroke="#34d399" stroke-dasharray="4 3" marker-end="url(#arr52)"/>
      </svg>
    </div>
    <div class="code-wrap">
      <span class="code-label">Flutter</span>
      <button class="copy-btn">Copy</button>
<pre><span class="k">final</span> <span class="n">router</span> = <span class="t">GoRouter</span>(
  <span class="n">initialLocation</span>: <span class="s">'/home/feed'</span>,
  <span class="n">redirect</span>: (<span class="n">context</span>, <span class="n">state</span>) {
    <span class="c">// Auth guard — redirect to login if not authenticated</span>
    <span class="k">final</span> <span class="n">isLoggedIn</span> = <span class="n">ref</span>.<span class="m">read</span>(<span class="n">authProvider</span>).<span class="n">isLoggedIn</span>;
    <span class="k">final</span> <span class="n">isAuthRoute</span> = <span class="n">state</span>.<span class="n">uri</span>.<span class="n">path</span>.<span class="m">startsWith</span>(<span class="s">'/auth'</span>);
    <span class="k">if</span> (!<span class="n">isLoggedIn</span> &amp;&amp; !<span class="n">isAuthRoute</span>) <span class="k">return</span> <span class="s">'/auth/login'</span>;
    <span class="k">if</span> (<span class="n">isLoggedIn</span> &amp;&amp; <span class="n">isAuthRoute</span>) <span class="k">return</span> <span class="s">'/home/feed'</span>;
    <span class="k">return</span> <span class="k">null</span>; <span class="c">// no redirect</span>
  },
  <span class="n">routes</span>: [
    <span class="t">ShellRoute</span>(
      <span class="n">builder</span>: (<span class="n">ctx</span>, <span class="n">state</span>, <span class="n">child</span>) =&gt;
          <span class="t">AppShell</span>(<span class="n">child</span>: <span class="n">child</span>),
      <span class="n">routes</span>: [
        <span class="t">GoRoute</span>(
          <span class="n">path</span>: <span class="s">'/home/feed'</span>,
          <span class="n">builder</span>: (<span class="n">_</span>, <span class="n">__</span>) =&gt; <span class="k">const</span> <span class="t">FeedScreen</span>(),
        ),
        <span class="t">GoRoute</span>(
          <span class="n">path</span>: <span class="s">'/home/search'</span>,
          <span class="n">builder</span>: (<span class="n">_</span>, <span class="n">__</span>) =&gt; <span class="k">const</span> <span class="t">SearchScreen</span>(),
        ),
      ],
    ),
    <span class="t">GoRoute</span>(
      <span class="n">path</span>: <span class="s">'/profile/:userId'</span>,
      <span class="n">builder</span>: (<span class="n">ctx</span>, <span class="n">state</span>) =&gt; <span class="t">ProfileScreen</span>(
        <span class="n">userId</span>: <span class="n">state</span>.<span class="n">pathParameters</span>[<span class="s">'userId'</span>]!,
      ),
    ),
    <span class="t">GoRoute</span>(
      <span class="n">path</span>: <span class="s">'/auth/login'</span>,
      <span class="n">builder</span>: (<span class="n">_</span>, <span class="n">__</span>) =&gt; <span class="k">const</span> <span class="t">LoginScreen</span>(),
    ),
  ],
);

<span class="c">// Navigation in widgets</span>
<span class="n">context</span>.<span class="m">go</span>(<span class="s">'/home/search'</span>);            <span class="c">// replace current</span>
<span class="n">context</span>.<span class="m">push</span>(<span class="s">'/profile/user123'</span>);      <span class="c">// push onto stack</span>
<span class="n">context</span>.<span class="m">go</span>(<span class="s">'/profile/${user.id}'</span>);     <span class="c">// dynamic path</span></pre>
    </div>
    <div class="info-box info-key"><strong>🔑 go() vs push() in GoRouter</strong><p><code>context.go()</code> replaces the entire navigation stack with the new URL — good for tab switching. <code>context.push()</code> pushes on top of the current stack — good for detail screens where you need the back button.</p></div>
    <div class="table-wrap"><table>
      <tr><th>Feature</th><th>Navigator 1.0</th><th>GoRouter</th></tr>
      <tr><td>Deep linking</td><td>Manual setup</td><td>✅ Built-in</td></tr>
      <tr><td>Web URL support</td><td>❌ Limited</td><td>✅ Full URL bar support</td></tr>
      <tr><td>Auth redirects</td><td>Manual in initState</td><td>✅ redirect property</td></tr>
      <tr><td>Nested nav</td><td>Manual Navigator widgets</td><td>✅ ShellRoute</td></tr>
      <tr><td>Type safety</td><td>Cast from arguments</td><td>✅ pathParameters typed</td></tr>
    </table></div>
  </div>
  <!-- 5.3 Advanced go_router -->
  <div class="subsection" id="s5-3">
    <h3 style="color:var(--coral);">5.3 Advanced go_router (Redirection &amp; Shell)</h3>
    <p>Modern apps require complex routing logic: redirecting unauthenticated users from protected screens, or keeping a BottomNavigationBar persistent while changing screens inside it. <code>go_router</code> handles both perfectly.</p>
    <div class="code-wrap">
      <div class="mac-header">
        <div class="mac-dots"><div class="mac-dot-r"></div><div class="mac-dot-y"></div><div class="mac-dot-g"></div></div>
        <span class="code-label-mac">Dart</span>
        <button class="copy-btn">Copy</button>
      </div>
<pre><span class="c">// 1. Redirection (Auth Guards)</span>
<span class="k">final</span> <span class="n">router</span> = <span class="t">GoRouter</span>(
  <span class="n">initialLocation</span>: <span class="s">'/home'</span>,
  <span class="n">redirect</span>: (<span class="n">context</span>, <span class="n">state</span>) {
    <span class="k">final</span> <span class="n">isAuthenticated</span> = <span class="n">authService</span>.<span class="n">isLoggedIn</span>;
    <span class="k">final</span> <span class="n">isLoginRoute</span> = <span class="n">state</span>.<span class="n">uri</span>.<span class="m">toString</span>() == <span class="s">'/login'</span>;

    <span class="k">if</span> (!<span class="n">isAuthenticated</span> &amp;&amp; !<span class="n">isLoginRoute</span>) <span class="k">return</span> <span class="s">'/login'</span>;
    <span class="k">if</span> (<span class="n">isAuthenticated</span> &amp;&amp; <span class="n">isLoginRoute</span>) <span class="k">return</span> <span class="s">'/home'</span>;
    <span class="k">return</span> <span class="k">null</span>; <span class="c">// No redirect needed</span>
  },
  <span class="c">// Listen to an auth notifier to re-evaluate redirect immediately </span>
  <span class="n">refreshListenable</span>: <span class="n">authService</span>.<span class="n">notifier</span>,
  
  <span class="n">routes</span>: [
    <span class="c">// 2. ShellRoute (Persistent Bottom Nav)</span>
    <span class="t">ShellRoute</span>(
      <span class="n">builder</span>: (<span class="n">context</span>, <span class="n">state</span>, <span class="n">child</span>) {
        <span class="c">// The 'child' is the current inner route (Home, Profile, etc)</span>
        <span class="k">return</span> <span class="t">ScaffoldWithNavBar</span>(<span class="n">child</span>: <span class="n">child</span>);
      },
      <span class="n">routes</span>: [
        <span class="t">GoRoute</span>(<span class="n">path</span>: <span class="s">'/home'</span>, <span class="n">builder</span>: (<span class="n">_</span>, <span class="n">__</span>) =&gt; <span class="t">HomeScreen</span>()),
        <span class="t">GoRoute</span>(<span class="n">path</span>: <span class="s">'/profile'</span>, <span class="n">builder</span>: (<span class="n">_</span>, <span class="n">__</span>) =&gt; <span class="t">ProfileScreen</span>()),
      ]
    ),
  ],
);</pre>
    </div>
  </div>
</section>
'''

with open('flutter_notes.html', 'a') as f:
    f.write(s5)
print('Section 5 appended. Len:', len(s5))
