/**
 * Export a poster from HTML to PNG using Puppeteer.
 * Run: npm install puppeteer && node export-node.js
 */

const puppeteer = require('puppeteer');
const fs = require('fs');
const path = require('path');

const HTML = `
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <style>
    body { margin: 0; padding: 20px; font-family: system-ui, sans-serif; }
    .poster {
      width: 600px; height: 800px;
      background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
      color: #eee; padding: 48px; border-radius: 8px;
    }
    .poster h1 { font-size: 36px; margin: 0 0 16px; }
    .poster p { font-size: 18px; opacity: 0.9; }
  </style>
</head>
<body>
  <div class="poster">
    <h1>MCCP Poster</h1>
    <p>Generated with Puppeteer (Node)</p>
  </div>
</body>
</html>
`;

async function main() {
  const browser = await puppeteer.launch({ headless: 'new' });
  const page = await browser.newPage();
  await page.setContent(HTML, { waitUntil: 'networkidle0' });
  const el = await page.$('.poster');
  const outPath = path.join(__dirname, 'output-poster.png');
  await el.screenshot({ path: outPath });
  await browser.close();
  console.log('Saved:', outPath);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
