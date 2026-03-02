# Insights: [overbool/poster](https://github.com/overbool/poster)

**~45 stars** · JavaScript canvas · MIT · [Demo](https://overbool.github.io/poster/)

## What It Is

A **standalone JS micro-library** that generates a poster from config: banner image, title, content, logo, description. Renders into a DOM container (canvas-based or similar). No framework required; use via npm or CDN.

## Actionable Takeaways

| Idea | How to use |
|------|------------|
| **Config-driven poster** | Single object with `banner`, `selector`, `title`, `content`, `logo`, `description`, `callback`. We can offer a JSON config → HTML or canvas in our scripts. |
| **Style overrides** | `titleStyle`, `contentStyle`, `logoStyle` (font, color, lineHeight, position). Map to CSS or canvas font/align when we generate programmatically. |
| **Callback when done** | `callback: function(container) {}` for post-render (e.g. trigger html2canvas). Reuse pattern in our export flow. |
| **Standalone / CDN** | Single `poster.min.js`; no build step for simple demos. Our posterScripts can stay dependency-light. |

## Code to Borrow (API pattern)

```js
poster.init({
  banner: './images/dream.png',
  selector: '.poster',
  title: 'Title text',
  titleStyle: { font: 'bold 50px Arial', color: 'rgba(66,66,66,1)' },
  content: 'Body text',
  contentStyle: { font: '24px Arial', lineHeight: 1.2, position: 'center', color: 'rgba(88,88,88,1)' },
  logo: 'Logo URL',
  description: 'Footer text',
  callback: function(container) { /* e.g. html2canvas(container) */ }
})
```

## References

- Repo: `src/poster.js`, `index.html`, `generate.html`.
- npm: `npm i @overbool/poster`.
- Use our `export-poster.html` for a similar “config + single container” export.
