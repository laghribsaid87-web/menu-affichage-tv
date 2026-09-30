import re

with open('dashboard.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the select options for animIn
# We find:
# <option value="fadeUp">Monte</option>
# <option value="fadeDown">Tombe</option>
# <option value="fadeLeft">Venant de Droite</option>
# <option value="fadeRight">Venant de Gauche</option>
# <option value="zoomIn">Zoom In</option>

new_options = """<option value="fadeUp">Lever (Monte)</option>
                                                        <option value="fadeDown">Tombe</option>
                                                        <option value="fadeLeft">Venant de Droite</option>
                                                        <option value="fadeRight">Venant de Gauche</option>
                                                        <option value="zoomIn">Zoom</option>
                                                        <option value="fade">Fondu (Fade)</option>
                                                        <option value="pop">Pop (Scale Pop)</option>
                                                        <option value="drop">Chute (Drop)</option>
                                                        <option value="rollIn">Roulade (Roll In)</option>
                                                        <option value="driftLeft">Dérive Gauche</option>
                                                        <option value="driftRight">Dérive Droite</option>"""

content = content.replace("""<option value="fadeUp">Monte</option>
                                                        <option value="fadeDown">Tombe</option>
                                                        <option value="fadeLeft">Venant de Droite</option>
                                                        <option value="fadeRight">Venant de Gauche</option>
                                                        <option value="zoomIn">Zoom In</option>""", new_options)

# Update getAnimOffset
new_getAnimOffset = """getAnimOffset(type) {
                    const config = { x: 0, y: 0, scale: 1, opacity: 0 };
                    const dist = 300;
                    switch(type) {
                        case 'fadeUp': config.y = dist; break;
                        case 'fadeDown': config.y = -dist; break;
                        case 'fadeLeft': config.x = dist; break;
                        case 'fadeRight': config.x = -dist; break;
                        case 'zoomIn': config.scale = 0; break;
                        case 'zoomOut': config.scale = 2; break;
                        case 'fade': break; // Opacity only
                        case 'pop': config.scale = 0.5; break;
                        case 'drop': config.y = -700; break;
                        case 'rollIn': config.rotationOffset = -180; config.scale = 0; break;
                        case 'driftLeft': config.x = 100; break;
                        case 'driftRight': config.x = -100; break;
                        default: config.y = 50; break;
                    }
                    return config;
                },"""

content = re.sub(r'getAnimOffset\(type\)\s*\{[\s\S]*?\},', new_getAnimOffset, content)

# Update tl.fromTo animation code to support rotationOffset
old_fromTo = """tl.fromTo(item, 
                                { x: fromOffset.x, y: fromOffset.y, scale: fromOffset.scale, opacity: 0, rotation: rotation },
                                { x: 0, y: 0, scale: 1, opacity: 1, rotation: rotation, duration: 1.5, ease: "back.out(1.2)" },
                                delay
                            );"""

new_fromTo = """tl.fromTo(item, 
                                { x: fromOffset.x, y: fromOffset.y, scale: fromOffset.scale, opacity: 0, rotation: (fromOffset.rotationOffset !== undefined ? rotation + fromOffset.rotationOffset : rotation) },
                                { x: 0, y: 0, scale: 1, opacity: 1, rotation: rotation, duration: 1.5, ease: "back.out(1.2)" },
                                delay
                            );"""

content = content.replace(old_fromTo, new_fromTo)

with open('dashboard.html', 'w', encoding='utf-8') as f:
    f.write(content)
