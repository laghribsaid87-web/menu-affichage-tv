with open('dashboard.html', 'r', encoding='utf-8') as f:
    content = f.read()
if "currentProject === 'smart'" not in content:
    content = content.replace(
        """<a :href="'/tv' + currentTvId + '.html?project=' + currentProject\"""",
        """<a :href="currentProject === 'smart' ? '/tv_dynamic.html' : '/tv' + currentTvId + '.html?project=' + currentProject\""""
    )
    # Also update the Lancer TV button if it exists
    content = content.replace(
        """window.open(`/tv${this.currentTvId}.html?project=${this.currentProject}`, '_blank');""",
        """window.open(this.currentProject === 'smart' ? '/tv_dynamic.html' : `/tv${this.currentTvId}.html?project=${this.currentProject}`, '_blank');"""
    )
    with open('dashboard.html', 'w', encoding='utf-8') as f:
        f.write(content)
print("Updated dashboard links")
