s13 = '''
<!-- ═══════════════════════════════════════════ SECTION 13 ═══ -->
<section class="section" id="s13">
  <div class="section-header">
    <div class="section-icon" style="background:var(--amber-bg);">⚡</div>
    <div class="section-meta">
      <span class="section-badge" style="background:var(--amber-bg);color:var(--amber);">Advanced Dart</span>
      <div class="section-title" style="color:var(--amber);">Async Deep Dive &amp; Best Practices</div>
      <div class="section-subtitle">Streams, Isolates, and helpful utility methods</div>
    </div>
  </div>

  <!-- 13.1 Isolates -->
  <div class="subsection" id="s13-1">
    <h3 style="color:var(--amber);">13.1 Concurrency vs Parallelism (Isolates)</h3>
    <p>Dart is <strong>single-threaded</strong> by default. Using <code>async/await</code> provides <strong>concurrency</strong> (not blocking the thread while waiting for network/disk I/O). However, if you do heavy computational work (e.g., parsing a 50MB JSON file or applying an image filter), you will freeze the UI thread and drop frames.</p>
    <p>For true <strong>parallelism</strong>, Dart provides <strong>Isolates</strong>. Isolates are independent execution threads with their own isolated memory heap. They communicate purely by passing messages via ports.</p>

    <div class="code-wrap">
      <span class="code-label">Dart</span>
      <button class="copy-btn">Copy</button>
<pre><span class="k">import</span> <span class="s">'dart:isolate'</span>;

<span class="c">// Heavy computational function (Must be a top-level or static function)</span>
<span class="t">int</span> <span class="m">complexMath</span>(<span class="t">int</span> <span class="n">iterationLimit</span>) {
  <span class="t">int</span> <span class="n">sum</span> = <span class="num">0</span>;
  <span class="k">for</span> (<span class="t">int</span> <span class="n">i</span> = <span class="num">0</span>; <span class="n">i</span> &lt; <span class="n">iterationLimit</span>; <span class="n">i</span>++) {
    <span class="n">sum</span> += <span class="n">i</span>;
  }
  <span class="k">return</span> <span class="n">sum</span>;
}

<span class="c">// Flutter simplifies isolates with Isolate.run() (Dart 2.15+)</span>
<span class="k">Future</span>&lt;<span class="k">void</span>&gt; <span class="m">processData</span>() <span class="k">async</span> {
  <span class="m">print</span>(<span class="s">'Starting heavy work on separate thread...'</span>);
  
  <span class="c">// Spawns an isolate, runs the function, returns result, and kills isolate</span>
  <span class="k">final</span> <span class="n">result</span> = <span class="k">await</span> <span class="t">Isolate</span>.<span class="m">run</span>(() =&gt; <span class="m">complexMath</span>(<span class="num">1000000000</span>));
  
  <span class="m">print</span>(<span class="s">'Result computed in background: $result'</span>);
}</pre>
    </div>
  </div>

  <!-- 13.2 Streams Deep Dive -->
  <div class="subsection" id="s13-2">
    <h3 style="color:var(--amber);">13.2 Streams &amp; Generators</h3>
    <p>Where <code>Future</code> represents a single value arriving later, a <code>Stream</code> represents <strong>multiple values</strong> arriving over time. You create complex streams easily using <code>sync*</code> (synchronous generators) and <code>async*</code> (asynchronous generators), utilizing the <code>yield</code> keyword.</p>

    <div class="info-box info-key"><strong>🔑 Single vs Broadcast Streams</strong><p>A standard Stream can only be listened to <strong>once</strong> (e.g., reading a file stream). If multiple parts of your app need to act on the same events (like a button click or a global bus), you must transform it using <code>.asBroadcastStream()</code>.</p></div>

    <div class="code-wrap">
      <span class="code-label">Dart</span>
      <button class="copy-btn">Copy</button>
<pre><span class="c">// Synchronous generator (Iterable)</span>
<span class="t">Iterable</span>&lt;<span class="t">int</span>&gt; <span class="m">countDownSync</span>(<span class="t">int</span> <span class="n">n</span>) <span class="k">sync</span>* {
  <span class="k">while</span> (<span class="n">n</span> &gt; <span class="num">0</span>) {
    <span class="k">yield</span> <span class="n">n</span>--;
  }
}

<span class="c">// Asynchronous generator (Stream)</span>
<span class="t">Stream</span>&lt;<span class="t">int</span>&gt; <span class="m">countDownAsync</span>(<span class="t">int</span> <span class="n">n</span>) <span class="k">async</span>* {
  <span class="k">while</span> (<span class="n">n</span> &gt; <span class="num">0</span>) {
    <span class="k">await</span> <span class="t">Future</span>.<span class="m">delayed</span>(<span class="k">const</span> <span class="t">Duration</span>(<span class="n">seconds</span>: <span class="num">1</span>));
    <span class="k">yield</span> <span class="n">n</span>--;
  }
}

<span class="c">// Listening to a stream natively using await for</span>
<span class="k">Future</span>&lt;<span class="k">void</span>&gt; <span class="m">monitorStream</span>() <span class="k">async</span> {
  <span class="k">final</span> <span class="n">stream</span> = <span class="m">countDownAsync</span>(<span class="num">3</span>);
  <span class="c">// This loop waits asynchronously for each emitted item</span>
  <span class="k">await for</span> (<span class="k">final</span> <span class="n">value</span> <span class="k">in</span> <span class="n">stream</span>) {
    <span class="m">print</span>(<span class="n">value</span>);
  }
  <span class="m">print</span>(<span class="s">'Stream complete'</span>);
}</pre>
    </div>
  </div>

  <!-- 13.3 Dart Helpers & Interview Cheatsheet -->
  <div class="subsection" id="s13-3">
    <h3 style="color:var(--amber);">13.3 Everyday Dart Helpers</h3>
    <p>A few common logic requirements from standard Dart usage.</p>
    
    <div class="table-wrap"><table>
      <tr><th>Action</th><th>Code Example</th></tr>
      <tr><td>Convert String to Int</td><td><code>int.parse('42')</code> or <code>int.tryParse('invalid') // returns null</code></td></tr>
      <tr><td>Random Number (0-9)</td><td><code>import 'dart:math'; final rnd = Random().nextInt(10);</code></td></tr>
      <tr><td>Reverse a List</td><td><code>myList.reversed.toList();</code></td></tr>
      <tr><td>DateTime Formatting</td><td><code>DateTime.now().toIso8601String()</code> (For beautiful UI time formats, use the <code>intl</code> package!)</td></tr>
      <tr><td>Cascade Null Check</td><td><code>myObject?..method1()..?field = value;</code> (Executes safely only if <code>myObject</code> is not null)</td></tr>
    </table></div>
  </div>
</section>
'''

with open('flutter_notes.html', 'a') as f:
    f.write(s13)
print('Section 13 (Async & Helpers) appended. Len:', len(s13))
