if (window.mermaid) {
  window.mermaid.initialize({ startOnLoad: true, theme: "default", securityLevel: "loose" });
}
document.addEventListener("DOMContentLoaded", () => {
  if (window.mermaid) {
    mermaid.initialize({ startOnLoad: true, securityLevel: 'loose', theme: 'base' });
  }
});

