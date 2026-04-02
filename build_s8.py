
s8 = """
<!-- SECTION 8 -->
<section class="section" id="s8">
  <div class="section-header">
    <div class="section-icon" style="background:var(--amber-bg);">💾</div>
    <div class="section-meta">
      <span class="section-badge" style="background:var(--amber-bg);color:var(--amber);">Intermediate</span>
      <div class="section-title" style="color:var(--amber);">Local Storage</div>
      <div class="section-subtitle">SharedPreferences, SQLite, Hive, and Secure Storage</div>
    </div>
  </div>

  <div class="subsection" id="s8-1">
    <h3 style="color:var(--amber);">8.1 SharedPreferences</h3>
    <p><strong>SharedPreferences</strong> provides a persistent key-value store backed by Android SharedPreferences and iOS NSUserDefaults. It survives app restarts and supports <code>bool</code>, <code>int</code>, <code>double</code>, <code>String</code>, and <code>List&lt;String&gt;</code>. Access is async — always await the instance. Use it for app settings, onboarding flags, and theme preferences. <strong>Never store sensitive data</strong> (tokens, passwords) here — it's stored as plain text.</p>
    <div class="code-wrap">
      <span class="code-label">Dart</span>
      <button class="copy-btn">Copy</button>
<pre><span class="c">// Singleton service wrapping SharedPreferences</span>
<span class="k">class</span> <span class="t">PrefsService</span> {
  <span class="k">static</span> <span class="k">late</span> <span class="k">final</span> <span class="t">SharedPreferences</span> <span class="n">_prefs</span>;

  <span class="k">static</span> <span class="k">Future</span>&lt;<span class="k">void</span>&gt; <span class="m">init</span>() <span class="k">async</span> {
    <span class="n">_prefs</span> = <span class="k">await</span> <span class="t">SharedPreferences</span>.<span class="m">getInstance</span>();
  }

  <span class="c">// Theme</span>
  <span class="k">static</span> <span class="t">ThemeMode</span> <span class="k">get</span> <span class="n">themeMode</span> {
    <span class="k">final</span> <span class="n">val</span> = <span class="n">_prefs</span>.<span class="m">getString</span>(<span class="s">'theme_mode'</span>) ?? <span class="s">'system'</span>;
    <span class="k">return</span> <span class="t">ThemeMode</span>.<span class="n">values</span>.<span class="m">firstWhere</span>((<span class="n">e</span>) =&gt; <span class="n">e</span>.<span class="n">name</span> == <span class="n">val</span>);
  }
  <span class="k">static</span> <span class="k">Future</span>&lt;<span class="k">void</span>&gt; <span class="m">setThemeMode</span>(<span class="t">ThemeMode</span> <span class="n">mode</span>) =&gt;
      <span class="n">_prefs</span>.<span class="m">setString</span>(<span class="s">'theme_mode'</span>, <span class="n">mode</span>.<span class="n">name</span>);

  <span class="c">// Onboarding</span>
  <span class="k">static</span> <span class="t">bool</span> <span class="k">get</span> <span class="n">hasSeenOnboarding</span> =&gt;
      <span class="n">_prefs</span>.<span class="m">getBool</span>(<span class="s">'onboarding_done'</span>) ?? <span class="k">false</span>;
  <span class="k">static</span> <span class="k">Future</span>&lt;<span class="k">void</span>&gt; <span class="m">markOnboardingDone</span>() =&gt;
      <span class="n">_prefs</span>.<span class="m">setBool</span>(<span class="s">'onboarding_done'</span>, <span class="k">true</span>);

  <span class="c">// Recent searches (List&lt;String&gt;)</span>
  <span class="k">static</span> <span class="t">List</span>&lt;<span class="t">String</span>&gt; <span class="k">get</span> <span class="n">recentSearches</span> =&gt;
      <span class="n">_prefs</span>.<span class="m">getStringList</span>(<span class="s">'recent_searches'</span>) ?? [];
  <span class="k">static</span> <span class="k">Future</span>&lt;<span class="k">void</span>&gt; <span class="m">addSearch</span>(<span class="t">String</span> <span class="n">query</span>) <span class="k">async</span> {
    <span class="k">final</span> <span class="n">list</span> = <span class="n">recentSearches</span>
      ..<span class="m">remove</span>(<span class="n">query</span>)
      ...<span class="m">insert</span>(<span class="num">0</span>, <span class="n">query</span>);
    <span class="k">await</span> <span class="n">_prefs</span>.<span class="m">setStringList</span>(<span class="s">'recent_searches'</span>, <span class="n">list</span>.<span class="m">take</span>(<span class="num">10</span>).<span class="m">toList</span>());
  }
}

<span class="c">// Init in main() before runApp</span>
<span class="k">void</span> <span class="m">main</span>() <span class="k">async</span> {
  <span class="t">WidgetsFlutterBinding</span>.<span class="m">ensureInitialized</span>();
  <span class="k">await</span> <span class="t">PrefsService</span>.<span class="m">init</span>();
  <span class="m">runApp</span>(<span class="k">const</span> <span class="t">MyApp</span>());
}</pre>
    </div>
    <div class="info-box info-warn"><strong>⚠️ Not for Sensitive Data</strong><p>SharedPreferences stores data as plain text in the app's data directory. On rooted/jailbroken devices this is readable. Store auth tokens in <code>flutter_secure_storage</code> which uses the OS Keychain/Keystore instead.</p></div>
  </div>

  <div class="subsection" id="s8-2">
    <h3 style="color:var(--amber);">8.2 SQLite with sqflite</h3>
    <p><strong>sqflite</strong> provides a full SQLite database on Android and iOS. Use it for structured relational data, complex queries, or when you need JOIN operations. The <strong>DatabaseHelper singleton</strong> pattern ensures only one connection is open at a time. Always run migrations in <code>onUpgrade</code> to handle schema changes across app versions.</p>
    <div class="code-wrap">
      <span class="code-label">Dart</span>
      <button class="copy-btn">Copy</button>
<pre><span class="k">class</span> <span class="t">NotesDatabase</span> {
  <span class="k">static</span> <span class="k">final</span> <span class="t">NotesDatabase</span> <span class="n">instance</span> = <span class="t">NotesDatabase</span>.<span class="n">_internal</span>();
  <span class="k">static</span> <span class="t">Database</span>? <span class="n">_db</span>;
  <span class="t">NotesDatabase</span>.<span class="n">_internal</span>();

  <span class="k">Future</span>&lt;<span class="t">Database</span>&gt; <span class="k">get</span> <span class="n">database</span> <span class="k">async</span> {
    <span class="n">_db</span> ??= <span class="k">await</span> <span class="m">_initDatabase</span>();
    <span class="k">return</span> <span class="n">_db</span>!;
  }

  <span class="k">Future</span>&lt;<span class="t">Database</span>&gt; <span class="m">_initDatabase</span>() <span class="k">async</span> {
    <span class="k">final</span> <span class="n">path</span> = <span class="m">join</span>(<span class="k">await</span> <span class="m">getDatabasesPath</span>(), <span class="s">'notes.db'</span>);
    <span class="k">return</span> <span class="m">openDatabase</span>(<span class="n">path</span>, <span class="n">version</span>: <span class="num">2</span>,
      <span class="n">onCreate</span>: (<span class="n">db</span>, <span class="n">version</span>) <span class="k">async</span> {
        <span class="k">await</span> <span class="n">db</span>.<span class="m">execute</span>(<span class="s">'''CREATE TABLE notes(
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          title TEXT NOT NULL, body TEXT,
          created_at INTEGER, is_pinned INTEGER DEFAULT 0)'''</span>);
      },
      <span class="n">onUpgrade</span>: (<span class="n">db</span>, <span class="n">oldV</span>, <span class="n">newV</span>) <span class="k">async</span> {
        <span class="k">if</span> (<span class="n">oldV</span> &lt; <span class="num">2</span>) <span class="k">await</span> <span class="n">db</span>.<span class="m">execute</span>(<span class="s">'ALTER TABLE notes ADD COLUMN is_pinned INTEGER DEFAULT 0'</span>);
      },
    );
  }

  <span class="k">Future</span>&lt;<span class="t">int</span>&gt; <span class="m">insertNote</span>(<span class="t">Note</span> <span class="n">note</span>) <span class="k">async</span> {
    <span class="k">final</span> <span class="n">db</span> = <span class="k">await</span> <span class="n">database</span>;
    <span class="k">return</span> <span class="n">db</span>.<span class="m">insert</span>(<span class="s">'notes'</span>, <span class="n">note</span>.<span class="m">toMap</span>(),
        <span class="n">conflictAlgorithm</span>: <span class="t">ConflictAlgorithm</span>.<span class="n">replace</span>);
  }

  <span class="k">Future</span>&lt;<span class="t">List</span>&lt;<span class="t">Note</span>&gt;&gt; <span class="m">getAllNotes</span>() <span class="k">async</span> {
    <span class="k">final</span> <span class="n">db</span> = <span class="k">await</span> <span class="n">database</span>;
    <span class="k">final</span> <span class="n">maps</span> = <span class="k">await</span> <span class="n">db</span>.<span class="m">query</span>(<span class="s">'notes'</span>, <span class="n">orderBy</span>: <span class="s">'is_pinned DESC, created_at DESC'</span>);
    <span class="k">return</span> <span class="n">maps</span>.<span class="m">map</span>(<span class="t">Note</span>.<span class="m">fromMap</span>).<span class="m">toList</span>();
  }

  <span class="k">Future</span>&lt;<span class="t">int</span>&gt; <span class="m">deleteNote</span>(<span class="t">int</span> <span class="n">id</span>) <span class="k">async</span> {
    <span class="k">final</span> <span class="n">db</span> = <span class="k">await</span> <span class="n">database</span>;
    <span class="k">return</span> <span class="n">db</span>.<span class="m">delete</span>(<span class="s">'notes'</span>, <span class="n">where</span>: <span class="s">'id = ?'</span>, <span class="n">whereArgs</span>: [<span class="n">id</span>]);
  }
}</pre>
    </div>
    <div class="info-box info-tip"><strong>💡 Use drift for Type-Safe SQL</strong><p><code>drift</code> (formerly moor) wraps sqflite with type-safe query builders and code generation. Instead of raw SQL strings, you write Dart code and the compiler catches query errors. Highly recommended for complex schemas.</p></div>
  </div>

  <div class="subsection" id="s8-3">
    <h3 style="color:var(--amber);">8.3 Hive (NoSQL)</h3>
    <p><strong>Hive</strong> is a lightweight, extremely fast key-value NoSQL database written in pure Dart — no native dependencies. It outperforms SQLite for simple read/write operations. <strong>TypeAdapters</strong> serialize custom Dart objects. <strong>Lazy boxes</strong> load values on demand — ideal for large datasets. <strong>Encrypted boxes</strong> use AES-256 for sensitive data.</p>
    <div class="code-wrap">
      <span class="code-label">Dart</span>
      <button class="copy-btn">Copy</button>
<pre><span class="c">// 1. Annotate your model</span>
<span class="ann">@HiveType</span>(<span class="n">typeId</span>: <span class="num">0</span>)
<span class="k">class</span> <span class="t">Product</span> <span class="k">extends</span> <span class="t">HiveObject</span> {
  <span class="ann">@HiveField</span>(<span class="num">0</span>) <span class="k">late</span> <span class="t">String</span> <span class="n">id</span>;
  <span class="ann">@HiveField</span>(<span class="num">1</span>) <span class="k">late</span> <span class="t">String</span> <span class="n">name</span>;
  <span class="ann">@HiveField</span>(<span class="num">2</span>) <span class="k">late</span> <span class="t">double</span> <span class="n">price</span>;
}

<span class="c">// 2. Register adapter and open box in main()</span>
<span class="k">void</span> <span class="m">main</span>() <span class="k">async</span> {
  <span class="k">await</span> <span class="t">Hive</span>.<span class="m">initFlutter</span>();
  <span class="t">Hive</span>.<span class="m">registerAdapter</span>(<span class="t">ProductAdapter</span>());  <span class="c">// generated by hive_generator</span>
  <span class="k">await</span> <span class="t">Hive</span>.<span class="m">openBox</span>&lt;<span class="t">Product</span>&gt;(<span class="s">'products'</span>);
  <span class="m">runApp</span>(<span class="k">const</span> <span class="t">MyApp</span>());
}

<span class="c">// 3. CRUD operations</span>
<span class="k">final</span> <span class="n">box</span> = <span class="t">Hive</span>.<span class="m">box</span>&lt;<span class="t">Product</span>&gt;(<span class="s">'products'</span>);

<span class="k">await</span> <span class="n">box</span>.<span class="m">put</span>(<span class="s">'prod_1'</span>, <span class="t">Product</span>()
  ..<span class="n">id</span> = <span class="s">'prod_1'</span>
  ..<span class="n">name</span> = <span class="s">'Flutter Book'</span>
  ..<span class="n">price</span> = <span class="num">29.99</span>);

<span class="k">final</span> <span class="t">Product</span>? <span class="n">product</span> = <span class="n">box</span>.<span class="m">get</span>(<span class="s">'prod_1'</span>);
<span class="k">final</span> <span class="t">List</span>&lt;<span class="t">Product</span>&gt; <span class="n">all</span> = <span class="n">box</span>.<span class="n">values</span>.<span class="m">toList</span>();
<span class="k">await</span> <span class="n">box</span>.<span class="m">delete</span>(<span class="s">'prod_1'</span>);

<span class="c">// ValueListenableBuilder for reactive UI</span>
<span class="t">ValueListenableBuilder</span>&lt;<span class="t">Box</span>&lt;<span class="t">Product</span>&gt;&gt;(
  <span class="n">valueListenable</span>: <span class="t">Hive</span>.<span class="m">box</span>&lt;<span class="t">Product</span>&gt;(<span class="s">'products'</span>).<span class="m">listenable</span>(),
  <span class="n">builder</span>: (<span class="n">context</span>, <span class="n">box</span>, <span class="n">_</span>) =&gt; <span class="t">ProductList</span>(<span class="n">products</span>: <span class="n">box</span>.<span class="n">values</span>.<span class="m">toList</span>()),
)</pre>
    </div>
    <div class="table-wrap"><table>
      <tr><th>Storage</th><th>Type</th><th>Speed</th><th>Complex Queries</th><th>Best For</th></tr>
      <tr><td><code style="background:var(--blue-bg);color:var(--blue);">SharedPrefs</code></td><td>Key-Value</td><td>Fast</td><td>❌</td><td>Settings, flags</td></tr>
      <tr><td><code style="background:var(--teal-bg);color:var(--teal);">sqflite</code></td><td>Relational SQL</td><td>Medium</td><td>✅ Full SQL</td><td>Structured data, joins</td></tr>
      <tr><td><code style="background:var(--amber-bg);color:var(--amber);">Hive</code></td><td>NoSQL</td><td>Very Fast</td><td>❌ Simple only</td><td>Caching, offline lists</td></tr>
      <tr><td><code style="background:var(--purple-bg);color:var(--purple);">Isar</code></td><td>NoSQL + indexes</td><td>Fastest</td><td>✅ Query DSL</td><td>Large datasets</td></tr>
    </table></div>
  </div>

  <div class="subsection" id="s8-4">
    <h3 style="color:var(--amber);">8.4 Secure Storage</h3>
    <p><strong>flutter_secure_storage</strong> stores data in the iOS Keychain and Android EncryptedSharedPreferences (backed by Android Keystore). This is cryptographically protected and not accessible without the app's credentials. Always store auth tokens, refresh tokens, and passwords here — never in SharedPreferences or Hive.</p>
    <div class="code-wrap">
      <span class="code-label">Dart</span>
      <button class="copy-btn">Copy</button>
<pre><span class="k">class</span> <span class="t">SecureStorageService</span> {
  <span class="k">static</span> <span class="k">const</span> <span class="n">_storage</span> = <span class="t">FlutterSecureStorage</span>(
    <span class="n">aOptions</span>: <span class="t">AndroidOptions</span>(<span class="n">encryptedSharedPreferences</span>: <span class="k">true</span>),
    <span class="n">iOptions</span>: <span class="t">IOSOptions</span>(<span class="n">accessibility</span>: <span class="t">KeychainAccessibility</span>.<span class="n">first_unlock</span>),
  );

  <span class="k">static</span> <span class="k">const</span> <span class="n">_accessKey</span>  = <span class="s">'access_token'</span>;
  <span class="k">static</span> <span class="k">const</span> <span class="n">_refreshKey</span> = <span class="s">'refresh_token'</span>;

  <span class="k">static</span> <span class="k">Future</span>&lt;<span class="k">void</span>&gt; <span class="m">saveTokens</span>(<span class="t">String</span> <span class="n">access</span>, <span class="t">String</span> <span class="n">refresh</span>) <span class="k">async</span> {
    <span class="k">await</span> <span class="t">Future</span>.<span class="m">wait</span>([
      <span class="n">_storage</span>.<span class="m">write</span>(<span class="n">key</span>: <span class="n">_accessKey</span>, <span class="n">value</span>: <span class="n">access</span>),
      <span class="n">_storage</span>.<span class="m">write</span>(<span class="n">key</span>: <span class="n">_refreshKey</span>, <span class="n">value</span>: <span class="n">refresh</span>),
    ]);
  }

  <span class="k">static</span> <span class="k">Future</span>&lt;<span class="t">String</span>?&gt; <span class="m">getAccessToken</span>() =&gt;
      <span class="n">_storage</span>.<span class="m">read</span>(<span class="n">key</span>: <span class="n">_accessKey</span>);
  <span class="k">static</span> <span class="k">Future</span>&lt;<span class="t">String</span>?&gt; <span class="m">getRefreshToken</span>() =&gt;
      <span class="n">_storage</span>.<span class="m">read</span>(<span class="n">key</span>: <span class="n">_refreshKey</span>);

  <span class="k">static</span> <span class="k">Future</span>&lt;<span class="k">void</span>&gt; <span class="m">clearTokens</span>() <span class="k">async</span> {
    <span class="k">await</span> <span class="t">Future</span>.<span class="m">wait</span>([
      <span class="n">_storage</span>.<span class="m">delete</span>(<span class="n">key</span>: <span class="n">_accessKey</span>),
      <span class="n">_storage</span>.<span class="m">delete</span>(<span class="n">key</span>: <span class="n">_refreshKey</span>),
    ]);
  }
}</pre>
    </div>
    <div class="info-box info-key"><strong>🔑 Security Rule #1</strong><p>The golden rule: if it's secret, use FlutterSecureStorage. Auth tokens, API keys, PINs, biometric data — all go in the secure enclave, not plain storage. On Android, set <code>encryptedSharedPreferences: true</code> to use EncryptedSharedPreferences backed by the Android Keystore.</p></div>
  </div>
  <!-- 8.4 Isar Database -->
  <div class="subsection" id="s8-4">
    <h3 style="color:var(--amber);">8.4 Isar Database (Fast NoSQL)</h3>
    <p>Written by the creator of Hive, <strong>Isar</strong> is a modern, high-performance NoSQL database for Flutter. It is fully asynchronous, supports full-text search, multi-entry indexing, and relations. Unlike Hive, it actually uses a structured schema via code generation.</p>
    <div class="code-wrap">
      <div class="mac-header">
        <div class="mac-dots"><div class="mac-dot-r"></div><div class="mac-dot-y"></div><div class="mac-dot-g"></div></div>
        <span class="code-label-mac">Dart</span>
        <button class="copy-btn">Copy</button>
      </div>
<pre><span class="c">// 1. Define Collection</span>
<span class="ann">@collection</span>
<span class="k">class</span> <span class="t">Product</span> {
  <span class="t">Id</span> <span class="n">id</span> = <span class="t">Isar</span>.<span class="n">autoIncrement</span>;
  
  <span class="ann">@Index</span>(<span class="n">type</span>: <span class="t">IndexType</span>.<span class="n">value</span>) <span class="c">// Create an index for fast querying</span>
  <span class="k">late</span> <span class="t">String</span> <span class="n">name</span>;
  <span class="k">late</span> <span class="t">double</span> <span class="n">price</span>;
}

<span class="c">// 2. Initialize Isar</span>
<span class="k">final</span> <span class="n">dir</span> = <span class="k">await</span> <span class="m">getApplicationDocumentsDirectory</span>();
<span class="k">final</span> <span class="n">isar</span> = <span class="k">await</span> <span class="t">Isar</span>.<span class="m">open</span>(
  [<span class="t">ProductSchema</span>],
  <span class="n">directory</span>: <span class="n">dir</span>.<span class="n">path</span>,
);

<span class="c">// 3. Async Write (Implicit Transaction)</span>
<span class="k">final</span> <span class="n">newProduct</span> = <span class="t">Product</span>()..<span class="n">name</span> = <span class="s">'MacBook'</span>..<span class="n">price</span> = <span class="num">1200.0</span>;
<span class="k">await</span> <span class="n">isar</span>.<span class="m">writeTxn</span>(() <span class="k">async</span> {
  <span class="k">await</span> <span class="n">isar</span>.<span class="n">products</span>.<span class="m">put</span>(<span class="n">newProduct</span>);
});

<span class="c">// 4. Powerful Queries &amp; Watchers</span>
<span class="c">// Find all products under $1500 starting with 'Mac'</span>
<span class="k">final</span> <span class="n">cheapMacs</span> = <span class="k">await</span> <span class="n">isar</span>.<span class="n">products</span>.<span class="m">filter</span>()
  .<span class="m">priceLessThan</span>(<span class="num">1500.0</span>)
  .<span class="m">nameStartsWith</span>(<span class="s">'Mac'</span>)
  .<span class="m">findAll</span>();

<span class="c">// Watch collection for reactive UI updates</span>
<span class="t">Stream</span>&lt;<span class="t">List</span>&lt;<span class="t">Product</span>&gt;&gt; <span class="n">productsStream</span> = <span class="n">isar</span>.<span class="n">products</span>.<span class="m">watchLazy</span>();</pre>
    </div>
  </div>
</section>
"""

with open('flutter_notes.html', 'a') as f:
    f.write(s8)
print('S8 done:', len(s8))
