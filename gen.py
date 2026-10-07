import re
D=[
(1963,'昭和38年',['会社設立'],'創業'),(1968,'昭和43年',['手巻き式イカ釣機発売']),(1970,'昭和45年',['全自動イカ釣機発売']),
(1973,'昭和48年',['全漁連・八戸漁連指定品認定','販売9100台突破']),(1974,'昭和49年',['イカ釣機用集中制御盤発売']),
(1975,'昭和50年',['サイリスタ制御式イカ釣機発売','体育館完成']),(1976,'昭和51年',['本社工場新設']),(1977,'昭和52年',['揚縄機発売','組立工場新設']),
(1978,'昭和53年',['小形揚縄機(ミニホーラー)発売','ギアードモータ開発']),(1980,'昭和55年',['P-1-A型イカ・魚釣機発売']),
(1982,'昭和57年',['ホタテ貝穴あけ機発売']),(1983,'昭和58年',['芋選別機ポテーラ発売','イカロボ開発']),
(1984,'昭和59年',['コンピューター式全自動イカ釣機MY-1型発売','初代社長交代']),(1985,'昭和60年',['バッテリー式マイコン内蔵イカ釣機MY-24型発売']),
(1986,'昭和61年',['ホタテカゴ洗浄機発売','一本釣機UGシリーズ発売']),(1990,'平成2年',['イカロボエースMY-3型発売','カーボンファイバードラム試作']),
(1991,'平成3年',['自動ホタテ貝穴あけ機HDA-100型発売','本社事務所新設']),(1992,'平成4年',['*発明協会北海道知事賞受賞']),
(1993,'平成5年',['マイコン式揚縄機発売','イカ生処理加工機開発']),(1995,'平成7年',['カーボンファイバー製軽量ドラム発売','マグロ一本釣機MR-2型発売']),
(1996,'平成8年',['資本金1,000万円に増資','ハワイ社員旅行実施']),(1997,'平成9年',['全自動イカ釣機MY-10型発売','FAD-800型発売']),
(1998,'平成10年',['FAD-800SS型発売']),(1999,'平成11年',['スルメ加工機試作','サンマ漁灯試作']),
(2000,'平成12年',['GPS利用測量機器発売','*発明協会地方発明賞受賞']),(2002,'平成14年',['全自動イカ釣機MY-7型発売','*特許庁長官知財功労賞受賞']),
(2003,'平成15年',['*北海道新聞文化賞受賞','LED漁灯開発着手']),(2004,'平成16年',['海水電解殺菌装置発売','LED漁灯(RGB)開発']),
(2005,'平成17年',['新型オモリ鉄矢発売','巻下制御ユニット発売']),(2006,'平成18年',['高出力全自動イカ釣機EX-1型発売','*「今年のロボット大賞」受賞']),
(2007,'平成19年',['ものづくり展出展']),(2008,'平成20年',['サンマ漁LED漁灯発売','資本金9,900万に増資']),
(2009,'平成21年',['高機能全自動イカ釣機MY-12型発売']),(2010,'平成22年',['*海洋水産システム協会協会賞受賞']),
(2012,'平成24年',['全自動ホタテ穴あけ結束装置TEC-3型発売']),(2013,'平成25年',['50周年記念式典実施'],'50周年'),
(2014,'平成26年',['*グローバルニッチトップ企業100選受賞']),(2017,'平成29年',['*社長が秋の叙勲「旭日双光章」受章']),
(2019,'令和元年',['三代目社長就任']),(2025,'令和7年',['九州事業部新設'],'NEW')]
def lis(items):
    o=''
    for i in items:
        o+= '<li><span class="flag">受賞</span>%s</li>'%i[1:] if i[0]=='*' else '<li>%s</li>'%i
    return o
def flags(e):
    return ''
