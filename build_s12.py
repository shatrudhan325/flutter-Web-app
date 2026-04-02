s12 = '''
<!-- ═══════════════════════════════════════════ SECTION 12 ═══ -->
<section class="section" id="s12">
  <div class="section-header">
    <div class="section-icon" style="background:var(--blue-bg);">🧬</div>
    <div class="section-meta">
      <span class="section-badge" style="background:var(--blue-bg);color:var(--blue);">Advanced Dart</span>
      <div class="section-title" style="color:var(--blue);">OOP Details &amp; File Handling</div>
      <div class="section-subtitle">Factory constructors, abstract interfaces, mixins, and I/O</div>
    </div>
  </div>

  <!-- 12.1 Factory Constructors -->
  <div class="subsection" id="s12-1">
    <h3 style="color:var(--blue);">12.1 Factory Constructors &amp; Singletons</h3>
    <p>A <strong>factory constructor</strong> does not strictly create a new instance of its class entirely from scratch like a generative constructor does. Instead, it can return an existing instance (like from a cache), return an instance of a subclass, or perform complex validation before returning an object.</p>

    <div class="code-wrap">
      <span class="code-label">Dart</span>
      <button class="copy-btn">Copy</button>
<pre><span class="k">class</span> <span class="t">Database</span> {
  <span class="c">// Internal private constructor</span>
  <span class="t">Database</span>.<span class="m">_internal</span>() {
    <span class="m">print</span>(<span class="s">'Database connection initialized'</span>);
  }

  <span class="c">// Static instance cache</span>
  <span class="k">static</span> <span class="k">final</span> <span class="t">Database</span> <span class="n">_instance</span> = <span class="t">Database</span>.<span class="m">_internal</span>();

  <span class="c">// Factory constructor returns the identical instance every time</span>
  <span class="k">factory</span> <span class="t">Database</span>() {
    <span class="k">return</span> <span class="n">_instance</span>;
  }
}

<span class="k">void</span> <span class="m">main</span>() {
  <span class="k">final</span> <span class="n">db1</span> = <span class="t">Database</span>();
  <span class="k">final</span> <span class="n">db2</span> = <span class="t">Database</span>();
  <span class="m">print</span>(<span class="m">identical</span>(<span class="n">db1</span>, <span class="n">db2</span>)); <span class="c">// true (both point to same memory)</span>
}</pre>
    </div>
  </div>

  <!-- 12.2 Mixins in Depth -->
  <div class="subsection" id="s12-2">
    <h3 style="color:var(--blue);">12.2 Mixins and 'on' Clause</h3>
    <p>Mixins allow for code reusability outside of traditional class inheritance. Using the <code>on</code> keyword, you can restrict a mixin so it can only be applied to classes that extend a specific base class. This allows the mixin to call methods from that base class.</p>

    <div class="code-wrap">
      <span class="code-label">Dart</span>
      <button class="copy-btn">Copy</button>
<pre><span class="k">abstract class</span> <span class="t">Animal</span> {
  <span class="k">void</span> <span class="m">breathe</span>() =&gt; <span class="m">print</span>(<span class="s">'Breathing...'</span>);
}

<span class="c">// Mixin restricted to Animals only</span>
<span class="k">mixin</span> <span class="t">Swimmer</span> <span class="k">on</span> <span class="t">Animal</span> {
  <span class="k">void</span> <span class="m">swim</span>() {
    <span class="m">breathe</span>(); <span class="c">// Safe because 'Swimmer' is guaranteed to be an 'Animal'</span>
    <span class="m">print</span>(<span class="s">'Swimming!'</span>);
  }
}

<span class="k">class</span> <span class="t">Dolphin</span> <span class="k">extends</span> <span class="t">Animal</span> <span class="k">with</span> <span class="t">Swimmer</span> { }

<span class="c">// class Stone with Swimmer { } // &lt;-- ERROR: Stone does not extend Animal</span></pre>
    </div>
  </div>

  <!-- 12.3 File Handling -->
  <div class="subsection" id="s12-3">
    <h3 style="color:var(--blue);">12.3 File Handling (dart:io)</h3>
    <p>Dart's <code>dart:io</code> library handles File reading and writing. Keep in mind that <code>dart:io</code> cannot be used in Flutter Web, as web browsers sandbox file systems. For web, you must use <code>dart:html</code> or cross-platform packages like <code>file_picker</code>.</p>

    <div class="grid-2">
      <div class="card glass glow-hover" style="border-top: 3px solid var(--blue);">
        <div class="card-title">Reading Files</div>
        <p>You can read files sync or async. Async is preferred so the main thread (UI) is not blocked.</p>
<pre style="background:transparent;border:none;margin-top:10px;"><code style="color:var(--muted);"><span class="k">final</span> <span class="n">file</span> = <span class="t">File</span>(<span class="s">'data.txt'</span>);
<span class="t">String</span> <span class="n">content</span> = <span class="k">await</span> <span class="n">file</span>.<span class="m">readAsString</span>();</code></pre>
      </div>
      <div class="card glass glow-hover" style="border-top: 3px solid var(--amber);">
        <div class="card-title">Writing Files</div>
        <p>You can overwrite or append to existing files using <code>FileMode</code>.</p>
<pre style="background:transparent;border:none;margin-top:10px;"><code style="color:var(--muted);"><span class="k">final</span> <span class="n">file</span> = <span class="t">File</span>(<span class="s">'log.txt'</span>);
<span class="k">await</span> <span class="n">file</span>.<span class="m">writeAsString</span>(<span class="s">'Log!'</span>, 
  <span class="n">mode</span>: <span class="t">FileMode</span>.<span class="n">append</span>);</code></pre>
      </div>
    </div>
    
    <div class="info-box info-warn"><strong>⚠️ Important Flutter Paths</strong><p>In Flutter mobile apps, you cannot hardcode file paths like <code>C:/files/</code> or <code>/home/user/</code>. You must use the <code>path_provider</code> package to dynamically get the correct directory path (like <code>getApplicationDocumentsDirectory()</code>).</p></div>
  </div>
</section>
'''

with open('flutter_notes.html', 'a') as f:
    f.write(s12)
print('Section 12 (OOP & Files) appended. Len:', len(s12))
