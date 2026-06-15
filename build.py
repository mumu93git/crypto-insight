"""
Hermes 内容工厂 - 自动生成SEO文章
策略: 长尾关键词 -> AI生成 -> 部署 -> 搜索流量 -> 引流变现
"""
import os
import json
import random
from datetime import datetime

# ====== 配置 ======
ADSENSE_CLIENT = "ca-pub-0000000000000000"
ADSENSE_SLOT_IN_ARTICLE = "0000000000"
SITE_URL = "https://mumu93git.github.io/crypto-insight"
SITE_NAME = "CryptoInsight - 加密货币专业分析"

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
}

# ====== 长篇文章内容模板 ======
CONTENT_MAP = {
    "比特币还会涨吗": [
        "## 市场背景",
        "截至2026年6月，比特币(BTC)价格在经历周期波动后，正面临多重因素交织的关键节点。全球宏观经济环境、机构资金的持续流入、以及减半后的供给端变化，共同构成了当前市场的基本面。",
        "",
        "## 技术面深度分析",
        "从技术指标来看，比特币的200日均线(MA200)仍然呈现稳健的上行趋势，这是长期牛市的典型特征。同时，MACD指标在周线级别已经出现金叉信号，表明中期动能正在转向积极。",
        "RSI指标目前在50-70区间运行，表明市场处于健康的中性偏多状态，既没有过热也没有超卖。这个位置通常被认为是趋势延续的信号。",
        "值得注意的是，比特币的布林带(Bollinger Bands)正在收窄，这往往预示着即将出现较大的方向性突破。根据历史数据，布林带收窄后的突破通常伴随着20%以上的单边行情。",
        "",
        "## 链上数据验证",
        "交易所的BTC余额持续下降，目前已经创下2018年以来的新低。这说明越来越多的投资者选择将BTC转入自托管钱包，减少了市场的潜在抛压。",
        "巨鲸地址(持有1000+ BTC)的数量在过去30天内增加了12%，表明大户正在积累。历史数据表明，巨鲸积累阶段往往出现在大行情启动之前。",
        "",
        "## 机构资金流向",
        "比特币现货ETF的资金流入是当前最重要的价格驱动因素。当ETF日净流入超过2亿美元时，BTC价格在随后7天内平均上涨5-8%。",
        "MicroStrategy等上市公司仍在持续增持BTC。目前MicroStrategy持有超过50万枚BTC，其持续的购买行为为市场提供了坚实的需求支撑。",
        "",
        "## 2026年下半年展望",
        "综合技术面、链上数据和机构资金流向三个维度，比特币在2026年下半年有望延续上行趋势。但需要注意以下风险因素：美联储政策转向、监管变化、以及地缘政治风险。",
        "对于普通投资者而言，采用定投(DCA)策略分批建仓，设置合理的止损位，比试图预测短期涨跌更稳妥。",
    ],
    "比特币ETF最新消息": [
        "## 比特币ETF市场最新概况",
        "截至2026年6月，美国比特币现货ETF市场持续壮大，管理资产规模(AUM)已经突破1500亿美元。各大ETF产品的竞争日趋激烈，费率持续下降。",
        "",
        "## 主要ETF产品对比分析",
        "BlackRock iShares Bitcoin Trust (IBIT): 管理资产规模最大，日均交易量超过20亿美元，费用率0.25%。",
        "Fidelity Wise Origin Bitcoin Fund (FBTC): 费用率仅0.12%，是市场上最便宜的比特币ETF之一，吸引了大量长期持有者。",
        "Grayscale Bitcoin Trust (GBTC): 转型为现货ETF后资金流出压力显著缓解，但其0.75%的费用率仍高于竞争对手。",
        "ARK 21Shares Bitcoin ETF (ARKB): 由Cathie Wood的ARK Invest管理，主打创新投资者群体。",
        "",
        "## 机构资金流入对价格的影响机制",
        "比特币ETF为机构投资者提供了合规、便捷的BTC配置通道。数据显示，ETF每净流入10亿美元，BTC价格在短期内平均上涨3-5%。",
        "更重要的是，ETF资金流入具有明显的趋势性。连续多日的净流入往往会强化市场信心，引发更多FOMO资金入场。",
        "",
        "## 对比特币市场的结构性影响",
        "ETF的推出从根本上改变了比特币的市场结构。过去，BTC价格主要由零售投资者和交易所资金驱动；现在，机构资金通过ETF渠道参与，使得市场更加稳定和成熟。",
        "ETF还引入了做市商机制，提高了BTC的流动性和价格发现效率。比特币的买卖价差显著收窄，日内波动率也有所降低。",
        "",
        "## 投资建议",
        "对于看好比特币长期前景的投资者，定期定额买入低成本ETF(如FBTC)是一个有效的配置策略。同时需要关注：ETF资金流向变化、监管政策更新、以及宏观经济环境。",
    ],
    "以太坊Layer2扩容方案": [
        "## 为什么需要Layer2扩容？",
        "以太坊主网的处理能力有限，在高峰期Gas费用可能高达数百美元。Layer2扩容方案通过在链下处理交易，大幅降低了费用并提升了吞吐量。",
        "",
        "## Arbitrum: 生态最成熟的Optimistic Rollup",
        "Arbitrum采用Optimistic Rollup技术，完全兼容EVM，这意味着现有的以太坊应用可以无缝迁移。其生态已涵盖Uniswap、Aave、Curve等头部DeFi协议。",
        "目前Arbitrum的TVL(总锁仓价值)超过50亿美元，是最大的以太坊Layer2网络。其原生代币ARB用于治理，持有者可以参与协议决策。",
        "",
        "## Optimism: 开源框架驱动生态扩张",
        "Optimism同样采用Optimistic Rollup技术，但其最大的创新是OP Stack开源框架。Coinbase的Base网络就是基于OP Stack构建的。",
        "OP Stack使得任何团队都可以快速启动自己的Layer2网络，极大地扩展了以太坊的生态版图。Optimism的原生代币OP用于治理和生态激励。",
        "",
        "## zkSync: ZK-Rollup的技术先锋",
        "zkSync采用ZK-Rollup(零知识证明)技术，具有更高的安全性和更快的最终确认时间。与Optimistic Rollup不同，ZK-Rollup不需要7天的提款等待期。",
        "zkSync Era主网上线以来生态发展迅速，特别是在支付和NFT领域表现突出。其原生代币ZK用于治理和网络费用。",
        "",
        "## Layer2赛道2026年展望",
        "随着EIP-4844(Proto-Danksharding)的实施，Layer2的费用进一步降低。预计到2026年底，超过90%的以太坊交易将在Layer2上完成。",
        "对于用户来说，选择合适的Layer2需要考虑：生态丰富度、安全性、提款速度、以及跨链桥的便利性。建议优先选择经过时间验证的主流方案。",
    ],
}

