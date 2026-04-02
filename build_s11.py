s11 = """
  </main>

  <footer>
    Built as a single-page reference for <span>Flutter &amp; Dart</span>.<br/>
    Designed for fast searching, offline reading, and continuous learning.
  </footer>

  <!-- Back to Top Button -->
  <button id="back-top" onclick="window.scrollTo({top: 0, behavior: 'smooth'})">⬆ Top</button>

  <script>
    // Copy to clipboard functionality
    document.querySelectorAll('.copy-btn').forEach(btn => {
      btn.addEventListener('click', async () => {
        const pre = btn.nextElementSibling;
        const textToCopy = pre.innerText;
        
        try {
          await navigator.clipboard.writeText(textToCopy);
          const originalText = btn.innerText;
          btn.innerText = 'Copied!';
          btn.style.background = 'var(--teal)';
          btn.style.color = '#000';
          btn.style.borderColor = 'var(--teal)';
          
          setTimeout(() => {
            btn.innerText = originalText;
            btn.style.background = 'var(--bg3)';
            btn.style.color = 'var(--muted)';
            btn.style.borderColor = 'var(--border)';
          }, 2000);
        } catch (err) {
          console.error('Failed to copy', err);
        }
      });
    });

    // Scroll progress bar
    const progressBar = document.getElementById('progress-bar');
    window.addEventListener('scroll', () => {
      const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
      const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
      const scrolled = (winScroll / height) * 100;
      progressBar.style.width = scrolled + '%';
      progressBar.style.position = 'fixed';
      progressBar.style.top = '0';
      progressBar.style.left = '0';
      progressBar.style.height = '4px';
      progressBar.style.background = 'linear-gradient(90deg, var(--blue), var(--purple), var(--teal))';
      progressBar.style.zIndex = '1000';
    });

    // Intersection Observer for highlighting active section in navigation
    const sections = document.querySelectorAll('.section');
    const navLinks = document.querySelectorAll('#main-nav a');
    const tocLinks = document.querySelectorAll('.toc-item');

    const observerOptions = {
      root: null,
      rootMargin: '0px',
      threshold: 0.2
    };

    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          // Highlight side nav (if any) or top nav
          navLinks.forEach(link => {
            link.style.color = 'var(--muted)';
            if (link.getAttribute('href') === '#' + entry.target.id) {
              link.style.color = 'var(--purple)';
              link.style.fontWeight = 'bold';
            } else {
              link.style.fontWeight = 'normal';
            }
          });
          // Highlight TOC items
          tocLinks.forEach(link => {
            if (link.getAttribute('href') === '#' + entry.target.id) {
              link.style.borderLeftColor = 'var(--purple)';
              link.style.background = 'rgba(167, 139, 250, 0.05)';
            } else {
              link.style.borderLeftColor = 'transparent';
              link.style.background = 'transparent';
            }
          });
        }
      });
    }, observerOptions);

    sections.forEach(section => {
      observer.observe(section);
    });

    // Back to top button visibility
    const backTopBtn = document.getElementById('back-top');
    window.addEventListener('scroll', () => {
      if (document.body.scrollTop > 500 || document.documentElement.scrollTop > 500) {
        backTopBtn.style.display = 'block';
      } else {
        backTopBtn.style.display = 'none';
      }
    });

    // Initialize CSS for progress bar if not defined
    if (!progressBar.style.width) {
      progressBar.style.width = '0%';
    }
  </script>
</body>
</html>
"""

with open('flutter_notes.html', 'a') as f:
    f.write(s11)
print('S11 done. Complete.')
