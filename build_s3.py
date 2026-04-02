
s3 = '''
<!-- ═══════════════════════════════════════════ SECTION 3 ═══ -->
<section class="section" id="s3">
  <div class="section-header">
    <div class="section-icon" style="background:var(--teal-bg);">🎨</div>
    <div class="section-meta">
      <span class="section-badge" style="background:var(--teal-bg);color:var(--teal);">Beginner → Intermediate</span>
      <div class="section-title" style="color:var(--teal);">UI &amp; Layout</div>
      <div class="section-subtitle">Container, Row/Column, Stack, ListView, responsive design</div>
    </div>
  </div>

  <!-- 3.1 Container -->
  <div class="subsection" id="s3-1">
    <h3 style="color:var(--teal);">3.1 Container &amp; Box Model</h3>
    <p><strong>Container</strong> is Flutter's swiss-army widget — it combines padding, margin, decoration, constraints, alignment, and transforms in one. When given no child, Container fills available space. With a child, it sizes to the child unless constrained. <strong>Never use both <code>color</code> and <code>decoration</code></strong> simultaneously — decoration subsumes color.</p>
    <p><strong>BoxDecoration</strong> unlocks rich styling: gradients, border radius, box shadows, and images. The <strong>constraints</strong> property defines min/max width and height — useful for making widgets flexible yet bounded. <strong>Transform</strong> applies matrix transformations (rotate, scale, translate) without affecting layout.</p>
    <div class="diagram">
      <svg viewBox="0 0 860 220" xmlns="http://www.w3.org/2000/svg">
        <!-- margin -->
        <rect x="40" y="20" width="780" height="180" rx="12" fill="#0d2b22" stroke="#34d399" stroke-width="2"/>
        <text x="100" y="50" font-family="JetBrains Mono" font-size="12" font-weight="700" fill="#34d399">margin</text>
        <!-- border -->
        <rect x="100" y="60" width="660" height="120" rx="10" fill="#1a1433" stroke="#a78bfa" stroke-width="2"/>
        <text x="160" y="85" font-family="JetBrains Mono" font-size="12" font-weight="700" fill="#a78bfa">border / decoration</text>
        <!-- padding -->
        <rect x="160" y="95" width="540" height="72" rx="8" fill="#0d1e3b" stroke="#60a5fa" stroke-width="1.5"/>
        <text x="220" y="118" font-family="JetBrains Mono" font-size="12" font-weight="700" fill="#60a5fa">padding</text>
        <!-- child -->
        <rect x="240" y="110" width="380" height="44" rx="6" fill="#161b22" stroke="#30363d" stroke-width="1.5"/>
        <text x="430" y="129" font-family="JetBrains Mono" font-size="12" font-weight="700" fill="#e6edf3" text-anchor="middle">child content</text>
        <text x="430" y="146" font-family="JetBrains Mono" font-size="10" fill="#8b949e" text-anchor="middle">Text · Image · Column · etc.</text>
      </svg>
    </div>
    <div class="code-wrap">
      <span class="code-label">Flutter</span>
      <button class="copy-btn">Copy</button>
<pre><span class="t">Container</span>(
  <span class="n">margin</span>: <span class="k">const</span> <span class="t">EdgeInsets</span>.<span class="m">all</span>(<span class="num">16</span>),
  <span class="n">padding</span>: <span class="k">const</span> <span class="t">EdgeInsets</span>.<span class="m">symmetric</span>(<span class="n">horizontal</span>: <span class="num">24</span>, <span class="n">vertical</span>: <span class="num">16</span>),
  <span class="n">width</span>: <span class="t">double</span>.<span class="n">infinity</span>,
  <span class="n">constraints</span>: <span class="k">const</span> <span class="t">BoxConstraints</span>(
    <span class="n">minHeight</span>: <span class="num">100</span>,
    <span class="n">maxHeight</span>: <span class="num">300</span>,
  ),
  <span class="n">decoration</span>: <span class="t">BoxDecoration</span>(  <span class="c">// ← use decoration, NOT color</span>
    <span class="n">gradient</span>: <span class="k">const</span> <span class="t">LinearGradient</span>(
      <span class="n">colors</span>: [<span class="t">Color</span>(<span class="num">0xFF667eea</span>), <span class="t">Color</span>(<span class="num">0xFF764ba2</span>)],
      <span class="n">begin</span>: <span class="t">Alignment</span>.<span class="n">topLeft</span>,
      <span class="n">end</span>: <span class="t">Alignment</span>.<span class="n">bottomRight</span>,
    ),
    <span class="n">borderRadius</span>: <span class="t">BorderRadius</span>.<span class="m">circular</span>(<span class="num">16</span>),
    <span class="n">boxShadow</span>: [
      <span class="t">BoxShadow</span>(
        <span class="n">color</span>: <span class="t">Colors</span>.<span class="n">black</span>.<span class="m">withOpacity</span>(<span class="num">0.3</span>),
        <span class="n">blurRadius</span>: <span class="num">12</span>,
        <span class="n">offset</span>: <span class="k">const</span> <span class="t">Offset</span>(<span class="num">0</span>, <span class="num">6</span>),
      ),
    ],
    <span class="n">border</span>: <span class="t">Border</span>.<span class="m">all</span>(<span class="n">color</span>: <span class="t">Colors</span>.<span class="n">white24</span>, <span class="n">width</span>: <span class="num">1</span>),
  ),
  <span class="n">child</span>: <span class="k">const</span> <span class="t">Text</span>(
    <span class="s">'Styled Container'</span>,
    <span class="n">style</span>: <span class="t">TextStyle</span>(<span class="n">color</span>: <span class="t">Colors</span>.<span class="n">white</span>, <span class="n">fontSize</span>: <span class="num">18</span>),
  ),
)</pre>
    </div>
    <div class="info-box info-warn"><strong>⚠️ color vs decoration</strong><p>Setting both <code>color</code> and <code>decoration</code> on a Container throws an assertion error at runtime. When using <code>BoxDecoration</code>, place your color inside <code>BoxDecoration(color: ...)</code> instead.</p></div>
  </div>

  <!-- 3.2 Row & Column -->
  <div class="subsection" id="s3-2">
    <h3 style="color:var(--teal);">3.2 Row &amp; Column Deep Dive</h3>
    <p><strong>Row</strong> lays children horizontally; <strong>Column</strong> lays them vertically. <strong>MainAxisAlignment</strong> controls spacing along the main axis. <strong>CrossAxisAlignment</strong> aligns children on the perpendicular axis. <strong>Expanded</strong> fills all remaining main-axis space. <strong>Flexible</strong> can fill some space proportionally via flex factor. <strong>Spacer</strong> is a convenient shorthand for a flexible empty space.</p>
    <p>Row overflow (children wider than available width) crashes with an overflow error. Fix it by wrapping children in <code>Expanded</code>, using <code>Flexible</code>, or wrapping the Row in a <code>SingleChildScrollView</code> with horizontal scroll.</p>
    <div class="diagram">
      <svg viewBox="0 0 860 180" xmlns="http://www.w3.org/2000/svg">
        <text x="20" y="20" font-family="JetBrains Mono" font-size="11" fill="#8b949e">MainAxisAlignment values in a Row:</text>
        <!-- start -->
        <rect x="10" y="30" width="130" height="50" rx="6" fill="#0d2b22" stroke="#34d399" stroke-width="1"/>
        <rect x="16" y="40" width="30" height="30" rx="4" fill="#34d399" opacity=".7"/>
        <rect x="50" y="40" width="30" height="30" rx="4" fill="#34d399" opacity=".5"/>
        <rect x="84" y="40" width="30" height="30" rx="4" fill="#34d399" opacity=".3"/>
        <text x="75" y="94" font-family="JetBrains Mono" font-size="10" fill="#34d399" text-anchor="middle">start</text>
        <!-- end -->
        <rect x="150" y="30" width="130" height="50" rx="6" fill="#0d2b22" stroke="#34d399" stroke-width="1"/>
        <rect x="156" y="40" width="30" height="30" rx="4" fill="#34d399" opacity=".3"/>
        <rect x="190" y="40" width="30" height="30" rx="4" fill="#34d399" opacity=".5"/>
        <rect x="224" y="40" width="30" height="30" rx="4" fill="#34d399" opacity=".7"/>
        <text x="215" y="94" font-family="JetBrains Mono" font-size="10" fill="#34d399" text-anchor="middle">end</text>
        <!-- center -->
        <rect x="290" y="30" width="130" height="50" rx="6" fill="#0d2b22" stroke="#34d399" stroke-width="1"/>
        <rect x="310" y="40" width="30" height="30" rx="4" fill="#34d399" opacity=".5"/>
        <rect x="344" y="40" width="30" height="30" rx="4" fill="#34d399" opacity=".7"/>
        <rect x="378" y="40" width="30" height="30" rx="4" fill="#34d399" opacity=".5"/>
        <text x="355" y="94" font-family="JetBrains Mono" font-size="10" fill="#34d399" text-anchor="middle">center</text>
        <!-- spaceBetween -->
        <rect x="430" y="30" width="130" height="50" rx="6" fill="#0d2b22" stroke="#34d399" stroke-width="1"/>
        <rect x="436" y="40" width="30" height="30" rx="4" fill="#34d399" opacity=".7"/>
        <rect x="490" y="40" width="30" height="30" rx="4" fill="#34d399" opacity=".7"/>
        <rect x="524" y="40" width="30" height="30" rx="4" fill="#34d399" opacity=".7"/>
        <text x="495" y="94" font-family="JetBrains Mono" font-size="10" fill="#34d399" text-anchor="middle">spaceBetween</text>
        <!-- spaceAround -->
        <rect x="570" y="30" width="130" height="50" rx="6" fill="#0d2b22" stroke="#34d399" stroke-width="1"/>
        <rect x="582" y="40" width="28" height="30" rx="4" fill="#34d399" opacity=".6"/>
        <rect x="621" y="40" width="28" height="30" rx="4" fill="#34d399" opacity=".6"/>
        <rect x="660" y="40" width="28" height="30" rx="4" fill="#34d399" opacity=".6"/>
        <text x="635" y="94" font-family="JetBrains Mono" font-size="10" fill="#34d399" text-anchor="middle">spaceAround</text>
        <!-- spaceEvenly -->
        <rect x="710" y="30" width="140" height="50" rx="6" fill="#0d2b22" stroke="#34d399" stroke-width="1"/>
        <rect x="720" y="40" width="28" height="30" rx="4" fill="#34d399" opacity=".7"/>
        <rect x="758" y="40" width="28" height="30" rx="4" fill="#34d399" opacity=".7"/>
        <rect x="796" y="40" width="28" height="30" rx="4" fill="#34d399" opacity=".7"/>
        <text x="780" y="94" font-family="JetBrains Mono" font-size="10" fill="#34d399" text-anchor="middle">spaceEvenly</text>
        <!-- labels -->
        <text x="75" y="115" font-family="JetBrains Mono" font-size="10" fill="#8b949e" text-anchor="middle">Expanded:</text>
        <rect x="10" y="125" width="130" height="30" rx="6" fill="#0d2b22" stroke="#34d399" stroke-width="1"/>
        <rect x="16" y="130" width="80" height="20" rx="4" fill="#34d399" opacity=".7"/>
        <text x="56" y="145" font-family="JetBrains Mono" font-size="10" fill="#0d1117" text-anchor="middle">Expanded</text>
        <rect x="100" y="130" width="34" height="20" rx="4" fill="#34d399" opacity=".3"/>
        <text x="215" y="115" font-family="JetBrains Mono" font-size="10" fill="#8b949e" text-anchor="middle">Spacer:</text>
        <rect x="150" y="125" width="130" height="30" rx="6" fill="#0d2b22" stroke="#34d399" stroke-width="1"/>
        <rect x="156" y="130" width="34" height="20" rx="4" fill="#34d399" opacity=".7"/>
        <rect x="210" y="130" width="30" height="20" rx="4" fill="#1a1433" opacity=".7"/>
        <rect x="244" y="130" width="30" height="20" rx="4" fill="#34d399" opacity=".7"/>
        <text x="240" y="145" font-family="JetBrains Mono" font-size="9" fill="#a78bfa" text-anchor="middle">←Spacer→</text>
      </svg>
    </div>
    <div class="code-wrap">
      <span class="code-label">Flutter</span>
      <button class="copy-btn">Copy</button>
<pre><span class="c">// Row with alignment and Expanded</span>
<span class="t">Row</span>(
  <span class="n">mainAxisAlignment</span>: <span class="t">MainAxisAlignment</span>.<span class="n">spaceBetween</span>,
  <span class="n">crossAxisAlignment</span>: <span class="t">CrossAxisAlignment</span>.<span class="n">center</span>,
  <span class="n">children</span>: [
    <span class="k">const</span> <span class="t">Icon</span>(<span class="t">Icons</span>.<span class="n">flutter_dash</span>, <span class="n">size</span>: <span class="num">32</span>),
    <span class="k">const</span> <span class="t">Expanded</span>(  <span class="c">// fills remaining space</span>
      <span class="n">child</span>: <span class="t">Text</span>(<span class="s">'Flutter is awesome'</span>, <span class="n">overflow</span>: <span class="t">TextOverflow</span>.<span class="n">ellipsis</span>),
    ),
    <span class="k">const</span> <span class="t">Spacer</span>(),  <span class="c">// flexible gap</span>
    <span class="t">ElevatedButton</span>(<span class="n">onPressed</span>: () {}, <span class="n">child</span>: <span class="k">const</span> <span class="t">Text</span>(<span class="s">'Go'</span>)),
  ],
)

<span class="c">// Column with flex proportions</span>
<span class="t">Column</span>(
  <span class="n">children</span>: [
    <span class="t">Flexible</span>(<span class="n">flex</span>: <span class="num">2</span>, <span class="n">child</span>: <span class="t">Container</span>(<span class="n">color</span>: <span class="t">Colors</span>.<span class="n">blue</span>)),   <span class="c">// 2/5 height</span>
    <span class="t">Flexible</span>(<span class="n">flex</span>: <span class="num">3</span>, <span class="n">child</span>: <span class="t">Container</span>(<span class="n">color</span>: <span class="t">Colors</span>.<span class="n">green</span>)),  <span class="c">// 3/5 height</span>
  ],
)

<span class="c">// Fix Row overflow with Flexible</span>
<span class="t">Row</span>(
  <span class="n">children</span>: [
    <span class="k">const</span> <span class="t">Icon</span>(<span class="t">Icons</span>.<span class="n">star</span>),
    <span class="k">const</span> <span class="t">Flexible</span>(  <span class="c">// shrinks to fit, won't overflow</span>
      <span class="n">child</span>: <span class="t">Text</span>(<span class="s">'Very long text that might overflow without Flexible'</span>,
        <span class="n">overflow</span>: <span class="t">TextOverflow</span>.<span class="n">ellipsis</span>),
    ),
  ],
)</pre>
    </div>
    <div class="info-box info-tip"><strong>💡 Expanded vs Flexible</strong><p><code>Expanded</code> is <code>Flexible</code> with <code>fit: FlexFit.tight</code> — it <em>must</em> fill the space. <code>Flexible</code> defaults to <code>FlexFit.loose</code> — it <em>can</em> use up to the flex space but can be smaller. Use <code>Flexible</code> when the child might be smaller than its allocation.</p></div>
  </div>

  <!-- 3.3 Stack -->
  <div class="subsection" id="s3-3">
    <h3 style="color:var(--teal);">3.3 Stack &amp; Positioned</h3>
    <p><strong>Stack</strong> layers children on the Z-axis — later children are painted on top. Non-<code>Positioned</code> children use the <code>alignment</code> property of the Stack. <code>Positioned</code> lets you place children at exact offsets from the Stack's edges. <code>Positioned.fill</code> is a shorthand for covering the entire Stack area.</p>
    <p>Common use cases: badge overlays on icons, gradient overlays on images, floating labels, bottom-of-card CTAs, and custom FAB-like components not tied to Scaffold.</p>
    <div class="code-wrap">
      <span class="code-label">Flutter</span>
      <button class="copy-btn">Copy</button>
<pre><span class="t">Stack</span>(
  <span class="n">children</span>: [
    <span class="c">// Base: full-size image</span>
    <span class="t">Image</span>.<span class="m">network</span>(
      <span class="s">'https://picsum.photos/400/200'</span>,
      <span class="n">fit</span>: <span class="t">BoxFit</span>.<span class="n">cover</span>,
      <span class="n">width</span>: <span class="t">double</span>.<span class="n">infinity</span>,
      <span class="n">height</span>: <span class="num">200</span>,
    ),
    <span class="c">// Gradient overlay — fades bottom to black</span>
    <span class="t">Positioned</span>.<span class="m">fill</span>(
      <span class="n">child</span>: <span class="k">const</span> <span class="t">DecoratedBox</span>(
        <span class="n">decoration</span>: <span class="t">BoxDecoration</span>(
          <span class="n">gradient</span>: <span class="t">LinearGradient</span>(
            <span class="n">begin</span>: <span class="t">Alignment</span>.<span class="n">topCenter</span>,
            <span class="n">end</span>: <span class="t">Alignment</span>.<span class="n">bottomCenter</span>,
            <span class="n">colors</span>: [<span class="t">Colors</span>.<span class="n">transparent</span>, <span class="t">Colors</span>.<span class="n">black87</span>],
          ),
        ),
      ),
    ),
    <span class="c">// Caption at bottom</span>
    <span class="k">const</span> <span class="t">Positioned</span>(
      <span class="n">bottom</span>: <span class="num">16</span>, <span class="n">left</span>: <span class="num">16</span>, <span class="n">right</span>: <span class="num">16</span>,
      <span class="n">child</span>: <span class="t">Text</span>(<span class="s">'Mountain Landscape'</span>,
        <span class="n">style</span>: <span class="t">TextStyle</span>(<span class="n">color</span>: <span class="t">Colors</span>.<span class="n">white</span>, <span class="n">fontSize</span>: <span class="num">18</span>, <span class="n">fontWeight</span>: <span class="t">FontWeight</span>.<span class="n">bold</span>)),
    ),
    <span class="c">// Badge top-right</span>
    <span class="k">const</span> <span class="t">Positioned</span>(
      <span class="n">top</span>: <span class="num">8</span>, <span class="n">right</span>: <span class="num">8</span>,
      <span class="n">child</span>: <span class="t">Chip</span>(
        <span class="n">label</span>: <span class="t">Text</span>(<span class="s">'NEW'</span>, <span class="n">style</span>: <span class="t">TextStyle</span>(<span class="n">fontSize</span>: <span class="num">11</span>)),
        <span class="n">backgroundColor</span>: <span class="t">Colors</span>.<span class="n">purple</span>,
      ),
    ),
  ],
)</pre>
    </div>
    <div class="info-box info-key"><strong>🔑 Stack Sizing</strong><p>By default, Stack sizes to its largest non-Positioned child. Set <code>fit: StackFit.expand</code> to force the Stack to fill its parent. All Positioned children are then placed relative to that expanded area.</p></div>
  </div>

  <!-- 3.4 ListView -->
  <div class="subsection" id="s3-4">
    <h3 style="color:var(--teal);">3.4 ListView &amp; GridView</h3>
    <p><strong>ListView</strong> is a scrollable column. <code>ListView(children: [...])</code> builds all children upfront — fine for short lists. <code>ListView.builder</code> is lazy — it only builds widgets currently visible on screen. For lists with thousands of items, <code>builder</code> is essential. <code>ListView.separated</code> adds dividers automatically between items.</p>
    <p><strong>GridView.count</strong> creates a fixed-column grid. <strong>GridView.builder</strong> is the lazy version for large grids. <strong>Never</strong> put a ListView inside a Column without either <code>Expanded</code>, <code>shrinkWrap: true</code> (avoid in long lists — expensive!), or a fixed height constraint.</p>
    <div class="code-wrap">
      <span class="code-label">Flutter</span>
      <button class="copy-btn">Copy</button>
<pre><span class="c">// ListView.builder — lazy, efficient</span>
<span class="t">ListView</span>.<span class="m">builder</span>(
  <span class="n">itemCount</span>: <span class="n">messages</span>.<span class="n">length</span>,
  <span class="n">itemBuilder</span>: (<span class="n">context</span>, <span class="n">index</span>) {
    <span class="k">final</span> <span class="n">msg</span> = <span class="n">messages</span>[<span class="n">index</span>];
    <span class="k">return</span> <span class="t">MessageTile</span>(<span class="n">message</span>: <span class="n">msg</span>, <span class="n">key</span>: <span class="t">ValueKey</span>(<span class="n">msg</span>.<span class="n">id</span>));
  },
)

<span class="c">// ListView.separated — with dividers</span>
<span class="t">ListView</span>.<span class="m">separated</span>(
  <span class="n">itemCount</span>: <span class="n">items</span>.<span class="n">length</span>,
  <span class="n">separatorBuilder</span>: (<span class="n">_</span>, <span class="n">__</span>) =&gt; <span class="k">const</span> <span class="t">Divider</span>(<span class="n">height</span>: <span class="num">1</span>),
  <span class="n">itemBuilder</span>: (<span class="n">context</span>, <span class="n">index</span>) =&gt; <span class="t">ListTile</span>(
    <span class="n">title</span>: <span class="t">Text</span>(<span class="n">items</span>[<span class="n">index</span>].<span class="n">title</span>),
    <span class="n">subtitle</span>: <span class="t">Text</span>(<span class="n">items</span>[<span class="n">index</span>].<span class="n">subtitle</span>),
    <span class="n">leading</span>: <span class="t">CircleAvatar</span>(<span class="n">child</span>: <span class="t">Text</span>(<span class="s">'${index + 1}'</span>)),
    <span class="n">onTap</span>: () =&gt; <span class="m">onItemTap</span>(<span class="n">items</span>[<span class="n">index</span>]),
  ),
)

<span class="c">// GridView.builder — lazy 2-column product grid</span>
<span class="t">GridView</span>.<span class="m">builder</span>(
  <span class="n">gridDelegate</span>: <span class="k">const</span> <span class="t">SliverGridDelegateWithFixedCrossAxisCount</span>(
    <span class="n">crossAxisCount</span>: <span class="num">2</span>,
    <span class="n">crossAxisSpacing</span>: <span class="num">12</span>,
    <span class="n">mainAxisSpacing</span>: <span class="num">12</span>,
    <span class="n">childAspectRatio</span>: <span class="num">0.75</span>,
  ),
  <span class="n">itemCount</span>: <span class="n">products</span>.<span class="n">length</span>,
  <span class="n">itemBuilder</span>: (<span class="n">context</span>, <span class="n">index</span>) =&gt;
      <span class="t">ProductCard</span>(<span class="n">product</span>: <span class="n">products</span>[<span class="n">index</span>]),
)</pre>
    </div>
    <div class="info-box info-warn"><strong>⚠️ shrinkWrap: true</strong><p><code>shrinkWrap: true</code> forces ListView to measure all children even if they're not visible — defeating the lazy loading entirely. Instead, wrap ListView in <code>Expanded</code> or give it a fixed height with a <code>SizedBox</code>.</p></div>
  </div>

  <!-- 3.5 Responsive -->
  <div class="subsection" id="s3-5">
    <h3 style="color:var(--teal);">3.5 Responsive Layouts</h3>
    <p><strong>MediaQuery</strong> provides screen dimensions, padding, orientation, and device pixel ratio. Use <code>MediaQuery.sizeOf(context)</code> (Flutter 3.10+) instead of <code>MediaQuery.of(context).size</code> — the former only rebuilds when size changes, reducing unnecessary rebuilds.</p>
    <p><strong>LayoutBuilder</strong> gives you the parent widget's constraints — better than MediaQuery when you need to respond to container size rather than screen size. This is essential for reusable components that might appear in sidebars or dialogs. <strong>SafeArea</strong> ensures content isn't hidden behind notches, status bars, or system gesture areas.</p>
    <div class="flow-row">
      <div class="flow-box" style="background:var(--teal-bg);border-color:var(--teal);color:var(--teal);">320px Mobile</div>
      <span class="flow-arrow">→</span>
      <div class="flow-box" style="background:var(--blue-bg);border-color:var(--blue);color:var(--blue);">600px Tablet</div>
      <span class="flow-arrow">→</span>
      <div class="flow-box" style="background:var(--purple-bg);border-color:var(--purple);color:var(--purple);">900px Desktop</div>
      <span class="flow-arrow">→</span>
      <div class="flow-box" style="background:var(--amber-bg);border-color:var(--amber);color:var(--amber);">1200px Wide</div>
    </div>
    <div class="code-wrap">
      <span class="code-label">Flutter</span>
      <button class="copy-btn">Copy</button>
<pre><span class="c">// LayoutBuilder — responds to parent constraints</span>
<span class="t">LayoutBuilder</span>(
  <span class="n">builder</span>: (<span class="n">context</span>, <span class="n">constraints</span>) {
    <span class="k">final</span> <span class="n">isWide</span> = <span class="n">constraints</span>.<span class="n">maxWidth</span> &gt; <span class="num">600</span>;
    <span class="k">return</span> isWide
        ? <span class="t">Row</span>(
            <span class="n">children</span>: [
              <span class="t">SizedBox</span>(<span class="n">width</span>: <span class="num">280</span>, <span class="n">child</span>: <span class="t">Sidebar</span>()),
              <span class="k">const</span> <span class="t">Expanded</span>(<span class="n">child</span>: <span class="t">MainContent</span>()),
            ],
          )
        : <span class="k">const</span> <span class="t">MainContent</span>();  <span class="c">// mobile: no sidebar</span>
  },
)

<span class="c">// AdaptiveLayout class (manual breakpoint)</span>
<span class="k">class</span> <span class="t">AppLayout</span> <span class="k">extends</span> <span class="t">StatelessWidget</span> {
  <span class="k">const</span> <span class="t">AppLayout</span>({<span class="k">super</span>.<span class="n">key</span>});
  <span class="ann">@override</span>
  <span class="t">Widget</span> <span class="m">build</span>(<span class="t">BuildContext</span> <span class="n">context</span>) {
    <span class="k">final</span> <span class="n">screenWidth</span> = <span class="t">MediaQuery</span>.<span class="m">sizeOf</span>(<span class="n">context</span>).<span class="n">width</span>;
    <span class="k">return</span> <span class="t">SafeArea</span>(
      <span class="n">child</span>: <span class="n">screenWidth</span> &lt; <span class="num">600</span>
          ? <span class="k">const</span> <span class="t">MobileLayout</span>()
          : <span class="n">screenWidth</span> &lt; <span class="num">900</span>
              ? <span class="k">const</span> <span class="t">TabletLayout</span>()
              : <span class="k">const</span> <span class="t">DesktopLayout</span>(),
    );
  }
}</pre>
    </div>
    <div class="info-box info-tip"><strong>💡 Use flutter_adaptive_scaffold</strong><p>The official <code>flutter_adaptive_scaffold</code> package (from the Flutter team) provides <code>AdaptiveScaffold</code> and <code>AdaptiveLayout</code> widgets that automatically implement Material You adaptive layout patterns for different breakpoints.</p></div>
  </div>
  <!-- 3.4 Slivers & Scrolling -->
  <div class="subsection" id="s3-4">
    <h3 style="color:var(--teal);">3.4 Slivers &amp; Custom Scrolling</h3>
    <p>When you use a <code>ListView</code>, Flutter actually wraps your content in a <strong>SliverList</strong> inside a <strong>CustomScrollView</strong>. A "Sliver" is a portion of a scrollable area. By dropping down to the Sliver API, you can create complex, custom scroll effects like collapsing headers, sticky headers, or grids that merge seamlessly into lists.</p>
    <div class="code-wrap">
      <div class="mac-header">
        <div class="mac-dots"><div class="mac-dot-r"></div><div class="mac-dot-y"></div><div class="mac-dot-g"></div></div>
        <span class="code-label-mac">Dart</span>
        <button class="copy-btn">Copy</button>
      </div>
<pre><span class="t">CustomScrollView</span>(
  <span class="n">slivers</span>: [
    <span class="c">// 1. Collapsing App Bar</span>
    <span class="t">SliverAppBar</span>(
      <span class="n">expandedHeight</span>: <span class="num">200.0</span>,
      <span class="n">floating</span>: <span class="k">false</span>,
      <span class="n">pinned</span>: <span class="k">true</span>, <span class="c">// Stays pinned at top when scrolling down</span>
      <span class="n">flexibleSpace</span>: <span class="t">FlexibleSpaceBar</span>(
        <span class="n">title</span>: <span class="t">Text</span>(<span class="s">'Sliver Mastery'</span>),
        <span class="n">background</span>: <span class="t">Image</span>.<span class="m">network</span>(<span class="n">bgUrl</span>, <span class="n">fit</span>: <span class="t">BoxFit</span>.<span class="n">cover</span>),
      ),
    ),
    
    <span class="c">// 2. A ListView equivalent that lives inside the main scroll</span>
    <span class="t">SliverList</span>(
      <span class="n">delegate</span>: <span class="t">SliverChildBuilderDelegate</span>(
        (<span class="n">context</span>, <span class="n">index</span>) =&gt; <span class="t">ListTile</span>(<span class="n">title</span>: <span class="t">Text</span>(<span class="s">'Item $index'</span>)),
        <span class="n">childCount</span>: <span class="num">20</span>,
      ),
    ),
    
    <span class="c">// 3. A GridView equivalent seamlessly following the list</span>
    <span class="t">SliverGrid</span>(
      <span class="n">gridDelegate</span>: <span class="k">const</span> <span class="t">SliverGridDelegateWithFixedCrossAxisCount</span>(
        <span class="n">crossAxisCount</span>: <span class="num">2</span>,
      ),
      <span class="n">delegate</span>: <span class="t">SliverChildBuilderDelegate</span>(
        (<span class="n">context</span>, <span class="n">index</span>) =&gt; <span class="t">GridTile</span>(<span class="n">child</span>: <span class="t">FlutterLogo</span>()),
        <span class="n">childCount</span>: <span class="num">10</span>,
      ),
    ),
  ],
)</pre>
    </div>
  </div>
</section>
'''

with open('flutter_notes.html', 'a') as f:
    f.write(s3)
print('Section 3 appended. Len:', len(s3))
