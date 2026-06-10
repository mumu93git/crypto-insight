"""
Hermes 内容工厂 - 自动生成SEO文章，赚广告费
策略: 长尾关键词 -> AI生成 -> 部署 -> AdSense -> 被动收入
"""
import os
import json
import random
from datetime import datetime

# Google AdSense
ADSENSE_CLIENT = "ca-pub-0000000000000000"
ADSENSE_SLOT_IN_ARTICLE = "0000000000"

ARTICLES_DIR = os.path.join(os.path.dirname(__file__), 'articles')

KEYWORDS = [
    "比特币还会涨吗", "以太坊2026价格预测", "加密货币新手入门",
    "币安合约交易教程", "BTC技术分析", "加密货币避税",
    "DeFi挖矿教程", "NFT怎么买", "Solana生态项目",
    "加密货币安全钱包推荐", "网格交易策略", "ETH gas费优化",
    "加密货币空投攻略", "Web3入门教程", "比特币减半影响分析",
]

TITLE_MAP = {
    "比特币还会涨吗": "2026年比特币(BTC)价格走势深度分析：还会继续上涨吗？",
    "以太坊2026价格预测": "以太坊(ETH)2026年价格预测：技术面+基本面全面解析",
    "加密货币新手入门": "2026年加密货币新手完全入门指南（从零到交易）",
    "币安合约交易教程": "币安合约交易完全指南：杠杆、保证金、风控策略",
    "BTC技术分析": "BTC技术分析入门：K线、均线、MACD全解析",
    "加密货币避税": "加密货币税务规划策略：合法优化你的税务负担",
    "DeFi挖矿教程": "DeFi流动性挖矿指南：如何在去中心化金融中赚取收益",
    "NFT怎么买": "NFT购买完全指南：从创建钱包到收藏第一件数字艺术品",
    "Solana生态项目": "Solana生态十大潜力项目盘点：2026年投资机会",
    "加密货币安全钱包推荐": "加密货币钱包安全排行：保护你的数字资产",
    "网格交易策略": "网格交易策略详解：震荡市中的稳健盈利方法",
    "ETH gas费优化": "以太坊Gas费优化技巧：如何节省90%的交易费用",
    "加密货币空投攻略": "加密货币空投获取指南：识别优质项目，免费领取代币",
    "Web3入门教程": "Web3概念与应用：下一代互联网的入门指南",
    "比特币减半影响分析": "比特币减半对市场的影响：历史回测与2026年展望",
    "比特币ETF最新消息": "比特币ETF最新进展：机构资金流入对价格的影响分析",
    "以太坊Layer2扩容方案": "以太坊Layer2扩容方案对比：Arbitrum vs Optimism vs zkSync",
    "加密货币定投策略": "加密货币定投(DCA)策略：熊市建仓牛市收获的最佳方式",
    "DePIN项目投资指南": "DePIN赛道深度分析：去中心化物理基础设施的投资机会",
    "AI概念币投资分析": "AI+区块链概念币全面分析：2026年哪些项目值得关注",
    "RWA赛道深度解析": "RWA(真实世界资产)代币化：万亿级市场的投资机会",
    "Meme币交易策略": "Meme币交易策略：如何捕捉百倍币而不被套牢",
    "比特币链上数据分析": "比特币链上数据分析：巨鲸动向、交易所流量与市场情绪",
    "稳定币理财攻略": "稳定币理财攻略：USDT/USDC年化收益最大化策略",
    "Restaking质押策略": "EigenLayer Restaking详解：以太坊质押收益翻倍攻略",
    "GameFi游戏打金教程": "2026年GameFi链游打金指南：值得投入时间的区块链游戏",
    "BRC20代币入门": "BRC20代币与Ordinals协议：比特币生态的新革命",
    "Perps去中心化合约": "去中心化永续合约交易平台对比：dYdX vs GMX vs Synthetix",
    "Inscription铭文市场": "铭文(Inscription)市场分析：比特币生态的NFT新范式",
    "Pendle收益策略": "Pendle Finance收益策略：未来收益代币化的掘金机会",
    "EigenLayer生态项目": "EigenLayer生态全景：再质押赛道的主流项目盘点",
}