head='''<!doctype html>
<html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>%s</title>
<meta name="description" content="株式会社 東和電機製作所 HAMADE — 創造的改革へ。">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@500;700;800;900&family=Noto+Sans+JP:wght@400;500;700;900&display=swap" rel="stylesheet">
<style>CSS</style></head><body>
<div id="progress"></div>
<header class="hd" id="hd"><div class="wrap">
<a class="logo" href="index.html"><i></i>HAMADE<small>東和電機製作所</small></a>
<nav class="gnb"><a href="index.html#about">会社情報</a><a href="history.html" %s>HAMADEの歴史</a><a href="index.html#products">製品情報</a><a href="index.html#news">お知らせ</a><a href="#">採用情報</a></nav>
<a class="pill" href="#">お問い合わせ</a>
<button class="menu-btn" aria-label="メニュー"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg></button>
</div></header>
<main>'''
foot='''</main>
<footer class="ft" id="ft"><div class="wrap">
<a class="logo" href="index.html"><i></i>HAMADE<small>株式会社 東和電機製作所</small></a>
<nav><a href="index.html#about">会社情報</a><a href="history.html">HAMADEの歴史</a><a href="index.html#products">製品情報</a><a href="#">採用情報</a><a href="#">お問い合わせ</a><a href="#">ENGLISH</a></nav>
<p style="flex-basis:100%;font-size:12px">© 2026 株式会社東和電機製作所 ／ デザインリニューアル案（コピーの一部は仮のものです）</p>
</div></footer>
<div class="dock" id="dock"><div class="dock-bar"><span>製品・導入のご相談はお気軽にどうぞ</span><a class="pill" href="#">お問い合わせ</a></div></div>
<script>JS</script></body></html>'''
arr='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 6l6 6-6 6"/></svg>'
arl='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 6l-6 6 6 6"/></svg>'
ic={
'squid':'<path d="M32 4c-8 8-12 16-12 26h24C44 20 40 12 32 4Z"/><path d="M22 34v22M28 34v26M36 34v26M42 34v22"/><circle cx="28" cy="24" r="1.5"/><circle cx="36" cy="24" r="1.5"/>',
'bulb':'<path d="M22 40c-6-4-8-9-8-14a18 18 0 0 1 36 0c0 5-2 10-8 14v6H22z"/><path d="M24 54h16M27 60h10"/>',
'rod':'<path d="M8 56 48 8"/><path d="M48 8c8 4 8 16 4 24"/><circle cx="52" cy="38" r="3"/>',
'fish':'<path d="M6 32c10-14 28-14 38 0-10 14-28 14-38 0Z"/><path d="M44 32l14-10v20z"/><circle cx="18" cy="29" r="1.5"/>',
'shell':'<path d="M32 56 8 28c0-14 10-22 24-22s24 8 24 22z"/><path d="M32 56V8M20 50 14 22M44 50l6-28"/>',
'drop':'<path d="M32 6C20 22 14 30 14 40a18 18 0 0 0 36 0c0-10-6-18-18-34Z"/><path d="M26 42l5 6 8-12"/>',
'chip':'<rect x="16" y="16" width="32" height="32" rx="3"/><path d="M24 8v8M32 8v8M40 8v8M24 48v8M32 48v8M40 48v8M8 24h8M8 32h8M8 40h8M48 24h8M48 32h8M48 40h8"/><rect x="26" y="26" width="12" height="12"/>',
'box':'<path d="M32 6 54 18v28L32 58 10 46V18z"/><path d="M10 18l22 12 22-12M32 30v28"/>'}
def icon(k): return '<svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round">%s</svg>'%ic[k]
def art(kind):
    if kind==1: # lamp row over waves
        s=''.join('<circle cx="%d" cy="%d" r="%d" fill="#fff3d0" opacity=".9"/><circle cx="%d" cy="%d" r="%d" fill="#ffe0a0" opacity=".16"/>'%(40+i*52,150,3,40+i*52,150,22) for i in range(7))
        w=''.join('<path d="M0 %d q50 -18 100 0 t100 0 100 0 100 0 100 0" fill="none" stroke="#fff" stroke-opacity="%s" stroke-width="1.5" transform="translate(-20 0)"/>'%(170+k*22,.35-k*.06) for k in range(6))
        return '<svg class="art" viewBox="0 0 400 500" preserveAspectRatio="xMidYMid slice">%s%s</svg>'%(s,w)
    if kind==2: # concentric
        return '<svg class="art" viewBox="0 0 400 500" preserveAspectRatio="xMidYMid slice"><g fill="none" stroke="#fff" stroke-opacity=".22">%s</g></svg>'%''.join('<circle cx="200" cy="170" r="%d"/>'%(30+i*30) for i in range(8))
    return '<svg class="art" viewBox="0 0 400 500" preserveAspectRatio="xMidYMid slice"><g fill="none" stroke="#fff" stroke-opacity=".22">%s</g></svg>'%''.join('<path d="M0 %d H400 M%d 0 V500"/>'%(i*50,i*50) for i in range(1,10))

