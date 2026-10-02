from pathlib import Path
from PIL import Image, ImageOps, ImageDraw
p=Path('tmp/pdfs/review')
files=sorted(p.glob('page-*.png'), key=lambda x:int(x.stem.split('-')[1]))
thumb_w=390
margin=20
cols,rows=3,2
for start in range(0,len(files),cols*rows):
    batch=files[start:start+cols*rows]
    thumbs=[]
    for f in batch:
        im=Image.open(f).convert('RGB')
        h=round(im.height*thumb_w/im.width)
        im=im.resize((thumb_w,h))
        canvas=Image.new('RGB',(thumb_w,h+30),'white')
        canvas.paste(im,(0,30))
        ImageDraw.Draw(canvas).text((8,7),f'Page {int(f.stem.split("-")[1])}',fill='black')
        thumbs.append(canvas)
    cell_h=max(im.height for im in thumbs)
    sheet=Image.new('RGB',(cols*thumb_w+(cols+1)*margin,rows*cell_h+(rows+1)*margin),(220,220,220))
    for j,im in enumerate(thumbs):
        x=margin+(j%cols)*(thumb_w+margin)
        y=margin+(j//cols)*(cell_h+margin)
        sheet.paste(im,(x,y))
    sheet.save(p/f'contact-{start//(cols*rows)+1}.png')