ARTICLE_HEAD = """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="google-site-verification" content="_UJqwOqD7KQXT5DvneoA-kQzpIE4isR8apvX6sOF1Vo" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="[{TITLE}] - 专业的加密货币分析和交易指南">
    <meta name="keywords" content="{KEYWORD},加密货币,比特币,交易,投资">
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={AD_CLIENT}" crossorigin="anonymous"></script>
    <title>{TITLE}</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; line-height: 1.8; color: #333; max-width: 800px; margin: 0 auto; padding: 20px; background: #fafafa; }}
        header {{ text-align: center; padding: 40px 0; border-bottom: 3px solid #f0b90b; margin-bottom: 30px; }}
        h1 {{ font-size: 2em; color: #1a1a1a; }}
        h2 {{ font-size: 1.4em; color: #2a2a2a; margin: 30px 0 15px 0; padding-bottom: 10px; border-bottom: 1px solid #eee; }}
        p {{ margin: 15px 0; }}
        ul, ol {{ margin: 15px 0 15px 30px; }}
        li {{ margin: 8px 0; }}
        strong {{ color: #f0b90b; }}
        .meta {{ color: #888; font-size: 0.9em; margin-top: 10px; }}
        .disclaimer {{ background: #fff3cd; padding: 15px; border-radius: 8px; margin-top: 40px; font-size: 0.9em; color: #856404; }}
        .cta {{ background: linear-gradient(135deg, #f0b90b, #f8d33a); color: #1a1a1a; padding: 20px; border-radius: 12px; text-align: center; margin: 40px 0; }}
        .cta a {{ color: #1a1a1a; font-weight: bold; font-size: 1.2em; text-decoration: none; }}
        .related {{ background: white; padding: 20px; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); margin: 30px 0; }}
        .related h2 {{ font-size: 1.2em; margin-top: 0; }}
        .related li {{ margin: 10px 0; }}
        .related a {{ color: #2a7de1; text-decoration: none; }}
        .related a:hover {{ text-decoration: underline; }}
        .ad-container {{ text-align: center; margin: 30px 0; padding: 10px 0; min-height: 90px; }}
        nav {{ margin: 20px 0; }}
        nav a {{ color: #f0b90b; text-decoration: none; margin-right: 15px; }}
        footer {{ text-align: center; padding: 30px 0; color: #888; border-top: 1px solid #eee; margin-top: 40px; }}
    </style>
</head>
<body>
    <nav>
        <a href="../index.html">首页</a>
        <a href="../sitemap.html">全部文章</a>
    </nav>
    <header>
        <h1>{TITLE}</h1>
        <p class="meta">发布时间: {DATE} | 分类: 加密货币分析</p>
    </header>
    <main>
        {BODY}
    </main>
    <div class="ad-container">
        <ins class="adsbygoogle"
             style="display:block"
             data-ad-client="{AD_CLIENT}"
             data-ad-slot="{AD_SLOT}"
             data-ad-format="auto"
             data-full-width-responsive="true"></ins>
        <script>(adsbygoogle = window.adsbygoogle || []).push({});</script>
    </div>
    <div class="cta">
        <p>获取实时交易信号？</p>
        <a href="../signal.html">了解 Q系统 智能交易信号服务</a>
    </div>
    <div class="disclaimer">
        *免责声明：本文仅供信息参考，不构成投资建议。
    </div>
    <footer>
        <p>(c) 2026 CryptoInsight - 专业的加密货币分析平台</p>
    </footer>
</body>
</html>
"""


def render_article(keyword, date, title, body_lines, client, slot, related_html):
    """用模板渲染文章HTML"""
    body = []
    for line in body_lines:
        if not line:
            body.append('<br>')
        elif line.startswith('## '):
            body.append('<h2>' + line[3:] + '</h2>')
        elif line.startswith('- '):
            body.append('<li>' + line[2:] + '</li>')
        elif line[0].isdigit() and '. ' in line[:4]:
            body.append('<li>' + line + '</li>')
        else:
            body.append('<p>' + line + '</p>')
    body_html = ''.join(body) + related_html

    tpl = ARTICLE_HEAD
    tpl = tpl.replace('{TITLE}', title)
    tpl = tpl.replace('{KEYWORD}', keyword)
    tpl = tpl.replace('{DATE}', date)
    tpl = tpl.replace('{AD_CLIENT}', client)
    tpl = tpl.replace('{AD_SLOT}', slot)
    tpl = tpl.replace('{BODY}', body_html)
    return tpl


