# Guang 的資料作品集

透過資料分析探索消費者行為與電商營運，從作品集入口前往線上成果，或查看 GitHub 專案原始碼。

## 作品集入口

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://my-all-proj.streamlit.app/)

**[前往 Streamlit 專案作品集](https://my-all-proj.streamlit.app/)**

## 精選專案

| 專案 | 線上成果 | GitHub 原始碼 |
| --- | --- | --- |
| 信用卡消費分析 | [閱讀分析文件](https://little-guang.github.io/credit_card/docs/index.html) | [credit_card](https://github.com/little-guang/credit_card) |
| Olist 電商分析 | [瀏覽專案成果](https://little-guang.github.io/olist_proj/) | [olist_proj](https://github.com/little-guang/olist_proj) |

## 關於我

[GitHub 個人頁 · little-guang](https://github.com/little-guang)

## 本機執行

需要 Python 3.14 以上版本與 [uv](https://docs.astral.sh/uv/)：

```powershell
uv sync
uv run streamlit run src/streamlit_all_proj/app.py
```

## 部署到 Streamlit Community Cloud

1. 前往 [Streamlit Community Cloud](https://share.streamlit.io/) 並登入 GitHub。
2. 建立新 app，選擇 `little-guang/streamlit_all_proj` 儲存庫與 `master` 分支。
3. 將主程式路徑設為 `src/streamlit_all_proj/app.py`，然後部署。
4. 部署完成後，可在 GitHub 儲存庫的 About 區域將 `https://my-all-proj.streamlit.app/` 設為 Website，讓訪客也能從儲存庫頁面直接開啟作品集。
