# -*- coding: utf-8 -*-
"""
Inject Broadcast Animations for Products and Prices across all 3 models:
- Modèle 1 : Luxe Emirates (menu_model1_emirates.html)
- Modèle 2 : Modern Urban (menu_model2_urban.html)
- Modèle 3 : Vibrant Tanger (menu_model3_vibrant.html)

Features:
1. Physical floating & breathing motion on sandwiches and fries using independent modern CSS 'translate' property.
2. Delicious dynamic lighting and glow on cutouts.
3. Light Sheen Sweep (brillance lumineuse) over all price badges with staggered timing.
4. Subtle pulse / heartbeat on price numbers.
5. Fully compatible with Tactile Studio Engine (no drag conflict).
"""

ANIMATION_CSS = """
    <!-- BROADCAST ANIMATIONS ENGINE FOR PRODUCTS & PRICES (2026 EDITION) -->
    <style id="broadcast-animations-style">
        /* 1. PRODUITS : SANDWICHES & FRITES FLOATING + GLOW */
        .food-sandwich {
            animation: anim-sandwich-live 4.5s ease-in-out infinite alternate !important;
            will-change: translate, filter !important;
        }

        .food-fries, .food-fries-side, .food-fries-corner {
            animation: anim-fries-live 3.8s ease-in-out infinite alternate !important;
            will-change: translate, filter !important;
        }

        /* Staggered Floating Delays across cards so motion is organic */
        .pop-card:nth-child(1) .food-sandwich, .urban-card:nth-child(1) .food-sandwich, .stall-cell:nth-child(1) .food-sandwich { animation-delay: 0s !important; }
        .pop-card:nth-child(2) .food-sandwich, .urban-card:nth-child(2) .food-sandwich, .stall-cell:nth-child(2) .food-sandwich { animation-delay: 0.8s !important; }
        .pop-card:nth-child(3) .food-sandwich, .urban-card:nth-child(3) .food-sandwich, .stall-cell:nth-child(3) .food-sandwich { animation-delay: 1.6s !important; }
        .pop-card:nth-child(4) .food-sandwich, .urban-card:nth-child(4) .food-sandwich, .stall-cell:nth-child(4) .food-sandwich { animation-delay: 0.4s !important; }
        .pop-card:nth-child(5) .food-sandwich, .urban-card:nth-child(5) .food-sandwich, .stall-cell:nth-child(5) .food-sandwich { animation-delay: 1.2s !important; }
        .pop-card:nth-child(6) .food-sandwich, .urban-card:nth-child(6) .food-sandwich, .stall-cell:nth-child(6) .food-sandwich { animation-delay: 2.0s !important; }

        .pop-card:nth-child(1) .food-fries-corner, .urban-card:nth-child(1) .food-fries-side, .stall-cell:nth-child(1) .food-fries { animation-delay: 0.5s !important; }
        .pop-card:nth-child(2) .food-fries-corner, .urban-card:nth-child(2) .food-fries-side, .stall-cell:nth-child(2) .food-fries { animation-delay: 1.3s !important; }
        .pop-card:nth-child(3) .food-fries-corner, .urban-card:nth-child(3) .food-fries-side, .stall-cell:nth-child(3) .food-fries { animation-delay: 2.1s !important; }
        .pop-card:nth-child(4) .food-fries-corner, .urban-card:nth-child(4) .food-fries-side, .stall-cell:nth-child(4) .food-fries { animation-delay: 0.9s !important; }
        .pop-card:nth-child(5) .food-fries-corner, .urban-card:nth-child(5) .food-fries-side, .stall-cell:nth-child(5) .food-fries { animation-delay: 1.7s !important; }
        .pop-card:nth-child(6) .food-fries-corner, .urban-card:nth-child(6) .food-fries-side, .stall-cell:nth-child(6) .food-fries { animation-delay: 2.5s !important; }

        @keyframes anim-sandwich-live {
            0% {
                translate: 0px 0px;
                filter: drop-shadow(0 14px 22px rgba(0,0,0,0.45)) brightness(1);
            }
            50% {
                filter: drop-shadow(0 20px 30px rgba(255, 107, 0, 0.35)) brightness(1.05);
            }
            100% {
                translate: 0px -10px;
                filter: drop-shadow(0 24px 34px rgba(0,0,0,0.55)) brightness(1.03);
            }
        }

        @keyframes anim-fries-live {
            0% {
                translate: 0px 0px;
                filter: drop-shadow(0 10px 18px rgba(0,0,0,0.5)) brightness(1);
            }
            100% {
                translate: 0px -8px;
                filter: drop-shadow(0 16px 26px rgba(255, 199, 44, 0.45)) brightness(1.08);
            }
        }

        /* 2. PRIX : LIGHT SHEEN SWEEP + GLOW PULSE */
        .price-chip-alone, .price-chip-menu, 
        .price-badge-alone, .price-badge-menu, 
        .price-chalkboard, .price-col, .urban-price-box {
            position: relative !important;
            overflow: hidden !important;
            animation: price-subtle-glow 3.5s ease-in-out infinite alternate !important;
        }

        /* Diagonal Beam of Light (Sheen) */
        .price-chip-alone::after, .price-chip-menu::after, 
        .price-badge-alone::after, .price-badge-menu::after, 
        .price-chalkboard::after, .urban-price-box::after {
            content: '' !important;
            position: absolute !important;
            top: -50% !important;
            left: -120% !important;
            width: 50% !important;
            height: 200% !important;
            background: linear-gradient(
                90deg, 
                transparent 0%, 
                rgba(255, 255, 255, 0) 25%, 
                rgba(255, 255, 255, 0.65) 50%, 
                rgba(255, 255, 255, 0) 75%, 
                transparent 100%
            ) !important;
            transform: rotate(25deg) !important;
            animation: price-sheen-sweep 4s cubic-bezier(0.4, 0, 0.2, 1) infinite !important;
            pointer-events: none !important;
            z-index: 5 !important;
        }

        /* Staggered Sheen Timing across cards */
        .pop-card:nth-child(1) .price-chip-alone::after, .urban-card:nth-child(1) .price-badge-alone::after, .stall-cell:nth-child(1) .price-chalkboard::after { animation-delay: 0s !important; }
        .pop-card:nth-child(2) .price-chip-alone::after, .urban-card:nth-child(2) .price-badge-alone::after, .stall-cell:nth-child(2) .price-chalkboard::after { animation-delay: 0.6s !important; }
        .pop-card:nth-child(3) .price-chip-alone::after, .urban-card:nth-child(3) .price-badge-alone::after, .stall-cell:nth-child(3) .price-chalkboard::after { animation-delay: 1.2s !important; }
        .pop-card:nth-child(4) .price-chip-alone::after, .urban-card:nth-child(4) .price-badge-alone::after, .stall-cell:nth-child(4) .price-chalkboard::after { animation-delay: 1.8s !important; }
        .pop-card:nth-child(5) .price-chip-alone::after, .urban-card:nth-child(5) .price-badge-alone::after, .stall-cell:nth-child(5) .price-chalkboard::after { animation-delay: 2.4s !important; }
        .pop-card:nth-child(6) .price-chip-alone::after, .urban-card:nth-child(6) .price-badge-alone::after, .stall-cell:nth-child(6) .price-chalkboard::after { animation-delay: 3.0s !important; }

        .price-chip-menu::after, .price-badge-menu::after {
            animation-delay: 0.3s !important;
        }

        @keyframes price-sheen-sweep {
            0% { left: -120%; }
            30% { left: 220%; }
            100% { left: 220%; }
        }

        @keyframes price-subtle-glow {
            0% {
                box-shadow: 0 3px 10px rgba(0, 0, 0, 0.4);
            }
            100% {
                box-shadow: 0 5px 18px rgba(255, 107, 0, 0.55), 0 0 10px rgba(255, 199, 44, 0.4);
            }
        }

        /* Attention pulse on price numbers */
        .p-number, .u-number, .price-num {
            display: inline-block !important;
            animation: number-subtle-pulse 3s ease-in-out infinite alternate !important;
        }

        @keyframes number-subtle-pulse {
            0% { transform: scale(1); }
            100% { transform: scale(1.05); color: #ffffff; text-shadow: 0 0 12px rgba(255, 199, 44, 0.7); }
        }
    </style>
"""

import os

files = [
    r'c:\Users\pc\Desktop\menu\menu_model1_emirates.html',
    r'c:\Users\pc\Desktop\menu\menu_model2_urban.html',
    r'c:\Users\pc\Desktop\menu\menu_model3_vibrant.html'
]

for file_path in files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove old broadcast-animations-style if exists
    import re
    content = re.sub(r'<!-- BROADCAST ANIMATIONS ENGINE.*?<\/style>', '', content, flags=re.DOTALL)
    
    # Inject before </head>
    if '</head>' in content:
        content = content.replace('</head>', ANIMATION_CSS + '\n</head>')
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Successfully injected broadcast animations into {os.path.basename(file_path)}!')
    else:
        print(f'Warning: </head> not found in {os.path.basename(file_path)}')

print('All 3 models updated with Broadcast Animations for Products & Prices!')

