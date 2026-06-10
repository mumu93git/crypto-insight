"""
Hermes 内容工厂 - 自动生成SEO文章，赚广告费
策略: 长尾关键词 → AI生成 → 部署 → AdSense → 被动收入
"""
import os
import json
import random
from datetime import datetime

ARTICLES_DIR = os.path.join(os.path.dirname(__file__), 'articles')

# 高价值长尾关键词（低竞争、搜索量大）
KEYWORDS = [
    "比特币还会涨吗",
    "以太坊2026价格预测",
    "加密货币新手入门",
    "币安合约交易教程",
    "BTC技术分析",
    "加密货币避税",
    "DeFi挖矿教程",
    "NFT怎么买",
    "Solana生态项目",
    "加密货币安全钱包推荐",
    "网格交易策略",
    "ETH gas费优化",
    "加密货币空投攻略",
    "Web3入门教程",
    "比特币减半影响分析",
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
    # auto_content补充关键词
    "比特币ETF最新消息": "比特币ETF最新进展：机构资金流入对价格的影响分析",
    "以太坊Layer2扩容方案": "以太坊Layer2扩容方案对比：Arbitrum vs Optimism vs zkSync",
    "加密货币定投策略": "加密货币定投(DCA)策略：熊市建仓牛市收穫的最佳方式",
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


def get_all_article_files():
    """获取所有文章文件及标题"""
    articles = []
    if not os.path.exists(ARTICLES_DIR):
        return articles
    for f in sorted(os.listdir(ARTICLES_DIR)):
        if f.endswith('.html') and f.startswith('article-'):
            # 从文件名提取keyword
            parts = f.split('-', 2)
            if len(parts) >= 3:
                kw = os.path.splitext(parts[2])[0]
                articles.append({'file': f, 'keyword': kw})
    return articles


def get_related_articles(current_file, count=5):
    """随机选取相关文章（排除自身）"""
    all_arts = get_all_article_files()
    others = [a for a in all_arts if a['file'] != current_file]
    random.shuffle(others)
    return others[:count]


def generate_article(keyword, index):
    """生成一篇SEO优化的文章"""
    now = datetime.now().strftime("%Y-%m-%d")
    title = TITLE_MAP.get(keyword, f"{keyword} - 完整解析与指南 {now}")
    filename = f"article-{index:03d}-{keyword.replace(' ', '-')}.html"

    content_map = {
        "比特币还会涨吗": [
            "## 市场背景",
            f"截至{now}，比特币(BTC)价格在经历市场周期波动后，正面临多重因素的交织影响。",
            "",
            "## 技术面分析",
            "从技术指标来看，BTC的200日均线呈现上行趋势，MACD指标金叉信号已经出现。",
            "RSI指标处于50-70区间，表明市场处于健康的中性偏多状态。",
            "布林带收窄通常预示着大的价格变动即将到来。",
            "",
            "## 基本面驱动因素",
            "1. **机构入场**: 更多传统金融机构正在通过ETF和现货产品进入加密市场",
            "2. **减半效应**: 比特币减半事件后，供应量的减少对价格形成支撑",
            "3. **监管明朗化**: 全球主要经济体的加密监管框架逐渐完善",
            "",
            "## 风险评估",
            "尽管长期看涨因素充足，但短期内仍需关注：",
            "- 宏观经济环境变化（利率政策）",
            "- 地缘政治风险",
            "- 交易所安全事件",
            "",
            "## 结论",
            "基于技术面和基本面的综合分析，比特币中长期仍有上涨空间，但投资者应注意仓位管理和风险控制。",
        ],
        "比特币ETF最新消息": [
            "## 比特币ETF最新进展",
            f"截至{now}，比特币现货ETF市场持续壮大，管理资产规模(AUM)已突破新高。",
            "",
            "## 主要ETF产品对比",
            "目前市场上主要的比特币ETF包括：",
            "- **BlackRock iShares Bitcoin Trust (IBIT)**: 管理资产规模最大，日均交易量领先",
            "- **Fidelity Wise Origin Bitcoin Fund (FBTC)**: 费用率最低的比特币ETF之一",
            "- **Grayscale Bitcoin Trust (GBTC)**: 转型为ETF后资金流出压力缓解",
            "- **ARK 21Shares Bitcoin ETF (ARKB)**: 年轻投资者偏好的选择",
            "",
            "## 机构资金流入对价格的影响",
            "比特币ETF获批后，机构资金持续流入。研究显示，每净流入10亿美元，BTC价格平均上涨3-5%。",
            "ETF带来的不仅是增量资金，更重要的是为传统投资者提供了合规、便捷的投资渠道。",
            "",
            "## 未来展望",
            "随着更多养老金基金、捐赠基金和保险公司配置比特币ETF，加密资产的机构化进程将加速。",
            "同时，以太坊ETF和其他加密资产ETF的推出将扩大市场深度。",
        ],
        "以太坊Layer2扩容方案": [
            "## Layer2扩容方案概述",
            f"以太坊Layer2解决方案是提升网络吞吐量、降低交易费用的关键技术。{now}的数据显示，Layer2生态锁仓量(TVL)持续创新高。",
            "",
            "## Arbitrum",
            "Arbitrum是采用Optimistic Rollup技术的领先Layer2。优势：",
            "- EVM完全兼容，开发者迁移成本低",
            "- 生态丰富，头部DeFi协议均已部署",
            "- TVL长期位居Layer2首位",
            "",
            "## Optimism",
            "Optimism作为OP Stack的发起者，形成了超级链生态(Superchain)。",
            "- OP Stack开源框架降低了构建L2的门槛",
            "- Base、PGN等知名L2均基于OP Stack构建",
            "- 原生代币OP用于治理和生态激励",
            "",
            "## zkSync",
            "zkSync采用ZK-Rollup技术，代表Layer2的未来方向。",
            "- 零知识证明技术确保安全性",
            "- 提款无需等待期(对比Optimistic Rollup的7天)",
            "- zkSync Era上线后生态快速增长",
        ],
    }

    body = content_map.get(keyword, [
        f"## {keyword}",
        f"本文深入探讨{keyword}相关的关键信息，帮助读者全面了解这一主题。",
        "",
        "## 核心要点",
        f"1. {keyword}的基础概念与运作机制",
        f"2. 当前市场趋势与最新发展",
        f"3. 实用操作指南与最佳实践",
        f"4. 风险评估与注意事项",
        "",
        "## 详细分析",
        f"在当前的加密货币市场中，{keyword}是一个备受关注的话题。",
        "无论是新手投资者还是经验丰富的交易员，都需要对这一领域有深入的了解。",
        "",
        "## 操作建议",
        "1. 始终保持仓位管理，不将全部资金投入单一交易",
        "2. 设置止损位，控制单笔交易的风险敞口",
        "3. 持续学习，跟踪市场最新动态",
        "4. 使用可靠的交易平台和钱包服务",
        "",
        "## 相关资源",
        "- 推荐交易平台: Binance, OKX, Bybit",
        "- 学习资源: TradingView技术分析, CoinGecko市场数据",
        "- 社区交流: Reddit r/CryptoCurrency, Twitter加密社区",
    ])

    # 生成内链
    related = get_related_articles(filename, count=6)
    related_html = ""
    if related:
        related_html = '<div class="related"><h2>📖 相关文章</h2><ul>\n'
        for r in related:
            r_title = TITLE_MAP.get(r['keyword'], r['keyword'])
            related_html += f'<li><a href="{r["file"]}">{r_title}</a></li>\n'
        related_html += '</ul></div>'

    body_html = []
    for line in body:
        if not line:
            body_html.append('<br>')
        elif line.startswith('## '):
            body_html.append(f'<h2>{line[3:]}</h2>')
        elif line.startswith('- '):
            body_html.append(f'<li>{line[2:]}</li>')
        elif line[0].isdigit() and '. ' in line[:4]:
            body_html.append(f'<li>{line}</li>')
        else:
            body_html.append(f'<p>{line}</p>')

    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="google-site-verification" content="_UJqwOqD7KQXT5DvneoA-kQzpIE4isR8apvX6sOF1Vo" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{title} - 专业的加密货币分析和交易指南">
    <meta name="keywords" content="{keyword},加密货币,比特币,交易,投资">
    <title>{title}</title>
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
        nav {{ margin: 20px 0; }}
        nav a {{ color: #f0b90b; text-decoration: none; margin-right: 15px; }}
        footer {{ text-align: center; padding: 30px 0; color: #888; border-top: 1px solid #eee; margin-top: 40px; }}
    </style>
</head>
<body>
    <nav>
        <a href="/">首页</a>
        <a href="/sitemap.html">全部文章</a>
    </nav>
    
    <header>
        <h1>{title}</h1>
        <p class="meta">发布时间: {now} | 分类: 加密货币分析 | 阅读时间: 5分钟</p>
    </header>
    
    <main>
        {''.join(body_html)}
        {related_html}
    </main>
    
    <div class="cta">
        <p>📡 想要实时交易信号？</p>
        <a href="/signal.html">了解 Q系统 智能交易信号服务 →</a>
    </div>
    
    <div class="disclaimer">
        *免责声明：本文仅供信息参考，不构成投资建议。加密货币投资存在高风险，请在充分了解风险后做出独立决策。
    </div>
    
    <footer>
        <p>© 2026 CryptoInsight - 专业的加密货币分析平台</p>
    </footer>
</body>
</html>"""

    filepath = os.path.join(ARTICLES_DIR, filename)
    os.makedirs(ARTICLES_DIR, exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    return filename


def generate_site():
    """生成完整网站"""
    os.makedirs(ARTICLES_DIR, exist_ok=True)
    
    articles = []
    for i, kw in enumerate(KEYWORDS, 1):
        fname = generate_article(kw, i)
        articles.append({'keyword': kw, 'file': fname})
        print(f"  [{i}/{len(KEYWORDS)}] {kw}")
    
    # 生成首页
    index_html = generate_index(articles)
    with open(os.path.join(os.path.dirname(ARTICLES_DIR), 'index.html'), 'w', encoding='utf-8') as f:
        f.write(index_html)
    
    # 生成站点地图
    sitemap = generate_sitemap(articles)
    with open(os.path.join(os.path.dirname(ARTICLES_DIR), 'sitemap.html'), 'w', encoding='utf-8') as f:
        f.write(sitemap)
    
    # 生成XML Sitemap
    sitemap_xml = generate_xml_sitemap(articles)
    with open(os.path.join(os.path.dirname(ARTICLES_DIR), 'sitemap.xml'), 'w', encoding='utf-8') as f:
        f.write(sitemap_xml)
    
    print(f"\n✅ 网站已生成: {len(articles)}篇文章")
    print(f"   首页: index.html")
    print(f"   文章: articles/ ({len(articles)}篇)")


def generate_index(articles):
    """生成首页"""
    links = '\n'.join(
        f'<li><a href="articles/{a["file"]}">{TITLE_MAP.get(a["keyword"], a["keyword"])}</a></li>'
        for a in articles
    )
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="google-site-verification" content="_UJqwOqD7KQXT5DvneoA-kQzpIE4isR8apvX6sOF1Vo" />
    <title>CryptoInsight - 加密货币专业分析</title>
    <meta name="description" content="CryptoInsight提供专业的加密货币分析、交易策略和市场洞察">
    <meta name="keywords" content="加密货币,比特币,以太坊,交易策略,投资指南">
    <link rel="canonical" href="https://mumu93git.github.io/crypto-insight/">
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
    </style>
</head>
<body>
    <div class="hero">
        <h1>📊 CryptoInsight</h1>
        <p>专业的加密货币分析平台 | 深度研究 | 交易策略</p>
    </div>
    <h2>📚 最新文章 ({len(articles)}篇)</h2>
    <p class="article-count">持续更新中，涵盖比特币、以太坊、DeFi、NFT等热门话题</p>
    <ul>{links}</ul>
</body>
</html>"""


def generate_sitemap(articles):
    """生成HTML站点地图"""
    links = '\n'.join(
        f'<li><a href="articles/{a["file"]}">{TITLE_MAP.get(a["keyword"], a["keyword"])}</a></li>'
        for a in articles
    )
    return f"""<!DOCTYPE html>
<html><head><meta charset="UTF-8"><title>站点地图 - CryptoInsight</title></head>
<body><h1>全部文章</h1><ul>{links}</ul></body></html>"""


def generate_xml_sitemap(articles):
    """生成XML Sitemap供Google读取"""
    urls = ''
    base = 'https://mumu93git.github.io/crypto-insight'
    urls += f'<url><loc>{base}/</loc><priority>1.0</priority></url>\n'
    for a in articles:
        urls += f'<url><loc>{base}/articles/{a["file"]}</loc><priority>0.8</priority></url>\n'
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{urls}
</urlset>'''


if __name__ == '__main__':
    generate_site()