# ====== 生成文章描述 ======
def make_description(keyword, body_lines):
    """从文章内容中提取唯一的meta description"""
    for line in body_lines:
        if line.startswith('## '):
            continue
        line = line.strip()
        if len(line) > 15 and not line.startswith('<'):
            # 取第一段有实际内容的句子
            desc = line[:120].rstrip('，。,.')
            if len(desc) > 10:
                return desc + "..."
    return f"{TITLE_MAP.get(keyword, keyword)} - 专业的加密货币分析和交易指南"

# ====== 文章HTML模板 ======
def make_article_html(keyword, title, date, body_lines, client, slot, related_html, filename):
    """生成完整文章HTML，包含所有SEO标签"""
    desc = make_description(keyword, body_lines)
    article_url = f"{SITE_URL}/articles/{filename}"
    desc_escaped = desc.replace('"', "'")
    title_escaped = title.replace('"', "'")

    head = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="google-site-verification" content="_UJqwOqD7KQXT5DvneoA-kQzpIE4isR8apvX6sOF1Vo" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <!-- 基础SEO -->
    <title>{title_escaped}</title>
    <meta name="description" content="{desc_escaped}">
    <meta name="keywords" content="{keyword},加密货币,比特币,交易,投资,区块链">
    <link rel="canonical" href="{article_url}">

    <!-- Open Graph -->
    <meta property="og:type" content="article">
    <meta property="og:title" content="{title_escaped}">
    <meta property="og:description" content="{desc_escaped}">
    <meta property="og:url" content="{article_url}">
    <meta property="og:site_name" content="CryptoInsight">
    <meta property="og:locale" content="zh_CN">
    <meta property="og:image" content="{SITE_URL}/assets/og-default.png">

    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{title_escaped}">
    <meta name="twitter:description" content="{desc_escaped}">

    <!-- 文章元数据 -->
    <meta name="article:published_time" content="{date}T00:00:00+08:00">
    <meta name="article:author" content="CryptoInsight">
    <meta name="article:section" content="加密货币分析">

    <!-- JSON-LD结构化数据 -->
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": "{title_escaped}",
        "description": "{desc_escaped}",
        "datePublished": "{date}T00:00:00+08:00",
        "dateModified": "{date}T00:00:00+08:00",
        "author": {{
            "@type": "Person",
            "name": "CryptoInsight",
            "url": "{SITE_URL}"
        }},
        "publisher": {{
            "@type": "Organization",
            "name": "CryptoInsight",
            "url": "{SITE_URL}"
        }},
        "mainEntityOfPage": {{
            "@type": "WebPage",
            "@id": "{article_url}"
        }},
        "about": {{
            "@type": "Thing",
            "name": "{keyword}"
        }},
        "inLanguage": "zh-CN"
    }}
    </script>

    <!-- Breadcrumb结构化数据 -->
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {{"@type": "ListItem", "position": 1, "name": "首页", "item": "{SITE_URL}/"}},
            {{"@type": "ListItem", "position": 2, "name": "{title_escaped}", "item": "{article_url}"}}
        ]
    }}
    </script>

    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={client}" crossorigin="anonymous"></script>
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
        .cta-box {{ background: linear-gradient(135deg, #f0b90b, #f8d33a); color: #1a1a1a; padding: 25px; border-radius: 12px; text-align: center; margin: 40px 0; }}
        .cta-box h3 {{ margin-bottom: 10px; font-size: 1.3em; }}
        .cta-box p {{ margin: 8px 0; font-size: 1em; }}
        .cta-btn {{ display: inline-block; background: #1a1a2e; color: #f0b90b !important; padding: 12px 30px; border-radius: 8px; font-weight: bold; font-size: 1.1em; text-decoration: none; margin-top: 10px; }}
        .cta-btn:hover {{ background: #16213e; }}
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
        <a href="../index.html">🏠 首页</a>
        <a href="../sitemap.html">📚 全部文章</a>
        <a href="../signal.html">📡 交易信号</a>
    </nav>
    <header>
        <h1>{title}</h1>
        <p class="meta">📅 {date} | 📂 加密货币分析 | ⏱ 约{max(3, len(body_lines)//5)}分钟阅读</p>
    </header>
    <main>
            {{BODY}}
        </main>
    <div class="ad-container">
        <ins class="adsbygoogle"
             style="display:block"
             data-ad-client="{client}"
             data-ad-slot="{slot}"
             data-ad-format="auto"
             data-full-width-responsive="true"></ins>
        <script>(adsbygoogle = window.adsbygoogle || []).push({{}});</script>
    </div>

    <!-- CTA区块：引导到付费信号 -->
    <div class="cta-box">
        <h3>📡 每日BTC实时信号推送</h3>
        <p>每天早8点，微信自动接收：<strong>买卖信号 + 止盈止损位 + 仓位建议</strong></p>
        <p>基于AI量化模型的实时分析，胜率公开可查</p>
        <a class="cta-btn" href="../signal.html">👀 了解详情</a>
        <p style="margin-top:12px;font-size:0.85em;opacity:0.7;">先免费体验3天 → 公众号「WxPusher消息推送」关注后联系客服</p>
    </div>

    <div class="disclaimer">
        ⚠️ 免责声明：本文仅供信息参考和学习交流，不构成任何投资建议。加密货币市场风险极高，投资需谨慎。请自行研究并承担风险。
    </div>
    <footer>
        <p>© 2026 CryptoInsight - 专业的加密货币分析平台 | <a href="../sitemap.html">站点地图</a></p>
    </footer>
</body>
</html>"""

    # 替换BODY占位符
    body = []
    for line in body_lines:
        if not line:
            body.append('<br>')
        elif line.startswith('## '):
            body.append(f'<h2>{line[3:]}</h2>')
        elif line.startswith('- '):
            body.append(f'<li>{line[2:]}</li>')
        elif line[0].isdigit() and '. ' in line[:4]:
            body.append(f'<li>{line}</li>')
        else:
            body.append(f'<p>{line}</p>')
    body_html = ''.join(body) + related_html
    # 注意: {BODY} 在head中是字面花括号，最终替换
    return head.replace('{BODY}', body_html)


def get_all_articles():
    """获取articles目录下所有文章"""
    arts = []
    if not os.path.exists(ARTICLES_DIR):
        return arts
    for f in sorted(os.listdir(ARTICLES_DIR)):
        if f.endswith('.html') and f.startswith('article-'):
            kw = os.path.splitext(f)[0]
            # 提取关键词：去掉article-XXX-前缀
            parts = kw.split('-', 2)
            kw_name = parts[2] if len(parts) >= 3 else parts[-1]
            arts.append({'file': f, 'keyword': kw_name})
    return arts


def get_related(current_file, count=6):
    """获取相关文章"""
    others = [a for a in get_all_articles() if a['file'] != current_file]
    random.shuffle(others)
    return others[:count]


def generate_article(keyword, index):
    """生成一篇完整文章"""
    now = datetime.now().strftime("%Y-%m-%d")
    title = TITLE_MAP.get(keyword, keyword + " - 完整解析与指南")
    filename = f"article-{index:03d}-{keyword}.html"

    # 优先使用预置内容，否则生成通用内容
    body = CONTENT_MAP.get(keyword, [
        f"## {keyword}概述",
        f"{keyword}是当前加密货币市场备受关注的话题。本文将从多个角度深入分析，帮助你全面理解这一领域。",
        "",
        "## 核心要点",
        f"在深入了解{keyword}之前，需要先掌握以下几个关键概念：",
        "1. 了解基础概念与运作机制",
        "2. 掌握当前市场趋势与最新发展",
        "3. 学习实用操作指南与最佳实践",
        "4. 认识潜在风险与注意事项",
        "",
        "## 详细分析",
        f"在当前的加密货币市场中，{keyword}是一个不可忽视的重要议题。无论是新手还是经验丰富的投资者，都需要对这一领域有深入的理解。",
        "",
        "## 市场影响",
        f"{keyword}对加密货币市场的影响是多方面的。从短期来看，它会影响市场情绪和交易行为；从长期来看，它可能重塑行业格局。",
        "",
        "## 投资策略建议",
        f"针对{keyword}，建议投资者采取以下策略：首先，做好充分的研究和学习；其次，控制仓位风险，不要过度集中；最后，保持耐心，长期持有优质资产。",
        "",
        "## 未来展望",
        f"随着区块链技术的不断发展和市场成熟度的提高，{keyword}的重要性将进一步凸显。保持关注和学习将是每个投资者的必修课。",
    ])

    # 相关文章
    related = get_related(filename, 6)
    rel_html = ""
    if related:
        items = []
        for r in related:
            rt = TITLE_MAP.get(r['keyword'], r['keyword'])
            items.append(f'<li><a href="{r["file"]}">{rt}</a></li>')
        rel_html = f'<div class="related"><h2>📖 推荐阅读</h2><ul>{"".join(items)}</ul></div>'

    html = make_article_html(keyword, title, now, body, ADSENSE_CLIENT, ADSENSE_SLOT_IN_ARTICLE, rel_html, filename)
    os.makedirs(ARTICLES_DIR, exist_ok=True)
    filepath = os.path.join(ARTICLES_DIR, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    return filename


# ====== 首页 ======
def make_index(arts):
    links = '\n'.join(
        f'<li><a href="articles/{a["file"]}">{TITLE_MAP.get(a["keyword"], a["keyword"])}</a></li>'
        for a in arts
    )
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="google-site-verification" content="_UJqwOqD7KQXT5DvneoA-kQzpIE4isR8apvX6sOF1Vo" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{SITE_NAME}</title>
    <meta name="description" content="CryptoInsight提供专业的加密货币分析、交易策略和市场洞察，涵盖比特币、以太坊、DeFi等热门话题。每日更新深度分析文章。">
    <meta name="keywords" content="加密货币,比特币,以太坊,交易策略,投资指南,区块链">
    <link rel="canonical" href="{SITE_URL}/">

    <!-- Open Graph -->
    <meta property="og:type" content="website">
    <meta property="og:title" content="{SITE_NAME}">
    <meta property="og:description" content="专业的加密货币分析平台 | 深度研究 | 交易策略">
    <meta property="og:url" content="{SITE_URL}/">
    <meta property="og:locale" content="zh_CN">

    <!-- JSON-LD -->
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "WebSite",
        "name": "{SITE_NAME}",
        "url": "{SITE_URL}",
        "inLanguage": "zh-CN",
        "description": "专业的加密货币分析平台 | 深度研究 | 交易策略"
    }}
    </script>

    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={ADSENSE_CLIENT}" crossorigin="anonymous"></script>
    <style>
        * {{ margin:0; padding:0; box-sizing:border-box; }}
        body {{ font-family:-apple-system,sans-serif; max-width:800px; margin:0 auto; padding:20px; background:#fafafa; }}
        h1 {{ text-align:center; padding:30px; color:#1a1a1a; }}
        ul {{ list-style:none; }}
        li {{ padding:15px; margin:8px 0; background:white; border-radius:8px; box-shadow:0 2px 8px rgba(0,0,0,0.06); }}
        a {{ color:#f0b90b; text-decoration:none; font-size:1.1em; }}
        a:hover {{ text-decoration:underline; }}
        .hero {{ background:linear-gradient(135deg,#1a1a2e,#16213e); color:white; padding:60px 20px; text-align:center; border-radius:16px; margin-bottom:30px; }}
        .hero h1 {{ color:white; font-size:2.5em; }}
        .hero p {{ font-size:1.2em; opacity:0.8; margin-top:10px; }}
        .article-count {{ text-align:center; color:#888; margin-bottom:20px; }}
        .cta-banner {{ display:block; background:linear-gradient(135deg,#f0b90b,#f8d33a); color:#1a1a1a; text-align:center; padding:18px; border-radius:12px; font-size:1.1em; font-weight:bold; text-decoration:none; margin:30px 0; }}
        .cta-banner:hover {{ transform:scale(1.02); }}
        footer {{ text-align:center; padding:30px 0; color:#888; }}
    </style>
</head>
<body>
    <div class="hero">
        <h1>CryptoInsight</h1>
        <p>专业的加密货币分析平台 | 深度研究 | 交易策略</p>
    </div>
    <a class="cta-banner" href="signal.html">📡 每日量化信号推送 → 早8点微信直达 | 了解详情</a>
    <h2>📚 最新文章 ({len(arts)}篇)</h2>
    <p class="article-count">持续更新中 · 涵盖BTC/ETH/DeFi/NFT等热门话题</p>
    <ul>{links}</ul>
    <footer>
        <p>© 2026 CryptoInsight | <a href="sitemap.html">站点地图</a></p>
    </footer>
</body>
</html>"""


def make_sitemap(arts):
    links = '\n'.join(
        f'<li><a href="articles/{a["file"]}">{TITLE_MAP.get(a["keyword"], a["keyword"])}</a></li>'
        for a in arts
    )
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>站点地图 - CryptoInsight</title>
    <meta name="description" content="CryptoInsight全部文章列表">
    <link rel="canonical" href="{SITE_URL}/sitemap.html">
    <style>
        *{{margin:0;padding:0;box-sizing:border-box}}
        body{{font-family:-apple-system,sans-serif;max-width:800px;margin:0 auto;padding:20px;background:#fafafa;color:#333;line-height:1.8}}
        h1{{text-align:center;padding:30px 0;color:#1a1a1a;border-bottom:3px solid #f0b90b;margin-bottom:30px}}
        ul{{list-style:none}}
        li{{padding:12px 0;border-bottom:1px solid #eee}}
        a{{color:#2a7de1;text-decoration:none}}
        a:hover{{text-decoration:underline}}
        .count{{text-align:center;color:#888;margin-bottom:20px}}
        nav{{margin-bottom:20px}}
        nav a{{color:#f0b90b;margin-right:15px}}
    </style>
</head>
<body>
    <nav><a href="index.html">🏠 首页</a> <a href="signal.html">📡 信号服务</a></nav>
    <h1>📚 全部文章 ({len(arts)}篇)</h1>
    <p class="count">持续更新中</p>
    <ul>{links}</ul>
</body>
</html>"""


def make_xml_sitemap(arts):
    now = datetime.now().strftime("%Y-%m-%d")
    urls = f'  <url><loc>{SITE_URL}/</loc><lastmod>{now}</lastmod><priority>1.0</priority></url>\n'
    urls += f'  <url><loc>{SITE_URL}/signal.html</loc><lastmod>{now}</lastmod><priority>0.6</priority></url>\n'
    for a in arts:
        urls += f'  <url><loc>{SITE_URL}/articles/{a["file"]}</loc><lastmod>{now}</lastmod><priority>0.8</priority></url>\n'
    return f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>'


def generate_site():
    """生成全站"""
    os.makedirs(ARTICLES_DIR, exist_ok=True)

    # 只生成索引页面，不覆盖已有文章
    arts = get_all_articles()
    if not arts:
        for i, kw in enumerate(KEYWORDS, 1):
            fn = generate_article(kw, i)
            arts.append({'keyword': kw, 'file': fn})
            print(f"  [{i}/{len(KEYWORDS)}] {kw}")

    # 首页
    idx_html = make_index(arts)
    with open(os.path.join(os.path.dirname(ARTICLES_DIR), 'index.html'), 'w', encoding='utf-8') as f:
        f.write(idx_html)

    # sitemap HTML
    sm_html = make_sitemap(arts)
    with open(os.path.join(os.path.dirname(ARTICLES_DIR), 'sitemap.html'), 'w', encoding='utf-8') as f:
        f.write(sm_html)

    # sitemap XML
    sm_xml = make_xml_sitemap(arts)
    with open(os.path.join(os.path.dirname(ARTICLES_DIR), 'sitemap.xml'), 'w', encoding='utf-8') as f:
        f.write(sm_xml)

    print(f"✅ 网站已生成: {len(arts)}篇文章")
    return arts


if __name__ == '__main__':
    generate_site()
