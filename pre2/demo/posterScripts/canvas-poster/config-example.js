/**
 * Config-driven poster pattern (inspired by overbool/poster).
 * Use with a template that reads this config and renders into #poster-container,
 * then call html2canvas on that container to export.
 *
 * Usage: include this file and your template script; or adapt to JSON for static site gens.
 */

const posterConfig = {
  banner: './images/banner.jpg',       // top image URL
  selector: '#poster-container',
  title: 'MCCP Spring 2026',
  titleStyle: {
    font: 'bold 48px system-ui, sans-serif',
    color: 'rgba(30, 30, 30, 1)',
  },
  content: 'Presentation 2 — Config-driven poster. Edit this object and re-run.',
  contentStyle: {
    font: '24px system-ui, sans-serif',
    lineHeight: 1.3,
    position: 'center',
    color: 'rgba(80, 80, 80, 1)',
  },
  logo: '',                            // optional logo URL
  description: 'Inspired by overbool/poster',
  callback(container) {
    // Called when poster is rendered; e.g. trigger export
    if (typeof html2canvas !== 'undefined') {
      html2canvas(container).then(canvas => {
        const link = document.createElement('a');
        link.download = 'poster.png';
        link.href = canvas.toDataURL('image/png');
        link.click();
      });
    }
  },
};

// Expose for browser or Node
if (typeof window !== 'undefined') {
  window.posterConfig = posterConfig;
}
if (typeof module !== 'undefined' && module.exports) {
  module.exports = posterConfig;
}
