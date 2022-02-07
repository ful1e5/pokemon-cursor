import path from "path";

import { BitmapsGenerator, SVGHandler } from "./core";

const root = path.resolve(__dirname, "../../");
const svgDir = path.resolve(root, "svg");
const themeName = "Pokemon";

const main = async () => {
  console.log("Generating bitmaps for", themeName);

  const bitmapsDir = path.resolve(root, "bitmaps", themeName);
  const svg = new SVGHandler.SvgDirectoryParser(svgDir);

  const png = new BitmapsGenerator(bitmapsDir);
  const browser = await png.getBrowser();

  for (let { key, content } of svg.getStatic()) {
    console.log(" ==> Saving", key, "...");
    await png.generateStatic(browser, content, key);
  }

  for (let { key, content } of svg.getAnimated()) {
    console.log(" ==> Saving", key, "...");
    await png.generateAnimated(browser, content, key, { playbackRate: 1.0 });
  }

  await browser.close();
};

main();
