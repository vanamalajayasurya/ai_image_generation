<!-- ===================== HEADER ===================== -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=220&section=header&text=AI%20Image%20Generator&fontSize=58&fontColor=ffffff&animation=fadeIn&fontAlignY=36&desc=Turn%20words%20into%20stunning%20visuals%20%E2%9C%A8&descAlignY=58&descSize=20" width="100%" alt="AI Image Generator banner"/>

<a href="https://git.io/typing-svg">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=24&duration=3000&pause=900&color=A855F7&center=true&vCenter=true&width=700&lines=Describe+it.+Generate+it.+Download+it.;Powered+by+FLUX+via+Pollinations.ai;Built+with+Python+%2B+Streamlit;From+text+prompt+to+image+in+seconds+%F0%9F%9A%80" alt="Typing animation"/>
</a>

<br/>

<img src="https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
<img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit"/>
<img src="https://img.shields.io/badge/FLUX-Model-8B5CF6?style=for-the-badge" alt="FLUX"/>
<img src="https://img.shields.io/badge/Pollinations.ai-API-22C55E?style=for-the-badge" alt="Pollinations"/>
<img src="https://img.shields.io/badge/HuggingFace-Hub-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black" alt="Hugging Face"/>

<br/><br/>

<img src="https://img.shields.io/github/stars/YOUR_USERNAME/YOUR_REPO?style=social" alt="Stars"/>
<img src="https://img.shields.io/github/forks/YOUR_USERNAME/YOUR_REPO?style=social" alt="Forks"/>

</div>

---

## 🎨 Preview

<div align="center">

<img src="generated_image.png" width="520" alt="Sample generated image"/>

<sub><i>Prompt: "A beautiful landscape with mountains and a river" — generated with FLUX</i></sub>

</div>

---

## ✨ Features

<img align="right" width="260" src="https://media.giphy.com/media/qgQUggAC3Pfv687qPC/giphy.gif" alt="AI animation"/>

- 🖌️ **Text-to-Image** — type a prompt, get an image
- ⚡ **FLUX model** through the free Pollinations.ai endpoint
- 🖥️ **Streamlit UI** — clean, interactive, runs in the browser
- 💾 **Save locally** — generated images are written to `generated_image.png`
- 🔐 **Secure config** — API keys kept in `.env` via `python-dotenv`
- 🖼️ **Pillow** for image handling and display

<br clear="right"/>

---

## 🛠️ Tech Stack

<div align="center">

| Layer | Technology |
|:---:|:---:|
| Language | ![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white) |
| Web UI | ![Streamlit](https://img.shields.io/badge/-Streamlit-FF4B4B?logo=streamlit&logoColor=white) |
| Image Model | ![FLUX](https://img.shields.io/badge/-FLUX-8B5CF6) |
| Image API | ![Pollinations](https://img.shields.io/badge/-Pollinations.ai-22C55E) |
| Hub / Models | ![HF](https://img.shields.io/badge/-Hugging%20Face-FFD21E?logoColor=black) |
| Imaging | ![Pillow](https://img.shields.io/badge/-Pillow-306998) |

</div>

---

## 🔄 How It Works

```mermaid
flowchart LR
    A[📝 User Prompt] --> B[🔗 URL Encode]
    B --> C[🌐 Pollinations.ai API<br/>model=flux]
    C --> D[🖼️ Image Bytes]
    D --> E[💾 Save PNG]
    D --> F[🖥️ Show in Streamlit]
    style A fill:#a855f7,color:#fff,stroke:none
    style C fill:#22c55e,color:#fff,stroke:none
    style F fill:#ff4b4b,color:#fff,stroke:none
```

---

## 📂 Project Structure

```
📦 ai-image-generator
 ┣ 📜 app.py              # Streamlit app (main UI)
 ┣ 📜 test_image.py       # Quick CLI test for the image API
 ┣ 📜 requirements.txt    # Dependencies
 ┣ 🖼️ generated_image.png  # Sample output
 ┗ 📜 README.md
```

---

## 🚀 Getting Started

### 1️⃣ Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO
```

### 2️⃣ Create a virtual environment *(recommended)*

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Add your environment variables *(if needed)*

Create a `.env` file in the project root:

```env
HF_TOKEN=your_huggingface_token_here
```

### 5️⃣ Run the app

```bash
streamlit run app.py
```

Open **http://localhost:8501** and start creating 🎉

---

## 🧪 Quick Test (no UI)

Verify the image API works from the command line:

```bash
python test_image.py
```

The core request looks like this:

```python
import requests
from urllib.parse import quote

prompt = "A beautiful landscape with mountains and a river"
url = f"https://image.pollinations.ai/prompt/{quote(prompt)}?model=flux"

response = requests.get(url, timeout=100)
if response.status_code == 200:
    with open("generated_image.png", "wb") as f:
        f.write(response.content)
    print("IMAGE GENERATED SUCCESSFULLY")
```

> 💡 **Note:** the `?` before `model=flux` is required — without it the model parameter becomes part of the prompt text and is ignored.

---

## 🧠 Prompt Tips

| ✅ Do | ❌ Avoid |
|---|---|
| Be specific: *"misty pine forest at sunrise, cinematic lighting"* | Vague prompts: *"nice picture"* |
| Add style: *"watercolor"*, *"3D render"*, *"photorealistic"* | Overly long, contradictory prompts |
| Mention lighting, mood and camera angle | Asking for text-heavy images |

---

## 🗺️ Roadmap

- [x] Basic text-to-image generation
- [x] Save output as PNG
- [ ] Image size / aspect-ratio controls
- [ ] Multiple model selection
- [ ] Prompt history gallery
- [ ] One-click download button
- [ ] Deploy to Streamlit Community Cloud

---

## 🤝 Contributing

Contributions, issues and feature requests are welcome!

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 👨‍💻 Author

<div align="center">

**Vanamala Jayasurya**
*B.Tech CSE (Data Science) Graduate • Software · Data · AI*

<a href="https://jayasuryaportfilio.vercel.app"><img src="https://img.shields.io/badge/Portfolio-000000?style=for-the-badge&logo=vercel&logoColor=white" alt="Portfolio"/></a>
<a href="https://linkedin.com/in/vanamala-jayasurya-5b1138324"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>

<br/><br/>

⭐ **If you like this project, give it a star!** ⭐

</div>

<!-- ===================== FOOTER ===================== -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=120&section=footer" width="100%" alt="footer"/>
