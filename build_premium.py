import os
import re
import subprocess

def build():
    print("Starting Premium Build...")
    # 1. Reset flutter_notes.html to base_head.html
    with open('base_head.html', 'r') as f:
        head_content = f.read()
    with open('flutter_notes.html', 'w') as f:
        f.write(head_content)
    
    # 2. Run all builders 1 to 11
    for i in range(1, 12):
        print(f'Running build_s{i}.py...')
        subprocess.run(['python3', f'build_s{i}.py'], check=True)
        
    # 3. Post-process to inject premium mac-headers into old code-wraps
    with open('flutter_notes.html', 'r') as f:
        html = f.read()
        
    def replacer(match):
        label = match.group(1)
        return f'''<div class="mac-header">
        <div class="mac-dots"><div class="mac-dot-r"></div><div class="mac-dot-y"></div><div class="mac-dot-g"></div></div>
        <span class="code-label-mac">{label}</span>
        <button class="copy-btn">Copy</button>
      </div>'''
      
    # Regex to match the old basic header snippet
    pattern = r'<span class="code-label">\s*(.*?)\s*</span>\s*<button class="copy-btn">Copy</button>'
    new_html = re.sub(pattern, replacer, html)
    
    with open('flutter_notes.html', 'w') as f:
        f.write(new_html)
        
    print("Premium Build Complete! ✨")

if __name__ == '__main__':
    build()
