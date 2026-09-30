import re

with open('dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Global Theme
html = html.replace('bg-[#0f172a] text-slate-300', 'bg-[#f3f4f6] text-[#0d1216] font-sans')
html = html.replace('bg-slate-900', 'bg-white')
html = html.replace('bg-slate-800', 'bg-gray-100')
html = html.replace('text-slate-400', 'text-gray-500')
html = html.replace('border-slate-800', 'border-gray-200')
html = html.replace('border-slate-700', 'border-gray-200')
html = html.replace('text-slate-300', 'text-gray-800')
html = html.replace('text-white', 'text-gray-900')

# 2. Main Layout changes
css_overrides = """
        /* CANVA UI OVERRIDES */
        body, #app { background: #f3f4f6 !important; color: #0d1216 !important; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif !important; }
        .dashboard-sidebar { width: 72px !important; background: #ffffff !important; border-right: 1px solid #e5e7eb !important; align-items: center; padding-top: 1rem; }
        .dashboard-sidebar button { flex-direction: column !important; justify-content: center !important; height: 72px; padding: 0 !important; font-size: 10px !important; color: #4b5563 !important; border: none !important; }
        .dashboard-sidebar button i { font-size: 20px !important; margin-bottom: 4px; margin-right: 0 !important; }
        .dashboard-sidebar button.active-tab { background: #f3f4f6 !important; color: #8b5cf6 !important; border-radius: 8px; margin: 0 4px; width: 64px; }
        .dashboard-sidebar .cat-header { display: none !important; }
        
        .main-layout { flex-direction: row !important; }
        .content-area { padding: 0 !important; }
        .glass-panel { background: transparent !important; border: none !important; box-shadow: none !important; margin: 0 !important; padding: 0 !important; height: 100vh; display: flex; flex-direction: column; }
        
        .controls-panel { flex-direction: column !important; gap: 0 !important; height: calc(100vh - 64px); }
        
        /* The Left Panel (Properties) -> becomes Top Toolbar */
        .controls-panel > div.order-2 { 
            order: 1 !important; 
            height: 60px !important; 
            min-height: 60px;
            background: #ffffff !important; 
            border-bottom: 1px solid #e5e7eb !important; 
            display: flex !important; 
            flex-direction: row !important; 
            overflow-x: auto !important; 
            overflow-y: hidden !important;
            padding: 0 16px !important;
            align-items: center !important;
            gap: 16px !important;
        }
        
        /* Hide component list in toolbar */
        .controls-panel > div.order-2 > .mb-6 { display: none !important; } 
        /* Hide all inactive cards */
        .comp-card:not(.ring-2) { display: none !important; }
        /* Style the active card as a toolbar row */
        .comp-card { background: transparent !important; border: none !important; padding: 0 !important; display: flex !important; flex-direction: row !important; align-items: center !important; gap: 12px !important; margin: 0 !important; box-shadow: none !important; width: max-content; }
        .comp-card .grid { display: flex !important; flex-direction: row !important; align-items: center !important; gap: 12px !important; }
        .comp-card label { display: none !important; } /* hide labels to save space */
        .comp-card select, .comp-card input { height: 32px !important; background: #f3f4f6 !important; border: 1px solid #e5e7eb !important; color: #111 !important; border-radius: 6px !important; padding: 0 8px !important; }
        .comp-card button { height: 32px !important; display: flex; align-items: center; }
        
        /* The Preview Panel */
        .controls-panel > div.order-1 { 
            order: 2 !important; 
            flex: 1 !important; 
            background: #f3f4f6 !important; 
            padding: 32px !important; 
            align-items: center; 
            justify-content: center;
            border: none !important;
            box-shadow: none !important;
        }
        .controls-panel > div.order-1 > .flex.justify-between { position: absolute; top: 16px; right: 16px; width: auto; z-index: 50; }
        
        /* Timeline */
        .timeline-container {
            position: fixed;
            bottom: 0;
            left: 72px;
            right: 0;
            height: 250px;
            background: #ffffff !important;
            border-top: 1px solid #e5e7eb !important;
            z-index: 100;
            padding: 0 !important;
            border-radius: 0 !important;
        }
        /* Hide timeline label */
        .timeline-container > .text-xs { padding: 8px 16px !important; border-bottom: 1px solid #e5e7eb; }
"""

html = html.replace('</style>', css_overrides + '\n    </style>')

# Wrap timeline in a specific class to style it fixed at bottom
html = html.replace('<!-- CapCut Style Timeline -->', '<!-- CapCut Style Timeline -->\n<div class="timeline-container">')
html = html.replace('<!-- Assets Library -->', '</div>\n<!-- Assets Library -->')

with open('dashboard.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Generated dashboard.html')