# ---------- index ----------
word=''.join('<span style="--i:%d">%s</span>'%(i,c) for i,c in enumerate('HAMADE'))
P=[('自動イカ釣機','世界トップシェアの自動イカ釣機。手巻き式から全自動、マイコン制御へ進化してきました。','squid','世界トップシェア'),
('照明（漁灯）','LED漁灯をはじめ、イカ・サンマ漁に最適化した照明をご提供します。','bulb',''),
('一本釣り機器','マグロなどの一本釣りを支える、軽量で信頼性の高い機器。','rod',''),
('魚釣り機器','イカ・魚釣機の技術を活かした、各種魚釣り機器をラインアップ。','fish',''),
('ホタテ養殖機器','穴あけ・結束・カゴ洗浄まで、養殖現場の作業を自動化します。','shell',''),
('海水電解装置','海水から殺菌水を生成。水産・食品現場の衛生を支えます。','drop',''),
('EMS事業','電子基板の製造・実装。長年の制御技術を活かした受託事業。','chip','NEW'),
('関連資材','オモリ、ドラム、制御ユニットなど、現場に必要な関連資材。','box','')]
vc=''.join('<article class="v-card"><div class="v-ico">%s</div><h3>%s</h3><p>%s</p>%s</article>'%(icon(k),t,d,'<span class="tag">%s</span>'%tg if tg else '') for t,d,k,tg in P)
hl=''
for e in D:
    y,j,items=e[0],e[1],e[2]
    fl='<span class="flag">%s</span>'%e[3] if len(e)>3 else ''
    body=''.join('<li>%s%s</li>'%('<span class="flag">受賞</span>' if i[0]=='*' else '',i.lstrip('*')) for i in items)
    if fl: body=body.replace('<li>','<li>'+fl,1)
    hl+='<li class="his-item" data-y="%d"><time>%d</time><ul>%s</ul></li>'%(y,y,body)
news=''.join('<a href="#"><time>%s</time><span class="flag">%s</span><span>%s</span><span>→</span></a>'%x for x in [('2026.06.24','EMS','電子回路基板の製造・実装 EMS事業のお知らせ'),('2026.04.30','重要','中東情勢に伴う供給制限のお知らせ'),('2026.03.31','製品','漁灯製品のアップデート情報'),('2026.01.01','お知らせ','新年のご挨拶・2026年カレンダー更新')])

