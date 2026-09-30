function applyBgEffect(container, effect, bgColor) {
    if(container.animationFrameId) cancelAnimationFrame(container.animationFrameId);
    container.innerHTML = '';
    
    // Support for video backgrounds
    if (bgColor && (bgColor.toLowerCase().endsWith('.mp4') || bgColor.toLowerCase().endsWith('.webm'))) {
        container.style.background = 'black'; // fallback
        const video = document.createElement('video');
        video.src = bgColor;
        video.autoplay = true;
        video.loop = true;
        video.muted = true;
        // Allows inline playback on many devices
        video.setAttribute('playsinline', ''); 
        video.style.position = 'absolute';
        video.style.top = '0';
        video.style.left = '0';
        video.style.width = '100%';
        video.style.height = '100%';
        video.style.objectFit = 'cover';
        video.style.zIndex = '0'; // Behind everything
        container.appendChild(video);
    } else {
        container.style.background = bgColor || '#1a1a1a';
    }
    
    if (!effect || effect === 'none') return;
    
    if (effect === 'beams') {
        container.innerHTML = `<div style="position: absolute; top: -50%; left: 50%; width: 800px; height: 2000px; background: linear-gradient(90deg, transparent, rgba(255,255,255,0.05), transparent); transform: rotate(35deg) translateX(-50%); z-index: 1; pointer-events: none; animation: anim-wobble 10s infinite alternate;"></div><div style="position: absolute; top: -50%; left: 50%; width: 800px; height: 2000px; background: linear-gradient(90deg, transparent, rgba(255,255,255,0.05), transparent); transform: rotate(-35deg) translateX(-50%); z-index: 1; pointer-events: none; animation: anim-wobble 8s infinite alternate-reverse;"></div>`;
        return;
    }
    
    if (effect === 'neon') {
        container.style.boxShadow = 'inset 0 0 150px rgba(255, 0, 255, 0.4), inset 0 0 50px rgba(0, 255, 255, 0.4)';
        container.innerHTML = `<div style="position:absolute; inset:0; background: radial-gradient(circle at center, transparent 30%, rgba(0,0,0,0.8)); pointer-events:none;"></div>`;
        return;
    }

    const canvas = document.createElement('canvas');
    canvas.width = 1920;
    canvas.height = 1080;
    canvas.style.position = 'absolute';
    canvas.style.top = '0';
    canvas.style.left = '0';
    canvas.style.width = '100%';
    canvas.style.height = '100%';
    canvas.style.pointerEvents = 'none';
    canvas.style.zIndex = '1';
    container.appendChild(canvas);
    
    const ctx = canvas.getContext('2d');
    let particles = [];
    let animationFrameId;

    function createParticle() {
        if (effect === 'fire') {
            return {
                x: Math.random() * canvas.width,
                y: canvas.height + 10,
                size: Math.random() * 4 + 1,
                speedY: Math.random() * -3 - 1,
                speedX: Math.random() * 2 - 1,
                color: Math.random() > 0.5 ? 'rgba(255, 100, 0, 0.8)' : 'rgba(255, 200, 0, 0.8)',
                life: 1
            };
        } else if (effect === 'smoke') {
            return {
                x: Math.random() * canvas.width,
                y: canvas.height + 100,
                size: Math.random() * 100 + 50,
                speedY: Math.random() * -1 - 0.5,
                speedX: Math.random() * 1 - 0.5,
                color: `rgba(200, 200, 200, ${Math.random() * 0.05 + 0.01})`,
                life: 1
            };
        } else if (effect === 'chalk') {
            return {
                x: Math.random() * canvas.width,
                y: Math.random() * canvas.height,
                size: Math.random() * 2 + 0.5,
                speedY: Math.random() * 0.5 - 0.25,
                speedX: Math.random() * 0.5 - 0.25,
                color: `rgba(255, 255, 255, ${Math.random() * 0.3 + 0.1})`,
                life: 1
            };
        } else if (effect === 'steam') {
            return {
                x: (Math.random() * canvas.width * 0.8) + (canvas.width * 0.1), // center mostly
                y: canvas.height + 50,
                size: Math.random() * 40 + 20,
                speedY: Math.random() * -1.5 - 0.5,
                speedX: Math.random() * 0.6 - 0.3,
                wobbleSpeed: Math.random() * 0.05 + 0.01,
                wobbleRadius: Math.random() * 2 + 1,
                angle: Math.random() * Math.PI * 2,
                color: `rgba(255, 255, 255, ${Math.random() * 0.15 + 0.05})`,
                life: 1
            };
        } else if (effect === 'sparks') {
            return {
                x: Math.random() * canvas.width,
                y: canvas.height + 10,
                size: Math.random() * 3 + 1,
                speedY: Math.random() * -6 - 2,
                speedX: Math.random() * 4 - 2,
                color: Math.random() > 0.5 ? 'rgba(255, 255, 100, 1)' : 'rgba(255, 150, 0, 1)',
                life: 1,
                gravity: 0.05
            };
        } else if (effect === 'snow') {
            return {
                x: Math.random() * canvas.width,
                y: -10,
                size: Math.random() * 3 + 1,
                speedY: Math.random() * 2 + 1,
                speedX: Math.random() * 1 - 0.5,
                color: `rgba(255, 255, 255, ${Math.random() * 0.8 + 0.2})`,
                life: 1
            };
        } else if (effect === 'bubbles') {
            return {
                x: Math.random() * canvas.width,
                y: canvas.height + 10,
                size: Math.random() * 8 + 2,
                speedY: Math.random() * -3 - 1,
                speedX: Math.random() * 1 - 0.5,
                wobbleSpeed: Math.random() * 0.1,
                wobbleRadius: Math.random() * 3,
                angle: Math.random() * Math.PI * 2,
                color: `rgba(255, 255, 255, 0.4)`,
                life: 1
            };
        } else if (effect === 'stars') {
            return {
                x: Math.random() * canvas.width,
                y: Math.random() * canvas.height,
                size: Math.random() * 2 + 0.5,
                speedY: 0,
                speedX: 0,
                alpha: Math.random(),
                fadeDir: Math.random() > 0.5 ? 1 : -1,
                fadeSpeed: Math.random() * 0.02 + 0.01,
                color: `255, 255, 255`,
                life: 1
            };
        } else if (effect === 'confetti') {
            const colors = ['#fce18a', '#ff726d', '#b48def', '#f4306d'];
            return {
                x: Math.random() * canvas.width,
                y: -20,
                size: Math.random() * 10 + 5,
                speedY: Math.random() * 3 + 2,
                speedX: Math.random() * 4 - 2,
                rotation: Math.random() * 360,
                rotSpeed: Math.random() * 10 - 5,
                color: colors[Math.floor(Math.random() * colors.length)],
                life: 1
            };
        }
    }

    let maxP = 150;
    if (effect === 'fire') maxP = 100;
    else if (effect === 'smoke') maxP = 20;
    else if (effect === 'steam') maxP = 40;
    else if (effect === 'sparks') maxP = 80;
    else if (effect === 'bubbles') maxP = 50;
    else if (effect === 'stars') maxP = 200;
    const maxParticles = maxP;
    
    for (let i = 0; i < maxParticles; i++) {
        const p = createParticle();
        if (effect === 'chalk' || effect === 'smoke' || effect === 'steam' || effect === 'snow' || effect === 'bubbles') p.y = Math.random() * canvas.height;
        particles.push(p);
    }

    function animate() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        for (let i = 0; i < particles.length; i++) {
            let p = particles[i];
            
            ctx.beginPath();
            if (effect === 'smoke' || effect === 'steam') {
                const grad = ctx.createRadialGradient(p.x, p.y, 0, p.x, p.y, p.size);
                grad.addColorStop(0, p.color);
                grad.addColorStop(1, 'rgba(0,0,0,0)');
                ctx.fillStyle = grad;
                ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
            } else if (effect === 'stars') {
                ctx.fillStyle = `rgba(${p.color}, ${p.alpha})`;
                ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
            } else if (effect === 'confetti') {
                ctx.save();
                ctx.translate(p.x, p.y);
                ctx.rotate(p.rotation * Math.PI / 180);
                ctx.fillStyle = p.color;
                ctx.fillRect(-p.size/2, -p.size/2, p.size, p.size/2);
                ctx.restore();
            } else {
                ctx.fillStyle = p.color;
                ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
            }
            if (effect !== 'confetti') ctx.fill();
            
            if (effect === 'steam' || effect === 'bubbles') {
                p.angle += p.wobbleSpeed;
                p.x += p.speedX + Math.sin(p.angle) * p.wobbleRadius;
                p.y += p.speedY;
                if (effect === 'steam') p.size += 0.2;
                if (p.y < -p.size) particles[i] = createParticle();
            } else if (effect === 'sparks') {
                p.speedY += p.gravity;
                p.x += p.speedX;
                p.y += p.speedY;
                p.size *= 0.95;
                if (p.size < 0.1 || p.y > canvas.height + 50) particles[i] = createParticle();
            } else if (effect === 'snow') {
                p.x += p.speedX;
                p.y += p.speedY;
                if (p.y > canvas.height + 10) particles[i] = createParticle();
            } else if (effect === 'stars') {
                p.alpha += p.fadeSpeed * p.fadeDir;
                if (p.alpha > 1) { p.alpha = 1; p.fadeDir = -1; }
                else if (p.alpha < 0) { p.alpha = 0; p.fadeDir = 1; p.x = Math.random() * canvas.width; p.y = Math.random() * canvas.height; }
            } else if (effect === 'confetti') {
                p.x += p.speedX;
                p.y += p.speedY;
                p.rotation += p.rotSpeed;
                if (p.y > canvas.height + 20) particles[i] = createParticle();
            } else {
                p.y += p.speedY;
                p.x += p.speedX;
            }
            
            if (effect === 'fire') {
                p.size *= 0.98;
                if (p.size < 0.2 || p.y < 0) particles[i] = createParticle();
            } else if (effect === 'smoke') {
                p.size += 0.5;
                if (p.y < -p.size) particles[i] = createParticle();
            } else if (effect === 'chalk') {
                if (p.x < 0 || p.x > canvas.width || p.y < 0 || p.y > canvas.height) particles[i] = createParticle();
            }
        }
        
        animationFrameId = requestAnimationFrame(animate);
    }
    
    animate();
    container.animationFrameId = animationFrameId;
}
