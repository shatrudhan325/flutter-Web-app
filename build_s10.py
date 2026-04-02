s10 = """
<!-- SECTION 10 -->
<section class="section" id="s10">
  <div class="section-header">
    <div class="section-icon" style="background:var(--green-bg);">🏗️</div>
    <div class="section-meta">
      <span class="section-badge" style="background:var(--green-bg);color:var(--green);">Architecture</span>
      <div class="section-title" style="color:var(--green);">Clean Architecture &amp; Production</div>
      <div class="section-subtitle">Scalable Code Structure, Testing strategies, Environments, and DI</div>
    </div>
  </div>

  <!-- 10.1 Clean Architecture -->
  <div class="subsection" id="s10-1">
    <h3 style="color:var(--green);">10.1 Clean Architecture Deep Dive</h3>
    <p>A "Big Ball of Mud" where API calls, business logic, and UI are mixed together in <code>StatefulWidget</code>s makes the app impossible to maintain or test. <strong>Clean Architecture</strong> divides responsibilities into independent layers. The central principle is the <strong>Dependency Rule</strong>: source code dependencies must only point inwards.</p>
    
    <div class="diagram">
      <svg viewBox="0 0 860 300" xmlns="http://www.w3.org/2000/svg">
        <defs>
          <marker id="arr10" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="#8b949e" stroke-width="1.5" stroke-linecap="round"/></marker>
          <marker id="arr-rev" viewBox="0 0 10 10" refX="2" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M8 1L2 5L8 9" fill="none" stroke="#60a5fa" stroke-width="1.5" stroke-linecap="round"/></marker>
        </defs>

        <!-- Presentation -->
        <rect x="40" y="40" width="220" height="150" rx="10" fill="#0d1e3b" stroke="#60a5fa" stroke-width="1.5"/>
        <text x="150" y="65" font-family="JetBrains Mono" font-size="13" font-weight="700" fill="#60a5fa" text-anchor="middle">Presentation Layer</text>
        <rect x="60" y="80" width="180" height="40" rx="6" fill="#161b22" stroke="#30363d"/>
        <text x="150" y="105" font-family="JetBrains Mono" font-size="11" fill="#e6edf3" text-anchor="middle">Pages &amp; Widgets</text>
        <rect x="60" y="130" width="180" height="40" rx="6" fill="#161b22" stroke="#30363d"/>
        <text x="150" y="155" font-family="JetBrains Mono" font-size="11" fill="#e6edf3" text-anchor="middle">Bloc / Riverpod (State)</text>

        <!-- Domain -->
        <rect x="320" y="40" width="220" height="220" rx="10" fill="#1a1433" stroke="#a78bfa" stroke-width="2"/>
        <text x="430" y="65" font-family="JetBrains Mono" font-size="13" font-weight="700" fill="#a78bfa" text-anchor="middle">Domain Layer (Core)</text>
        <text x="430" y="85" font-family="JetBrains Mono" font-size="10" fill="#8b949e" text-anchor="middle">No Flutter Dependencies!</text>
        <rect x="340" y="100" width="180" height="40" rx="6" fill="#161b22" stroke="#30363d"/>
        <text x="430" y="125" font-family="JetBrains Mono" font-size="11" fill="#e6edf3" text-anchor="middle">Use Cases</text>
        <rect x="340" y="150" width="180" height="40" rx="6" fill="#161b22" stroke="#30363d"/>
        <text x="430" y="175" font-family="JetBrains Mono" font-size="11" fill="#e6edf3" text-anchor="middle">Entities (Business Data)</text>
        <rect x="340" y="200" width="180" height="40" rx="6" fill="#161b22" stroke="#a78bfa" stroke-dasharray="4 2"/>
        <text x="430" y="225" font-family="JetBrains Mono" font-size="11" fill="#a78bfa" text-anchor="middle">Repository Interfaces</text>

        <!-- Data -->
        <rect x="600" y="40" width="220" height="200" rx="10" fill="#0d2b22" stroke="#34d399" stroke-width="1.5"/>
        <text x="710" y="65" font-family="JetBrains Mono" font-size="13" font-weight="700" fill="#34d399" text-anchor="middle">Data Layer</text>
        <rect x="620" y="80" width="180" height="40" rx="6" fill="#161b22" stroke="#30363d"/>
        <text x="710" y="105" font-family="JetBrains Mono" font-size="11" fill="#e6edf3" text-anchor="middle">Repositories Impl</text>
        <rect x="620" y="130" width="180" height="40" rx="6" fill="#161b22" stroke="#30363d"/>
        <text x="710" y="155" font-family="JetBrains Mono" font-size="11" fill="#e6edf3" text-anchor="middle">Models (JSON parsing)</text>
        <rect x="620" y="180" width="180" height="40" rx="6" fill="#161b22" stroke="#30363d"/>
        <text x="710" y="205" font-family="JetBrains Mono" font-size="11" fill="#e6edf3" text-anchor="middle">Data Sources (API/DB)</text>

        <!-- Dependencies -->
        <line x1="260" y1="120" x2="320" y2="120" stroke="#a78bfa" stroke-width="1.5" marker-end="url(#arr10)"/>
        <line x1="600" y1="220" x2="520" y2="220" stroke="#a78bfa" stroke-width="1.5" marker-end="url(#arr10)"/>
        <text x="560" y="245" font-family="Syne" font-size="11" fill="#8b949e" text-anchor="middle">Implements Interface</text>
      </svg>
    </div>

    <ul>
      <li><strong>Domain Layer:</strong> The heart of the software. Contains pure Dart <code>Entities</code> (like <code>User</code>) and <code>UseCases</code> (like <code>LoginUserUseCase</code>). It knows absolutely nothing about HTTP, JSON, or Flutter UI. It defines abstract <code>UserRepository</code> interfaces.</li>
      <li><strong>Data Layer:</strong> Contains the implementation of the Domain's Repositories. It fetches data via <code>DataSource</code>s (API or local DB), parses JSON into <code>Model</code>s, and converts them to pure <code>Entities</code>.</li>
      <li><strong>Presentation Layer:</strong> Knows only about the Domain layer. State managers (Bloc/Riverpod) call UseCases, get Entities back, and update local state to trigger Widget rebuilds.</li>
    </ul>

    <div class="code-wrap">
      <span class="code-label">Dart (Dependency Inversion)</span>
      <button class="copy-btn">Copy</button>
<pre><span class="c">// 1. DOMAIN LAYER</span>
<span class="k">class</span> <span class="t">User</span> { <span class="k">final</span> <span class="t">String</span> <span class="n">name</span>; <span class="k">const</span> <span class="t">User</span>(<span class="k">this</span>.<span class="n">name</span>); }

<span class="k">abstract class</span> <span class="t">AuthRepository</span> {
  <span class="k">Future</span>&lt;<span class="t">User</span>&gt; <span class="m">login</span>(<span class="t">String</span> <span class="n">email</span>, <span class="t">String</span> <span class="n">pass</span>);
}

<span class="k">class</span> <span class="t">LoginUseCase</span> {
  <span class="k">final</span> <span class="t">AuthRepository</span> <span class="n">repo</span>;
  <span class="k">const</span> <span class="t">LoginUseCase</span>(<span class="k">this</span>.<span class="n">repo</span>); <span class="c">// Expects interface, not implementation!</span>

  <span class="k">Future</span>&lt;<span class="t">User</span>&gt; <span class="m">execute</span>(<span class="t">String</span> <span class="n">e</span>, <span class="t">String</span> <span class="n">p</span>) {
    <span class="k">if</span> (!<span class="n">e</span>.<span class="m">contains</span>(<span class="s">'@'</span>)) <span class="k">throw</span> <span class="t">Exception</span>(<span class="s">'Invalid email'</span>);
    <span class="k">return</span> <span class="n">repo</span>.<span class="m">login</span>(<span class="n">e</span>, <span class="n">p</span>);
  }
}

<span class="c">// 2. DATA LAYER</span>
<span class="k">class</span> <span class="t">AuthRepositoryImpl</span> <span class="k">implements</span> <span class="t">AuthRepository</span> {
  <span class="k">final</span> <span class="t">ApiDataSource</span> <span class="n">api</span>;
  <span class="t">AuthRepositoryImpl</span>(<span class="k">this</span>.<span class="n">api</span>);

  <span class="ann">@override</span>
  <span class="k">Future</span>&lt;<span class="t">User</span>&gt; <span class="m">login</span>(<span class="t">String</span> <span class="n">email</span>, <span class="t">String</span> <span class="n">pass</span>) <span class="k">async</span> {
    <span class="k">final</span> <span class="n">jsonStr</span> = <span class="k">await</span> <span class="n">api</span>.<span class="m">post</span>(<span class="s">'/login'</span>, {<span class="s">'e'</span>:<span class="n">email</span>, <span class="s">'p'</span>:<span class="n">pass</span>});
    <span class="c">// Parse JSON model, convert to pure User entity, return it</span>
    <span class="k">return</span> <span class="t">UserModel</span>.<span class="m">fromJson</span>(<span class="n">jsonStr</span>).<span class="m">toEntity</span>();
  }
}</pre>
    </div>
  </div>

  <!-- 10.2 Dependency Injection -->
  <div class="subsection" id="s10-2">
    <h3 style="color:var(--green);">10.2 Dependency Injection (DI)</h3>
    <p>Clean architecture requires passing dependencies (repositories, data sources) into objects rather than objects creating them internally. To wire the whole app together, you use a <strong>DI container</strong> or <strong>Service Locator</strong>.</p>
    <ul>
      <li><strong>get_it:</strong> The most popular service locator in Flutter. Extremely lightweight.</li>
      <li><strong>Riverpod / Provider:</strong> While state managers, they are excellent tools for passing dependencies down the tree safely.</li>
    </ul>
    <div class="code-wrap">
      <span class="code-label">Dart (get_it DI Setup)</span>
      <button class="copy-btn">Copy</button>
<pre><span class="k">final</span> <span class="n">sl</span> = <span class="t">GetIt</span>.<span class="n">instance</span>;

<span class="k">void</span> <span class="m">initDependencies</span>() {
  <span class="c">// Core</span>
  <span class="n">sl</span>.<span class="m">registerLazySingleton</span>(() =&gt; <span class="t">ApiDataSource</span>());

  <span class="c">// Repository (Bind abstract class to implementation)</span>
  <span class="n">sl</span>.<span class="m">registerLazySingleton</span>&lt;<span class="t">AuthRepository</span>&gt;(() =&gt; <span class="t">AuthRepositoryImpl</span>(<span class="n">sl</span>()));

  <span class="c">// UseCase</span>
  <span class="n">sl</span>.<span class="m">registerLazySingleton</span>(() =&gt; <span class="t">LoginUseCase</span>(<span class="n">sl</span>()));

  <span class="c">// Bloc / State</span>
  <span class="n">sl</span>.<span class="m">registerFactory</span>(() =&gt; <span class="t">AuthBloc</span>(<span class="n">loginUseCase</span>: <span class="n">sl</span>()));
}</pre>
    </div>
  </div>

  <!-- 10.3 Testing -->
  <div class="subsection" id="s10-3">
    <h3 style="color:var(--green);">10.3 Testing Pyramid</h3>
    <p>Because code is decoupled via architecture, testing becomes incredibly easy.</p>
    <div class="table-wrap"><table>
      <tr><th>Test Type</th><th>What it does</th><th>Tools</th></tr>
      <tr><td><code style="background:var(--blue-bg);color:var(--blue);">Unit Tests</code></td><td>Tests logic in Domain/Data. Pure Dart. Since `LoginUseCase` takes an abstract `AuthRepository`, you pass in a Mock.</td><td><code>flutter test</code>, <code>mockito</code>, <code>mocktail</code></td></tr>
      <tr><td><code style="background:var(--teal-bg);color:var(--teal);">Widget Tests</code></td><td>Renders a single widget independently to verify the UI tree builds correctly and handles taps.</td><td><code>flutter test</code>, <code>WidgetTester</code></td></tr>
      <tr><td><code style="background:var(--purple-bg);color:var(--purple);">Golden Tests</code></td><td>A type of Widget test that takes a screenshot of the widget and compares it pixel-by-pixel to an approved image. Catches 1px padding regressions.</td><td><code>golden_toolkit</code></td></tr>
      <tr><td><code style="background:var(--coral-bg);color:var(--coral);">Integration Tests</code></td><td>Spins up the entire app on a real iOS/Android emulator and runs through user journeys from end to end.</td><td><code>integration_test</code> plugin</td></tr>
    </table></div>

    <div class="code-wrap">
      <span class="code-label">Dart (Unit testing with Mocktail)</span>
      <button class="copy-btn">Copy</button>
<pre><span class="k">class</span> <span class="t">MockAuthRepo</span> <span class="k">extends</span> <span class="t">Mock</span> <span class="k">implements</span> <span class="t">AuthRepository</span> {}

<span class="k">void</span> <span class="m">main</span>() {
  <span class="k">late</span> <span class="t">LoginUseCase</span> <span class="n">usecase</span>;
  <span class="k">late</span> <span class="t">MockAuthRepo</span> <span class="n">mockRepo</span>;

  <span class="m">setUp</span>(() {
    <span class="n">mockRepo</span> = <span class="t">MockAuthRepo</span>();
    <span class="n">usecase</span> = <span class="t">LoginUseCase</span>(<span class="n">mockRepo</span>);
  });

  <span class="m">test</span>(<span class="s">'should return User when repo succeeds'</span>, () <span class="k">async</span> {
    <span class="c">// Arrange</span>
    <span class="t">when</span>(() =&gt; <span class="n">mockRepo</span>.<span class="m">login</span>(<span class="n">any</span>(), <span class="n">any</span>()))
        .<span class="m">thenAnswer</span>((<span class="n">_</span>) <span class="k">async</span> =&gt; <span class="t">User</span>(<span class="s">'Alice'</span>));

    <span class="c">// Act</span>
    <span class="k">final</span> <span class="n">result</span> = <span class="k">await</span> <span class="n">usecase</span>.<span class="m">execute</span>(<span class="s">'a@b.com'</span>, <span class="s">'pass'</span>);

    <span class="c">// Assert</span>
    <span class="m">expect</span>(<span class="n">result</span>.<span class="n">name</span>, <span class="s">'Alice'</span>);
    <span class="t">verify</span>(() =&gt; <span class="n">mockRepo</span>.<span class="m">login</span>(<span class="s">'a@b.com'</span>, <span class="s">'pass'</span>)).<span class="m">called</span>(<span class="num">1</span>);
  });
}</pre>
    </div>
  </div>

  <!-- 10.4 Environments -->
  <div class="subsection" id="s10-4">
    <h3 style="color:var(--green);">10.4 Environments &amp; Security</h3>
    <p>Managing API URLs and secrets per environment (Dev / Staging / Prod):</p>
    <ul>
      <li><strong>Native Flavors:</strong> Configures Android's <code>productFlavors</code> and iOS <code>Schemes</code> to generate entirely separate apps (different icons, Bundle IDs) from the same codebase. Crucial for parallel installs (Prod app vs Dev app).</li>
      <li><strong><code>--dart-define</code>:</strong> Inject compile time variables. Best used with a JSON file: <code>flutter build apk --dart-define-from-file=envs/dev.json</code></li>
      <li><strong>Obfuscation:</strong> Protect IP by scrambling code during build: <code>flutter build apk --obfuscate --split-debug-info=./debug</code></li>
      <li><strong>Secrets:</strong> Never hardcode API Keys. Use <strong>envied</strong> to bake `.env` keys securely into obfuscated Dart code at compile time.</li>
    </ul>
    
    <div class="code-wrap">
      <span class="code-label">Dart (Compile time env)</span>
      <button class="copy-btn">Copy</button>
<pre><span class="c">// The value is injected at compile time. If not found, fall back to default.</span>
<span class="k">const</span> <span class="t">String</span> <span class="n">apiUrl</span> = <span class="t">String</span>.<span class="m">fromEnvironment</span>(
  <span class="s">'API_URL'</span>, 
  <span class="n">defaultValue</span>: <span class="s">'https://dev.api.com'</span>
);</pre>
    </div>
  </div>
</section>
"""

with open('flutter_notes.html', 'a') as f:
    f.write(s10)
print('S10 Architecture rewrite done.')