def get_all_articles():
    arts = []
    if not os.path.exists(ARTICLES_DIR):
        return arts
    for f in sorted(os.listdir(ARTICLES_DIR)):
        if f.endswith('.html') and f.startswith('article-'):
            parts = f.split('-', 2)
            if len(parts) >= 3:
                kw = os.path.splitext(parts[2])[0]
                arts.append({'file': f, 'keyword': kw})
    return arts


def get_related(current_file, count=5):
    others = [a for a in get_all_articles() if a['file'] != current_file]
    random.shuffle(others)
    return others[:count]


def generate_article(keyword, index):
    now = datetime.now().strftime("%Y-%m-%d")
    title = TITLE_MAP.get(keyword, keyword + " - 完整解析与指南")
    filename = "article-{:03d}-{}.html".format(index, keyword.replace(' ', '-'))

    content_map = {
        "比特币还会涨吗": [
            "## 市场背景",
            "截至{}, 比特币(BTC)价格在经历周期波动后面临多重因素交织。".format(now),
            "",
            "## 技术面分析",
            "从技术指标看BTC的200日均线呈现上行趋势MACD指标金叉信号已经出现。",
            "RSI指标处于50-70区间表明市场处于健康的中性偏多状态。",
        ],
        "比特币ETF最新消息": [
            "## 比特币ETF最新进展",
            "截至{}比特币现货ETF市场持续壮大管理资产规模突破新高。".format(now),
            "",
            "## 主要ETF产品对比",
            "BlackRock iShares Bitcoin Trust (IBIT): 管理资产规模最大日均交易量领先",
            "Fidelity Wise Origin Bitcoin Fund (FBTC): 费用率最低的比特币ETF之一",
            "Grayscale Bitcoin Trust (GBTC): 转型为ETF后资金流出压力缓解",
            "",
            "## 机构资金流入对价格的影响",
            "比特币ETF获批后机构资金持续流入每净流入10亿美元BTC价格平均上涨3-5%。",
        ],
        "以太坊Layer2扩容方案": [
            "## Layer2扩容方案概述",
            "以太坊Layer2是提升网络吞吐量降低交易费用的关键技术。",
            "",
            "## Arbitrum",
            "采用Optimistic Rollup技术EVM完全兼容生态丰富头部DeFi协议均已部署。",
            "",
            "## Optimism",
            "OP Stack开源框架降低了构建L2的门槛Base等知名L2均基于OP Stack。",
            "",
            "## zkSync",
            "采用ZK-Rollup技术零知识证明确保安全提款无需等待期。",
        ],
    }

    body = content_map.get(keyword, [
        "## " + keyword,
        "本文深入探讨" + keyword + "相关信息帮助读者全面了解。",
        "",
        "## 核心要点",
        "1. " + keyword + "的基础概念与运作机制",
        "2. 当前市场趋势与最新发展",
        "3. 实用操作指南与最佳实践",
        "4. 风险评估与注意事项",
        "",
        "## 详细分析",
        "在当前的加密货币市场中" + keyword + "是一个备受关注的话题。",
        "无论是新手还是老手都需要对这一领域有深入理解。",
    ])

    related = get_related(filename, 6)
    rel_html = ""
    if related:
        rel_html = '<div class="related"><h2>相关文章</h2><ul>'
        for r in related:
            rt = TITLE_MAP.get(r['keyword'], r['keyword'])
            rel_html += '<li><a href="{}">{}</a></li>'.format(r['file'], rt)
        rel_html += '</ul></div>'

    html = render_article(keyword, now, title, body, ADSENSE_CLIENT, ADSENSE_SLOT_IN_ARTICLE, rel_html)
    os.makedirs(ARTICLES_DIR, exist_ok=True)
    filepath = os.path.join(ARTICLES_DIR, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    return filename


def generate_site():
    os.makedirs(ARTICLES_DIR, exist_ok=True)
    arts = []
    for i, kw in enumerate(KEYWORDS, 1):
        fn = generate_article(kw, i)
        arts.append({'keyword': kw, 'file': fn})
        print("  [{}/{}] {}".format(i, len(KEYWORDS), kw))

    idx_html = make_index(arts)
    with open(os.path.join(os.path.dirname(ARTICLES_DIR), 'index.html'), 'w', encoding='utf-8') as f:
        f.write(idx_html)

    sm_html = make_sitemap(arts)
    with open(os.path.join(os.path.dirname(ARTICLES_DIR), 'sitemap.html'), 'w', encoding='utf-8') as f:
        f.write(sm_html)

    sm_xml = make_xml_sitemap(arts)
    with open(os.path.join(os.path.dirname(ARTICLES_DIR), 'sitemap.xml'), 'w', encoding='utf-8') as f:
        f.write(sm_xml)

    print("\n网站已生成: {}篇文章".format(len(arts)))


def make_index(arts):
    links = '\n'.join(
        '<li><a href="articles/{}">{}</a></li>'.format(a['file'], TITLE_MAP.get(a['keyword'], a['keyword']))
        for a in arts
    )
    return """<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="google-site-verification" content="_UJqwOqD7KQXT5DvneoA-kQzpIE4isR8apvX6sOF1Vo" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CryptoInsight - 加密货币专业分析</title>
    <meta name="description" content="CryptoInsight提供专业的加密货币分析、交易策略和市场洞察">
    <meta name="keywords" content="加密货币,比特币,以太坊,交易策略,投资指南">
    <link rel="canonical" href="https://mumu93git.github.io/crypto-insight/">
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=""" + ADSENSE_CLIENT + """" crossorigin="anonymous"></script>
    <style>
        * { margin:0; padding:0; box-sizing:border-box; }
        body { font-family:-apple-system,sans-serif; max-width:800px; margin:0 auto; padding:20px; background:#fafafa; }
        h1 { text-align:center; padding:30px; color:#1a1a1a; }
        ul { list-style:none; }
        li { padding:15px; margin:8px 0; background:white; border-radius:8px; box-shadow:0 2px 8px rgba(0,0,0,0.06); }
        a { color:#f0b90b; text-decoration:none; font-size:1.1em; }
        a:hover { text-decoration:underline; }
        .hero { background:linear-gradient(135deg,#1a1a2e,#16213e); color:white; padding:60px 20px; text-align:center; border-radius:16px; margin-bottom:30px; }
        .hero h1 { color:white; font-size:2.5em; }
        .hero p { font-size:1.2em; opacity:0.8; margin-top:10px; }
        .article-count { text-align:center; color:#888; margin-bottom:20px; }
    </style>
</head>
<body>
    <div class="hero">
        <h1>CryptoInsight</h1>
        <p>专业的加密货币分析平台 | 深度研究 | 交易策略</p>
    </div>
    <h2>最新文章 (""" + str(len(arts)) + """篇)</h2>
    <p class="article-count">持续更新中涵盖比特币以太坊DeFi NFT等热门话题</p>
    <ul>""" + links + """</ul>
</body>
</html>"""


def make_sitemap(arts):
    links = '\n'.join(
        '<li><a href="articles/{}">{}</a></li>'.format(a['file'], TITLE_MAP.get(a['keyword'], a['keyword']))
        for a in arts
    )
    return "<html><head><meta charset='UTF-8'><title>站点地图</title></head><body><h1>全部文章</h1><ul>" + links + "</ul></body></html>"


def make_xml_sitemap(arts):
    base = 'https://mumu93git.github.io/crypto-insight'
    urls = '  <url><loc>{}/</loc><priority>1.0</priority></url>\n'.format(base)
    for a in arts:
        urls += '  <url><loc>{}/articles/{}</loc><priority>0.8</priority></url>\n'.format(base, a['file'])
    return '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + urls + '</urlset>'


if __name__ == '__main__':
    generate_site()
