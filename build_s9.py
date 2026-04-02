s9 = """
<!-- SECTION 9 -->
<section class="section" id="s9">
  <div class="section-header">
    <div class="section-icon" style="background:var(--purple-bg);">🚀</div>
    <div class="section-meta">
      <span class="section-badge" style="background:var(--purple-bg);color:var(--purple);">Advanced</span>
      <div class="section-title" style="color:var(--purple);">Advanced Topics</div>
      <div class="section-subtitle">Isolates, Platform Channels, Background Services, and Deep Performance</div>
    </div>
  </div>

  <!-- 9.1 Isolates -->
  <div class="subsection" id="s9-1">
    <h3 style="color:var(--purple);">9.1 Isolates &amp; True Multithreading</h3>
    <p>Dart code runs in an <strong>Isolate</strong>, which has its own memory heap and a single thread running an <strong>Event Loop</strong>. Heavy synchronous code (like parsing a 10MB JSON file or applying image filters) blocks the Event Loop, causing UI "jank" (dropped frames). To fix this, you spawn a new Isolate. Isolates do not share memory; they communicate by passing messages via <code>SendPort</code> and <code>ReceivePort</code>.</p>

    <div class="grid-2">
      <div class="card">
        <div class="card-title" style="color:var(--teal);">Single Threaded (Blocking)</div>
        <p>Main Isolate handles UI, touches, and async I/O. A heavy computation here will freeze the app until it finishes.</p>
        <div class="code-wrap"><button class="copy-btn">Copy</button>
<pre><span class="c">// UI freezes until done!</span>
<span class="t">List</span>&lt;<span class="t">User</span>&gt; <span class="m">users</span> = <span class="m">parseLargeJson</span>(<span class="n">data</span>);</pre>
        </div>
      </div>
      <div class="card">
        <div class="card-title" style="color:var(--purple);">Multi Isolate (Non-blocking)</div>
        <p>Heavy work is offloaded to a background Isolate. The main Isolate is free to render 60/120fps animations.</p>
        <div class="code-wrap"><button class="copy-btn">Copy</button>
<pre><span class="c">// UI remains perfectly smooth</span>
<span class="t">List</span>&lt;<span class="t">User</span>&gt; <span class="m">users</span> = <span class="k">await</span> <span class="t">Isolate</span>.<span class="m">run</span>(
  () =&gt; <span class="m">parseLargeJson</span>(<span class="n">data</span>)
);</pre>
        </div>
      </div>
    </div>

    <div class="code-wrap">
      <span class="code-label">Dart (Isolate deep dive)</span>
      <button class="copy-btn">Copy</button>
<pre><span class="c">// 1. Isolate.run() (Dart 2.19+) - THE BEST WAY</span>
<span class="c">// Automatic spawn, execute, return, and kill. Can capture variables!</span>
<span class="k">Future</span>&lt;<span class="t">List</span>&lt;<span class="t">Product</span>&gt;&gt; <span class="m">fetchAndParseProducts</span>() <span class="k">async</span> {
  <span class="k">final</span> <span class="n">response</span> = <span class="k">await</span> <span class="n">http</span>.<span class="m">get</span>(<span class="t">Uri</span>.<span class="m">parse</span>(<span class="s">'https://api/products'</span>));
  
  <span class="k">return</span> <span class="k">await</span> <span class="t">Isolate</span>.<span class="m">run</span>(() {
    <span class="k">final</span> <span class="n">jsonList</span> = <span class="m">jsonDecode</span>(<span class="n">response</span>.<span class="n">body</span>) <span class="k">as</span> <span class="t">List</span>;
    <span class="k">return</span> <span class="n">jsonList</span>.<span class="m">map</span>((<span class="n">p</span>) =&gt; <span class="t">Product</span>.<span class="m">fromJson</span>(<span class="n">p</span>)).<span class="m">toList</span>();
  });
}

<span class="c">// 2. compute() - The legacy way (requires static/top-level function)</span>
<span class="t">List</span>&lt;<span class="t">Product</span>&gt; <span class="m">deserialize</span>(<span class="t">String</span> <span class="n">json</span>) =&gt; <span class="c">/* parsing logic ... */</span>;
<span class="k">final</span> <span class="n">products</span> = <span class="k">await</span> <span class="m">compute</span>(<span class="n">deserialize</span>, <span class="n">response</span>.<span class="n">body</span>);

<span class="c">// 3. Manual Compute (Two-way continuous communication)</span>
<span class="c">// Use when you need a long-running background worker</span>
<span class="k">void</span> <span class="m">startWorker</span>() <span class="k">async</span> {
  <span class="k">final</span> <span class="n">receivePort</span> = <span class="t">ReceivePort</span>();
  <span class="k">await</span> <span class="t">Isolate</span>.<span class="m">spawn</span>(<span class="n">_heavyWorker</span>, <span class="n">receivePort</span>.<span class="n">sendPort</span>);

  <span class="c">// Listen to messages from the worker</span>
  <span class="n">receivePort</span>.<span class="m">listen</span>((<span class="n">message</span>) {
    <span class="k">if</span> (<span class="n">message</span> <span class="k">is</span> <span class="t">SendPort</span>) {
      <span class="n">message</span>.<span class="m">send</span>(<span class="s">'Do task A'</span>); <span class="c">// Send instruction to worker</span>
    } <span class="k">else</span> {
      <span class="m">print</span>(<span class="s">'Worker result: $message'</span>);
    }
  });
}

<span class="k">static</span> <span class="k">void</span> <span class="m">_heavyWorker</span>(<span class="t">SendPort</span> <span class="n">mainSendPort</span>) {
  <span class="k">final</span> <span class="n">workerReceivePort</span> = <span class="t">ReceivePort</span>();
  <span class="n">mainSendPort</span>.<span class="m">send</span>(<span class="n">workerReceivePort</span>.<span class="n">sendPort</span>); <span class="c">// Handshake</span>

  <span class="n">workerReceivePort</span>.<span class="m">listen</span>((<span class="n">message</span>) {
    <span class="c">// Process heavy task based on message</span>
    <span class="k">final</span> <span class="n">result</span> = <span class="m">calculateFibonacci</span>(<span class="num">50</span>); 
    <span class="n">mainSendPort</span>.<span class="m">send</span>(<span class="n">result</span>);
  });
}</pre>
    </div>
  </div>

  <!-- 9.2 Platform Channels -->
  <div class="subsection" id="s9-2">
    <h3 style="color:var(--purple);">9.2 Platform Channels &amp; Pigeon</h3>
    <p>Plugins provide access to native features, but sometimes you need a custom native SDK (e.g., custom POS hardware, proprietary C++ library). <strong>MethodChannel</strong> allows Dart to call Kotlin/Swift asynchronously. <strong>EventChannel</strong> allows native to push data streams to Dart (e.g., streaming sensor data). <strong>Pigeon</strong> is the modern, type-safe alternative to raw channels.</p>
    
    <div class="code-wrap">
      <span class="code-label">Dart (Method Channel)</span>
      <button class="copy-btn">Copy</button>
<pre><span class="c">// 1. Dart Side</span>
<span class="k">class</span> <span class="t">NativeService</span> {
  <span class="k">static</span> <span class="k">const</span> <span class="n">_channel</span> = <span class="t">MethodChannel</span>(<span class="s">'com.company.app/native'</span>);

  <span class="k">Future</span>&lt;<span class="t">String</span>&gt; <span class="m">getDeviceHash</span>() <span class="k">async</span> {
    <span class="k">try</span> {
      <span class="c">// Pass arguments map if needed</span>
      <span class="k">final</span> <span class="t">String</span> <span class="n">result</span> = <span class="k">await</span> <span class="n">_channel</span>.<span class="m">invokeMethod</span>(<span class="s">'getHash'</span>, {<span class="s">'salt'</span>: <span class="s">'abc'</span>});
      <span class="k">return</span> <span class="n">result</span>;
    } <span class="k">on</span> <span class="t">PlatformException</span> <span class="k">catch</span> (<span class="n">e</span>) {
      <span class="k">return</span> <span class="s">'Error: ${e.message}'</span>;
    }
  }
}</pre>
    </div>

    <div class="code-wrap">
      <span class="code-label">Kotlin (Android Side)</span>
      <button class="copy-btn">Copy</button>
<pre><span class="c">// MainActivity.kt</span>
<span class="k">class</span> <span class="t">MainActivity</span>: <span class="t">FlutterActivity</span>() {
    <span class="k">private val</span> <span class="n">CHANNEL</span> = <span class="s">"com.company.app/native"</span>

    <span class="k">override fun</span> <span class="m">configureFlutterEngine</span>(<span class="n">flutterEngine</span>: <span class="t">FlutterEngine</span>) {
        <span class="k">super</span>.<span class="m">configureFlutterEngine</span>(<span class="n">flutterEngine</span>)
        <span class="t">MethodChannel</span>(<span class="n">flutterEngine</span>.<span class="n">dartExecutor</span>.<span class="n">binaryMessenger</span>, <span class="n">CHANNEL</span>).<span class="m">setMethodCallHandler</span> {
            <span class="n">call</span>, <span class="n">result</span> <span class="k">-&gt;</span>
            <span class="k">if</span> (<span class="n">call</span>.<span class="n">method</span> == <span class="s">"getHash"</span>) {
                <span class="k">val</span> <span class="n">salt</span> = <span class="n">call</span>.<span class="m">argument</span>&lt;<span class="t">String</span>&gt;(<span class="s">"salt"</span>)
                <span class="n">result</span>.<span class="m">success</span>(<span class="s">"NativeHash123_$salt"</span>)
            } <span class="k">else</span> {
                <span class="n">result</span>.<span class="m">notImplemented</span>()
            }
        }
    }
}</pre>
    </div>
    <div class="info-box info-tip"><strong>💡 Pigeon Code Generator</strong><p>Writing raw <code>MethodChannel</code> code is error-prone because types are checked at runtime. The team behind Flutter recommends <strong>Pigeon</strong>: you define an interface in Dart, and it generates type-safe Dart, Kotlin, and Swift code automatically.</p></div>
  </div>

  <!-- 9.3 Performance & Jank -->
  <div class="subsection" id="s9-3">
    <h3 style="color:var(--purple);">9.3 Performance Optimization Deep-Dive</h3>
    <p>Achieving stable 60/120 FPS requires understanding how Flutter renders. The framework builds a <strong>Widget Tree</strong>, diffs it to create an <strong>Element Tree</strong>, and finally creates a <strong>RenderObject Tree</strong> which does the actual painting.</p>
    
    <div class="table-wrap"><table>
      <tr><th>Optimization</th><th>Problem Solved</th><th>How to apply</th></tr>
      <tr><td><code style="background:var(--blue-bg);color:var(--blue);">const</code> constructors</td><td>Prevents widget rebuilds</td><td>Use <code>const</code> everywhere. If a widget is <code>const</code>, Flutter literally skips it during the diffing phase if its parent rebuilds.</td></tr>
      <tr><td><code style="background:var(--teal-bg);color:var(--teal);">RepaintBoundary</code></td><td>Isolates repaints</td><td>Wrap complex animations or scroll targets in <code>RepaintBoundary</code>. It tells Flutter "paint this subtree into a separate buffer" so other parts aren't forced to redraw.</td></tr>
      <tr><td><code style="background:var(--coral-bg);color:var(--coral);">Opacity</code> vs Color</td><td>Alpha blending cost</td><td><code>Opacity</code> is expensive because it paints the child to a temporary buffer first. Instead of <code>Opacity(opacity: 0.5, child: Container(color: Colors.red))</code> use <code>Container(color: Colors.red.withOpacity(0.5))</code>.</td></tr>
      <tr><td><code style="background:var(--amber-bg);color:var(--amber);">ListView.builder</code></td><td>OOM / Memory limit</td><td>Never use <code>ListView(children: [...1000 items])</code>. <code>builder</code> constructs widgets lazily as they scroll into view.</td></tr>
      <tr><td>Widget extraction</td><td>Excessive rebuild scope</td><td>Don't put a complex <code>setState</code> animation inside a giant <code>build()</code> method. Extract the animated part into a tiny stateful widget.</td></tr>
    </table></div>
    
    <p><strong>Tools:</strong> Run your app in <code>Profile</code> mode (<code>flutter run --profile</code>) to get accurate performance metrics. The <strong>Dart DevTools</strong> provides a timeline to spot UI/Raster jank, and a Memory Profiler to find memory leaks (e.g., forgetting to <code>dispose()</code> controllers).</p>
  </div>
  
  <!-- 9.4 Deep Linking -->
  <div class="subsection" id="s9-4">
    <h3 style="color:var(--purple);">9.4 Deep Links &amp; Universal Links</h3>
    <p>Handling custom URL schemes (<code>myapp://page/123</code>) or Universal Links (<code>https://myapp.com/page/123</code>) so clicking a link on WhatsApp opens your app directly to the right screen.</p>
    <ul>
      <li><strong>App Links / Universal Links:</strong> Requires domain ownership verification via <code>assetlinks.json</code> (Android) and <code>apple-app-site-association</code> (iOS). Very secure.</li>
      <li><strong>Routing:</strong> Packages like <code>go_router</code> handle this seamlessly. When the app opens via a link, <code>go_router</code> automatically parses the path and renders the exact nested tree of screens.</li>
    </ul>
    <div class="code-wrap">
      <span class="code-label">Dart (go_router)</span>
      <button class="copy-btn">Copy</button>
<pre><span class="c">// go_router automatically handles the initial incoming link</span>
<span class="t">GoRoute</span>(
  <span class="n">path</span>: <span class="s">'/products/:id'</span>,
  <span class="n">builder</span>: (<span class="n">context</span>, <span class="n">state</span>) {
    <span class="k">final</span> <span class="n">id</span> = <span class="n">state</span>.<span class="n">pathParameters</span>[<span class="s">'id'</span>]!;
    <span class="k">return</span> <span class="t">ProductDetailsScreen</span>(<span class="n">productId</span>: <span class="n">id</span>);
  },
)</pre>
    </div>
  </div>
</section>
"""

with open('flutter_notes.html', 'a') as f:
    f.write(s9)
print('S9 advanced rewrite done.')
