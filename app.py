import time
import streamlit as st

# =========================================================
# Global config (standard black/white)
# =========================================================
st.set_page_config(
    page_title="Treasure Hunt",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# =========================================================
# Hide sidebar + toggle completely
# =========================================================
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
# Password gates
# =========================================================
def pw_norm(pw: str, *, casefold: bool = True) -> str:
    pw = (pw or "").strip()
    return pw.upper() if casefold else pw

def require_password_one_of(page_key: str, allowed_passwords: list[str], *, casefold: bool = True) -> None:
    auth_key = f"auth_{page_key}"
    if st.session_state.get(auth_key, False):
        return

    st.title("Passwort erforderlich")
    pw = st.text_input("Passwort", type="password", key=f"pw_input_{page_key}")
    if st.button("Freischalten", key=f"pw_btn_{page_key}"):
        pw_in = pw_norm(pw, casefold=casefold)
        allowed = [pw_norm(x, casefold=casefold) for x in allowed_passwords]
        if pw_in in allowed:
            st.session_state[auth_key] = True
            st.rerun()
        else:
            st.error("Falsches Passwort.")
    st.stop()

# =========================================================
# Typewriter with pauses after "," and "..."
# =========================================================
def typewriter(text: str, char_delay: float = 0.015, pause_after_comma: float = 1.0, pause_after_ellipsis: float = 1.0):
    placeholder = st.empty()
    out = ""
    i = 0
    n = len(text)

    while i < n:
        if text[i:i+3] == "...":
            out += "..."
            placeholder.markdown(out)
            time.sleep(pause_after_ellipsis)
            i += 3
            continue

        ch = text[i]
        out += ch
        placeholder.markdown(out)

        if ch == ",":
            time.sleep(pause_after_comma)
        else:
            time.sleep(char_delay)

        i += 1

# =========================================================
# AUFGABE 01
# =========================================================
def aufgabe01():
    require_password_one_of("aufgabe01", ["2AK"], casefold=True)

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

    st.latex(r"\frac{1}{2} + \frac{3}{4} : \frac{6}{5} - \frac{2}{3}\cdot\frac{9}{4} = \, ?")

# =========================================================
# AUFGABE 02
# =========================================================
def aufgabe02():
    # akzeptiere Punkt oder Komma
    require_password_one_of("aufgabe02", ["0.375", "0,375"], casefold=False)

    st.title("AUFGABE 02")
    st.markdown(
        """
Lili besucht den Tag der offenen Türe und kauft etwas bei einem der Verkaufsstände der Junior Companys.  
Sie kauft **5-mal Produkt A** und **3-mal Produkt B** und bezahlt insgesamt **€ 28,-**.

Weil sich ihre Schwester so sehr über die Produkte freut, geht Lili nochmal hin und kauft von jedem Produkt je ein Stück.  
Dieser Extra-Einkauf kostet sie **€ 7,-**.

**→ Ermittle den Preis für Produkt A und Produkt B.**  
**→ Finde die Junior Company, die Produkte zu solchen Preisen anbietet – dort findest du die nächste Aufgabe.**  
**→ Passwort für die nächste Aufgabe ist der Name der Junior Company.**
"""
    )

# =========================================================
# AUFGABE 03
# =========================================================
def aufgabe03():
    require_password_one_of("aufgabe03", ["GLAMORA"], casefold=True)

    st.title("AUFGABE 03")

    st.markdown(
        """
Diesmal ein Sprung in die Zukunft – oder zumindest in ein paralleles Universum.

Ein interstellarer Konzern produziert **Energiezellen für Sprungantriebe**.  
Die **monatlichen Kosten** setzen sich aus **fixen Wartungskosten** der Orbitalfabrik und **variablen Produktionskosten pro Zelle** zusammen.  
Die **Erlöse** entstehen durch den Verkauf der Energiezellen an Raumstationen im äußeren Sektor.

Gegeben sind:
- **Fixkosten:** 500 000 Credits  
- **Variable Kosten:** 4 Credits pro Energiezelle  
- **Erlös pro Zelle:** 6 Credits  
- **Startbonus:** 63 696.88 Credits
"""
    )

    st.markdown("Kostenfunktion:")
    st.latex(r"K(x)=500000+4x")

    st.markdown("Erlösfunktion:")
    st.latex(r"E(x)=63696.88+6x")

    st.markdown(
        """
**Aufgabe:**  
1. Stelle die Gewinnfunktion \(G(x)=E(x)-K(x)\) auf.  
2. Bestimme den **Break-Even-Point** (Nullstelle von \(G(x)\)) **auf 3 Nachkommastellen** genau.

---
Wenn du den Break-Even-Point hast:

Klicke auf **Fortsetzung** und folge dann der Anleitung:
- Entferne das Komma.  
- Teile die Ziffern im Muster **1–2–2–2–1–1** auf.  
- Wandle die Zahlen in Buchstaben um.

**Hinweis zum Code:** In diesem Universum gilt zusätzlich:  
- **6 → K**  
- **0 → IE**  

Das Codewort ist das Passwort für die nächste Aufgabe.
"""
    )

    if st.button("Fortsetzung", key="continue_03"):
        st.session_state["reveal_03"] = True

    if st.session_state.get("reveal_03", False):
        st.info("Weiter mit Aufgabe 04, sobald ihr das Codewort habt.")

# =========================================================
# AUFGABE 04
# =========================================================
def aufgabe04():
    require_password_one_of("aufgabe04", ["BROOKIE"], casefold=True)

    st.title("AUFGABE 04")

    st.markdown(
        """
Aktuell finden die Rennen in **Kitzbühel** statt: manche Pisten sind steil, manche weniger.  
… aber was ist mit **unserer Schultreppe**?

**Finde die Steigung unserer Schultreppe** im Hauptgebäude vom **2. Stock in den 3. Stock**.

**Tipp:** Steigungsdreieck: \(\Delta y/\Delta x\).  
Eine Stufe der Treppe erinnert sehr an so ein Dreieck.
"""
    )

    if st.button("Fortsetzung", key="continue_04_a"):
        st.session_state["reveal_04_a"] = True

    if st.session_state.get("reveal_04_a", False):
        st.markdown(
            """
**Vergleichswerte (Pisten):**
- Ganserlhang: Steigung **0.35**  
- Planai (Zielhang): Steigung **0.45**  
- Streif (Mausefalle): Steigung **0.85**

**Aufgabe:**  
Wähle aus, welche Piste am besten zur Steigung eurer Treppe passt.  
Finde heraus, in welchem **Bundesland** diese Piste ist.
"""
        )

        if st.button("Fortsetzung", key="continue_04_b"):
            st.session_state["reveal_04_b"] = True

    if st.session_state.get("reveal_04_b", False):
        st.markdown(
            """
**Jetzt wird codiert:**
1. Schreib das **Bundesland** auf.  
2. Nimm nur die Buchstaben auf den **geraden Stellen** (2., 4., 6., …).  
3. Wandle diese Buchstaben in **Zahlen** um.  
4. **Addiere** diese Zahlen.  
5. Wandle die **Ziffern** des Ergebnisses wieder in **Buchstaben** um.
"""
        )

        if st.button("Fortsetzung", key="continue_04_c"):
            st.session_state["reveal_04_c"] = True

    if st.session_state.get("reveal_04_c", False):
        st.markdown(
            """
**Letzter Schritt:**  
Mit welchen **Ferien/Feiertagen** wird dieses Wort am häufigsten in Verbindung gebracht?  
➡️ Das ist das **letzte Passwort**.

Geht zu den **3D-Druckern**, scannt den letzten Tag und gebt das finale Passwort ein.
"""
        )

# =========================================================
# AUFGABE 05 (Finale)
# =========================================================
def aufgabe05():
    require_password_one_of("aufgabe05", ["OSTERN"], casefold=True)

    st.title("AUFGABE 05")

    names = st.text_input("Gib die Namen aller Personen in deinem Team ein:", key="team_names")

    if st.button("CONGRATS", key="congrats_btn"):
        if names.strip():
            st.balloons()
            st.success(f"CONGRATS, {names}!")
            st.markdown("Mache einen Screenshot und gib diesen bei der Aufgabe in Teams ab.")
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
