
s7 = '''
<!-- SECTION 7 -->
<section class="section" id="s7">
  <div class="section-header">
    <div class="section-icon" style="background:var(--teal-bg);">🌐</div>
    <div class="section-meta">
      <span class="section-badge" style="background:var(--teal-bg);color:var(--teal);">Intermediate</span>
      <div class="section-title" style="color:var(--teal);">Networking &amp; APIs</div>
      <div class="section-subtitle">HTTP, Dio interceptors, JSON models, FutureBuilder, Repository pattern</div>
    </div>
  </div>

  <div class="subsection" id="s7-1">
    <h3 style="color:var(--teal);">7.1 HTTP &amp; Dio</h3>
    <p>The built-in <strong>http</strong> package handles simple GET/POST requests. <strong>Dio</strong> is the production-ready HTTP client — it adds interceptors (middleware for every request/response), automatic retries, FormData uploads, download progress, and request cancellation via <code>CancelToken</code>.</p>
    <p>The <strong>interceptor pattern</strong> is critical for auth: attach the Bearer token on every request, and if the server returns 401, automatically refresh the token and retry the original request — all transparent to the rest of the app. <code>BaseOptions</code> sets global timeouts and headers.</p>
    <div class="diagram">
      <svg viewBox="0 0 860 140" xmlns="http://www.w3.org/2000/svg">
        <defs><marker id="arr71" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="#8b949e" stroke-width="1.5" stroke-linecap="round"/></marker></defs>
        <rect x="20" y="45" width="110" height="50" rx="8" fill="#0d2b22" stroke="#34d399" stroke-width="1.5"/>
        <text x="75" y="65" font-family="JetBrains Mono" font-size="10" fill="#34d399" text-anchor="middle">App Code</text>
        <text x="75" y="83" font-family="JetBrains Mono" font-size="9" fill="#8b949e" text-anchor="middle">dio.get()</text>
        <rect x="185" y="35" width="140" height="70" rx="8" fill="#2b1d0d" stroke="#fbbf24" stroke-width="1.5"/>
        <text x="255" y="58" font-family="JetBrains Mono" font-size="10" fill="#fbbf24" text-anchor="middle">Auth Interceptor</text>
        <text x="255" y="75" font-family="JetBrains Mono" font-size="9" fill="#8b949e" text-anchor="middle">add Bearer token</text>
        <text x="255" y="91" font-family="JetBrains Mono" font-size="9" fill="#8b949e" text-anchor="middle">retry on 401</text>
        <rect x="390" y="45" width="110" height="50" rx="8" fill="#0d1e3b" stroke="#60a5fa" stroke-width="1.5"/>
        <text x="445" y="65" font-family="JetBrains Mono" font-size="10" fill="#60a5fa" text-anchor="middle">HTTP Request</text>
        <text x="445" y="83" font-family="JetBrains Mono" font-size="9" fill="#8b949e" text-anchor="middle">TLS + headers</text>
        <rect x="565" y="45" width="110" height="50" rx="8" fill="#161b22" stroke="#30363d" stroke-width="1.5"/>
        <text x="620" y="65" font-family="JetBrains Mono" font-size="10" fill="#e6edf3" text-anchor="middle">Server</text>
        <text x="620" y="83" font-family="JetBrains Mono" font-size="9" fill="#8b949e" text-anchor="middle">JSON response</text>
        <rect x="730" y="45" width="110" height="50" rx="8" fill="#0d2b22" stroke="#34d399" stroke-width="1.5"/>
        <text x="785" y="65" font-family="JetBrains Mono" font-size="10" fill="#34d399" text-anchor="middle">App Model</text>
        <text x="785" y="83" font-family="JetBrains Mono" font-size="9" fill="#8b949e" text-anchor="middle">fromJson()</text>
        <line x1="130" y1="70" x2="185" y2="70" stroke="#8b949e" marker-end="url(#arr71)"/>
        <line x1="325" y1="70" x2="390" y2="70" stroke="#8b949e" marker-end="url(#arr71)"/>
        <line x1="500" y1="70" x2="565" y2="70" stroke="#8b949e" marker-end="url(#arr71)"/>
        <line x1="675" y1="70" x2="730" y2="70" stroke="#34d399" marker-end="url(#arr71)"/>
      </svg>
    </div>
    <div class="code-wrap">
      <span class="code-label">Dart</span>
      <button class="copy-btn">Copy</button>
<pre><span class="k">class</span> <span class="t">DioClient</span> {
  <span class="k">late final</span> <span class="t">Dio</span> <span class="n">_dio</span>;

  <span class="t">DioClient</span>() {
    <span class="n">_dio</span> = <span class="t">Dio</span>(<span class="t">BaseOptions</span>(
      <span class="n">baseUrl</span>: <span class="s">'https://api.example.com/v1'</span>,
      <span class="n">connectTimeout</span>: <span class="k">const</span> <span class="t">Duration</span>(<span class="n">seconds</span>: <span class="num">10</span>),
      <span class="n">receiveTimeout</span>: <span class="k">const</span> <span class="t">Duration</span>(<span class="n">seconds</span>: <span class="num">30</span>),
      <span class="n">headers</span>: {<span class="s">'Content-Type'</span>: <span class="s">'application/json'</span>},
    ));
    <span class="n">_dio</span>.<span class="n">interceptors</span>.<span class="m">addAll</span>([
      <span class="t">_AuthInterceptor</span>(<span class="n">_dio</span>),
      <span class="t">LogInterceptor</span>(<span class="n">requestBody</span>: <span class="k">true</span>, <span class="n">responseBody</span>: <span class="k">true</span>),
    ]);
  }

  <span class="k">Future</span>&lt;<span class="n">T</span>&gt; <span class="m">get</span>&lt;<span class="n">T</span>&gt;(<span class="t">String</span> <span class="n">path</span>, {
    <span class="t">Map</span>&lt;<span class="t">String</span>, <span class="k">dynamic</span>&gt;? <span class="n">params</span>,
    <span class="k">required</span> <span class="n">T</span> <span class="t">Function</span>(<span class="k">dynamic</span>) <span class="n">parser</span>,
  }) <span class="k">async</span> {
    <span class="k">final</span> <span class="n">res</span> = <span class="k">await</span> <span class="n">_dio</span>.<span class="m">get</span>(<span class="n">path</span>, <span class="n">queryParameters</span>: <span class="n">params</span>);
    <span class="k">return</span> <span class="m">parser</span>(<span class="n">res</span>.<span class="n">data</span>);
  }
}

<span class="c">// Auth interceptor — auto-attach + refresh token</span>
<span class="k">class</span> <span class="t">_AuthInterceptor</span> <span class="k">extends</span> <span class="t">Interceptor</span> {
  <span class="k">final</span> <span class="t">Dio</span> <span class="n">dio</span>;
  <span class="t">_AuthInterceptor</span>(<span class="k">this</span>.<span class="n">dio</span>);

  <span class="ann">@override</span>
  <span class="k">void</span> <span class="m">onRequest</span>(<span class="t">RequestOptions</span> <span class="n">options</span>, <span class="t">RequestInterceptorHandler</span> <span class="n">handler</span>) {
    <span class="k">final</span> <span class="n">token</span> = <span class="t">TokenStorage</span>.<span class="m">getAccessToken</span>();
    <span class="k">if</span> (<span class="n">token</span> != <span class="k">null</span>) <span class="n">options</span>.<span class="n">headers</span>[<span class="s">'Authorization'</span>] = <span class="s">'Bearer $token'</span>;
    <span class="n">handler</span>.<span class="m">next</span>(<span class="n">options</span>);
  }

  <span class="ann">@override</span>
  <span class="k">void</span> <span class="m">onError</span>(<span class="t">DioException</span> <span class="n">err</span>, <span class="t">ErrorInterceptorHandler</span> <span class="n">handler</span>) <span class="k">async</span> {
    <span class="k">if</span> (<span class="n">err</span>.<span class="n">response</span>?.<span class="n">statusCode</span> == <span class="num">401</span>) {
      <span class="k">await</span> <span class="t">TokenStorage</span>.<span class="m">refreshToken</span>();
      <span class="k">return</span> <span class="n">handler</span>.<span class="m">resolve</span>(<span class="k">await</span> <span class="n">dio</span>.<span class="m">fetch</span>(<span class="n">err</span>.<span class="n">requestOptions</span>));
    }
    <span class="n">handler</span>.<span class="m">next</span>(<span class="n">err</span>);
  }
}</pre>
    </div>
    <div class="info-box info-tip"><strong>💡 dio vs http</strong><p>Use <code>http</code> for simple one-off requests in scripts or small apps. Use <code>Dio</code> when you need interceptors (auth), retries, FormData, multipart uploads, download progress tracking, or request cancellation.</p></div>
  </div>

  <div class="subsection" id="s7-2">
    <h3 style="color:var(--teal);">7.2 JSON &amp; Models</h3>
    <p>Every API response should be parsed into a <strong>typed Dart model</strong> immediately — never pass raw <code>Map&lt;String, dynamic&gt;</code> through your app. Use a <strong>factory constructor</strong> named <code>fromJson</code> for deserialization and a <code>toJson()</code> method for serialization. For large codebases, <code>json_serializable</code> generates this boilerplate automatically.</p>
    <div class="code-wrap">
      <span class="code-label">Dart</span>
      <button class="copy-btn">Copy</button>
<pre><span class="c">// Nested model — Address + User</span>
<span class="k">class</span> <span class="t">Address</span> {
  <span class="k">final</span> <span class="t">String</span> <span class="n">street</span>, <span class="n">city</span>, <span class="n">country</span>;
  <span class="k">const</span> <span class="t">Address</span>({<span class="k">required</span> <span class="k">this</span>.<span class="n">street</span>, <span class="k">required</span> <span class="k">this</span>.<span class="n">city</span>, <span class="k">required</span> <span class="k">this</span>.<span class="n">country</span>});

  <span class="k">factory</span> <span class="t">Address</span>.<span class="m">fromJson</span>(<span class="t">Map</span>&lt;<span class="t">String</span>, <span class="k">dynamic</span>&gt; <span class="n">j</span>) =&gt; <span class="t">Address</span>(
    <span class="n">street</span>: <span class="n">j</span>[<span class="s">'street'</span>] <span class="k">as</span> <span class="t">String</span>,
    <span class="n">city</span>: <span class="n">j</span>[<span class="s">'city'</span>] <span class="k">as</span> <span class="t">String</span>,
    <span class="n">country</span>: <span class="n">j</span>[<span class="s">'country'</span>] <span class="k">as</span> <span class="t">String</span>,
  );
  <span class="t">Map</span>&lt;<span class="t">String</span>, <span class="k">dynamic</span>&gt; <span class="m">toJson</span>() =&gt; {<span class="s">'street'</span>: <span class="n">street</span>, <span class="s">'city'</span>: <span class="n">city</span>, <span class="s">'country'</span>: <span class="n">country</span>};
}

<span class="k">class</span> <span class="t">User</span> {
  <span class="k">final</span> <span class="t">int</span> <span class="n">id</span>;
  <span class="k">final</span> <span class="t">String</span> <span class="n">name</span>, <span class="n">email</span>;
  <span class="k">final</span> <span class="t">Address</span> <span class="n">address</span>;
  <span class="k">final</span> <span class="t">List</span>&lt;<span class="t">String</span>&gt; <span class="n">roles</span>;
  <span class="k">final</span> <span class="t">DateTime</span> <span class="n">createdAt</span>;

  <span class="k">const</span> <span class="t">User</span>({<span class="k">required</span> <span class="k">this</span>.<span class="n">id</span>, <span class="k">required</span> <span class="k">this</span>.<span class="n">name</span>, <span class="k">required</span> <span class="k">this</span>.<span class="n">email</span>,
    <span class="k">required</span> <span class="k">this</span>.<span class="n">address</span>, <span class="k">required</span> <span class="k">this</span>.<span class="n">roles</span>, <span class="k">required</span> <span class="k">this</span>.<span class="n">createdAt</span>});

  <span class="k">factory</span> <span class="t">User</span>.<span class="m">fromJson</span>(<span class="t">Map</span>&lt;<span class="t">String</span>, <span class="k">dynamic</span>&gt; <span class="n">j</span>) =&gt; <span class="t">User</span>(
    <span class="n">id</span>: <span class="n">j</span>[<span class="s">'id'</span>] <span class="k">as</span> <span class="t">int</span>,
    <span class="n">name</span>: <span class="n">j</span>[<span class="s">'name'</span>] <span class="k">as</span> <span class="t">String</span>,
    <span class="n">email</span>: <span class="n">j</span>[<span class="s">'email'</span>] <span class="k">as</span> <span class="t">String</span>,
    <span class="n">address</span>: <span class="t">Address</span>.<span class="m">fromJson</span>(<span class="n">j</span>[<span class="s">'address'</span>] <span class="k">as</span> <span class="t">Map</span>&lt;<span class="t">String</span>, <span class="k">dynamic</span>&gt;),
    <span class="n">roles</span>: (<span class="n">j</span>[<span class="s">'roles'</span>] <span class="k">as</span> <span class="t">List</span>).<span class="m">cast</span>&lt;<span class="t">String</span>&gt;(),
    <span class="n">createdAt</span>: <span class="t">DateTime</span>.<span class="m">parse</span>(<span class="n">j</span>[<span class="s">'created_at'</span>] <span class="k">as</span> <span class="t">String</span>),
  );
}</pre>
    </div>
    <div class="info-box info-key"><strong>🔑 Use json_serializable for Scale</strong><p>For projects with 10+ models, add <code>json_serializable</code> and <code>build_runner</code>. Annotate with <code>@JsonSerializable()</code> and run <code>dart run build_runner build</code>. It generates <code>fromJson</code>/<code>toJson</code> automatically with proper null handling.</p></div>
  </div>

  <div class="subsection" id="s7-3">
    <h3 style="color:var(--teal);">7.3 FutureBuilder &amp; StreamBuilder</h3>
    <p><strong>FutureBuilder</strong> builds UI based on a Future's current state. Always create the Future in <code>initState()</code> or a provider — never inside <code>build()</code>, as that creates a new Future on every rebuild. <strong>StreamBuilder</strong> handles live data that updates over time (WebSocket, Firestore, location updates).</p>
    <div class="code-wrap">
      <span class="code-label">Flutter</span>
      <button class="copy-btn">Copy</button>
<pre><span class="k">class</span> <span class="t">UserProfilePage</span> <span class="k">extends</span> <span class="t">StatefulWidget</span> {
  <span class="k">final</span> <span class="t">int</span> <span class="n">userId</span>;
  <span class="k">const</span> <span class="t">UserProfilePage</span>({<span class="k">super</span>.<span class="n">key</span>, <span class="k">required</span> <span class="k">this</span>.<span class="n">userId</span>});
  <span class="ann">@override</span> <span class="t">State</span>&lt;<span class="t">UserProfilePage</span>&gt; <span class="m">createState</span>() =&gt; <span class="t">_UserProfilePageState</span>();
}

<span class="k">class</span> <span class="t">_UserProfilePageState</span> <span class="k">extends</span> <span class="t">State</span>&lt;<span class="t">UserProfilePage</span>&gt; {
  <span class="k">late</span> <span class="k">final</span> <span class="t">Future</span>&lt;<span class="t">User</span>&gt; <span class="n">_userFuture</span>;

  <span class="ann">@override</span>
  <span class="k">void</span> <span class="m">initState</span>() {
    <span class="k">super</span>.<span class="m">initState</span>();
    <span class="n">_userFuture</span> = <span class="n">userRepo</span>.<span class="m">getUser</span>(<span class="n">widget</span>.<span class="n">userId</span>);  <span class="c">// created once!</span>
  }

  <span class="ann">@override</span>
  <span class="t">Widget</span> <span class="m">build</span>(<span class="t">BuildContext</span> <span class="n">context</span>) {
    <span class="k">return</span> <span class="t">FutureBuilder</span>&lt;<span class="t">User</span>&gt;(
      <span class="n">future</span>: <span class="n">_userFuture</span>,
      <span class="n">builder</span>: (<span class="n">context</span>, <span class="n">snapshot</span>) {
        <span class="k">if</span> (<span class="n">snapshot</span>.<span class="n">connectionState</span> == <span class="t">ConnectionState</span>.<span class="n">waiting</span>) {
          <span class="k">return</span> <span class="k">const</span> <span class="t">Center</span>(<span class="n">child</span>: <span class="t">CircularProgressIndicator</span>());
        }
        <span class="k">if</span> (<span class="n">snapshot</span>.<span class="n">hasError</span>) {
          <span class="k">return</span> <span class="t">ErrorView</span>(<span class="n">error</span>: <span class="n">snapshot</span>.<span class="n">error</span>.<span class="m">toString</span>());
        }
        <span class="k">final</span> <span class="n">user</span> = <span class="n">snapshot</span>.<span class="n">data</span>!;
        <span class="k">return</span> <span class="t">UserCard</span>(<span class="n">user</span>: <span class="n">user</span>);
      },
    );
  }
}

<span class="c">// StreamBuilder — live message feed</span>
<span class="t">StreamBuilder</span>&lt;<span class="t">List</span>&lt;<span class="t">Message</span>&gt;&gt;(
  <span class="n">stream</span>: <span class="n">chatRepo</span>.<span class="m">messagesStream</span>(<span class="n">chatId</span>),
  <span class="n">builder</span>: (<span class="n">context</span>, <span class="n">snapshot</span>) {
    <span class="k">if</span> (!<span class="n">snapshot</span>.<span class="n">hasData</span>) <span class="k">return</span> <span class="k">const</span> <span class="t">SizedBox</span>();
    <span class="k">final</span> <span class="n">messages</span> = <span class="n">snapshot</span>.<span class="n">data</span>!;
    <span class="k">return</span> <span class="t">MessageList</span>(<span class="n">messages</span>: <span class="n">messages</span>);
  },
)</pre>
    </div>
    <div class="info-box info-warn"><strong>⚠️ Future in build()</strong><p>Never write <code>future: fetchUser(id)</code> directly in FutureBuilder inside <code>build()</code>. Each rebuild calls <code>fetchUser()</code> again, making a new network request every time setState fires. Always store the Future in a field.</p></div>
  </div>

  <div class="subsection" id="s7-4">
    <h3 style="color:var(--teal);">7.4 Repository Pattern</h3>
    <p>The <strong>Repository pattern</strong> abstracts data sources behind a clean interface. The UI layer only knows about the repository interface — it doesn't care whether data comes from an API, cache, or local database. This enables easy mocking in tests and swapping data sources without touching UI code.</p>
    <div class="diagram">
      <svg viewBox="0 0 860 170" xmlns="http://www.w3.org/2000/svg">
        <defs><marker id="arr74" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="#8b949e" stroke-width="1.5" stroke-linecap="round"/></marker></defs>
        <rect x="10" y="60" width="110" height="50" rx="8" fill="#1a1433" stroke="#a78bfa" stroke-width="1.5"/>
        <text x="65" y="82" font-family="JetBrains Mono" font-size="10" fill="#a78bfa" text-anchor="middle">UI / BLoC</text>
        <text x="65" y="98" font-family="JetBrains Mono" font-size="9" fill="#8b949e" text-anchor="middle">Widget/Notifier</text>
        <rect x="180" y="50" width="160" height="70" rx="8" fill="#0d1e3b" stroke="#60a5fa" stroke-width="2" stroke-dasharray="6 3"/>
        <text x="260" y="73" font-family="JetBrains Mono" font-size="10" fill="#60a5fa" text-anchor="middle">UserRepository</text>
        <text x="260" y="91" font-family="JetBrains Mono" font-size="9" fill="#8b949e" text-anchor="middle">abstract interface</text>
        <text x="260" y="107" font-family="JetBrains Mono" font-size="9" fill="#8b949e" text-anchor="middle">getUser / saveUser</text>
        <rect x="410" y="50" width="160" height="70" rx="8" fill="#0d1e3b" stroke="#60a5fa" stroke-width="1.5"/>
        <text x="490" y="73" font-family="JetBrains Mono" font-size="10" fill="#60a5fa" text-anchor="middle">UserRepoImpl</text>
        <text x="490" y="91" font-family="JetBrains Mono" font-size="9" fill="#8b949e" text-anchor="middle">Remote DS</text>
        <text x="490" y="107" font-family="JetBrains Mono" font-size="9" fill="#8b949e" text-anchor="middle">Local DS (cache)</text>
        <rect x="640" y="30" width="110" height="45" rx="6" fill="#0d2b22" stroke="#34d399"/>
        <text x="695" y="52" font-family="JetBrains Mono" font-size="10" fill="#34d399" text-anchor="middle">Dio / http</text>
        <text x="695" y="68" font-family="JetBrains Mono" font-size="9" fill="#8b949e" text-anchor="middle">Remote API</text>
        <rect x="640" y="100" width="110" height="45" rx="6" fill="#2b1d0d" stroke="#fbbf24"/>
        <text x="695" y="122" font-family="JetBrains Mono" font-size="10" fill="#fbbf24" text-anchor="middle">Hive / SQLite</text>
        <text x="695" y="138" font-family="JetBrains Mono" font-size="9" fill="#8b949e" text-anchor="middle">Local Cache</text>
        <line x1="120" y1="85" x2="180" y2="85" stroke="#8b949e" marker-end="url(#arr74)"/>
        <line x1="340" y1="85" x2="410" y2="85" stroke="#8b949e" marker-end="url(#arr74)"/>
        <line x1="570" y1="70" x2="640" y2="52" stroke="#34d399" marker-end="url(#arr74)"/>
        <line x1="570" y1="100" x2="640" y2="122" stroke="#fbbf24" marker-end="url(#arr74)"/>
      </svg>
    </div>
    <div class="code-wrap">
      <span class="code-label">Dart</span>
      <button class="copy-btn">Copy</button>
<pre><span class="c">// Abstract interface (domain layer)</span>
<span class="k">abstract interface class</span> <span class="t">UserRepository</span> {
  <span class="t">Future</span>&lt;<span class="t">User</span>&gt; <span class="m">getUser</span>(<span class="t">int</span> <span class="n">id</span>);
  <span class="t">Future</span>&lt;<span class="t">List</span>&lt;<span class="t">User</span>&gt;&gt; <span class="m">getUsers</span>({<span class="t">int</span> <span class="n">page</span> = <span class="num">1</span>});
  <span class="t">Future</span>&lt;<span class="k">void</span>&gt; <span class="m">saveUser</span>(<span class="t">User</span> <span class="n">user</span>);
}

<span class="c">// Implementation (data layer) with cache-then-network</span>
<span class="k">class</span> <span class="t">UserRepositoryImpl</span> <span class="k">implements</span> <span class="t">UserRepository</span> {
  <span class="k">final</span> <span class="t">UserRemoteDataSource</span> <span class="n">_remote</span>;
  <span class="k">final</span> <span class="t">UserLocalDataSource</span> <span class="n">_local</span>;

  <span class="t">UserRepositoryImpl</span>(<span class="k">this</span>.<span class="n">_remote</span>, <span class="k">this</span>.<span class="n">_local</span>);

  <span class="ann">@override</span>
  <span class="k">Future</span>&lt;<span class="t">User</span>&gt; <span class="m">getUser</span>(<span class="t">int</span> <span class="n">id</span>) <span class="k">async</span> {
    <span class="k">final</span> <span class="n">cached</span> = <span class="k">await</span> <span class="n">_local</span>.<span class="m">getUser</span>(<span class="n">id</span>);
    <span class="k">if</span> (<span class="n">cached</span> != <span class="k">null</span>) <span class="k">return</span> <span class="n">cached</span>;  <span class="c">// serve from cache</span>
    <span class="k">final</span> <span class="n">user</span> = <span class="k">await</span> <span class="n">_remote</span>.<span class="m">fetchUser</span>(<span class="n">id</span>);
    <span class="k">await</span> <span class="n">_local</span>.<span class="m">saveUser</span>(<span class="n">user</span>);         <span class="c">// cache result</span>
    <span class="k">return</span> <span class="n">user</span>;
  }
}</pre>
    </div>
    <div class="info-box info-tip"><strong>💡 Test the Repository Contract</strong><p>With an abstract interface, you can create a <code>MockUserRepository</code> in tests that returns hardcoded data. Your BLoC/Notifier tests never need a real network connection — they just test logic against the mock.</p></div>
  </div>
  <!-- 7.4 Dio Interceptors -->
  <div class="subsection" id="s7-4">
    <h3 style="color:var(--teal);">7.4 Advanced Networking: Dio Interceptors</h3>
    <p>For production apps, <code>http</code> package is often too basic. The <code>dio</code> package is the industry standard because of <strong>Interceptors</strong>. Interceptors act as middlewares for all outgoing requests and incoming responses. You can use them to automatically attach Auth Tokens, log requests, or seamlessly refresh expired tokens.</p>
    <div class="code-wrap">
      <div class="mac-header">
        <div class="mac-dots"><div class="mac-dot-r"></div><div class="mac-dot-y"></div><div class="mac-dot-g"></div></div>
        <span class="code-label-mac">Dart</span>
        <button class="copy-btn">Copy</button>
      </div>
<pre><span class="k">final</span> <span class="n">dio</span> = <span class="t">Dio</span>(<span class="t">BaseOptions</span>(<span class="n">baseUrl</span>: <span class="s">'https://api.example.com/'</span>));

<span class="n">dio</span>.<span class="n">interceptors</span>.<span class="m">add</span>(<span class="t">InterceptorsWrapper</span>(
  <span class="c">// 1. ON REQUEST (Inject Token)</span>
  <span class="n">onRequest</span>: (<span class="n">options</span>, <span class="n">handler</span>) <span class="k">async</span> {
    <span class="k">final</span> <span class="n">token</span> = <span class="k">await</span> <span class="n">secureStorage</span>.<span class="m">read</span>(<span class="n">key</span>: <span class="s">'token'</span>);
    <span class="k">if</span> (<span class="n">token</span> != <span class="k">null</span>) {
      <span class="n">options</span>.<span class="n">headers</span>[<span class="s">'Authorization'</span>] = <span class="s">'Bearer $token'</span>;
    }
    <span class="k">return</span> <span class="n">handler</span>.<span class="m">next</span>(<span class="n">options</span>); <span class="c">// Continue the request</span>
  },
  
  <span class="c">// 2. ON RESPONSE (Log or Parse)</span>
  <span class="n">onResponse</span>: (<span class="n">response</span>, <span class="n">handler</span>) {
    <span class="m">print</span>(<span class="s">'Data Received: ${response.statusCode}'</span>);
    <span class="k">return</span> <span class="n">handler</span>.<span class="m">next</span>(<span class="n">response</span>); 
  },
  
  <span class="c">// 3. ON ERROR (Handle Token Expiration &amp; Refresh)</span>
  <span class="n">onError</span>: (<span class="t">DioException</span> <span class="n">e</span>, <span class="n">handler</span>) <span class="k">async</span> {
    <span class="k">if</span> (<span class="n">e</span>.<span class="n">response</span>?.<span class="n">statusCode</span> == <span class="num">401</span>) {
      <span class="c">// Token expired! Attempt to refresh it</span>
      <span class="k">final</span> <span class="n">newToken</span> = <span class="k">await</span> <span class="m">refreshAuthToken</span>();
      <span class="k">if</span> (<span class="n">newToken</span> != <span class="k">null</span>) {
        <span class="c">// Retry the original failed request</span>
        <span class="n">e</span>.<span class="n">requestOptions</span>.<span class="n">headers</span>[<span class="s">'Authorization'</span>] = <span class="s">'Bearer $newToken'</span>;
        <span class="k">final</span> <span class="n">retryResponse</span> = <span class="k">await</span> <span class="n">dio</span>.<span class="m">fetch</span>(<span class="n">e</span>.<span class="n">requestOptions</span>);
        <span class="k">return</span> <span class="n">handler</span>.<span class="m">resolve</span>(<span class="n">retryResponse</span>);
      }
    }
    <span class="k">return</span> <span class="n">handler</span>.<span class="m">next</span>(<span class="n">e</span>); <span class="c">// Pass error down if not handled</span>
  },
));</pre>
    </div>
  </div>
</section>
'''

with open('flutter_notes.html', 'a') as f:
    f.write(s7)
print('Section 7 appended. Len:', len(s7))