idx=head%('HAMADE | 株式会社 東和電機製作所','')+'''
<section class="hero" id="hero" aria-label="東和電機製作所">
<div class="hero-stick">
<div class="hero-media" id="heroMedia"><video id="heroVideo" src="video.mp4" autoplay muted loop playsinline preload="auto" aria-hidden="true"></video></div>
<h1 class="hero-word" id="heroWord" aria-label="HAMADE">WORD</h1>
<div class="hero-meta" id="heroMeta"><p>自動イカ釣機で世界トップシェア</p>
<div class="chips"><span class="chip brand">#世界トップシェア</span><span class="chip">#自動イカ釣機</span><span class="chip">#LED漁灯</span><span class="chip">#EMS事業</span></div></div>
<div class="hero-caption" id="heroCap"><p class="q">海を照らし、漁を支える。<br><em>創造的改革</em>へ。<small>Creative innovation &amp; Renovation.</small></p></div>
<div class="scroll-cue" aria-hidden="true">SCROLL<i></i></div>
</div></section>

<div class="chapters" id="about">
<section class="chapter"><div class="ch-stick" aria-hidden="true"><div class="ch-word">Since 1963</div></div>
<div class="ch-body"><div class="wrap ch-grid">
<div class="ch-head"><p class="eyebrow">About</p><h2>60年、海とともに</h2><p>手巻き式イカ釣機から始まった、ものづくりの物語</p></div>
<div class="ch-card g1">ART1<div class="stat"><b>1963</b><span>会社設立 ／ 1968年 手巻き式イカ釣機を発売</span></div></div>
</div></div></section>
<section class="chapter flip"><div class="ch-stick" aria-hidden="true"><div class="ch-word ko">自動イカ釣機</div></div>
<div class="ch-body"><div class="wrap ch-grid">
<div class="ch-head"><p class="eyebrow">Squid Fishing Machines</p><h2>全自動化、マイコン制御、<br>そして世界トップシェアへ</h2><p>1970年の全自動イカ釣機から、進化は止まりません</p></div>
<div class="ch-card g2">ART2<div class="stat"><b>9,100台</b><span>1973年 販売突破 ／ 全漁連・八戸漁連指定品に認定</span></div></div>
</div></div></section>
<section class="chapter"><div class="ch-stick" aria-hidden="true"><div class="ch-word">Beyond</div></div>
<div class="ch-body"><div class="wrap ch-grid">
<div class="ch-head"><p class="eyebrow">Business</p><h2>海から、陸へ。<br>広がる事業領域</h2><p>ホタテ養殖・海水電解・EMS、そして九州事業部の新設</p></div>
<div class="ch-card g3">ART3<div class="stat"><b>8分野</b><span>イカ釣機から電子基板のEMSまで</span></div></div>
</div></div></section>
</div>

<section class="message"><div class="wrap msg-grid">
<div class="msg-title"><span class="qm" aria-hidden="true">“</span><h2>創造的改革へ。</h2></div>
<div class="msg-body" id="msgBody">
<p class="sm">株式会社 東和電機製作所 ／ HAMADE</p>
<p>私たちは、自動イカ釣機の分野で世界トップのシェアを持つ、北海道のものづくり企業です。</p>
<p>1963年の創業以来、現場の漁師の声に耳を傾け、手巻き式から全自動、マイコン制御、LED漁灯へと技術を磨いてきました。</p>
<p>イカ釣機で培った制御技術は、ホタテ養殖機器、海水電解装置、電子基板のEMS事業へと広がっています。</p>
<p>2025年には九州事業部を新設。これからも変わり続けることを恐れず、海と産業の未来に挑みます。</p>
<p class="closing">創造的改革へ。<br><em>HAMADE</em>は、挑戦を続けます。</p>
</div></div></section>

<section class="numbers"><div class="wrap">
<p class="eyebrow">HAMADE in numbers</p>
<h2 style="margin-top:14px">数字で見るHAMADE<br><span>海とともに、歩み続けています</span></h2>
<dl class="num-grid">
<div class="num"><dt>創業</dt><dd><span data-count="1963" data-plain="1">0</span><small>年</small></dd></div>
<div class="num"><dt>イカ釣機 販売実績（1973年時点）</dt><dd><span data-count="9100">0</span><small>台</small></dd></div>
<div class="num"><dt>ものづくりの歴史</dt><dd><span data-count="62">0</span><small>年</small></dd></div>
<div class="num"><dt>事業領域</dt><dd><span data-count="8">0</span><small>分野</small></dd></div>
</dl>
<div class="badge-row"><span class="chip">グローバルニッチトップ企業100選 <b>受賞</b></span><span class="chip">今年のロボット大賞 <b>受賞</b></span><span class="chip">社長 旭日双光章 <b>受章</b></span><span class="chip">自動イカ釣機 <b>世界トップシェア</b></span></div>
</div></section>

<section class="values" id="products"><div class="wrap val-head"><div><p class="eyebrow">Products</p>
<h2 style="margin-top:14px">海の現場のために、<br>8つの分野で挑みます</h2></div>
<div class="arrows"><button id="prev" aria-label="前へ">ARL</button><button id="next" aria-label="次へ">ARR</button></div></div>
<div class="track" id="track">VC</div></section>

<section class="history"><div class="wrap his-grid">
<aside class="his-aside"><h2>HAMADEが歩んできた道</h2><div class="his-year" id="hisYear" aria-hidden="true"></div>
<div class="his-era" id="hisEra"></div><div class="his-progress" aria-hidden="true"><i id="hisBar"></i></div>
<a class="pill" href="history.html" style="margin-top:28px">年表ページへ</a></aside>
<ol class="his-list">HL</ol></div></section>

<section class="panels" id="panels" aria-label="ショートカット">
<a class="panel active" href="#products"><div class="bg b1"></div><div class="p-in"><span class="p-label">製品情報</span><p class="p-title">8つの分野の製品ラインアップ</p><span class="p-go">製品を見る <i>→</i></span></div></a>
<a class="panel" href="history.html"><div class="bg b2"></div><div class="p-in"><span class="p-label">HAMADEの歴史</span><p class="p-title">1963年から続く挑戦の年表</p><span class="p-go">年表を見る <i>→</i></span></div></a>
<a class="panel" href="#about"><div class="bg b3"></div><div class="p-in"><span class="p-label">会社情報</span><p class="p-title">企業理念と会社概要</p><span class="p-go">会社を知る <i>→</i></span></div></a>
<a class="panel" href="#"><div class="bg b4"></div><div class="p-in"><span class="p-label">採用情報</span><p class="p-title">世界トップのものづくりを、一緒に</p><span class="p-go">採用情報へ <i>→</i></span></div></a>
<a class="panel" href="#"><div class="bg b5"></div><div class="p-in"><span class="p-label">お問い合わせ</span><p class="p-title">製品・導入のご相談はこちら</p><span class="p-go">問い合わせる <i>→</i></span></div></a>
</section>

<section class="news" id="news"><div class="wrap"><p class="eyebrow">News</p><h2>お知らせ</h2><div class="news-list">NEWS</div></div></section>
'''+foot
idx=idx.replace('WORD',word).replace('ART1',art(1)).replace('ART2',art(2)).replace('ART3',art(3)).replace('ARL',arl).replace('ARR',arr).replace('VC',vc).replace('HL',hl).replace('NEWS',news)

