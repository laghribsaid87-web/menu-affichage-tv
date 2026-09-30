with open('dashboard.html', 'r', encoding='utf-8') as f:
    content = f.read()

animOutBlock = """
                                                <div>
                                                    <label class="text-[10px] text-slate-400 uppercase">Anim Sortie</label>
                                                    <select v-model="comp.animOut" class="select-field text-xs py-1"
                                                            @wheel.prevent="cycleSelectOption($event, comp, 'animOut', Math.sign($event.deltaY))"
                                                            @keydown.up.prevent="cycleSelectOption($event, comp, 'animOut', -1)"
                                                            @keydown.down.prevent="cycleSelectOption($event, comp, 'animOut', 1)">
                                                        <option value="none">Aucune</option>
                                                        <option value="fadeDown">Tombe (S'en va vers le bas)</option>
                                                        <option value="fadeUp">Monte (S'en va vers le haut)</option>
                                                        <option value="fadeRight">Vers la Gauche</option>
                                                        <option value="fadeLeft">Vers la Droite</option>
                                                        <option value="zoomOut">Zoom Arrière (Sortie)</option>
                                                        <option value="fade">Fondu (Fade Out)</option>
                                                        <option value="pop">Pop Inverse</option>
                                                        <option value="drop">Envole (Drop Inverse)</option>
                                                        <option value="rollIn">Roulade Arrière</option>
                                                        <option value="driftLeft">Dérive Droite</option>
                                                        <option value="driftRight">Dérive Gauche</option>
                                                    </select>
                                                </div>
"""

layoutAnimOutBlock = animOutBlock.replace('comp.animOut', 'layout.animOut').replace(', comp,', ', layout,')

# Find the end of the animIn div for components
animInStr = """<option value="driftLeft">Dérive Gauche</option>
                                                        <option value="driftRight">Dérive Droite</option>
                                                    </select>
                                                </div>"""

parts = content.split(animInStr)
if len(parts) == 3:
    # First split is for component, second is for layout
    content = parts[0] + animInStr + animOutBlock + parts[1] + animInStr + layoutAnimOutBlock + parts[2]
else:
    print(f"Expected 3 parts, got {len(parts)}")

with open('dashboard.html', 'w', encoding='utf-8') as f:
    f.write(content)
