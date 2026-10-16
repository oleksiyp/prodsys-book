// App icons and favicons for the Signals cover: a small book whose lower half holds four telemetry traces, one in vermilion with a spike.
// Usage: node icons.mjs (writes ../assets/icons)
import puppeteer from 'puppeteer-core';
const INK = '#111318', RED = '#D9482B', PAPER = '#F6F4EF', GHOST = '#9E998D';
// A 64-unit book: frame, title plate, traces.
function book() {
  const trace = (y, amp, color, w) => {
    let d = `M15 ${y}`;
    for (let x = 15; x <= 49; x += 1) {
      const u = (x - 32) / 17, env = Math.max(0, 1 - u * u);
      const s = amp ? amp * Math.exp(-Math.pow((x - 33) / 2.6, 2)) + amp * 0.35 * Math.exp(-Math.pow((x - 39) / 3.2, 2)) : 0;
      d += ` L${x} ${(y - s - env * 1.2 * Math.sin(x * 1.3 + y)).toFixed(2)}`;
    }
    return `<path d="${d}" fill="none" stroke="${color}" stroke-width="${w}" stroke-linecap="round" stroke-linejoin="round"/>`;
  };
  return `<rect x="9" y="2" width="46" height="60" rx="4" fill="${PAPER}" stroke="${INK}" stroke-width="3"/>` +
    `<rect x="13" y="7" width="38" height="16" rx="1.5" fill="#fff" stroke="${INK}" stroke-width="1.6"/>` +
    `<rect x="16" y="10" width="26" height="3.2" fill="${INK}"/><rect x="16" y="14.6" width="18" height="2.2" fill="${INK}"/><rect x="16" y="18.6" width="32" height="1.6" fill="${RED}"/>` +
    trace(34, 0, GHOST, 1.4) + trace(41, 0, GHOST, 1.4) + trace(48, 9, RED, 2.6) + trace(55, 0, GHOST, 1.4);
}
const svg = (size, scale, bg) => `<svg xmlns="http://www.w3.org/2000/svg" width="${size}" height="${size}" viewBox="0 0 64 64">${bg ? `<rect width="64" height="64" fill="${bg}"/>` : ''}<g transform="translate(32 32) scale(${scale}) translate(-32 -32)">${book()}</g></svg>`;
const OUT = [
  ['../assets/icons/favicon-64.png', 64, 1, null], ['../assets/icons/favicon-32.png', 32, 1, null],
  ['../assets/icons/apple-touch-icon.png', 180, 0.86, '#f3f1ec'], ['../assets/icons/icon-192.png', 192, 1, null],
  ['../assets/icons/icon-512.png', 512, 1, null], ['../assets/icons/icon-512-maskable.png', 512, 0.68, '#f3f1ec'],
];
const b = await puppeteer.launch({ executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', headless: true });
const p = await b.newPage();
for (const [file, size, scale, bg] of OUT) {
  await p.setViewport({ width: size, height: size });
  await p.setContent(`<html><body style="margin:0;background:transparent">${svg(size, scale, bg)}</body></html>`);
  await p.screenshot({ path: file, omitBackground: true, clip: { x: 0, y: 0, width: size, height: size } });
  console.log('wrote', file);
}
await b.close();
