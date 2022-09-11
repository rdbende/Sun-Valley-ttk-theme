// Huge thanks to @TransparentLC on Github for this script

import fs from "fs";
import path from "path";
import sharp from "sharp";
import { globbyStream } from "globby";
import { MaxRectsPacker } from "maxrects-packer";


for (const theme of ["dark", "light"]) {
    const packer = new MaxRectsPacker(Infinity, Infinity, 0, {
        pot: false,
        square: false,
    });

    let images = [];

    for await (const path of globbyStream(`${theme}/*.png`)) {
        images.push(path)
    }

    packer.addArray(await Promise.all(images.map(async f => {
        const p = f;
        const { width, height } = await sharp(p).metadata();
        const imagePath = f;
        return {
            width,
            height,
            imagePath,
        };
    })));

    const packedBin = packer.bins[0];

    const packedImage = await sharp({
        create: {
            width: packedBin.width,
            height: packedBin.height,
            channels: 4,
            background: 'transparent',
        },
    })
        .composite(packedBin.rects.map(e => ({
            input: e.imagePath,
            left: e.x,
            top: e.y,
        })))
        .png({
            compressionLevel: 9,
        })
        .toBuffer();

    fs.writeFileSync(`../theme/spritesheet_${theme}.png`, packedImage);
    fs.writeFileSync(`../theme/sprites_${theme}.tcl`, `set ::spriteinfo [list \\\n  ${packedBin.rects.map(e => `${path.parse(e.imagePath).name} ${e.x} ${e.y} ${e.width} ${e.height}`).join(' \\\n  ')} \\\n]\n`);
}
