# Build Complete 72-Slide Premium Animated HTML Presentation Deck
# Threat Intelligence and Incident Response — Live Keynote Application
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PRESENTATION_DIR = BASE_DIR
INDEX_HTML_PATH = os.path.join(PRESENTATION_DIR, "index.html")

def generate_deck():
    print("Compiling Complete 72-Slide Interactive HTML Presentation...")
    
    html = []
    html.append('''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>Threat Intelligence and Incident Response — Live Master Keynote</title>
  
  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;500;700&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@500;700&display=swap" rel="stylesheet">
  
  <!-- Presentation Stylesheets -->
  <link rel="stylesheet" href="css/reset.css">
  <link rel="stylesheet" href="css/reveal.css">
  <link rel="stylesheet" href="css/theme-cyber-soc.css">
  <link rel="stylesheet" href="css/animations.css">
</head>
<body>

  <!-- Top Real-Time Telemetry Bar -->
  <div class="telemetry-status-bar">
    <div class="status-left">
      <div class="status-pill">
        <span class="live-indicator"></span>
        <span style="color: var(--cyber-cyan); font-weight: 700;">LH3 SOC</span>
      </div>
      <div class="status-pill">
        <span>VENUE:</span> <strong style="color: #F8FAFC;">LH3 – 4TH FLOOR</strong>
      </div>
      <div class="status-pill">
        <span>DATES:</span> <strong style="color: #F8FAFC;">26–31 OCT 2026</strong>
      </div>
    </div>
    
    <div class="status-center">
      <div class="status-pill">
        <span>ACTIVE DAY:</span> <strong id="status-day" style="color: var(--cyber-cyan);">DAY 01</strong>
      </div>
      <div class="status-pill">
        <span>FOCUS:</span> <strong id="status-module" style="color: #F8FAFC;">CTI FUNDAMENTALS</strong>
      </div>
    </div>
    
    <div class="status-right">
      <div class="status-pill">
        <span>INSTRUCTOR:</span> <strong style="color: #F8FAFC;">GOPINATH A</strong>
      </div>
      <button onclick="toggleShortcutModal()" style="background: none; border: 1px solid rgba(255,255,255,0.2); color: var(--text-muted); padding: 2px 8px; border-radius: 4px; font-family: var(--font-mono); font-size: 10px; cursor: pointer;">KEYS [?]</button>
      <button onclick="toggleFullScreen()" style="background: none; border: 1px solid rgba(255,255,255,0.2); color: var(--text-muted); padding: 2px 8px; border-radius: 4px; font-family: var(--font-mono); font-size: 10px; cursor: pointer;">FULL [F]</button>
    </div>
  </div>

  <!-- Bottom Custom Slide Counter -->
  <div id="custom-slide-counter" class="custom-slide-counter">SLIDE <span>01</span> / 72</div>

  <!-- Keyboard Shortcuts Modal -->
  <div id="shortcut-modal" style="position: fixed; top: 0; left: 0; right: 0; bottom: 0; background: rgba(5,8,20,0.85); backdrop-filter: blur(8px); z-index: 2000; display: none; align-items: center; justify-content: center;" onclick="if(event.target===this) toggleShortcutModal()">
    <div style="background: #0F172A; border: 1px solid var(--cyber-cyan); border-radius: 12px; padding: 28px 36px; max-width: 500px; width: 90%; box-shadow: 0 0 40px rgba(0,242,254,0.3); text-align: left;">
      <h3 style="margin-top: 0; color: #FFF; font-family: var(--font-heading);">⌨️ Classroom Navigation Shortcuts</h3>
      <table style="width: 100%; font-family: var(--font-mono); font-size: 12px; color: var(--text-secondary); border-collapse: collapse;">
        <tr><td style="padding: 6px 0; color: var(--cyber-cyan);">Space / Right Arrow</td><td>Next Slide / Fragment</td></tr>
        <tr><td style="padding: 6px 0; color: var(--cyber-cyan);">Left Arrow</td><td>Previous Slide</td></tr>
        <tr><td style="padding: 6px 0; color: var(--cyber-cyan);">F</td><td>Toggle Full-Screen Mode</td></tr>
        <tr><td style="padding: 6px 0; color: var(--cyber-cyan);">1 – 6</td><td>Jump Directly to Day 1 through Day 6</td></tr>
        <tr><td style="padding: 6px 0; color: var(--cyber-cyan);">Esc / ?</td><td>Close Modal / Help</td></tr>
      </table>
      <button onclick="toggleShortcutModal()" style="margin-top: 20px; width: 100%; padding: 8px; background: var(--gradient-cyber); border: none; border-radius: 6px; font-weight: 700; color: #050814; cursor: pointer;">CLOSE SHORTCUTS</button>
    </div>
  </div>

  <!-- ===================================================================
       REVEAL.JS PRESENTATION SLIDES CONTAINER
       =================================================================== -->
  <div class="reveal">
    <div class="slides">
''')

    # Now let's append all slides sequentially
    from presentation_slides_data import SLIDES_DATA
    
    for s_idx, s in enumerate(SLIDES_DATA, 1):
        day_attr = f' data-day="{s.get("day", "ORIENTATION")}"'
        mod_attr = f' data-module="{s.get("module", "OVERVIEW")}"'
        sess_attr = f' data-session="{s.get("session", "LH3 – 4TH FLOOR")}"'
        ref_attr = f' data-ref="{s.get("ref", "Complete Trainer Handbook")}"'
        start_attr = f' data-day-start="{s.get("day_start")}"' if s.get("day_start") else ''
        
        html.append(f'      <!-- SLIDE {s_idx:02d}: {s["title"]} -->')
        html.append(f'      <section{day_attr}{mod_attr}{sess_attr}{ref_attr}{start_attr}>')
        html.append(s['content'])
        
        # Speaker notes
        html.append('        <aside class="notes">')
        html.append(f'          [SAY:] {s.get("notes_say", "")}')
        html.append(f'          [PEDAGOGY:] {s.get("notes_pedagogy", "")}')
        html.append('        </aside>')
        html.append('      </section>\n')
        
    html.append('''    </div>
  </div>

  <!-- Presentation Script Engines -->
  <script src="js/reveal.js"></script>
  <script src="js/presentation-app.js"></script>
</body>
</html>''')

    with open(INDEX_HTML_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(html))
    print(f"Generated Index HTML: {INDEX_HTML_PATH} ({len(html):,} lines)")

if __name__ == "__main__":
    generate_deck()
