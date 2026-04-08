import streamlit as st
from modulos.projetos import Projetos, ProjetosManager


class Interface:
    def __init__(self):
        # Registrar páginas
        self.pages = {
            "home": self.home_page,
            "skill": self.skill_page,
        }

        # Fonte única de projetos
        self.projetos_manager = ProjetosManager(
            [
                Projetos("Dashboard de Dados", "Análise de Dados", "https://github.com/seuusuario/dashboard"),
                Projetos("API de Pedidos", "Desenvolvimento de Sistemas", "https://github.com/seuusuario/api-pedidos"),
                Projetos("Landing Page", "Desenvolvimento Web", "https://github.com/seuusuario/landing-page"),
                Projetos("Modelo de Risco", "Machine Learning", "https://github.com/seuusuario/modelo-risco"),
                Projetos("Backtesting Estratégias", "Quantitative Finance", "https://github.com/seuusuario/backtesting"),
            ]
        )

        st.set_page_config(
            page_title="Portfólio | Luís",
            page_icon="💻",
            layout="wide",
        )

    def run(self):
        if "page" not in st.session_state:
            st.session_state.page = "home"

        page = self.pages.get(st.session_state.page, self.home_page)
        page()

    # ---------- Páginas ----------
    def home_page(self):
        self._inject_style()

        nome = "Luis Andrade"
        resumo = (
            "Automações, ciência de dados e desenvolvimento de sistemas. "
            "Desenvolvo soluções de métricas e análises com modelos de ML."
        )
        contatos = {
            "GitHub": "https://github.com/1conto",
            "LinkedIn": "https://www.linkedin.com/in/luisgrandrade/",
            "E-mail": "mailto:lgandrade35@gmail.com",
        }
        habilidades = [
            "Automações",
            "Análise de Dados",
            "Ciência de Dados",
            "Econometria",
            "Machine Learning",
            "Desenvolvimento de Sistemas",
            "Desenvolvimento Web",
            "Quantitative Finance",
            "Outras Habilidades",
        ]
        principais_stacks = [
            "Python",
            "R",
            "SQL",
            "Streamlit",
            "Snowflake",
            "CI/CD",
            "Cloud",
            "Pandas",
            "NumPy",
            "Excel",
            "PowerBI",
            "Scikit-learn",
            "HTML",
            "CSS",
            "JavaScript",
            "React",
            "Git",
        ]

        # Hero
        hero_col, info_col = st.columns([2, 1], gap="large")
        with hero_col:
            st.markdown(
                f"""
                <div class="glass">
                    <h1 class="headline">Oi, eu sou o {nome} 👋</h1>
                    <h3 style="margin-top:-6px;">Crio soluções digitais do rascunho à produção.</h3>
                    <p style="line-height:1.7;">{resumo}</p>
                    <p style="line-height:1.7;">
                        Atuo end-to-end: arquitetura, implementação, integrações e métricas.
                    </p>
                </div>
                """,
                unsafe_allow_html=True,
            )
        with info_col:
            contatos_html = "".join(
                [f"<li><a href='{link}' target='_blank'>{label}</a></li>" for label, link in contatos.items()]
            )
            st.markdown(
                f"""
                <div class="glass">
                    <p style="margin:0; opacity:0.7; font-size:0.9rem;">Contato rápido</p>
                    <ul style="padding-left:18px; margin-top:6px; line-height:1.6;">
                        {contatos_html}
                    </ul>
                    <p style="margin:4px 0 0 0; opacity:0.7; font-size:0.9rem;">Localização</p>
                    <p style="margin:2px 0 0 0;">Brasil · Disponível para remoto</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

        st.divider()

        # Habilidades -> navegação por página
        st.subheader("Habilidades principais")
        skill_cols = st.columns(3, gap="large")
        for idx, skill in enumerate(habilidades):
            col = skill_cols[idx % 3]
            with col:
                if st.button(skill, use_container_width=True, key=f"skill-{skill}"):
                    st.session_state.selected_skill = skill
                    st.session_state.page = "skill"
                    st.rerun()

        st.divider()

        # Stacks principais (chips)
        st.subheader("Stacks e ferramentas")
        stack_cols = st.columns(5)
        for stack, col in zip(principais_stacks, stack_cols * ((len(principais_stacks) // 5) + 1)):
            if stack:
                with col:
                    st.button(stack, use_container_width=True, key=f"stack-{stack}")

        st.divider()

        # Projetos em destaque (primeiros 3)
        st.subheader("Projetos em destaque")
        projetos = self.projetos_manager.listar()[:3]
        proj_cols = st.columns(3, gap="large")
        for projeto, col in zip(projetos, proj_cols):
            with col:
                st.markdown(
                    f"""
                    <div class="glass">
                        <h4 class="headline" style="margin-bottom:6px;">{projeto._nome}</h4>
                        <p style="margin:0 0 10px 0; opacity:0.8;">{projeto.categoria}</p>
                        <p style="margin:0 0 12px 0;">
                            <a href="{projeto._link}" target="_blank">Abrir repositório</a>
                        </p>
                        <div class="progress-wrap">
                            <span class="progress-bar" style="width: 90%;"></span>
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

        st.divider()

        # Chamada final
        st.markdown(
            f"""
            <div class="glass">
                <h3 class="headline">Vamos conversar?</h3>
                <p style="line-height:1.7;">
                    Curto discutir problemas reais e encontrar a menor solução viável.
                    Me envie uma mensagem e começamos algo novo.
                </p>
                <p><a href="{contatos.get('LinkedIn')}" target="_blank">Falar no LinkedIn</a></p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    def skill_page(self):
        self._inject_style()

        skill = st.session_state.get("selected_skill", "Habilidade")
        st.markdown(
            f"""
            <div class="glass" style="margin-bottom:16px;">
                <p style="margin:0; opacity:0.7;">Você está em</p>
                <h3 class="headline" style="margin:4px 0;">{skill}</h3>
            </div>
            """,
            unsafe_allow_html=True,
        )

        filtrados = self.projetos_manager.filtrar_por_categoria(skill)

        if not filtrados:
            st.markdown(
                """
                <div class="glass">
                    <p style="margin:0;">Ainda não há projetos cadastrados para esta habilidade.</p>
                </div>
                """,
                unsafe_allow_html=True,
            )
        else:
            cols = st.columns(3, gap="large")
            for projeto, col in zip(filtrados, cols * ((len(filtrados) // 3) + 1)):
                with col:
                    st.markdown(
                        f"""
                        <div class="glass">
                            <h4 class="headline" style="margin-bottom:6px;">{projeto._nome}</h4>
                            <p style="margin:0 0 10px 0; opacity:0.8;">{projeto.categoria}</p>
                            <p style="margin:0 0 12px 0;">
                                <a href="{projeto._link}" target="_blank">Abrir repositório</a>
                            </p>
                            <div class="progress-wrap">
                                <span class="progress-bar" style="width: 90%;"></span>
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

        st.divider()
        if st.button("⬅ Voltar", use_container_width=True):
            st.session_state.page = "home"
            st.rerun()

    # ---------- Utilidades ----------
    def _inject_style(self):
        st.markdown(
            """
            <style>
            @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600&display=swap');

            .stApp {
                background: radial-gradient(circle at 18% 22%, rgba(99,102,241,0.18), transparent 25%),
                            radial-gradient(circle at 82% 8%, rgba(16,185,129,0.16), transparent 28%),
                            linear-gradient(140deg, #0b1020 0%, #0f172a 35%, #0b1020 100%);
                color: #e7eefc;
                font-family: 'Space Grotesk', 'Segoe UI', system-ui, -apple-system, sans-serif;
            }
            .glass {
                background: rgba(255, 255, 255, 0.04);
                border: 1px solid rgba(255, 255, 255, 0.08);
                border-radius: 16px;
                padding: 16px 18px;
                box-shadow: 0 12px 40px rgba(0,0,0,0.35);
                backdrop-filter: blur(14px);
            }
            .headline {
                font-weight: 600;
                letter-spacing: -0.02em;
            }
            div.stButton > button {
                background: linear-gradient(145deg, #111827, #0b1328) !important;
                border: 1px solid rgba(255,255,255,0.18) !important;
                color: #e7eefc !important;
                border-radius: 12px;
                box-shadow: 0 10px 22px rgba(0,0,0,0.35);
            }
            div.stButton > button:hover {
                border-color: #22d3ee !important;
                transform: translateY(-1px);
            }
            a { color: #22d3ee; }
            a:hover { color: #7dd3fc; }
            .stDivider { opacity: 0.5; }
            .progress-wrap {
                width: 100%;
                background: rgba(255,255,255,0.06);
                border-radius: 999px;
                overflow: hidden;
                border: 1px solid rgba(255,255,255,0.08);
                height: 10px;
            }
            .progress-bar {
                display: block;
                height: 10px;
                background: linear-gradient(90deg, #22d3ee, #7c3aed);
            }
            </style>
            """,
            unsafe_allow_html=True,
        )
        st.session_state._style_injected = True
