# -*- coding: utf-8 -*-
"""
Build Behance-Grade Fast-Food Menu Board 1080p
Rich chalkboard background, chalk doodles, 3D spotlight, 
light sheen animation, steam vapor, and full tactile studio control.
"""

HTML_CONTENT = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Modèle Behance Pro : Tacos Gratiné & Fast-Food Master 1080p</title>
    <!-- Fonts Google Fast-Food Behance -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Montserrat:ital,wght@0,400;0,700;0,800;0,900;1,900&family=Permanent+Marker&family=Kalam:wght@700&display=swap" rel="stylesheet">
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        html, body {
            width: 100%;
            height: 100%;
            overflow: hidden;
            background: #08090b;
            font-family: 'Montserrat', sans-serif;
            color: #ffffff;
            user-select: none;
            -webkit-user-select: none;
        }

        #viewport-wrapper {
            position: absolute;
            top: 0; left: 0; width: 100vw; height: 100vh;
            display: flex; align-items: center; justify-content: center;
            background: #040405;
        }

        #menu-stage {
            width: 1920px;
            height: 1080px;
            position: relative;
            transform-origin: center center;
            overflow: hidden;
            box-shadow: 0 25px 80px rgba(0,0,0,0.95);
            background: #111215;
        }

        /* ========================================================
           1. ARRIÈRE-PLAN GRAPHIQUE BEHANCE (Chalkboard Slate + Doodles)
           ======================================================== */
        .bg-layer-slate {
            position: absolute;
            inset: 0;
            background: 
                radial-gradient(circle at 75% 50%, rgba(255, 107, 0, 0.22) 0%, transparent 60%),
                radial-gradient(circle at 20% 30%, rgba(245, 158, 11, 0.15) 0%, transparent 50%),
                radial-gradient(circle at 50% 90%, rgba(220, 38, 38, 0.18) 0%, transparent 60%),
                linear-gradient(145deg, #18191f 0%, #0e0f13 50%, #09090c 100%);
            z-index: 1;
        }

        /* Chalk Dust Texture Overlay */
        .bg-chalk-texture {
            position: absolute;
            inset: 0;
            background-image: radial-gradient(rgba(255, 255, 255, 0.05) 1px, transparent 1px);
            background-size: 28px 28px;
            opacity: 0.8;
            z-index: 2;
            pointer-events: none;
        }

        /* Fast-Food Chalk Doodles SVG Layer */
        .bg-doodles-svg {
            position: absolute;
            inset: 0;
            width: 100%;
            height: 100%;
            z-index: 3;
            pointer-events: none;
            opacity: 0.22;
        }

        /* Spotlight Over Hero */
        .hero-spotlight {
            position: absolute;
            right: 60px;
            top: 80px;
            width: 800px;
            height: 800px;
            background: radial-gradient(circle, rgba(255, 120, 0, 0.38) 0%, rgba(245, 158, 11, 0.18) 40%, transparent 70%);
            border-radius: 50%;
            filter: blur(50px);
            z-index: 4;
            pointer-events: none;
            animation: pulse-spotlight 5s ease-in-out infinite alternate;
        }

        @keyframes pulse-spotlight {
            0% { transform: scale(0.92); opacity: 0.7; }
            100% { transform: scale(1.08); opacity: 1; }
        }

        /* 3D Floor Shadow */
        .floor-shadow-3d {
            position: absolute;
            bottom: 110px;
            right: 120px;
            width: 660px;
            height: 90px;
            background: radial-gradient(ellipse at center, rgba(0,0,0,0.9) 0%, rgba(0,0,0,0.45) 50%, transparent 75%);
            border-radius: 50%;
            z-index: 6;
            pointer-events: none;
            transform: scaleY(0.45);
        }

        /* ========================================================
           2. HEADER FAST-FOOD BROADCAST BEHANCE
           ======================================================== */
        .header-bar {
            position: absolute;
            top: 0; left: 0; width: 100%; height: 115px;
            z-index: 20;
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0 50px;
            background: linear-gradient(180deg, rgba(10,10,12,0.98) 0%, rgba(10,10,12,0.8) 70%, transparent 100%);
            border-bottom: 2px solid rgba(255, 107, 0, 0.35);
        }

        .brand-block {
            display: flex;
            align-items: center;
            gap: 18px;
        }

        .brand-badge {
            background: linear-gradient(135deg, #ff6b00, #dc2626);
            color: #ffffff;
            font-family: 'Bebas Neue', sans-serif;
            font-size: 26px;
            padding: 6px 18px;
            border-radius: 6px;
            letter-spacing: 2px;
            box-shadow: 0 6px 20px rgba(255, 107, 0, 0.5);
            text-shadow: 0 2px 4px rgba(0,0,0,0.5);
        }

        .brand-title {
            font-family: 'Bebas Neue', sans-serif;
            font-size: 50px;
            letter-spacing: 3px;
            color: #ffffff;
            text-shadow: 0 4px 15px rgba(0,0,0,0.8);
        }

        .brand-title span {
            color: #ff6b00;
        }

        .header-promo-banner {
            display: flex;
            align-items: center;
            gap: 16px;
            background: rgba(255, 255, 255, 0.06);
            border: 2px dashed rgba(255, 199, 44, 0.6);
            padding: 10px 26px;
            border-radius: 40px;
        }

        .promo-tag {
            font-family: 'Permanent Marker', cursive;
            color: #ffc72c;
            font-size: 22px;
            transform: rotate(-3deg);
        }

        .promo-desc {
            font-size: 15px;
            font-weight: 800;
            color: #f1f5f9;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        /* ========================================================
           3. MAIN LAYOUT (Split: Fast-Food Matrix vs 3D Hero)
           ======================================================== */
        .stage-content {
            position: absolute;
            top: 115px;
            left: 0;
            width: 1920px;
            height: 965px;
            z-index: 10;
            padding: 30px 50px 30px 50px;
            display: flex;
            gap: 40px;
        }

        /* LEFT COLUMN (60%): Step-by-Step Chalkboard Matrix */
        .left-matrix {
            flex: 1.35;
            display: flex;
            flex-direction: column;
            gap: 20px;
        }

        /* Section Box (Chalkboard Card) */
        .chalk-card {
            background: rgba(20, 22, 28, 0.85);
            border: 2px solid rgba(255, 255, 255, 0.12);
            border-radius: 16px;
            padding: 18px 24px;
            position: relative;
            backdrop-filter: blur(10px);
            box-shadow: 0 10px 35px rgba(0,0,0,0.6), inset 0 1px 0 rgba(255,255,255,0.1);
        }

        .chalk-card-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 14px;
        }

        .step-pill {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: #ff6b00;
            color: #ffffff;
            font-family: 'Bebas Neue', sans-serif;
            font-size: 24px;
            letter-spacing: 1.5px;
            padding: 4px 16px;
            border-radius: 8px;
            box-shadow: 0 4px 15px rgba(255, 107, 0, 0.45);
        }

        .step-subtext {
            font-family: 'Kalam', cursive;
            color: #ffc72c;
            font-size: 18px;
        }

        /* Tailles Matrix (M, L, XL, XXL) */
        .sizes-row {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 16px;
        }

        .size-box {
            background: rgba(30, 33, 42, 0.9);
            border: 1px solid rgba(255, 255, 255, 0.15);
            border-radius: 12px;
            padding: 12px 14px;
            text-align: center;
            position: relative;
            overflow: hidden;
            transition: transform 0.2s ease, border-color 0.2s ease;
        }

        .size-box:hover {
            transform: translateY(-4px);
            border-color: #ff6b00;
        }

        .size-letter {
            font-family: 'Bebas Neue', sans-serif;
            font-size: 44px;
            line-height: 1;
            color: #ffffff;
            margin-bottom: 2px;
        }

        .size-detail {
            font-size: 12px;
            font-weight: 800;
            color: #94a3b8;
            text-transform: uppercase;
            margin-bottom: 8px;
        }

        .size-price-tag {
            background: linear-gradient(135deg, #ff6b00, #e11d48);
            border-radius: 8px;
            padding: 6px 10px;
            font-family: 'Bebas Neue', sans-serif;
            font-size: 26px;
            color: #ffffff;
            letter-spacing: 1px;
            position: relative;
            overflow: hidden;
            box-shadow: 0 4px 12px rgba(255, 107, 0, 0.35);
        }

        /* Viandes & Sauces Grid */
        .chips-grid {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
        }

        .item-chip {
            background: rgba(255, 255, 255, 0.07);
            border: 1px solid rgba(255, 255, 255, 0.16);
            border-radius: 30px;
            padding: 8px 18px;
            font-size: 14px;
            font-weight: 800;
            color: #f1f5f9;
            display: flex;
            align-items: center;
            gap: 8px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        .item-chip span.icon {
            font-size: 17px;
        }

        .item-chip.highlight {
            background: rgba(255, 107, 0, 0.18);
            border-color: #ff6b00;
            color: #ff9d42;
        }

        /* Gratinage 4 Cards (Bottom Row) */
        .gratin-row {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 14px;
        }

        .gratin-card {
            background: rgba(30, 33, 40, 0.95);
            border: 1px solid rgba(255, 199, 44, 0.35);
            border-radius: 12px;
            padding: 12px 10px;
            text-align: center;
            position: relative;
            overflow: hidden;
            transition: transform 0.2s ease;
        }

        .gratin-card:hover {
            transform: translateY(-3px);
            border-color: #ffc72c;
        }

        .gratin-badge {
            background: #ffc72c;
            color: #111;
            font-family: 'Bebas Neue', sans-serif;
            font-size: 15px;
            padding: 2px 10px;
            border-radius: 4px;
            display: inline-block;
            margin-bottom: 6px;
            letter-spacing: 1px;
            font-weight: 900;
        }

        .gratin-name {
            font-family: 'Bebas Neue', sans-serif;
            font-size: 22px;
            color: #ffffff;
            margin-bottom: 4px;
            letter-spacing: 1px;
        }

        .gratin-price {
            font-family: 'Bebas Neue', sans-serif;
            font-size: 22px;
            color: #ff6b00;
        }

        /* RIGHT COLUMN (40%): Broadcast 3D Hero Staging */
        .right-hero-stage {
            flex: 0.98;
            position: relative;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }

        .hero-banner-title {
            position: absolute;
            top: 15px;
            text-align: center;
            z-index: 15;
            width: 100%;
        }

        .hero-banner-title h2 {
            font-family: 'Bebas Neue', sans-serif;
            font-size: 66px;
            letter-spacing: 4px;
            line-height: 0.95;
            color: #ffffff;
            text-shadow: 0 6px 25px rgba(0,0,0,0.95), 0 0 35px rgba(255,107,0,0.5);
        }

        .hero-banner-title h2 span {
            color: #ff6b00;
            display: block;
            font-size: 40px;
            font-family: 'Permanent Marker', cursive;
            transform: rotate(-2deg);
            margin-top: 5px;
            text-shadow: 0 4px 15px rgba(0,0,0,0.8);
        }

        /* The Hero Food Container */
        .hero-food-container {
            position: relative;
            width: 100%;
            height: 540px;
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 10;
        }

        .hero-sandwich-img {
            max-width: 96%;
            max-height: 500px;
            object-fit: contain;
            filter: drop-shadow(0 25px 35px rgba(0, 0, 0, 0.9)) drop-shadow(0 0 30px rgba(255, 107, 0, 0.3));
            animation: hero-breathing 5s ease-in-out infinite alternate;
        }

        @keyframes hero-breathing {
            0% { transform: translateY(0px) scale(1); }
            100% { transform: translateY(-14px) scale(1.025); }
        }

        /* Side Fry Cone */
        .hero-fry-cone {
            position: absolute;
            bottom: 30px;
            right: 15px;
            width: 230px;
            height: auto;
            z-index: 12;
            filter: drop-shadow(0 15px 30px rgba(0,0,0,0.9));
            animation: hero-fries-float 4.5s ease-in-out infinite alternate;
        }

        @keyframes hero-fries-float {
            0% { transform: translateY(0px) rotate(-3deg); }
            100% { transform: translateY(-9px) rotate(2deg); }
        }

        /* Giant Circular Price Stamp Badge */
        .hero-stamp-badge {
            position: absolute;
            top: 120px;
            right: 25px;
            width: 165px;
            height: 165px;
            background: radial-gradient(circle, #ff6b00 0%, #dc2626 100%);
            border: 4px dashed #ffffff;
            border-radius: 50%;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            box-shadow: 0 15px 40px rgba(220, 38, 38, 0.65);
            transform: rotate(12deg);
            z-index: 20;
            animation: stamp-pulse 3s ease-in-out infinite alternate;
        }

        @keyframes stamp-pulse {
            0% { transform: rotate(12deg) scale(0.96); }
            100% { transform: rotate(12deg) scale(1.04); }
        }

        .stamp-top {
            font-size: 13px;
            font-weight: 900;
            text-transform: uppercase;
            letter-spacing: 1px;
            color: #ffedd5;
        }

        .stamp-price {
            font-family: 'Bebas Neue', sans-serif;
            font-size: 64px;
            line-height: 0.9;
            color: #ffffff;
            text-shadow: 0 2px 10px rgba(0,0,0,0.5);
        }

        .stamp-sub {
            font-size: 11px;
            font-weight: 800;
            text-transform: uppercase;
            color: #ffedd5;
        }

        /* ========================================================
           4. BROADCAST ANIMATIONS (Light Sheen / Reflet)
           ======================================================== */
        .sheen-effect {
            position: relative;
            overflow: hidden;
        }

        .sheen-effect::after {
            content: '';
            position: absolute;
            top: -50%;
            left: -120%;
            width: 60%;
            height: 200%;
            background: linear-gradient(
                90deg, 
                transparent 0%, 
                rgba(255, 255, 255, 0) 30%, 
                rgba(255, 255, 255, 0.55) 50%, 
                rgba(255, 255, 255, 0) 70%, 
                transparent 100%
            );
            transform: rotate(25deg);
            animation: broadcast-sheen 4s cubic-bezier(0.4, 0, 0.2, 1) infinite;
        }

        @keyframes broadcast-sheen {
            0% { left: -120%; }
            35% { left: 220%; }
            100% { left: 220%; }
        }

        /* Subtle Steam Simulation */
        .steam-bubble {
            position: absolute;
            width: 16px;
            height: 16px;
            background: rgba(255, 255, 255, 0.35);
            border-radius: 50%;
            filter: blur(8px);
            pointer-events: none;
            z-index: 18;
            animation: rise-steam 3.5s infinite ease-out;
        }

        @keyframes rise-steam {
            0% { transform: translateY(0) scale(1); opacity: 0.6; }
            50% { transform: translateY(-70px) translateX(15px) scale(2.6); opacity: 0.3; }
            100% { transform: translateY(-130px) translateX(-10px) scale(4); opacity: 0; }
        }

        /* Bottom Floating TV Controls Bar */
        #tv-control-bar {
            position: fixed;
            bottom: 20px;
            left: 50%;
            transform: translateX(-50%);
            display: flex;
            align-items: center;
            gap: 12px;
            background: rgba(15, 17, 23, 0.94);
            padding: 8px 18px;
            border-radius: 35px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.85);
            border: 1px solid rgba(255, 255, 255, 0.18);
            z-index: 999999;
            backdrop-filter: blur(14px);
        }

        .btn-ctl {
            background: rgba(255, 255, 255, 0.1);
            color: #fff;
            border: 1px solid rgba(255, 255, 255, 0.2);
            padding: 8px 16px;
            border-radius: 20px;
            font-size: 13px;
            font-weight: 800;
            cursor: pointer;
            transition: all 0.2s ease;
            white-space: nowrap;
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            gap: 6px;
        }

        .btn-ctl:hover {
            background: rgba(255, 255, 255, 0.25);
            transform: translateY(-2px);
        }

        /* ========================================================
           5. TACTILE STUDIO ENGINE V3 STYLES
           ======================================================== */
        .editable-item {
            cursor: grab !important;
            user-select: none !important;
            -webkit-user-select: none !important;
            -webkit-user-drag: none !important;
            position: relative;
            transition: outline 0.15s ease, box-shadow 0.15s ease !important;
        }
        .editable-item:hover {
            outline: 2px dashed #f59e0b !important;
            outline-offset: 4px;
        }
        .editable-item.item-selected {
            outline: 3px solid #10b981 !important;
            outline-offset: 5px;
            box-shadow: 0 0 25px rgba(16, 185, 129, 0.6) !important;
        }

        #studio-floating-bar {
            position: fixed;
            display: none;
            z-index: 99999999;
            background: rgba(15, 23, 42, 0.98);
            border: 2px solid #10b981;
            border-radius: 40px;
            padding: 8px 18px;
            gap: 8px;
            align-items: center;
            box-shadow: 0 15px 40px rgba(0, 0, 0, 0.95), 0 0 25px rgba(16, 185, 129, 0.4);
            backdrop-filter: blur(16px);
            font-family: 'Montserrat', sans-serif;
            max-width: 95vw;
        }
        .studio-tag {
            font-size: 11px;
            font-weight: 800;
            color: #fcd535;
            text-transform: uppercase;
            margin-right: 6px;
            max-width: 140px;
            overflow: hidden;
            text-overflow: ellipsis;
            white-space: nowrap;
        }
        .studio-btn {
            background: rgba(255, 255, 255, 0.12);
            border: 1px solid rgba(255, 255, 255, 0.2);
            color: #ffffff;
            width: 32px;
            height: 32px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 16px;
            font-weight: 900;
            cursor: pointer;
            transition: all 0.15s ease;
        }
        .studio-btn:hover { background: #10b981; color: #fff; transform: scale(1.1); }
        .studio-val { font-size: 12px; font-weight: 800; color: #fff; min-width: 38px; text-align: center; }

        .studio-pill-btn {
            background: rgba(255, 255, 255, 0.1);
            border: 1px solid rgba(255, 255, 255, 0.2);
            color: #ffffff;
            padding: 5px 10px;
            border-radius: 20px;
            font-size: 11px;
            font-weight: 800;
            cursor: pointer;
            transition: all 0.15s ease;
            white-space: nowrap;
            display: flex;
            align-items: center;
            gap: 4px;
        }
        .studio-pill-btn:hover { background: rgba(255, 255, 255, 0.25); transform: scale(1.05); }
        .studio-pill-btn.btn-front { border-color: #10b981; color: #6ee7b7; }
        .studio-pill-btn.btn-back { border-color: #3b82f6; color: #93c5fd; }
        .studio-pill-btn.btn-dup { border-color: #f59e0b; color: #fcd34d; }
        .studio-pill-btn.btn-del { border-color: #ef4444; color: #fca5a5; }

        /* Save Toast */
        #save-toast {
            position: fixed;
            top: 30px;
            left: 50%;
            transform: translateX(-50%) translateY(-100px);
            background: #10b981;
            color: #fff;
            padding: 12px 28px;
            border-radius: 30px;
            font-weight: 900;
            font-size: 16px;
            box-shadow: 0 10px 30px rgba(16, 185, 129, 0.5);
            z-index: 999999999;
            transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            display: flex;
            align-items: center;
            gap: 10px;
        }
        #save-toast.visible {
            transform: translateX(-50%) translateY(0);
        }

        /* Modal Export Vidéo */
        .modal-overlay {
            position: fixed;
            inset: 0;
            background: rgba(0, 0, 0, 0.85);
            backdrop-filter: blur(8px);
            z-index: 999999999;
            display: none;
            align-items: center;
            justify-content: center;
        }
        .modal-box {
            background: #1e293b;
            border: 2px solid #334155;
            border-radius: 20px;
            width: 580px;
            max-width: 90vw;
            padding: 30px;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.8);
            color: #f8fafc;
        }
        .modal-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 20px;
            border-bottom: 1px solid #334155;
            padding-bottom: 12px;
        }
        .modal-title { font-size: 20px; font-weight: 900; color: #f8fafc; }
        .modal-close { cursor: pointer; font-size: 22px; color: #94a3b8; }
        .btn-modal-action {
            width: 100%;
            padding: 14px;
            border-radius: 12px;
            background: linear-gradient(135deg, #10b981, #059669);
            color: #fff;
            font-size: 16px;
            font-weight: 900;
            border: none;
            cursor: pointer;
            margin-top: 20px;
        }
    </style>
</head>
<body>

<div id="save-toast">✅ Mise en page enregistrée avec succès sur le serveur !</div>

<div id="viewport-wrapper">
    <div id="menu-stage">
        
        <!-- 1. GRAPHIC ARRIÈRE-PLAN BEHANCE -->
        <div class="bg-layer-slate"></div>
        <div class="bg-chalk-texture"></div>
        
        <!-- FAST FOOD CHALK DOODLE LAYER (SVG) -->
        <svg class="bg-doodles-svg" viewBox="0 0 1920 1080" fill="none" stroke="#ffffff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
            <!-- Chili Pepper -->
            <path d="M150 180 Q190 200 210 260 Q170 250 140 210 Z" />
            <path d="M210 260 Q225 280 230 300" stroke="#ff6b00" stroke-width="3" />
            
            <!-- Burger Outline Left -->
            <path d="M120 480 Q180 430 240 480 Z" />
            <line x1="115" y1="495" x2="245" y2="495" />
            <line x1="115" y1="510" x2="245" y2="510" />
            <path d="M120 520 Q180 540 240 520" />
            
            <!-- Pizza Slice Doodle -->
            <path d="M80 820 L160 760 L180 860 Z" />
            <circle cx="140" cy="800" r="6" />
            <circle cx="140" cy="830" r="8" />
            <circle cx="160" cy="820" r="5" />
            
            <!-- Chalk Arrows -->
            <path d="M580 260 Q630 240 680 270" />
            <path d="M1050 480 Q1120 490 1180 460" />
            
            <!-- Stars & Sparkles -->
            <path d="M320 160 L325 175 L340 180 L325 185 L320 200 L315 185 L300 180 L315 175 Z" fill="#ffffff" opacity="0.4" />
            <path d="M1120 220 L1125 235 L1140 240 L1125 245 L1120 260 L1115 245 L1100 240 L1115 235 Z" fill="#ffffff" opacity="0.4" />
            <path d="M1780 780 L1785 795 L1800 800 L1785 805 L1780 820 L1775 805 L1760 800 L1775 795 Z" fill="#ffffff" opacity="0.4" />
        </svg>

        <!-- DRAMATIC SPOTLIGHT & 3D FLOOR SHADOW -->
        <div class="hero-spotlight"></div>
        <div class="floor-shadow-3d"></div>

        <!-- 2. BROADCAST TOP HEADER -->
        <header class="header-bar">
            <div class="brand-block">
                <div class="brand-badge sheen-effect">AUTHENTIQUE FAST-FOOD</div>
                <div class="brand-title">TACOS <span>MASTER</span> &amp; BOCADILLOS</div>
            </div>
            
            <div class="header-promo-banner sheen-effect">
                <div class="promo-tag">Offre Spéciale !</div>
                <div class="promo-desc">Tous nos menus sont servis avec frites fraîches et boisson fraîche au choix</div>
            </div>
        </header>

        <!-- 3. STAGE CONTENT (Split Matrix vs 3D Hero) -->
        <main class="stage-content">
            
            <!-- LEFT FAST-FOOD COMPOSITION MATRIX -->
            <div class="left-matrix">
                
                <!-- STEP 1: TAILLES DU TACOS -->
                <div class="chalk-card">
                    <div class="chalk-card-header">
                        <div class="step-pill sheen-effect">1. CHOISISSEZ VOTRE TAILLE</div>
                        <div class="step-subtext">Galette toastée &amp; sauce fromagère maison incluse</div>
                    </div>
                    <div class="sizes-row">
                        <div class="size-box editable-item" data-item-id="size_m">
                            <div class="size-letter">M</div>
                            <div class="size-detail">1 Viande au choix</div>
                            <div class="size-price-tag sheen-effect">35 <span style="font-size:16px;">DH</span></div>
                        </div>
                        <div class="size-box editable-item" data-item-id="size_l">
                            <div class="size-letter" style="color:#ffc72c;">L</div>
                            <div class="size-detail">2 Viandes au choix</div>
                            <div class="size-price-tag sheen-effect">45 <span style="font-size:16px;">DH</span></div>
                        </div>
                        <div class="size-box editable-item" data-item-id="size_xl">
                            <div class="size-letter" style="color:#ff6b00;">XL</div>
                            <div class="size-detail">3 Viandes + 2 Galettes</div>
                            <div class="size-price-tag sheen-effect">60 <span style="font-size:16px;">DH</span></div>
                        </div>
                        <div class="size-box editable-item" data-item-id="size_xxl">
                            <div class="size-letter" style="color:#ef4444;">GIGA</div>
                            <div class="size-detail">4 Viandes Familial</div>
                            <div class="size-price-tag sheen-effect">85 <span style="font-size:16px;">DH</span></div>
                        </div>
                    </div>
                </div>

                <!-- STEP 2: VIANDES AU CHOIX -->
                <div class="chalk-card">
                    <div class="chalk-card-header">
                        <div class="step-pill" style="background:#dc2626;">2. VOS VIANDES AU CHOIX</div>
                        <div class="step-subtext">100% Viandes fraîches assaisonnées</div>
                    </div>
                    <div class="chips-grid">
                        <div class="item-chip highlight editable-item" data-item-id="meat_poulet"><span class="icon">🍗</span> Poulet Mariné Maison</div>
                        <div class="item-chip highlight editable-item" data-item-id="meat_beef"><span class="icon">🥩</span> Viande Hachée Pur Bœuf</div>
                        <div class="item-chip editable-item" data-item-id="meat_cordon"><span class="icon">🧀</span> Cordon Bleu Fumé</div>
                        <div class="item-chip editable-item" data-item-id="meat_merguez"><span class="icon">🌭</span> Merguez Épicée</div>
                        <div class="item-chip editable-item" data-item-id="meat_tenders"><span class="icon">🔥</span> Tenders Croustillants</div>
                        <div class="item-chip editable-item" data-item-id="meat_thon"><span class="icon">🐟</span> Thon 1er Choix</div>
                    </div>
                </div>

                <!-- STEP 3 & 4: SAUCES & GRATINAGE GOURMAND -->
                <div class="chalk-card">
                    <div class="chalk-card-header">
                        <div class="step-pill" style="background:#f59e0b;">3. GRATINAGE AU FOUR (SPÉCIALITÉ)</div>
                        <div class="step-subtext">Cuit et doré au four traditionnel</div>
                    </div>
                    <div class="gratin-row">
                        <div class="gratin-card editable-item" data-item-id="gratin_cheddar">
                            <div class="gratin-badge">TOP VENTE</div>
                            <div class="gratin-name">CHEDDAR FONDU</div>
                            <div class="gratin-price">+ 7 DH</div>
                        </div>
                        <div class="gratin-card editable-item" data-item-id="gratin_raclette">
                            <div class="gratin-badge">GOURMAND</div>
                            <div class="gratin-name">RACLETTE ALPIN</div>
                            <div class="gratin-price">+ 8 DH</div>
                        </div>
                        <div class="gratin-card editable-item" data-item-id="gratin_chevre">
                            <div class="gratin-badge">SAVEUR</div>
                            <div class="gratin-name">CHÈVRE &amp; MIEL</div>
                            <div class="gratin-price">+ 8 DH</div>
                        </div>
                        <div class="gratin-card editable-item" data-item-id="gratin_mozza">
                            <div class="gratin-badge">ITALIAN</div>
                            <div class="gratin-name">4 FROMAGES</div>
                            <div class="gratin-price">+ 9 DH</div>
                        </div>
                    </div>
                </div>

            </div>

            <!-- RIGHT 3D HERO BROADCAST STAGING -->
            <div class="right-hero-stage">
                
                <div class="hero-banner-title">
                    <h2>LE ROYAL GRATINÉ <span>CHEF SIGNATURE 2026</span></h2>
                </div>

                <!-- GIANT STAMP PRICE BADGE -->
                <div class="hero-stamp-badge sheen-effect editable-item" data-item-id="hero_stamp">
                    <div class="stamp-top">MENU COMPLET</div>
                    <div class="stamp-price">48<span style="font-size:24px;">DH</span></div>
                    <div class="stamp-sub">FRITES + BOISSON</div>
                </div>

                <!-- THE 3D HERO PRODUCT -->
                <div class="hero-food-container">
                    <!-- Steam vapor simulation -->
                    <div class="steam-bubble" style="bottom: 180px; left: 45%;"></div>
                    <div class="steam-bubble" style="bottom: 160px; left: 52%; animation-delay: 1.2s;"></div>
                    <div class="steam-bubble" style="bottom: 170px; left: 38%; animation-delay: 2.1s;"></div>

                    <!-- Hero Sandwich -->
                    <img src="/cutouts_cropped/bocadillo tortillia royale 30 dh.png" 
                         class="hero-sandwich-img editable-item" 
                         id="hero_sandwich" 
                         data-item-id="hero_sandwich" 
                         alt="Hero Tacos Gratiné">
                         
                    <!-- Side French Fries Cone -->
                    <img src="/cutouts_cropped/frites_cone_kraft_2026.png" 
                         class="hero-fry-cone editable-item" 
                         id="hero_side_fries" 
                         data-item-id="hero_side_fries" 
                         alt="Cornet Frites Kraft">
                </div>

            </div>

        </main>

    </div>
</div>

<!-- STUDIO FLOATING TOOLBAR -->
<div id="studio-floating-bar">
    <span class="studio-tag" id="bar-item-name">✨ Élément</span>
    <button class="studio-btn" id="sbar-minus" title="Réduire">−</button>
    <span class="studio-val" id="sbar-size-text">100%</span>
    <button class="studio-btn" id="sbar-plus" title="Agrandir">+</button>
    
    <button class="studio-pill-btn btn-front" id="sbar-front" title="Mettre au premier plan">🔝 Devant</button>
    <button class="studio-pill-btn btn-back" id="sbar-back" title="Mettre à l'arrière-plan">🥪 Derrière</button>
    <button class="studio-pill-btn btn-dup" id="sbar-duplicate" title="Dupliquer">📑 Dupliquer</button>
    <button class="studio-pill-btn btn-del" id="sbar-delete" title="Supprimer">🗑️</button>
    <span style="color:#94a3b8; cursor:pointer; font-size:20px; margin-left:6px;" id="sbar-close">✕</span>
</div>

<!-- FLOATING TV CONTROLS -->
<div id="tv-control-bar">
    <button class="btn-ctl" onclick="saveLayoutToServer()" style="background:#10b981; border-color:#059669; font-weight:900;">💾 Sauvegarder la Mise en Page</button>
    <button class="btn-ctl" onclick="resetAllLayout()">↺ Réinitialiser</button>
    <button id="btn-video-export" class="btn-ctl" onclick="openVideoModal()" style="background: linear-gradient(135deg, #8b5cf6, #6d28d9); font-weight:900;">🎬 Exporter Vidéo MP4</button>
    <a href="/menu_showcase.html" class="btn-ctl" style="background:#ef4444; text-decoration:none;">📺 Tous les Modèles</a>
</div>

<!-- MODAL EXPORT VIDEO -->
<div class="modal-overlay" id="modal-video-export">
    <div class="modal-box">
        <div class="modal-header">
            <div class="modal-title">🎬 Exporter en Vidéo MP4 (Clé USB)</div>
            <div class="modal-close" onclick="closeVideoModal()">✕</div>
        </div>
        <p style="color:#94a3b8; font-size:14px; line-height:1.5;">Générez une vidéo <strong>Full HD 1080p à 60fps</strong> prête à être branchée sur n'importe quelle télévision par clé USB.</p>
        <button class="btn-modal-action" id="btn-start-render" onclick="startVideoRender()">Lancer le Rendu MP4 60fps</button>
        <div id="render-status" style="margin-top:15px; font-weight:800; font-size:14px; color:#f59e0b; display:none;"></div>
    </div>
</div>

<script>
    // AUTO SCALE TO 1080P
    function autoScale() {
        const stage = document.getElementById('menu-stage');
        const vw = window.innerWidth;
        const vh = window.innerHeight;
        const scale = Math.min(vw / 1920, vh / 1080);
        stage.style.transform = `scale(${scale})`;
    }
    window.addEventListener('resize', autoScale);
    autoScale();

    // TACTILE STUDIO ENGINE V3
    (function() {
        const modelName = 'menu_model4_behance';
        const STORAGE_KEY = 'universal_layout_' + modelName;
        let layoutState = {};
        let activeEl = null;

        const bar = document.getElementById('studio-floating-bar');
        const itemName = document.getElementById('bar-item-name');
        const sizeText = document.getElementById('sbar-size-text');
        const toast = document.getElementById('save-toast');

        function getStageScale() {
            const stage = document.getElementById('menu-stage');
            if (!stage) return 1;
            return stage.getBoundingClientRect().width / 1920;
        }

        function getElementId(el) {
            return el.getAttribute('data-item-id') || el.id || ('item_' + Math.random().toString(36).substr(2, 9));
        }

        function applyStateToElement(el, data) {
            if (!data) return;
            const x = data.x || 0;
            const y = data.y || 0;
            const s = data.scale || 1;
            const r = data.rot || 0;
            const z = data.zIndex || '';

            el.style.setProperty('transform', `translate(${x}px, ${y}px) scale(${s}) rotate(${r}deg)`, 'important');
            if (z) el.style.setProperty('z-index', z, 'important');
        }

        // Load layout from server / localStorage
        async function loadLayout() {
            try {
                const res = await fetch('/api/get_custom_layout/' + modelName);
                if (res.ok) {
                    const data = await res.json();
                    if (data && data.layout) layoutState = data.layout;
                }
            } catch(e) {
                const local = localStorage.getItem(STORAGE_KEY);
                if (local) layoutState = JSON.parse(local);
            }

            document.querySelectorAll('.editable-item').forEach(el => {
                const id = getElementId(el);
                if (layoutState[id]) applyStateToElement(el, layoutState[id]);
            });
        }

        window.saveLayoutToServer = async function() {
            localStorage.setItem(STORAGE_KEY, JSON.stringify(layoutState));
            try {
                await fetch('/api/save_custom_layout', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ model: modelName, layout: layoutState })
                });
            } catch(e) {}
            toast.classList.add('visible');
            setTimeout(() => toast.classList.remove('visible'), 3000);
        };

        window.resetAllLayout = function() {
            if (!confirm('Voulez-vous réinitialiser toutes les modifications ?')) return;
            layoutState = {};
            localStorage.removeItem(STORAGE_KEY);
            saveLayoutToServer();
            window.location.reload();
        };

        function selectElement(el) {
            if (activeEl) activeEl.classList.remove('item-selected');
            activeEl = el;
            activeEl.classList.add('item-selected');
            const id = getElementId(activeEl);
            if (!layoutState[id]) layoutState[id] = { x: 0, y: 0, scale: 1, rot: 0, zIndex: 10 };

            itemName.textContent = id.replace(/_/g, ' ');
            sizeText.textContent = Math.round((layoutState[id].scale || 1) * 100) + '%';
            bar.style.display = 'flex';
            bar.style.top = '25px';
            bar.style.right = '40px';
        }

        function deselect() {
            if (activeEl) activeEl.classList.remove('item-selected');
            activeEl = null;
            bar.style.display = 'none';
        }

        // DRAG & DROP
        let isDragging = false;
        let startX, startY, origX, origY;

        document.addEventListener('pointerdown', (e) => {
            const target = e.target.closest('.editable-item');
            if (target) {
                selectElement(target);
                isDragging = true;
                const id = getElementId(target);
                startX = e.clientX;
                startY = e.clientY;
                origX = layoutState[id].x || 0;
                origY = layoutState[id].y || 0;
                e.preventDefault();
            } else if (!e.target.closest('#studio-floating-bar') && !e.target.closest('#tv-control-bar')) {
                deselect();
            }
        });

        document.addEventListener('pointermove', (e) => {
            if (!isDragging || !activeEl) return;
            const id = getElementId(activeEl);
            const scale = getStageScale();
            const dx = (e.clientX - startX) / scale;
            const dy = (e.clientY - startY) / scale;

            layoutState[id].x = Math.round(origX + dx);
            layoutState[id].y = Math.round(origY + dy);
            applyStateToElement(activeEl, layoutState[id]);
        });

        document.addEventListener('pointerup', () => { isDragging = false; });

        // MOUSE WHEEL ZOOM
        document.addEventListener('wheel', (e) => {
            if (!activeEl) return;
            e.preventDefault();
            const id = getElementId(activeEl);
            let s = layoutState[id].scale || 1;
            s = e.deltaY < 0 ? s + 0.05 : s - 0.05;
            s = Math.max(0.3, Math.min(3.0, s));
            layoutState[id].scale = parseFloat(s.toFixed(2));
            sizeText.textContent = Math.round(s * 100) + '%';
            applyStateToElement(activeEl, layoutState[id]);
        }, { passive: false });

        // KEYBOARD ARROWS
        window.addEventListener('keydown', (e) => {
            if (!activeEl) return;
            const id = getElementId(activeEl);
            const step = e.shiftKey ? 15 : 3;

            if (e.key === 'ArrowUp') { layoutState[id].y = (layoutState[id].y || 0) - step; e.preventDefault(); }
            else if (e.key === 'ArrowDown') { layoutState[id].y = (layoutState[id].y || 0) + step; e.preventDefault(); }
            else if (e.key === 'ArrowLeft') { layoutState[id].x = (layoutState[id].x || 0) - step; e.preventDefault(); }
            else if (e.key === 'ArrowRight') { layoutState[id].x = (layoutState[id].x || 0) + step; e.preventDefault(); }
            else if (e.key === '+' || e.key === '=') {
                layoutState[id].scale = Math.min(3, (layoutState[id].scale || 1) + 0.05);
                sizeText.textContent = Math.round(layoutState[id].scale * 100) + '%';
                e.preventDefault();
            } else if (e.key === '-') {
                layoutState[id].scale = Math.max(0.3, (layoutState[id].scale || 1) - 0.05);
                sizeText.textContent = Math.round(layoutState[id].scale * 100) + '%';
                e.preventDefault();
            } else if (e.key === 'Escape') {
                deselect();
            }
            applyStateToElement(activeEl, layoutState[id]);
        });

        // BUTTON ACTIONS
        document.getElementById('sbar-plus').onclick = () => {
            if (!activeEl) return;
            const id = getElementId(activeEl);
            layoutState[id].scale = Math.min(3, (layoutState[id].scale || 1) + 0.08);
            sizeText.textContent = Math.round(layoutState[id].scale * 100) + '%';
            applyStateToElement(activeEl, layoutState[id]);
        };
        document.getElementById('sbar-minus').onclick = () => {
            if (!activeEl) return;
            const id = getElementId(activeEl);
            layoutState[id].scale = Math.max(0.3, (layoutState[id].scale || 1) - 0.08);
            sizeText.textContent = Math.round(layoutState[id].scale * 100) + '%';
            applyStateToElement(activeEl, layoutState[id]);
        };
        document.getElementById('sbar-front').onclick = () => {
            if (!activeEl) return;
            const id = getElementId(activeEl);
            layoutState[id].zIndex = 999;
            applyStateToElement(activeEl, layoutState[id]);
        };
        document.getElementById('sbar-back').onclick = () => {
            if (!activeEl) return;
            const id = getElementId(activeEl);
            layoutState[id].zIndex = 1;
            applyStateToElement(activeEl, layoutState[id]);
        };
        document.getElementById('sbar-close').onclick = deselect;

        loadLayout();
    })();

    // VIDEO MODAL EXPORT
    function openVideoModal() { document.getElementById('modal-video-export').style.display = 'flex'; }
    function closeVideoModal() { document.getElementById('modal-video-export').style.display = 'none'; }
    async function startVideoRender() {
        const status = document.getElementById('render-status');
        const btn = document.getElementById('btn-start-render');
        status.style.display = 'block';
        status.innerHTML = '⏳ Rendu vidéo en cours... Veuillez patienter 15 à 30 secondes.';
        btn.disabled = true;

        try {
            const res = await fetch('/api/export_menu_video', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ model: 'menu_model4_behance', duration: 15 })
            });
            const data = await res.json();
            if (data.status === 'success') {
                status.innerHTML = `✅ Vidéo générée avec succès !<br>📁 <a href="/${data.filename}" download style="color:#10b981; text-decoration:underline;">Télécharger ${data.filename} (${data.size_mb} MB)</a>`;
            } else {
                status.innerHTML = '❌ Erreur: ' + (data.message || 'Échec du rendu');
            }
        } catch(e) {
            status.innerHTML = '❌ Erreur serveur lors du rendu vidéo.';
        }
        btn.disabled = false;
    }
</script>

</body>
</html>
"""

with open(r'c:\Users\pc\Desktop\menu\menu_model4_behance.html', 'w', encoding='utf-8') as f:
    f.write(HTML_CONTENT)

print('File menu_model4_behance.html written successfully!')

