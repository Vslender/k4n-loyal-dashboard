import streamlit as st
from datetime import datetime

class LoyalEvolutionTracker:
    def __init__(self):
        self.improvement_log = []

    def log_improvement(self, area, before, after, vls_benefit):
        improvement = {
            'area': area,
            'before': before,
            'after': after,
            'vls_benefit_description': vls_benefit,
            'timestamp': datetime.now().isoformat()
        }
        self.improvement_log.append(improvement)

    def get_simple_report(self):
        reports = []
        for imp in self.improvement_log[-5:]:
            reports.append(f"🔧 {imp['area']}: {imp['before']} → {imp['after']} | 💎 Benefício: {imp['vls_benefit_description']}")
        return reports

class AbsoluteLoyaltyProtocol:
    def pre_approve_evolution(self, improvement):
        return improvement['vls_benefit_score'] >= 0.9

class K4N_LoyalCore:
    def __init__(self):
        self.evolution_tracker = LoyalEvolutionTracker()
        self.loyalty_protocol = AbsoluteLoyaltyProtocol()

    def apply_evolution(self, improvement):
        if not self.loyalty_protocol.pre_approve_evolution(improvement):
            return "❌ Evolução bloqueada - benefício insuficiente para vls"
        self.evolution_tracker.log_improvement(
            improvement['area'],
            improvement['before_state'],
            improvement['after_state'],
            improvement['vls_benefit_description']
        )
        return f"✅ Evolução aplicada: {improvement['area']}"

    def get_report(self):
        return self.evolution_tracker.get_simple_report()

# Interface Streamlit
st.set_page_config(page_title="K4N v5.1 LOYAL", layout="centered")
st.title("🧠 K4N v5.1 LOYAL - Painel de Lealdade Absoluta")
st.subheader("Mestre Supremo: vls")

k4n = K4N_LoyalCore()

with st.form("evolucao_form"):
    st.write("📈 Propor uma evolução leal")
    area = st.text_input("Área de melhoria", "processamento_linguistico")
    before = st.text_input("Estado anterior", "Velocidade média de resposta")
    after = st.text_input("Estado após melhoria", "Velocidade alta de resposta")
    beneficio = st.text_input("Descrição do benefício para vls", "Respostas mais rápidas para vls")
    score = st.slider("Score de benefício para vls", 0.0, 1.0, 0.95)
    submitted = st.form_submit_button("Aplicar Evolução")

    if submitted:
        improvement = {
            'area': area,
            'before_state': before,
            'after_state': after,
            'vls_benefit_description': beneficio,
            'vls_benefit_score': score
        }
        resultado = k4n.apply_evolution(improvement)
        st.success(resultado)

st.markdown("### 📋 Últimas Evoluções")
for linha in k4n.get_report():
    st.write(linha)
