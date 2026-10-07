import streamlit as st


CREDIT_CARD_SITE = "https://little-guang.github.io/credit_card/docs/index.html"
CREDIT_CARD_REPO = "https://github.com/little-guang/credit_card"
OLIST_SITE = "https://little-guang.github.io/olist_proj/"
OLIST_REPO = "https://github.com/little-guang/olist_proj"
GITHUB_PROFILE = "https://github.com/little-guang"

st.set_page_config(
    page_title="Guang 的資料作品集",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Noto+Sans+TC:wght@400;500;600;700;800&display=swap');

    :root {
        --ink: #f2f5f3;
        --muted: #a9b8b4;
        --mint: #a7f3d0;
        --line: rgba(180, 214, 201, 0.16);
        --panel: rgba(16, 34, 34, 0.86);
    }

    .stApp {
        background:
            radial-gradient(ellipse at 18% 0%, rgba(23, 111, 93, 0.28), transparent 38%),
            radial-gradient(ellipse at 92% 20%, rgba(62, 91, 133, 0.20), transparent 34%),
            #091312;
        color: var(--ink);
        font-family: 'DM Sans', 'Noto Sans TC', sans-serif;
    }

    .block-container {
        max-width: 1120px;
        padding-top: 3.5rem;
        padding-bottom: 2.5rem;
    }

    .hero {
        position: relative;
        overflow: hidden;
        padding: clamp(2rem, 6vw, 4.5rem);
        border: 1px solid var(--line);
        border-radius: 28px;
        background:
            linear-gradient(115deg, rgba(16, 43, 39, 0.96), rgba(14, 27, 33, 0.94)),
            var(--panel);
        box-shadow: 0 28px 90px rgba(0, 0, 0, 0.25);
    }

    .hero::after {
        content: '';
        position: absolute;
        width: 300px;
        height: 300px;
        right: -70px;
        top: -130px;
        border-radius: 50%;
        background: rgba(110, 231, 183, 0.13);
        filter: blur(3px);
        pointer-events: none;
    }

    .eyebrow {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        padding: 7px 12px;
        border: 1px solid rgba(167, 243, 208, 0.25);
        border-radius: 999px;
        background: rgba(167, 243, 208, 0.08);
        color: var(--mint);
        font-size: 0.78rem;
        font-weight: 700;
        letter-spacing: 0.12em;
        text-transform: uppercase;
    }

    .hero h1 {
        margin: 1.2rem 0 0.75rem;
        color: var(--ink);
        font-size: clamp(2.4rem, 6vw, 4.5rem);
        font-weight: 800;
        letter-spacing: -0.055em;
        line-height: 1.12;
    }

    .hero p {
        max-width: 650px;
        margin: 0;
        color: var(--muted);
        font-size: clamp(1rem, 2vw, 1.12rem);
        line-height: 1.9;
    }

    .hero a, .project-card a {
        color: var(--mint);
        text-decoration: none;
    }

    .profile-link {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        margin-top: 1.5rem;
        font-size: 0.95rem;
        font-weight: 700;
    }

    .section-heading {
        margin: 2.5rem 0 1.2rem;
    }

    .section-heading h2 {
        margin: 0 0 0.35rem;
        color: var(--ink);
        font-size: 1.55rem;
        letter-spacing: -0.03em;
    }

    .section-heading p {
        margin: 0;
        color: var(--muted);
        font-size: 0.98rem;
    }

    .project-card {
        height: 100%;
        min-height: 295px;
        padding: 1.65rem;
        border: 1px solid var(--line);
        border-radius: 22px;
        background: linear-gradient(145deg, rgba(18, 39, 38, 0.94), rgba(13, 25, 29, 0.96));
        box-shadow: 0 16px 48px rgba(0, 0, 0, 0.16);
        transition: transform 180ms ease, border-color 180ms ease, box-shadow 180ms ease;
    }

    .project-card:hover {
        transform: translateY(-4px);
        border-color: rgba(167, 243, 208, 0.38);
        box-shadow: 0 22px 55px rgba(0, 0, 0, 0.24);
    }

    .project-icon {
        display: grid;
        width: 48px;
        height: 48px;
        place-items: center;
        margin-bottom: 1.25rem;
        border: 1px solid rgba(167, 243, 208, 0.18);
        border-radius: 15px;
        background: rgba(167, 243, 208, 0.09);
        font-size: 1.45rem;
    }

    .project-card h3 {
        margin: 0 0 0.65rem;
        color: var(--ink);
        font-size: 1.3rem;
        letter-spacing: -0.025em;
    }

    .project-card p {
        min-height: 3.4rem;
        margin: 0;
        color: var(--muted);
        font-size: 0.96rem;
        line-height: 1.8;
    }

    .card-links {
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
        margin-top: 1.45rem;
    }

    .card-links a {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        min-height: 42px;
        padding: 0 14px;
        border: 1px solid rgba(167, 243, 208, 0.24);
        border-radius: 12px;
        background: rgba(167, 243, 208, 0.08);
        color: var(--mint);
        font-size: 0.88rem;
        font-weight: 700;
        transition: background 160ms ease, border-color 160ms ease;
    }

    .card-links a:hover {
        border-color: rgba(167, 243, 208, 0.55);
        background: rgba(167, 243, 208, 0.15);
    }

    .portfolio-footer {
        display: flex;
        justify-content: space-between;
        gap: 1rem;
        margin-top: 2.25rem;
        padding-top: 1.2rem;
        border-top: 1px solid var(--line);
        color: var(--muted);
        font-size: 0.84rem;
    }

    @media (max-width: 700px) {
        .block-container {
            padding-top: 1.5rem;
        }

        .hero {
            border-radius: 22px;
        }

        .project-card {
            min-height: auto;
        }

        .portfolio-footer {
            flex-direction: column;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    f"""
    <section class="hero">
        <span class="eyebrow">✦ Data &amp; Analytics Portfolio</span>
        <h1>把資料，變成<br>有用的洞察。</h1>
        <p>
            歡迎來到我的資料分析作品集。這裡整理了信用卡消費分析與
            Olist 電商分析專案，歡迎閱讀線上成果或前往 GitHub 查看原始碼。
        </p>
        <a class="profile-link" href="{GITHUB_PROFILE}" target="_blank" rel="noopener noreferrer">
            ↗ 查看我的 GitHub 個人頁
        </a>
    </section>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="section-heading">
        <h2>精選專案</h2>
        <p>探索專案成果，或直接前往 GitHub 查看程式碼與文件。</p>
    </div>
    """,
    unsafe_allow_html=True,
)

credit_card, olist = st.columns(2, gap="large")

with credit_card:
    st.markdown(
        f"""
        <article class="project-card">
            <div class="project-icon">💳</div>
            <h3>信用卡消費分析</h3>
            <p>從信用卡消費資料探索顧客行為、消費型態與分析模型，閱讀完整專案文件與成果。</p>
            <div class="card-links">
                <a href="{CREDIT_CARD_SITE}" target="_blank" rel="noopener noreferrer">↗ 線上分析文件</a>
                <a href="{CREDIT_CARD_REPO}" target="_blank" rel="noopener noreferrer">⌘ GitHub 原始碼</a>
            </div>
        </article>
        """,
        unsafe_allow_html=True,
    )

with olist:
    st.markdown(
        f"""
        <article class="project-card">
            <div class="project-icon">🛍️</div>
            <h3>Olist 電商分析</h3>
            <p>透過 Olist 電商資料了解訂單、顧客與營運表現，瀏覽分析成果及專案實作。</p>
            <div class="card-links">
                <a href="{OLIST_SITE}" target="_blank" rel="noopener noreferrer">↗ 線上專案成果</a>
                <a href="{OLIST_REPO}" target="_blank" rel="noopener noreferrer">⌘ GitHub 原始碼</a>
            </div>
        </article>
        """,
        unsafe_allow_html=True,
    )

st.markdown(
    f"""
    <footer class="portfolio-footer">
        <span>以資料探索問題，讓分析連結決策。</span>
        <a href="{GITHUB_PROFILE}" target="_blank" rel="noopener noreferrer">GitHub · little-guang ↗</a>
    </footer>
    """,
    unsafe_allow_html=True,
)
