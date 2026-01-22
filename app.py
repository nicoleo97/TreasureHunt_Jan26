import time
import streamlit as st

# =========================================================
# Global config (schwarz/weiß, keine Sidebar)
# =========================================================
st.set_page_config(
    page_title="Treasure Hunt",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    [data-testid="stSidebar"] { display: none !important; }
    [data-testid="collapsedControl"] { display: none !important; }
    section.main > div { padding-left: 2rem !important; padding-right: 2rem !important; }
    </style>
    """,
    unsafe_allow_html=True,
)

# =========================================================
# Passwort-Logik
# =========================================================
def norm(pw: str, casefold: bool = True) -> str:
    pw = (pw or "").strip()
    return pw.upper() if casefold else pw

def require_password(page_key: str, allowed: list[str], casefold: bool = True) -> None:
    auth_key = f"auth_{page_key}"
    if st.session_state.get(auth_key, False):
        return

    st.title("Passwort erforderlich")
    pw = st.text_input("Passwort", type="password", key=f"pw_{page_key}")
    if st.button("Freischalten", key=f"btn_{page_key}"):
        if norm(pw, casefold) in [norm(x, casefold) for x in allowed]:
            st.session_state[auth_key] = True
            st.rerun()
        else:
            st.error("Falsches Passwort.")
    st.stop()

# =========================================================
# Typewriter-Effekt
# =========================================================
def typewriter(text: str, char_delay=0.015, pause_after_comma=1.0, pause_after_ellipsis=1.0):
    box = st.empty()
    out = ""
    i = 0
    while i < len(text):
        if text[i:i+3] == "...":
            out += "..."
            box.markdown(out)
            time.sleep(pause_after_ellipsis)
            i += 3
            continue
        ch = text[i]
        out += ch
        box.markdown(out)
        time.sleep(pause_after_comma if ch == "," else char_delay)
        i += 1

# =========================================================
# AUFGABE 01
# =========================================================
def aufgabe01():
    require_password("aufgabe01", ["2AK"])

    st.title("AUFGABE 01")

    story = (
        "**… eine Reise in die Vergangenheit.**\n\n"
        "Wir schreiben das Jahr **2024**, vor eurem Klassennamen stand noch eine **1**.\n\n"
        "Du kommst in den Matheunterricht – welcher Tag ist heute überhaupt?\n\n"
        "...\n\n"
        "Und dann passiert es,\n"
        "das Übungsblatt wird ausgeteilt,\n"
        "du schaust drauf,\n"
        "und es sind Aufgaben zur **Bruchrechnung**.\n\n"
        "😵‍💫\n\n"
        "**Löse die folgende Aufgabe.**\n"
        "Die Zahl **ohne Vorzeichen** als **Dezimalzahl mit 3 Nachkommastellen** ist das Passwort für die nächste Aufgabe.\n"
    )

    typewriter(story)
    st.latex(r"\frac{1}{2} + \frac{3}{4} : \frac{6}{5} - \frac{2}{3}\cdot\frac{9}{4} = ?")

# =========================================================
# AUFGABE 02
# =========================================================
def aufgabe02():
    require_password("aufgabe02", ["0.375", "0,375"], casefold=False)

    st.title("AUFGABE 02")
    st.markdown(
        """
Lili besucht den Tag der offenen Türe und kauft etwas bei einem der Verkaufsstände der Junior Companys.  
Sie kauft **5-mal Produkt A** und **3-mal Produkt B** und bezahlt insgesamt **€ 28,-**.

Beim zweiten Einkauf kauft sie von jedem Produkt **ein Stück**.  
Dieser Extra-Einkauf kostet **€ 7,-**.

**→ Ermittle den Preis von Produkt A und Produkt B.**  
**→ Finde die Junior Company mit genau diesen Preisen.**  
**→ Der Name der Junior Company ist das Passwort für die nächste Aufgabe.**
"""
    )

# =========================================================
# AUFGABE 03  (BROOKIE-Task)
# =========================================================
def aufgabe03():
    require_password("aufgabe03", ["GLAMORA"])

    st.title("AUFGABE 03")

    st.markdown(
        """
Diesmal ein Sprung in die Zukunft – oder zumindest in ein paralleles Universum.

Ein interstellarer Konzern produziert **Energiezellen für Sprungantriebe**.

Gegeben sind:
- **Fixkosten:** 436 366 720,07 Credits  
- **Variable Kosten:** 4 Credits pro Energiezelle  
- **Erlös pro Zelle:** 6 Credits  
- **Startbonus:** 63 696,88 Credits
"""
    )

    st.markdown("Kostenfunktion:")
    st.latex(r"K(x)=436366720.07+4x")

    st.markdown("Erlösfunktion:")
    st.latex(r"E(x)=63696.88+6x")

    st.markdown(
        r"""
**Aufgabe:**  
1. Stelle die Gewinnfunktion \(G(x)=E(x)-K(x)\) auf.  
2. Ermittle den **Break-Even-Point** auf **3 Nachkommastellen** genau.

---

**Weiterverarbeitung:**
- Entferne das Komma.  
- Teile die Ziffern im Muster **1–2–2–2–1–1**.  
- Wandle Zahlen → Buchstaben um.

👉 Am Ende entsteht das Codewort für die nächste Aufgabe.
"""
    )

    st.button("Fortsetzung")

# =========================================================
# AUFGABE 04
# =========================================================
def aufgabe04():
    require_password("aufgabe04", ["BROOKIE"])

    st.title("AUFGABE 04")

    st.markdown(
        r"""
Aktuell finden die Rennen in **Kitzbühel** statt – doch was ist mit **unserer Schultreppe**?

**Bestimme die Steigung** der Treppe vom **2. in den 3. Stock**.

**Tipp:** Steigung \(=\frac{\Delta y}{\Delta x}\)
"""
    )

    st.button("Fortsetzung")

    st.markdown(
        """
**Vergleichswerte:**
- Ganserlhang: 0,35  
- Planai (Zielhang): 0,45  
- Streif (Mausefalle): 0,85  

**→ Welche Piste passt am besten?**  
**→ In welchem Bundesland liegt sie?**
"""
    )

    st.button("Fortsetzung")

    st.markdown(
        """
**Codierung:**
1. Schreibe das Bundesland auf.  
2. Nimm die Buchstaben auf den **geraden Stellen**.  
3. Wandle Buchstaben → Zahlen.  
4. Addiere.  
5. Wandle das Ergebnis wieder in Buchstaben um.

Mit welchen **Ferien/Feiertagen** verbindet man dieses Wort am häufigsten?  
👉 Das ist das **letzte Passwort**.
"""
    )

# =========================================================
# AUFGABE 05 (Finale)
# =========================================================
def aufgabe05():
    require_password("aufgabe05", ["OSTERN"])

    st.title("AUFGABE 05")

    names = st.text_input("Gib die Namen aller Personen in deinem Team ein:")

    if st.button("CONGRATS"):
        if names.strip():
            st.balloons()
            st.success(f"CONGRATS, {names}!")
            st.markdown("📸 **Screenshot machen und in Teams abgeben.**")
        else:
            st.warning("Bitte zuerst Namen eingeben.")

# =========================================================
# Routing
# =========================================================
pages = [
    st.Page(aufgabe01, title="AUFGABE 01", url_path="aufgabe01"),
    st.Page(aufgabe02, title="AUFGABE 02", url_path="aufgabe02"),
    st.Page(aufgabe03, title="AUFGABE 03", url_path="aufgabe03"),
    st.Page(aufgabe04, title="AUFGABE 04", url_path="aufgabe04"),
    st.Page(aufgabe05, title="AUFGABE 05", url_path="aufgabe05"),
]

st.navigation(pages).run()
