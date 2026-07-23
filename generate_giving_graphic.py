import math, sys, cairosvg
from PIL import Image

MS=[240000,480000,600000,720000,960000,1200000]
CX=CY=230; RADIUS=142; STROKE=32; LABEL_R=178; GAP=1.0
SEG=360/len(MS)
GREEN="#7CB342"; BLUE="#2E80C2"; TEXT="#111827"; FONT="Poppins"
TITLE_SIZE=25; AMOUNT_SIZE=30   # "Together we've / raised" size + amount size

def polar(r,deg):
    a=math.radians(deg); return (CX+r*math.sin(a), CY-r*math.cos(a))
def arc(r,s,e):
    x1,y1=polar(r,s); x2,y2=polar(r,e); large=1 if (e-s)>180 else 0
    return f"M {x1:.2f} {y1:.2f} A {r} {r} 0 {large} 1 {x2:.2f} {y2:.2f}"
def seg(r,a,b,c):
    return f'<path d="{arc(r,a,b)}" fill="none" stroke="{c}" stroke-width="{STROKE}" stroke-linecap="butt"/>'
def prog_angle(amt):
    if amt<=0: return 0
    prev=0
    for i,m in enumerate(MS):
        if amt<m: return (i+(amt-prev)/(m-prev))*SEG
        prev=m
    return 360
def ring(angle):
    h=""
    for i in range(len(MS)):
        a=i*SEG; b=(i+1)*SEG; s=a+GAP; e=b-GAP
        if e<=s: continue
        c=max(s,min(e,angle))
        if c>s+0.01: h+=seg(RADIUS,s,c,GREEN)
        if c<e-0.01: h+=seg(RADIUS,c,e,BLUE)
    return h
def labels():
    h=""
    for i,v in enumerate(MS):
        deg=(i+1)*SEG; x,y=polar(LABEL_R,deg); sin=math.sin(math.radians(deg))
        anc="middle"
        if sin>0.2: anc="start"
        elif sin<-0.2: anc="end"
        h+=f'<text x="{x:.1f}" y="{y+5:.1f}" text-anchor="{anc}" font-family="{FONT}" font-weight="700" font-size="15" fill="#000">${v:,.0f}</text>'
    return h
def center_block(current):
    ts=TITLE_SIZE; amt=AMOUNT_SIZE
    lineGap=ts*1.25; amtGap=amt*1.15; total=lineGap+amtGap; c=232
    b1=c-total/2+ts*0.3; b2=b1+lineGap; b3=b2+amtGap   # matches editor layoutCenter()
    return (f'<text x="230" y="{b1:.1f}" text-anchor="middle" font-family="{FONT}" font-weight="700" font-size="{ts}" fill="{TEXT}">Together we\'ve</text>'
            f'<text x="230" y="{b2:.1f}" text-anchor="middle" font-family="{FONT}" font-weight="700" font-size="{ts}" fill="{TEXT}">raised</text>'
            f'<text x="230" y="{b3:.1f}" text-anchor="middle" font-family="{FONT}" font-weight="700" font-size="{amt}" fill="{TEXT}">${current:,.2f}</text>')

def build(current, goal, banner_path, out_path):
    inner=ring(prog_angle(current))+labels()
    svg=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-50 0 560 460" preserveAspectRatio="xMidYMid meet" width="740" height="740">{inner}{center_block(current)}</svg>'
    cairosvg.svg2png(bytestring=svg.encode(),write_to="_ring_tmp.png",output_width=740,output_height=740,background_color="rgba(0,0,0,0)")
    banner=Image.open(banner_path).convert('RGBA').resize((2048,1152), Image.LANCZOS)
    ringimg=Image.open("_ring_tmp.png").convert('RGBA')
    banner.alpha_composite(ringimg,(8,204))   # box centre (189,287)*2, size 740
    banner.convert('RGB').save(out_path)
    return out_path

if __name__=="__main__":
    cur=float(sys.argv[1]); goal=float(sys.argv[2]); banner=sys.argv[3]; out=sys.argv[4]
    print(build(cur,goal,banner,out))