# ---------- history ----------
decs=[(1960,'1960s','創業と手巻き式の時代'),(1970,'1970s','全自動化と事業拡大'),(1980,'1980s','マイコン制御の時代'),(1990,'1990s','技術革新と受賞'),(2000,'2000s','LEDと海水電解への挑戦'),(2010,'2010s','世界へ、そして継承'),(2020,'2020s','新たな航海')]
hw=''.join('<span style="--i:%d">%s</span>'%(i,c) for i,c in enumerate('History'))
ch=''
for n,(d,lab,t) in enumerate(decs):
    its=[e for e in D if d<=e[0]<d+10]
    aw=sum(1 for e in its for i in e[2] if i[0]=='*')
    rows=''
    for e in its:
        fl='<span class="flag">%s</span>'%e[3] if len(e)>3 else ''
        body=''.join('<li>%s%s</li>'%('<span class="flag">受賞</span>' if i[0]=='*' else '',i.lstrip('*')) for i in e[2])
        if fl: body=body.replace('<li>','<li>'+fl,1)
        rows+='<li class="era-item"><time>%d</time><ul>%s<li style="color:var(--muted);font-size:13px">%s</li></ul></li>'%(e[0],body,e[1])
    ch+='''<section class="chapter"><div class="ch-stick" aria-hidden="true"><div class="ch-word">%s</div></div>
<div class="ch-body hist"><div class="wrap hist-grid"><div class="ch-head"><p class="eyebrow">%s</p><h2>%s</h2><p>%d件の出来事%s</p></div>
<ol class="era-list">%s</ol></div></div></section>'''%(lab,lab,t,len(its),'（うち受賞 %d）'%aw if aw else '',rows)
hist=head%('HAMADEの歴史｜株式会社 東和電機製作所','aria-current="page"')+'''
<section class="ph"><div class="crumb"><a href="index.html">トップ</a><i>›</i><a href="index.html#about">会社情報</a><i>›</i>HAMADEの歴史</div>
<div><h1 aria-label="History">HW</h1><p>1963年の創業から現在まで。技術と挑戦の歩み。</p>
<div class="chips"><span class="chip brand">#1963–2025</span><span class="chip">#全40の出来事</span><span class="chip">#受賞8件</span></div></div></section>
<div class="chapters">CH</div>
<section class="numbers" style="border:0;padding-top:0"><div class="wrap"><a class="pill" href="index.html">← トップへ戻る</a></div></section>
'''.replace('HW',hw).replace('CH',ch)+foot

css=open('ref.css').read();js=open('ref.js').read()
for f,h in(('index.html',idx),('history.html',hist)):
    open(f,'w').write(h.replace('<style>CSS</style>','<style>'+css+'</style>').replace('<script>JS</script>','<script>'+js+'</script>'))
