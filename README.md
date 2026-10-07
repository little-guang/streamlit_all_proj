# 專案作品集入口

這個 Streamlit 網站是作品集的集中入口，提供以下專案的介紹與連結：

- **信用卡消費分析**：瀏覽信用卡消費分析文件與成果。
- **Olist 電商分析**：瀏覽 Olist 電商資料分析專案。

## 線上入口

Streamlit 網站部署完成後，請將下方網址替換成 Streamlit Community Cloud 提供的應用程式網址，讓訪客可以從 GitHub README 直接進入作品集：

> 尚未部署：請在部署完成後補上 Streamlit 網站網址。

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
4. 部署完成後，將取得的 app 網址放到本 README 的「線上入口」，並可在 GitHub 儲存庫的 About 區域加入相同網址。

部署後，訪客即可依序從 GitHub README 進入 Streamlit 作品集，再開啟信用卡分析文件或 Olist 專案。
